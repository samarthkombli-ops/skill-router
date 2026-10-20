# Contributing

Thanks for helping improve skill-router.

## Reporting a routing mistake

Open an issue with:

- What you asked the agent to do
- Which skill it picked (or installed), and which one it should have picked
- Your agent and model (e.g. Claude Code + Sonnet, Codex + GPT-5)

## Reporting a vetting gap

If a skill got past the vetting checklist that should not have, open an issue describing the
pattern. **Do not paste live malicious payloads or real credentials**; describe the technique
and give a defanged example.

## Catalog changes

Regenerate candidates with `python scripts/sweep.py --out sweep-report.md` (standard library
only; it reads the public skills.sh search API and installs nothing). Use the report to propose
additions; flagged COPY / ALIAS entries should point to the original publisher instead.

`skills/skill-router/references/catalog.md` lets agents skip the full review of a skill when its
repository is still at the listed commit. A pull request that adds or changes a reviewed commit
must say that you read every instruction file and script of that skill at that commit, and list
anything scanned rather than read. Maintainers re-check before merging.

## Pull requests

- Keep the skill instruction-only. No scripts, no dependencies: users should be able to read
  the whole thing in five minutes, and the router must pass its own vetting.
- Keep `SKILL.md` short. Detail belongs in `references/`.
- Test your change on a real task before opening the PR, and say in the PR what you tested
  and on which agent.
- Do not add invisible Unicode characters. Write escapes like `\u200b` as plain ASCII text.
  The check in `references/vetting.md` should report nothing when run on this repository.
