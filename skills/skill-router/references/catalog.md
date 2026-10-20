# Catalog: high-value skills by type of work

Built from a sweep of the skills.sh search API (about 5,400 unique results across 25 types of
work, October 2026; regenerate with `scripts/sweep.py` in the skill-router repository), then
filtered by hand for relevance and genuine publishers. It is a **starting map, not a whitelist and
not the whole ecosystem**: for any gap it doesn't cover well, search live (`SKILL.md` Step 2).

## How to read it

**Need**
- **Essential**: clearly improves speed, token use or presentation for this type of work. Install
  when the safety tier allows.
- **When relevant**: essential only when the task includes that activity or stack.
- **Optional**: useful, not needed to finish this task well. Offer once, batched.

**Tier** (safety, see `vetting.md`)
- `reviewed <commit>`: fully reviewed at that commit. Fast path allowed if HEAD still matches.
- `md-only <commit>`: file inventory at that commit had no scripts. **Not a review: no fast path**;
  do the full review.
- `scripts <commit>`: the skill folder contains scripts. Full review; bundled-scripts or
  system-changing tier.
- `cli`: normal use needs a separate CLI or account. System-changing: ask.
- `vet`: not inventoried yet.

Several skills from one repository form a **pack**; install counts are often shared across a pack,
so they reflect the pack's popularity, not each skill's. Packs listed as "pack:" can supply
side skills (`SKILL.md` Step 3).

## Coding: every task that writes or changes code

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| ponytail | `dietrichgebert/ponytail@ponytail` | Essential | reviewed 09c434a | Smallest change that fully solves the task; fewer tokens, smaller diffs. Run it at **ultra** (`/ponytail ultra`) unless the user or standing rules choose another level. |
| ponytail-review | `dietrichgebert/ponytail@ponytail-review` | When reviewing | md-only 09c434a | Review that removes unneeded code. |
| ponytail-audit, ponytail-debt | `dietrichgebert/ponytail@…` | Optional | md-only 09c434a | Whole-codebase bloat and debt passes. |
| improve-codebase-architecture | `mattpocock/skills@improve-codebase-architecture` | When restructuring | md-only 5beb35b | Architecture improvement method. |
| request-refactor-plan | `mattpocock/skills@request-refactor-plan` | When refactoring | md-only 5beb35b | Plan before large refactors. |

Packs: `mattpocock/skills` (38 skills, 35 md-only), `obra/superpowers` (15), `addyosmani/agent-skills` (25).

## Debugging

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| systematic-debugging | `obra/superpowers@systematic-debugging` | Essential when debugging | reviewed bb92a77 (one shell helper running the project's tests) | Root cause before fixes. |
| diagnosing-bugs | `mattpocock/skills@diagnosing-bugs` | Alternative to the above | scripts 5beb35b | Pick one of the two. |
| debugging-and-error-recovery | `addyosmani/agent-skills@debugging-and-error-recovery` | Optional | md-only aeac41d | |

## Testing

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| tdd | `mattpocock/skills@tdd` | When writing tests | md-only 5beb35b | Test-first workflow; most-installed testing skill. |
| webapp-testing | `anthropics/skills@webapp-testing` | When testing a web UI | scripts dbd4588 | Anthropic's browser testing with Playwright. |
| playwright-best-practices | `currents-dev/playwright-best-practices-skill@playwright-best-practices` | When the project uses Playwright | vet | |
| setup-pre-commit | `mattpocock/skills@setup-pre-commit` | Optional | md-only 5beb35b | |

## Code review and Git

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| code-review | `mattpocock/skills@code-review` | When reviewing | md-only 5beb35b | Structured review. |
| requesting-code-review, receiving-code-review | `obra/superpowers@…` | When working through PR review | md-only bb92a77 | |
| resolving-merge-conflicts | `mattpocock/skills@resolving-merge-conflicts` | When merging | md-only 5beb35b | |
| using-git-worktrees | `obra/superpowers@using-git-worktrees` | Optional | md-only bb92a77 | |
| git-guardrails-claude-code | `mattpocock/skills@git-guardrails-claude-code` | Optional | scripts 5beb35b (installs a hook: system-changing) | |

## Planning a build or feature

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| brainstorming | `obra/superpowers@brainstorming` | When the request is vague | scripts bb92a77 | Clarify before building. |
| writing-plans, executing-plans | `obra/superpowers@…` | For multi-step builds | md-only bb92a77 | |
| grill-with-docs, to-prd, to-issues | `mattpocock/skills@…` | When turning ideas into specs | md-only 5beb35b | |

## Frontend / React / Next.js

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| vercel-react-best-practices | `vercel-labs/agent-skills@vercel-react-best-practices` | Essential for React/Next.js | md-only 063bee9 | Vercel's React performance rules. |
| vercel-composition-patterns | `vercel-labs/agent-skills@vercel-composition-patterns` | When relevant | md-only 063bee9 | |
| shadcn | `shadcn-ui/ui@shadcn` | When using shadcn/ui | scripts ba1503c | Official. |

## Websites, landing pages, UI design

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| design-taste-frontend ("Taste") | `leonxlnx/taste-skill@design-taste-frontend` | Essential | reviewed 63aba5f (bundled scripts: Node stdlib, local Chrome, public-domain image APIs) | Art direction from award-winning sites; anti-generic style; inspector loop. |
| motion | `motiondivision/ai-kit@motion` | Essential when animating; always if the project uses Motion | reviewed 8dc4f7a (optional MCP / `npx motionscore` extras) | Official Motion best practices. |
| frontend-design | `anthropics/skills@frontend-design` | Essential if no design skill is installed | md-only dbd4588 | |
| web-design-guidelines | `vercel-labs/agent-skills@web-design-guidelines` | When relevant | md-only 063bee9 | Interface guidelines. |
| impeccable | `pbakaus/impeccable@impeccable` | Optional | vet | Polish and critique. |
| ui-taste | `uizze.sh@ui-taste` | Optional | vet | |

Pack: `leonxlnx/taste-skill` (also `high-end-visual-design`, `redesign-existing-projects`,
`minimalist-ui`, `brandkit`): take `redesign-existing-projects` when restyling an existing site.

## Animation and motion design

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| motion | `motiondivision/ai-kit@motion` | Essential with Motion | reviewed 8dc4f7a | |
| emil-design-eng, improve-animations, review-animations | `emilkowalski/skills@…` | Essential for UI animation work | md-only 2d22863 | Animation craft from a well-known design engineer. |
| find-animation-opportunities | `emilkowalski/skills@find-animation-opportunities` | Optional | md-only 2d22863 | |

## Mobile apps

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| expo-native-ui, expo-animation, expo-router | `expo/skills@…` | Essential for Expo / React Native | reviewed 7ddc1f5 (optional extra: a feedback command; don't run it) | Official Expo. `expo-animation` supersedes `emilkowalski/skills@animate-expo`. |
| expo-dev-client, expo-tailwind-setup, expo-data-fetching, expo-ui | `expo/skills@…` | When relevant | md-only 7ddc1f5 | |
| vercel-react-native-skills | `vercel-labs/agent-skills@vercel-react-native-skills` | When React Native | reviewed 063bee9 | For animation, follow `expo-animation` where they differ. |
| animate-expo, mobile-native, write-swift | `emilkowalski/skills@…` | When relevant | md-only 2d22863 | |
| design-mobile-apps | `designed-by-ai/skills@design-mobile-apps` | Optional | vet | |

## Databases and backend

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| supabase, supabase-postgres-best-practices | `supabase/agent-skills@…` | Essential with Supabase/Postgres | reviewed c9be0e9 (optional extras: Supabase CLI, MCP troubleshooting) | Official. |
| prisma-* | `prisma/skills@…` | Essential with Prisma | vet | Official. |
| neon-postgres | `neondatabase/agent-skills@neon-postgres` | With Neon | vet | Official. |
| firebase-* | `firebase/agent-skills@…` | With Firebase | vet | Official. |
| convex | `convex/agent-skills@convex` | With Convex | vet | Official. |
| better-auth-best-practices | `better-auth/skills@better-auth-best-practices` | With Better Auth | vet | Official. |

## Payments

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| stripe-best-practices | `stripe/ai@stripe-best-practices` | Essential with Stripe | reviewed 579b067 (optional extra: Stripe CLI) | Official: Checkout, subscriptions, Customer Portal, webhooks, keys. |

## Cloud, DevOps, security

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| cloudflare, durable-objects | `cloudflare/skills@…` | With Cloudflare | vet | Official. |
| deploy-to-vercel | `vercel-labs/agent-skills@deploy-to-vercel` | With Vercel | scripts 063bee9 | |
| azure-* | `microsoft/azure-skills@…` | Only with Azure | vet | Official; large pack. |
| ci-cd-and-automation, security-and-hardening | `addyosmani/agent-skills@…` | When relevant | md-only aeac41d | |
| differential-review | `trailofbits/skills@differential-review` | For security review | vet | Trail of Bits. |

## Video

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| remotion-create, -render, -studio, -interactivity | `remotion-dev/skills@…` | Essential for Remotion | reviewed 039e8a2 | Official Remotion. |
| remotion-markup | `remotion-dev/skills@remotion-markup` | When animating Remotion scenes | system-changing at 039e8a2 (maps script needs `@turf/turf`) | Ask. |
| hyperframes, general-video, product-launch-video, faceless-explainer, pr-to-video, talking-head-recut | `heygen-com/hyperframes@…` | Alternative engine to Remotion (HTML-based) | cli (`npx hyperframes`, usage quotas) | HeyGen's official pack; ask, check cost. |
| ffmpeg skills | search | When cutting, encoding, captioning | vet | |

## Images, graphics, audio

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| canvas-design | `anthropics/skills@canvas-design` | For posters and static graphics | md-only dbd4588 | |
| brandkit, image-to-code | `leonxlnx/taste-skill@…` | Brand assets; turning images into UI | vet | |
| algorithmic-art | `anthropics/skills@algorithmic-art` | Generative art | scripts dbd4588 | |
| AI image / video / music generation | many | — | usually cli + paid API | Most need paid API keys. Check the user's budget rules first. |

## Writing and documents

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| writing-beats, writing-shape, writing-fragments | `mattpocock/skills@…` | For long-form writing | md-only 5beb35b | |
| doc-coauthoring | `anthropics/skills@doc-coauthoring` | Co-writing long documents | md-only dbd4588 | |
| docx, pptx, xlsx, pdf | `anthropics/skills@…` | Essential when producing that file type | scripts dbd4588 | Anthropic's official document skills. |

## Marketing, SEO, sales

Pack: `coreyhaines31/marketingskills` (52 skills, 51 md-only at e85f3cb). Essential picks by task:
`copywriting`, `seo-audit`, `programmatic-seo`, `content-strategy`, `site-architecture`,
`ad-creative`, `cold-email`, `customer-research`, `competitor-profiling`. `copywriting`, `cold-email`
and `seo-audit` are reviewed e85f3cb; the rest are md-only e85f3cb except `conversion-tracking`
(scripts).

## Research and web data

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| agent-reach | `panniantong/agent-reach@agent-reach` | Essential for multi-platform research (Reddit, X, YouTube…) | cli (`agent-reach` via pipx) | Ask. |
| research | `mattpocock/skills@research` | For research tasks | md-only 5beb35b | |
| agent-browser | `vercel-labs/agent-browser@agent-browser` | When a scripted browser is needed | cli | |
| playwright-cli | `microsoft/playwright-cli@playwright-cli` | Browser automation | cli | |

## Codebase understanding and agent workflow

| Skill | Install as | Need | Tier | Why |
|---|---|---|---|---|
| graphify | `graphify-labs/graphify` | Optional | cli (Python, `uv tool install`) | Knowledge graph of a large codebase. |
| zoom-out, handoff, triage | `mattpocock/skills@…` | Optional | md-only 5beb35b | |
| verification-before-completion | `obra/superpowers@verification-before-completion` | Optional | md-only bb92a77 | |
| skill-creator | `anthropics/skills@skill-creator` | When writing skills | scripts dbd4588 | |

## Publishers

Prefer, in order: the tool's own publisher (`motiondivision`, `remotion-dev`, `supabase`,
`prisma`, `expo`, `cloudflare`, `firebase`, `shadcn-ui`, `microsoft`, `heygen-com`…); Anthropic
(`anthropics`); established practitioners with real adoption (`mattpocock`, `obra`, `vercel-labs`,
`addyosmani`, `emilkowalski`, `coreyhaines31`, `trailofbits`, `leonxlnx`, `dietrichgebert`); then
others with a skill built for the exact task.

**Copies and lookalikes.** The sweep found accounts whose every skill is a copy of another
publisher's skill, several in repositories named after a famous pack (e.g. `<owner>/superpowers`
where the original is `obra/superpowers`), with install counts in the hundreds of thousands. When
the same skill name appears under several owners, find and use the original publisher. A repo that
reuses a well-known pack's name under a different owner is a red flag (`vetting.md` section 4).

## Installed already?

A skill counts as installed if any installed skill has the same `name`, including plugin
namespaces (`anthropic-skills:ponytail` is `ponytail`). Do not install a second copy.
