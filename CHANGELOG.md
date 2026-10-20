# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-10-20

### Added

- Companion skills: for each type of work (coding, websites, research, documents…) the router
  checks the skills that make every such task faster, cheaper or more polished, not only skills
  matching the literal request.
- `references/catalog.md`: map of widely used skills across 24 types of work, built from a sweep of
  about 5,400 skills.sh results, with need level (essential / when relevant / optional), safety tier,
  reviewed commits, and a publisher guide.
- `scripts/sweep.py`: regenerates the catalog candidates from the skills.sh search API and flags
  copies (same skill under 3+ owners), lookalike repos named after famous packs, and pack-shared
  install counts.
- Copy and lookalike handling: prefer the original publisher; skip repos imitating a known pack.
- Facets: multi-discipline tasks are split into parts, each matched or filled separately, with a
  specialist check for the task's main deliverable.
- Packs and side skills: relevant siblings from the same repository are installed together.
- One batched message for skills needing approval and optional offers; the task continues
  meanwhile.
- Opt-in `skill-router: auto-install vetted bundled scripts` for skills with standard-library
  helper scripts.
- Conflict order: user and standing rules, then the facet specialist, then general skills.
- Plugin `UserPromptSubmit` hook that prints a one-line reminder to use the router; without it,
  agents skipped the skill on tasks that looked small.
- Always-on companions table at the top of `SKILL.md` (ponytail at ultra for any code change).

### Changed

- Safety tiers are now instruction-only, bundled scripts, system-changing, and rejected. Optional,
  user-triggered extras no longer block an otherwise instruction-only skill.
- Large reference data files may be scanned programmatically; instructions and scripts are still
  read in full.
- Up to 6 skills per task (a pack counts as one), installed user-wide by default.

## [1.0.0] - 2026-10-20

### Added

- `skill-router` skill: matches a task against installed skills, searches skills.sh when none
  fits, shortlists on fit before popularity, vets the chosen skill by reading every file, and
  installs the reviewed copy.
- Vetting checklist (`references/vetting.md`): instruction-only vs code-bearing classification,
  red flags (prompt injection, credential access, exfiltration, hidden Unicode, HTML comments),
  dependency handling, install and removal steps for Claude Code and Codex.
- Claude Code plugin and marketplace manifests for `/plugin` installs.
- CI check for hidden Unicode characters, `SKILL.md` frontmatter, and instruction-only contents.

[1.1.0]: https://github.com/samarthkombli-ops/skill-router/releases/tag/v1.1.0
[1.0.0]: https://github.com/samarthkombli-ops/skill-router/releases/tag/v1.0.0
