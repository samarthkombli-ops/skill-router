# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

[1.0.0]: https://github.com/samarthkombli-ops/skill-router/releases/tag/v1.0.0
