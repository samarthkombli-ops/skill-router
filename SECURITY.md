# Security policy

skill-router installs third-party instructions into AI agents, so its vetting rules are its
security boundary. Reports that improve them are very welcome.

## Reporting a vulnerability

Please report privately through GitHub's
[private vulnerability reporting](https://github.com/samarthkombli-ops/skill-router/security/advisories/new)
instead of opening a public issue. Include:

- The technique that gets an unsafe skill past `skills/skill-router/references/vetting.md`, or
  makes the router install without the user's approval when it should ask
- A **defanged** example: no working payloads, real credentials or live exfiltration endpoints
- The agent and model you tested with

You can expect an acknowledgement within 7 days. Fixes ship as a new release, with credit if you
want it.

## Scope

In scope: the router's instructions and vetting checklist, and the repository's CI check.

Out of scope: vulnerabilities in third-party skills themselves (report those to their
maintainers), in the `skills` CLI, or in the agents that run skills.

## Limits

Vetting is performed by the agent reading files. It substantially reduces risk but is not a
malware scanner. Code-bearing skills always require the user's explicit approval for this reason.
