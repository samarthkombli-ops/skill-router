"""Sweep skills.sh across types of work and report candidates for references/catalog.md.

Usage:  python scripts/sweep.py [--out sweep-report.md] [--json sweep.json]

Uses only the Python standard library and the public skills.sh search API (the same one
`npx skills find` uses). It never downloads or installs a skill. The report is input for a
human-reviewed catalog update, not something to install from directly.

For each type of work it lists the most-installed results and flags:
  COPY  - the same skill name is published by 3+ owners; prefer the original publisher
  ALIAS - a repo named after a well-known pack (e.g. "superpowers") by a different owner
  PACK  - install count is shared by every skill in that repo (pack installs), so it says
          little about this one skill
"""
import argparse
import collections
import json
import sys
import time
import urllib.parse
import urllib.request

API = "https://skills.sh/api/search"

# Repos whose names are commonly reused by unrelated owners: name -> original owner.
KNOWN_PACKS = {"superpowers": "obra", "taste-skill": "leonxlnx", "ponytail": "dietrichgebert"}

NICHES = {
    "Coding (general)": ["coding", "refactor", "clean code", "simplify code", "code quality"],
    "Debugging": ["debugging", "bug fix", "root cause"],
    "Testing": ["tdd", "testing", "unit test", "e2e playwright"],
    "Code review": ["code review", "pull request review"],
    "Git / GitHub": ["git", "github", "commit"],
    "Planning / product": ["product manager", "prd", "planning", "brainstorming", "roadmap"],
    "Frontend / React": ["react", "nextjs", "frontend", "tailwind", "shadcn"],
    "Web / UI design": ["web design", "ui design", "design system", "landing page", "taste"],
    "Animation / motion": ["animation", "motion", "gsap", "framer motion"],
    "Mobile apps": ["react native", "expo", "swiftui", "flutter", "android"],
    "Backend / APIs": ["backend", "api design", "fastapi", "node express", "auth"],
    "Databases": ["postgres", "supabase", "database", "sql", "prisma"],
    "DevOps / cloud": ["docker", "kubernetes", "ci cd", "github actions", "terraform",
                       "vercel", "cloudflare", "aws", "azure", "firebase"],
    "Security": ["security", "security audit", "vulnerability"],
    "Video": ["video", "remotion", "video editing", "youtube", "subtitles"],
    "Images / photos": ["image generation", "photo editing", "image", "svg", "icons"],
    "Audio / music": ["audio", "text to speech", "voice", "music", "podcast"],
    "3D / games": ["threejs", "3d", "game development", "unity", "blender"],
    "Writing": ["copywriting", "writing", "blog", "technical writing", "humanize"],
    "Marketing / SEO / sales": ["seo", "marketing", "social media", "email marketing", "ads",
                                "sales", "cold email"],
    "Documents": ["pdf", "docx", "xlsx", "pptx", "presentation"],
    "Data / analysis": ["data analysis", "visualization", "pandas", "dashboard", "charts"],
    "AI / LLM apps": ["llm", "ai sdk", "rag", "mcp", "prompt engineering"],
    "Research / web data": ["research", "web search", "scraping", "browser automation", "crawl"],
    "Agent workflow": ["skill creator", "find skills", "memory", "context", "subagent"],
}


def search(query, limit=50):
    url = API + "?" + urllib.parse.urlencode({"q": query, "limit": limit})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                return json.load(resp).get("skills", [])
        except Exception:
            time.sleep(2 * (attempt + 1))
    print(f"warning: no results for {query!r}", file=sys.stderr)
    return []


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default="sweep-report.md")
    ap.add_argument("--json", default=None, help="also write raw results here")
    ap.add_argument("--top", type=int, default=20, help="rows per type of work")
    args = ap.parse_args()

    results = {}
    for niche, queries in NICHES.items():
        seen = {}
        for q in queries:
            for s in search(q):
                row = {"id": s["id"], "source": s.get("source", ""), "name": s.get("name", ""),
                       "installs": s.get("installs") or 0}
                if row["id"] not in seen or row["installs"] > seen[row["id"]]["installs"]:
                    seen[row["id"]] = row
            time.sleep(0.3)
        results[niche] = sorted(seen.values(), key=lambda r: -r["installs"])
        print(f"{niche}: {len(results[niche])} unique", file=sys.stderr)

    every = {r["id"]: r for rows in results.values() for r in rows}
    owners_by_name = collections.defaultdict(set)
    installs_by_repo = collections.defaultdict(list)
    for r in every.values():
        owners_by_name[r["name"]].add(r["source"].split("/")[0])
        installs_by_repo[r["source"]].append(r["installs"])

    def flags(r):
        f = []
        if len(owners_by_name[r["name"]]) >= 3:
            f.append(f"COPY x{len(owners_by_name[r['name']])}")
        owner, _, repo = r["source"].partition("/")
        if KNOWN_PACKS.get(repo) and KNOWN_PACKS[repo] != owner:
            f.append(f"ALIAS of {KNOWN_PACKS[repo]}/{repo}")
        counts = installs_by_repo[r["source"]]
        if len(counts) >= 3 and max(counts) <= 1.05 * min(counts):
            f.append("PACK")
        return " ".join(f)

    lines = ["# skills.sh sweep", "",
             f"Generated {time.strftime('%Y-%m-%d')} from {len(every)} unique results.",
             "Flags: COPY = same name from 3+ owners; ALIAS = imitates a known pack's repo name;",
             "PACK = every skill in the repo shows the same installs.", ""]
    for niche, rows in results.items():
        lines += [f"## {niche}", "", "| Installs | Skill | Flags |", "|---:|---|---|"]
        for r in rows[: args.top]:
            lines.append(f"| {r['installs']:,} | `{r['source']}@{r['name']}` | {flags(r)} |")
        lines.append("")
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines))
    if args.json:
        with open(args.json, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(results, fh, indent=1)
    print(f"wrote {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
