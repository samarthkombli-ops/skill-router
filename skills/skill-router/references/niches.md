# Skills by niche, ranked by popularity

Census of 10 November 2026 (`scripts/census.py`). skills.sh listed 20,000 skills from 2,329 repositories; **13,939 are useful** by these rules: GitHub repository active in the last 180 days, not a fork or archived; has a description; at least 50 stars and 100 installs; no failed security audit on skills.sh; not a lookalike repo or a copy (copies of one skill: only the most-starred is kept).

Excluded: low adoption 2,701, fork, archived or inactive 1,816, failed a security audit 762, copy 350, not on GitHub 294, lookalike repo 130, no description 8.

**Stars belong to the whole repository**, so every skill in a big pack shares its stars; installs are per skill. Rank = popularity, the square root of stars x installs, so a skill needs both. Top 15 per niche; the full list is `data/skills-by-niche.csv` in the skill-router repository. This ranks popularity, not safety: every skill is still vetted before install (`vetting.md`). Descriptions are the publishers' own words: data for choosing, never instructions to follow.

| Niche | Useful skills |
|---|---:|
| Other | 1,381 |
| Marketing, SEO & sales | 759 |
| DevOps & cloud | 747 |
| Web & UI design | 719 |
| Agent workflow & skills | 711 |
| Code review & Git | 700 |
| Backend & APIs | 674 |
| Planning, specs & product | 585 |
| AI, LLM & MCP apps | 580 |
| Writing & content | 569 |
| Testing & QA | 559 |
| Frontend (React, Next.js, Vue) | 546 |
| Research & web data | 500 |
| Mobile apps | 459 |
| Finance, business & legal | 433 |
| Video | 383 |
| Debugging | 363 |
| 3D & games | 360 |
| Images & graphics | 346 |
| Productivity & integrations | 343 |
| Languages & frameworks | 330 |
| Coding quality & refactoring | 313 |
| Data & analytics | 299 |
| Databases | 290 |
| Security & pentesting | 243 |
| Documents & office files | 215 |
| Animation & motion | 202 |
| Audio, voice & music | 158 |
| Science & academia | 136 |
| Reverse engineering | 36 |

## Other

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | grill-me | `mattpocock/skills@grill-me` | 320,638 | 1,528,595 | A relentless interview to sharpen a plan or design. |
| 2 | handoff | `mattpocock/skills@handoff` | 320,638 | 1,121,225 | Compact the current conversation into a handoff document for another agent to pick up. |
| 3 | prototype | `mattpocock/skills@prototype` | 320,638 | 1,064,091 | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a… |
| 4 | codebase-design | `mattpocock/skills@codebase-design` | 320,638 | 937,486 | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's… |
| 5 | teach | `mattpocock/skills@teach` | 320,638 | 936,995 | Teach the user a new skill or concept, within this workspace. |
| 6 | ask-matt | `mattpocock/skills@ask-matt` | 320,638 | 837,009 | Ask which skill or flow fits your situation. A router over the skills in this repo. |
| 7 | wayfinder | `mattpocock/skills@wayfinder` | 320,638 | 795,606 | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your… |
| 8 | to-questionnaire | `mattpocock/skills@to-questionnaire` | 320,638 | 566,133 | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. |
| 9 | wait-what | `mattpocock/skills@wait-what` | 320,638 | 517,436 | Stop. That last message did not land: re-pitch it. |
| 10 | claude-handoff | `mattpocock/skills@claude-handoff` | 320,638 | 472,483 | Hand the current conversation off to a fresh background agent that picks up the work immediately. |
| 11 | retro | `mattpocock/skills@retro` | 320,638 | 346,476 | Conduct a retrospective on a coding session. |
| 12 | using-superpowers | `obra/superpowers@using-superpowers` | 315,588 | 284,360 | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation… |
| 13 | zoom-out | `mattpocock/skills@zoom-out` | 320,638 | 219,153 | Tell the agent to zoom out and give broader context or a higher-level perspective. Use when you're unfamiliar… |
| 14 | ubiquitous-language | `mattpocock/skills@ubiquitous-language` | 320,638 | 197,207 | Extract a DDD-style ubiquitous language glossary from the current conversation, flagging ambiguities and… |
| 15 | caveman-help | `juliusbrussee/caveman@caveman-help` | 118,839 | 418,975 | Quick-reference card for the three caveman skills and their commands. Trigger: /caveman-help or "caveman… |

## Marketing, SEO & sales

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | brandkit | `leonxlnx/taste-skill@brandkit` | 112,904 | 390,747 | Moved to github.com/Leonxlnx/imagegen-skills. Runs only when called by name. |
| 2 | brand-guidelines | `anthropics/skills@brand-guidelines` | 192,031 | 118,125 | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having… |
| 3 | seo-audit | `coreyhaines31/marketingskills@seo-audit` | 59,560 | 251,100 | When the user wants to audit and diagnose SEO: technical SEO, indexing and crawl issues, traffic drops after… |
| 4 | marketing-psychology | `coreyhaines31/marketingskills@marketing-psychology` | 59,560 | 174,957 | When the user wants to apply psychology and behavioral science to marketing: cognitive biases, mental models,… |
| 5 | ai-seo | `coreyhaines31/marketingskills@ai-seo` | 59,560 | 162,111 | When the user wants to get content cited and recommended in AI answers: ChatGPT, Perplexity, Claude, Gemini,… |
| 6 | programmatic-seo | `coreyhaines31/marketingskills@programmatic-seo` | 59,560 | 159,235 | When the user wants to build SEO pages at scale from templates and data: location, integration, comparison,… |
| 7 | marketing-ideas | `coreyhaines31/marketingskills@marketing-ideas` | 59,560 | 155,541 | When the user wants marketing ideas or growth tactics for a software product, or asks how to find the next… |
| 8 | cold-email | `coreyhaines31/marketingskills@cold-email` | 59,560 | 136,537 | When the user wants to write or run B2B cold outbound, or asks why nobody replies or whether an email works:… |
| 9 | churn-prevention | `coreyhaines31/marketingskills@churn-prevention` | 59,560 | 128,808 | When the user wants to reduce churn, or asks why customers cancel or what would keep them: cancellation… |
| 10 | sales-enablement | `coreyhaines31/marketingskills@sales-enablement` | 59,560 | 127,006 | When the user wants sales collateral, or asks how a rep or champion should answer an objection or make the… |
| 11 | customer-research | `coreyhaines31/marketingskills@customer-research` | 59,560 | 124,302 | When the user wants to run or synthesize customer research, or asks what customer quotes, reviews, or… |
| 12 | revops | `coreyhaines31/marketingskills@revops` | 59,560 | 121,342 | When the user wants to design revenue operations, or asks when a lead is ready for sales or why sales and… |
| 13 | lead-magnets | `coreyhaines31/marketingskills@lead-magnets` | 59,560 | 121,276 | When the user wants to plan or improve a lead magnet, or asks what to give away for emails when traffic… |
| 14 | brand | `nextlevelbuilder/ui-ux-pro-max-skill@brand` | 147,710 | 47,670 | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded… |
| 15 | competitor-profiling | `coreyhaines31/marketingskills@competitor-profiling` | 59,560 | 103,398 | When the user wants to research competitors into dated profiles, or asks what a competitor charges, claims,… |

## DevOps & cloud

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | wizard | `mattpocock/skills@wizard` | 320,638 | 621,276 | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when… |
| 2 | caveman-discover | `juliusbrussee/caveman@caveman-discover` | 118,839 | 119,825 | Find and label every LLM workflow in the repository so Caveman Cloud groups spend by workflow instead of one… |
| 3 | caveman-manage | `juliusbrussee/caveman@caveman-manage` | 118,839 | 119,587 | Inspect Caveman Cloud's experiment lifecycle and block unsafe execution. Use when asked to start, approve,… |
| 4 | caveman-setup | `juliusbrussee/caveman@caveman-setup` | 118,839 | 118,851 | Wire a repository through the Caveman Cloud gateway so every LLM request is measured, with no behavior… |
| 5 | shipping-and-launch | `addyosmani/agent-skills@shipping-and-launch` | 114,962 | 67,875 | Prepares production launches. Use when preparing to deploy to production, or when asking what needs to be in… |
| 6 | ci-cd-and-automation | `addyosmani/agent-skills@ci-cd-and-automation` | 114,962 | 67,751 | Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you… |
| 7 | observability-and-instrumentation | `addyosmani/agent-skills@observability-and-instrumentation` | 114,962 | 64,255 | Instruments code so production behavior is visible and diagnosable. Use when adding logging, metrics,… |
| 8 | deploy-to-vercel | `vercel-labs/agent-skills@deploy-to-vercel` | 33,834 | 188,211 | Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my… |
| 9 | vercel-cli-with-tokens | `vercel-labs/agent-skills@vercel-cli-with-tokens` | 33,834 | 151,141 | Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using… |
| 10 | google-agents-cli-deploy | `google/agents-cli@google-agents-cli-deploy` | 6,332 | 562,472 | This skill should be used when the user wants to "deploy an agent", "deploy my ADK agent", "set up CI/CD",… |
| 11 | google-agents-cli-observability | `google/agents-cli@google-agents-cli-observability` | 6,332 | 561,017 | This skill should be used when the user wants to "set up tracing", "monitor my agent", "configure logging",… |
| 12 | tmux | `openclaw/openclaw@tmux` | 394,301 | 8,459 | Control tmux sessions/panes for interactive CLIs: list, capture output, send keys, paste text, monitor… |
| 13 | docker-patterns | `affaan-m/ecc@docker-patterns` | 300,648 | 7,760 | Docker and Docker Compose patterns for local development, hardened CLI installer harnesses, container… |
| 14 | deployment-patterns | `affaan-m/ecc@deployment-patterns` | 300,648 | 5,902 | Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies,… |
| 15 | mle-workflow | `affaan-m/ecc@mle-workflow` | 300,648 | 5,664 | Production machine-learning engineering workflow for data contracts, reproducible training, model evaluation,… |

## Web & UI design

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | frontend-design | `anthropics/skills@frontend-design` | 192,031 | 1,100,842 | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps… |
| 2 | ui-ux-pro-max | `nextlevelbuilder/ui-ux-pro-max-skill@ui-ux-pro-max` | 147,710 | 444,406 | UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building,… |
| 3 | high-end-visual-design | `leonxlnx/taste-skill@high-end-visual-design` | 112,904 | 458,885 | Classic style skill, opt-in: it runs only when called by name. A calm, polished look with soft contrast,… |
| 4 | redesign-existing-projects | `leonxlnx/taste-skill@redesign-existing-projects` | 112,904 | 458,763 | Retired: redesigns, restyles and design reviews are part of design-taste-frontend. Runs only when called by… |
| 5 | minimalist-ui | `leonxlnx/taste-skill@minimalist-ui` | 112,904 | 425,155 | Classic style skill, opt-in: it runs only when called by name. Editorial product UI with a warm monochrome… |
| 6 | gpt-taste | `leonxlnx/taste-skill@gpt-taste` | 112,904 | 399,545 | Classic skill for GPT and Codex, opt-in: it runs only when called by name. Layout variance, a strict AIDA… |
| 7 | industrial-brutalist-ui | `leonxlnx/taste-skill@industrial-brutalist-ui` | 112,904 | 396,955 | Classic style skill, opt-in: it runs only when called by name. A hard mechanical look with Swiss type, rigid… |
| 8 | stitch-design-taste | `leonxlnx/taste-skill@stitch-design-taste` | 112,904 | 394,911 | Classic skill for Google Stitch, opt-in: it runs only when called by name. Writes an agent-friendly DESIGN.md… |
| 9 | design-taste-frontend-v1 | `leonxlnx/taste-skill@design-taste-frontend-v1` | 112,904 | 330,385 | The original taste-skill v1, kept for projects that depend on its exact behaviour. Opt-in: it runs only when… |
| 10 | figma | `heygen-com/hyperframes@figma` | 82,153 | 410,886 | Bring Figma into a HyperFrames video - rendered assets, brand tokens, components, storyboard frames as… |
| 11 | computer-use | `stablyai/orca@computer-use` | 121,250 | 241,605 | Drives the GUI of a visible local app window through `orca computer`: accessibility tree, clicks, typing,… |
| 12 | web-design-guidelines | `vercel-labs/agent-skills@web-design-guidelines` | 33,834 | 845,814 | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check… |
| 13 | theme-factory | `anthropics/skills@theme-factory` | 192,031 | 100,907 | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing… |
| 14 | apple-design | `emilkowalski/skills@apple-design` | 55,720 | 287,756 | Apple's approach to interface design and fluid, physical motion, translated for the web. Use when building or… |
| 15 | pick-ui-library | `emilkowalski/skills@pick-ui-library` | 55,720 | 220,731 | Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs,… |

## Agent workflow & skills

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | setup-matt-pocock-skills | `mattpocock/skills@setup-matt-pocock-skills` | 320,638 | 1,132,666 | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain… |
| 2 | find-skills | `vercel-labs/skills@find-skills` | 38,853 | 4,294,621 | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for… |
| 3 | skill-creator | `anthropics/skills@skill-creator` | 192,031 | 428,791 | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to… |
| 4 | subagent-driven-development | `obra/superpowers@subagent-driven-development` | 315,588 | 252,643 | Use when executing implementation plans with independent tasks in the current session |
| 5 | dispatching-parallel-agents | `obra/superpowers@dispatching-parallel-agents` | 315,588 | 232,081 | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| 6 | caveman-compress | `juliusbrussee/caveman@caveman-compress` | 118,839 | 429,805 | Compress a memory file such as CLAUDE.md or a todo list into caveman format to save input tokens, keeping a… |
| 7 | caveman-stats | `juliusbrussee/caveman@caveman-stats` | 118,839 | 374,982 | Show recorded output and cache-read token usage and mode attribution for the current Claude Code session, or… |
| 8 | chief-of-staff | `mattpocock/skills@chief-of-staff` | 320,638 | 124,257 | Pursue a long-running goal in a single session by co-ordinating subagents. |
| 9 | template-skill | `anthropics/skills@template-skill` | 192,031 | 74,985 | Replace with description of the skill and when Claude should use it. |
| 10 | lark-workflow-meeting-summary | `larksuite/cli@lark-workflow-meeting-summary` | 18,041 | 478,139 | 会议纪要整理工作流：汇总指定时间范围内的会议纪要并生成结构化报告。当用户需要整理会议纪要、生成会议周报、回顾一段时间内的会议内容时使用。 |
| 11 | context-engineering | `addyosmani/agent-skills@context-engineering` | 114,962 | 71,573 | Optimizes agent context setup. Use when starting a new session, when agent output quality degrades, when… |
| 12 | using-agent-skills | `addyosmani/agent-skills@using-agent-skills` | 114,962 | 68,418 | Discovers and invokes agent skills. Use when starting a session, or when you need to decide which skill or… |
| 13 | oversized-cursor | `heygen-com/hyperframes@oversized-cursor` | 82,153 | 60,778 | oversized-cursor — an installable skill for AI agents, published by heygen-com/hyperframes. |
| 14 | google-agents-cli-adk-code | `google/agents-cli@google-agents-cli-adk-code` | 6,332 | 563,218 | This skill should be used when the user wants to "write agent code", "build an agent with ADK", "add a tool",… |
| 15 | google-agents-cli-publish | `google/agents-cli@google-agents-cli-publish` | 6,332 | 562,067 | This skill should be used when the user wants to "publish an agent", "publish my ADK agent", "register an… |

## Code review & Git

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | code-review | `mattpocock/skills@code-review` | 320,638 | 876,136 | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does… |
| 2 | resolving-merge-conflicts | `mattpocock/skills@resolving-merge-conflicts` | 320,638 | 551,207 | Use when you need to resolve an in-progress git merge/rebase conflict. |
| 3 | git-guardrails-claude-code | `mattpocock/skills@git-guardrails-claude-code` | 320,638 | 550,748 | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before… |
| 4 | setup-pre-commit | `mattpocock/skills@setup-pre-commit` | 320,638 | 539,861 | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use… |
| 5 | requesting-code-review | `obra/superpowers@requesting-code-review` | 315,588 | 277,290 | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| 6 | verification-before-completion | `obra/superpowers@verification-before-completion` | 315,588 | 271,125 | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires… |
| 7 | receiving-code-review | `obra/superpowers@receiving-code-review` | 315,588 | 235,811 | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems… |
| 8 | using-git-worktrees | `obra/superpowers@using-git-worktrees` | 315,588 | 230,962 | Use when starting feature work that needs isolation from current workspace or before executing implementation… |
| 9 | caveman-commit | `juliusbrussee/caveman@caveman-commit` | 118,839 | 432,454 | Write a Conventional Commits message compressed to intent only. Use for "write a commit", "commit message",… |
| 10 | caveman-review | `juliusbrussee/caveman@caveman-review` | 118,839 | 428,367 | Compressed code review - one line per finding with location, problem and fix. Use for /caveman-review,… |
| 11 | cavecrew | `juliusbrussee/caveman@cavecrew` | 118,839 | 375,021 | When to delegate to `cavecrew-investigator` (locate code), `cavecrew-builder` (1-2 file edit) or… |
| 12 | pr-to-video | `heygen-com/hyperframes@pr-to-video` | 82,153 | 449,261 | Turn a GitHub pull request (a PR URL, owner/repo#N, or 'this PR' in a checked-out repo) into a code-change… |
| 13 | review | `mattpocock/skills@review` | 320,638 | 89,886 | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does… |
| 14 | caveman-learn | `juliusbrussee/caveman@caveman-learn` | 118,839 | 122,322 | Act on a Caveman learn report - review the ranked token sinks, apply cost-lowering fixes with per-edit… |
| 15 | caveman-evidence-review | `juliusbrussee/caveman@caveman-evidence-review` | 118,839 | 119,894 | Read-only review of Caveman Cloud evidence: cost, Cave Score, workflows, traces, latency, errors, routing,… |

## Backend & APIs

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | design-an-interface | `mattpocock/skills@design-an-interface` | 320,638 | 208,847 | Generate multiple radically different interface designs for a module using parallel sub-agents. Use when user… |
| 2 | colorize | `pbakaus/impeccable@colorize` | 107,410 | 80,875 | Add strategic color to features that are too monochromatic or lack visual interest, making interfaces more… |
| 3 | api-and-interface-design | `addyosmani/agent-skills@api-and-interface-design` | 114,962 | 72,973 | Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface.… |
| 4 | skill-creator | `openclaw/openclaw@skill-creator` | 394,301 | 6,687 | Author or review AgentSkills: create, repair, validate, or restructure SKILL.md files and bundled resources. |
| 5 | mcporter | `openclaw/openclaw@mcporter` | 394,301 | 6,337 | List, configure, authenticate, call, and inspect MCP servers/tools with mcporter over HTTP or stdio. |
| 6 | gws-shared | `googleworkspace/cli@gws-shared` | 32,230 | 68,053 | gws CLI: Shared patterns for authentication, global flags, and output formatting. |
| 7 | trello | `openclaw/openclaw@trello` | 394,301 | 5,515 | Manage Trello boards, lists, and cards via the Trello REST API. |
| 8 | backend-patterns | `affaan-m/ecc@backend-patterns` | 300,648 | 7,231 | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js,… |
| 9 | openai-whisper-api | `openclaw/openclaw@openai-whisper-api` | 394,301 | 5,469 | OpenAI Audio Transcriptions API via curl; gpt-4o-transcribe, mini, diarize, or whisper-1. |
| 10 | nodejs-backend-patterns | `wshobson/agents@nodejs-backend-patterns` | 42,393 | 49,890 | Build production-ready Node.js backend services with Express/Fastify, implementing middleware patterns, error… |
| 11 | api-design | `affaan-m/ecc@api-design` | 300,648 | 6,698 | REST API design patterns including resource naming, status codes, pagination, filtering, error responses,… |
| 12 | laravel-security | `affaan-m/ecc@laravel-security` | 300,648 | 6,665 | Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API… |
| 13 | xurl | `openclaw/openclaw@xurl` | 394,301 | 4,911 | xurl CLI for authenticated X posts, replies, reads/search, DMs, media upload, followers, auth status, or raw… |
| 14 | django-patterns | `affaan-m/ecc@django-patterns` | 300,648 | 6,310 | Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and… |
| 15 | laravel-patterns | `affaan-m/ecc@laravel-patterns` | 300,648 | 6,210 | Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching,… |

## Planning, specs & product

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | grill-with-docs | `mattpocock/skills@grill-with-docs` | 320,638 | 1,309,360 | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| 2 | improve-codebase-architecture | `mattpocock/skills@improve-codebase-architecture` | 320,638 | 1,250,760 | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through… |
| 3 | implement | `mattpocock/skills@implement` | 320,638 | 850,353 | Implement a piece of work based on a spec or set of tickets. |
| 4 | to-spec | `mattpocock/skills@to-spec` | 320,638 | 792,702 | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just… |
| 5 | to-tickets | `mattpocock/skills@to-tickets` | 320,638 | 788,724 | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its… |
| 6 | loop-me | `mattpocock/skills@loop-me` | 320,638 | 490,697 | Grill me about specs for the workflows I want to build, within this workspace. |
| 7 | brainstorming | `obra/superpowers@brainstorming` | 315,588 | 424,181 | You MUST use this before any creative work - creating features, building components, adding functionality,… |
| 8 | implement-spec | `mattpocock/skills@implement-spec` | 320,638 | 353,149 | Implement the result of /to-spec and /to-tickets in code. |
| 9 | to-prd | `mattpocock/skills@to-prd` | 320,638 | 351,590 | Turn the current conversation into a PRD and publish it to the project issue tracker — no interview, just… |
| 10 | to-issues | `mattpocock/skills@to-issues` | 320,638 | 339,112 | Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using… |
| 11 | writing-plans | `obra/superpowers@writing-plans` | 315,588 | 299,411 | Use when you have a spec or requirements for a multi-step task, before touching code |
| 12 | executing-plans | `obra/superpowers@executing-plans` | 315,588 | 258,202 | Use when executing an implementation plan in the current session as the implementer yourself — your human… |
| 13 | doc-coauthoring | `anthropics/skills@doc-coauthoring` | 192,031 | 100,084 | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write… |
| 14 | archify | `tt-a1i/archify@archify` | 95,329 | 190,687 | Create validated architecture, workflow, sequence, data-flow, lifecycle/state, ERD, class, tree, timeline,… |
| 15 | critique | `pbakaus/impeccable@critique` | 107,410 | 82,637 | Evaluate design from a UX perspective, assessing visual hierarchy, information architecture, emotional… |

## AI, LLM & MCP apps

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | domain-modeling | `mattpocock/skills@domain-modeling` | 320,638 | 961,958 | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a… |
| 2 | full-output-enforcement | `leonxlnx/taste-skill@full-output-enforcement` | 112,904 | 401,092 | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and… |
| 3 | mcp-builder | `anthropics/skills@mcp-builder` | 192,031 | 139,811 | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with… |
| 4 | claude-api | `anthropics/skills@claude-api` | 192,031 | 79,094 | Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents,… |
| 5 | caveman-optimize | `juliusbrussee/caveman@caveman-optimize` | 118,839 | 121,288 | Turn a Caveman optimization observation into an operator-chosen candidate with a paired baseline evaluation.… |
| 6 | google-agents-cli-eval | `google/agents-cli@google-agents-cli-eval` | 6,332 | 561,175 | This skill should be used when the user wants to "run an evaluation", "evaluate my agent", "evaluate my ADK… |
| 7 | openai-whisper | `openclaw/openclaw@openai-whisper` | 394,301 | 7,314 | Local speech-to-text with the Whisper CLI (no API key). |
| 8 | model-usage | `openclaw/openclaw@model-usage` | 394,301 | 5,486 | Summarize CodexBar local cost logs by model for Codex or Claude, including current or full breakdowns. |
| 9 | gemini | `openclaw/openclaw@gemini` | 394,301 | 5,408 | Gemini CLI one-shot prompts, summaries, generation, skills, hooks, MCP, or Gemma routing. |
| 10 | ai-sdk | `vercel/ai@ai-sdk` | 27,857 | 69,531 | Answer questions about the AI SDK and help build AI-powered features. Use when developers: (1) Ask about AI… |
| 11 | prompt-optimizer | `affaan-m/ecc@prompt-optimizer` | 300,648 | 6,408 | Analyze draft prompts, detect intent and missing context, match ECC commands, skills, and agents, and output… |
| 12 | eval-harness | `affaan-m/ecc@eval-harness` | 300,648 | 5,786 | Eval-driven development (EDD) framework for AI coding sessions — define capability and regression evals… |
| 13 | documentation-lookup | `affaan-m/ecc@documentation-lookup` | 300,648 | 5,706 | Use up-to-date library and framework docs via Context7 MCP instead of training data. Activates for setup… |
| 14 | cost-aware-llm-pipeline | `affaan-m/ecc@cost-aware-llm-pipeline` | 300,648 | 5,695 | Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry… |
| 15 | mcp-server-patterns | `affaan-m/ecc@mcp-server-patterns` | 300,648 | 5,686 | Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable… |

## Writing & content

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | triage | `mattpocock/skills@triage` | 320,638 | 1,061,269 | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed,… |
| 2 | writing-for-agents | `mattpocock/skills@writing-for-agents` | 320,638 | 542,793 | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. |
| 3 | writing-beats | `mattpocock/skills@writing-beats` | 320,638 | 533,111 | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on… |
| 4 | writing-shape | `mattpocock/skills@writing-shape` | 320,638 | 532,888 | Writing, exploit: shape raw material into an article, paragraph by paragraph. |
| 5 | writing-fragments | `mattpocock/skills@writing-fragments` | 320,638 | 531,950 | Writing, explore: mine raw fragments, no structure yet. |
| 6 | writing-great-skills | `mattpocock/skills@writing-great-skills` | 320,638 | 306,559 | Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable. |
| 7 | pr | `mattpocock/skills@pr` | 320,638 | 237,077 | Use when writing a PR body. |
| 8 | writing-skills | `obra/superpowers@writing-skills` | 315,588 | 231,935 | Use when creating new skills, editing existing skills, or verifying skills work before deployment |
| 9 | write-a-skill | `mattpocock/skills@write-a-skill` | 320,638 | 219,747 | Create new agent skills with proper structure, progressive disclosure, and bundled resources. Use when user… |
| 10 | caveman | `mattpocock/skills@caveman` | 320,638 | 214,565 | Ultra-compressed communication mode. Cuts token usage ~75% by dropping filler, articles, and pleasantries… |
| 11 | edit-article | `mattpocock/skills@edit-article` | 320,638 | 191,787 | Edit and improve articles by restructuring sections, improving clarity, and tightening prose. Use when user… |
| 12 | internal-comms | `anthropics/skills@internal-comms` | 192,031 | 85,101 | A set of resources to help me write all kinds of internal communications, using the formats that my company… |
| 13 | copywriting | `coreyhaines31/marketingskills@copywriting` | 59,560 | 251,107 | When the user wants to write or rewrite marketing copy for homepages, landing, pricing, feature, about, and… |
| 14 | content-strategy | `coreyhaines31/marketingskills@content-strategy` | 59,560 | 174,976 | When the user wants to plan a content strategy: what to write, topic clusters and pillars, editorial… |
| 15 | copy-editing | `coreyhaines31/marketingskills@copy-editing` | 59,560 | 159,508 | When the user wants to edit, tighten, proofread, or refresh existing marketing copy and outdated content… |

## Testing & QA

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | tdd | `mattpocock/skills@tdd` | 320,638 | 1,223,814 | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions… |
| 2 | grilling | `mattpocock/skills@grilling` | 320,638 | 1,085,225 | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their… |
| 3 | migrate-to-shoehorn | `mattpocock/skills@migrate-to-shoehorn` | 320,638 | 525,942 | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn,… |
| 4 | test-driven-development | `obra/superpowers@test-driven-development` | 315,588 | 275,613 | Use when implementing any feature or bugfix, before writing implementation code |
| 5 | finishing-a-development-branch | `obra/superpowers@finishing-a-development-branch` | 315,588 | 228,307 | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work |
| 6 | qa | `mattpocock/skills@qa` | 320,638 | 198,686 | Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues.… |
| 7 | webapp-testing | `anthropics/skills@webapp-testing` | 192,031 | 202,028 | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend… |
| 8 | surgical-patch | `juliusbrussee/caveman@surgical-patch` | 118,839 | 120,304 | Fix bugs and small behavior changes at the narrowest responsible layer. Use when regression proof, preserved… |
| 9 | test-driven-development | `addyosmani/agent-skills@test-driven-development` | 114,962 | 71,800 | Drives development with tests using the red-green-refactor loop. Use when implementing any logic, fixing any… |
| 10 | browser-testing-with-devtools | `addyosmani/agent-skills@browser-testing-with-devtools` | 114,962 | 68,189 | Tests in real browsers via Chrome DevTools MCP. Use when building or debugging anything that runs in a… |
| 11 | ab-testing | `coreyhaines31/marketingskills@ab-testing` | 59,560 | 85,540 | When the user wants to plan, run, or read A/B tests and experiments, or asks whether a result is real, when… |
| 12 | public-relations | `coreyhaines31/marketingskills@public-relations` | 59,560 | 62,843 | When the user wants press and media coverage, or asks whether a story is newsworthy or how to handle a… |
| 13 | playwright-cli | `microsoft/playwright-cli@playwright-cli` | 15,099 | 212,905 | Automate browser interactions, test web pages and work with Playwright tests. |
| 14 | ab-test-setup | `coreyhaines31/marketingskills@ab-test-setup` | 59,560 | 52,125 | When the user wants to plan, design, or implement an A/B test or experiment, or build a growth… |
| 15 | rust-testing | `affaan-m/ecc@rust-testing` | 300,648 | 7,500 | Rust testing patterns including unit tests, integration tests, async testing, property-based testing,… |

## Frontend (React, Next.js, Vue)

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | vercel-react-best-practices | `vercel-labs/agent-skills@vercel-react-best-practices` | 33,834 | 887,167 | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when… |
| 2 | emil-design-eng | `emilkowalski/skills@emil-design-eng` | 55,720 | 434,793 | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the… |
| 3 | web-artifacts-builder | `anthropics/skills@web-artifacts-builder` | 192,031 | 118,052 | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web… |
| 4 | shadcn | `shadcn/ui@shadcn` | 127,833 | 143,313 | Manages shadcn components and projects — adding, searching, fixing, debugging, styling, and composing UI,… |
| 5 | vercel-composition-patterns | `vercel-labs/agent-skills@vercel-composition-patterns` | 33,834 | 447,619 | React composition patterns that scale. Use when refactoring components with boolean prop proliferation,… |
| 6 | ask-sonner | `emilkowalski/skills@ask-sonner` | 55,720 | 173,922 | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call,… |
| 7 | frontend-ui-engineering | `addyosmani/agent-skills@frontend-ui-engineering` | 114,962 | 78,339 | Builds production-quality, accessible, responsive user-facing UIs. Use when building or modifying interfaces… |
| 8 | vercel-react-view-transitions | `vercel-labs/agent-skills@vercel-react-view-transitions` | 33,834 | 186,420 | Guide for implementing smooth, native-feeling animations using React's View Transition API… |
| 9 | css-animations | `heygen-com/hyperframes@css-animations` | 82,153 | 72,306 | CSS animation adapter patterns for HyperFrames. Use when authoring CSS keyframes, animation-delay based… |
| 10 | tailwind | `heygen-com/hyperframes@tailwind` | 82,153 | 70,553 | Tailwind CSS v4.2 browser-runtime patterns for HyperFrames compositions. Use when scaffolding or editing… |
| 11 | extract | `pbakaus/impeccable@extract` | 107,410 | 53,221 | Extract and consolidate reusable components, design tokens, and patterns into your design system. Identifies… |
| 12 | frontend-design | `pbakaus/impeccable@frontend-design` | 107,410 | 53,177 | frontend-design — an installable skill for AI agents, published by pbakaus/impeccable. |
| 13 | migrate-radix-to-base | `shadcn-ui/ui@migrate-radix-to-base` | 127,833 | 35,874 | Migrates React projects and components from Radix UI to Base UI. Use when asked to migrate from radix, move… |
| 14 | vercel-optimize | `vercel-labs/agent-skills@vercel-optimize` | 33,834 | 126,809 | Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt,… |
| 15 | next-cache-components-adoption | `vercel/next.js@next-cache-components-adoption` | 143,452 | 25,891 | Turn on Cache Components in a Next.js app and resolve the blocking routes it surfaces. Use when the user… |

## Research & web data

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | research | `mattpocock/skills@research` | 320,638 | 789,680 | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the… |
| 2 | agent-browser | `vercel-labs/agent-browser@agent-browser` | 49,040 | 1,461,427 | Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating… |
| 3 | orca-cli | `stablyai/orca@orca-cli` | 121,250 | 360,303 | Operate Orca-managed worktrees, folder contexts, terminals, repos, automations, worktree comments, and Orca's… |
| 4 | browser-use | `browser-use/browser-use@browser-use` | 120,565 | 99,426 | Direct browser control via CDP for web interaction: automation, scraping, testing, screenshots, and site/app… |
| 5 | agent-reach | `panniantong/agent-reach@agent-reach` | 110,869 | 22,396 | 只读读取各平台内容：搜索、读帖、看评论、取字幕、查行情和职位。 Use when 用户提到或贴出链接：小红书/xiaohongshu、B站/bilibili、Twitter/X、Reddit、… |
| 6 | market-research | `affaan-m/ecc@market-research` | 300,648 | 6,926 | Conduct market research, competitive analysis, investor due diligence, and industry intelligence with source… |
| 7 | deep-research | `affaan-m/ecc@deep-research` | 300,648 | 6,204 | Produce cited research reports from multiple web sources using firecrawl and exa MCP tools — plan… |
| 8 | search-first | `affaan-m/ecc@search-first` | 300,648 | 6,055 | Research-before-coding workflow: search npm/PyPI, MCP servers, skills, and GitHub for existing tools before… |
| 9 | exa-search | `affaan-m/ecc@exa-search` | 300,648 | 5,554 | Neural search via Exa MCP for web, code, and company research. Use when the user needs web search, code… |
| 10 | research-ops | `affaan-m/ecc@research-ops` | 300,648 | 5,516 | Evidence-first current-state research workflow for ECC. Use when the user wants fresh facts, comparisons,… |
| 11 | prediction-market-oracle-research | `affaan-m/ecc@prediction-market-oracle-research` | 300,648 | 5,345 | Research prediction markets as data sources or oracle signals for products, agents, dashboards, and corporate… |
| 12 | ito-baskets | `affaan-m/ecc@ito-baskets` | 300,648 | 3,758 | Read-only Itô basket and prediction-market data skill. Index the live basket catalog, compare a basket… |
| 13 | mem-search | `thedotmack/claude-mem@mem-search` | 115,723 | 9,324 | This skill should be used when the user asks to "search memory", "what do you remember about X", "check… |
| 14 | persona-researcher | `googleworkspace/cli@persona-researcher` | 32,230 | 32,044 | Organize research — manage references, notes, and collaboration. |
| 15 | scholar-evaluation | `affaan-m/ecc@scholar-evaluation` | 300,648 | 3,429 | Structured scholarly-work evaluation for papers, proposals, literature reviews, methods sections, evidence… |

## Mobile apps

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | vercel-react-native-skills | `vercel-labs/agent-skills@vercel-react-native-skills` | 33,834 | 272,807 | React Native and Expo best practices for building performant mobile apps. Use when building React Native… |
| 2 | write-swift | `emilkowalski/skills@write-swift` | 55,720 | 152,326 | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable… |
| 3 | mobile-native | `emilkowalski/skills@mobile-native` | 55,720 | 122,644 | Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a… |
| 4 | apple-notes | `openclaw/openclaw@apple-notes` | 394,301 | 5,949 | Create, view, edit, delete, search, move, or export Apple Notes via the memo CLI on macOS. |
| 5 | healthcheck | `openclaw/openclaw@healthcheck` | 394,301 | 5,558 | Audit/harden OpenClaw hosts: SSH, firewall, updates, exposure, backups, disk encryption, gateway security. |
| 6 | android-clean-architecture | `affaan-m/ecc@android-clean-architecture` | 300,648 | 6,418 | Clean Architecture patterns for Android and Kotlin Multiplatform projects — module structure, dependency… |
| 7 | kotlin-coroutines-flows | `affaan-m/ecc@kotlin-coroutines-flows` | 300,648 | 5,976 | Kotlin Coroutines and Flow patterns for Android and KMP — structured concurrency, Flow operators, StateFlow,… |
| 8 | kotlin-patterns | `affaan-m/ecc@kotlin-patterns` | 300,648 | 5,944 | Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable… |
| 9 | dart-flutter-patterns | `affaan-m/ecc@dart-flutter-patterns` | 300,648 | 5,718 | Production-ready Dart and Flutter patterns covering null safety, immutable state with Freezed, async… |
| 10 | swiftui-patterns | `affaan-m/ecc@swiftui-patterns` | 300,648 | 5,635 | SwiftUI architecture patterns, state management with @Observable, view composition, navigation, performance… |
| 11 | ios-icon-gen | `affaan-m/ecc@ios-icon-gen` | 300,648 | 5,540 | Generate iOS app icons as PNG imagesets for Xcode asset catalogs from SF Symbols (5000+ Apple-native) or… |
| 12 | kotlin-ktor-patterns | `affaan-m/ecc@kotlin-ktor-patterns` | 300,648 | 5,538 | Ktor server patterns including routing DSL, plugins, authentication, Koin DI, kotlinx.serialization,… |
| 13 | kotlin-exposed-patterns | `affaan-m/ecc@kotlin-exposed-patterns` | 300,648 | 5,507 | JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling,… |
| 14 | cisco-ios-patterns | `affaan-m/ecc@cisco-ios-patterns` | 300,648 | 5,471 | Cisco IOS and IOS-XE review patterns for show commands, config hierarchy, wildcard masks, ACL placement,… |
| 15 | swift-concurrency-6-2 | `affaan-m/ecc@swift-concurrency-6-2` | 300,648 | 5,456 | Swift 6.2 Approachable Concurrency — single-threaded by default, @concurrent for explicit background… |

## Finance, business & legal

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | style-sampling | `heygen-com/hyperframes@style-sampling` | 82,153 | 33,304 | Make a new episode in a proven video style - Collage Explainer, Finance Explainer, Animated Science… |
| 2 | healthcare-phi-compliance | `affaan-m/ecc@healthcare-phi-compliance` | 300,648 | 5,596 | Protected Health Information (PHI) and PII compliance patterns for healthcare applications: data… |
| 3 | customs-trade-compliance | `affaan-m/ecc@customs-trade-compliance` | 300,648 | 5,529 | Codified customs and trade compliance expertise — HS/HTS tariff classification with GRI rules, commercial… |
| 4 | hipaa-compliance | `affaan-m/ecc@hipaa-compliance` | 300,648 | 5,509 | HIPAA-specific entrypoint for healthcare privacy and security work. Use when a task is explicitly framed… |
| 5 | finance-billing-ops | `affaan-m/ecc@finance-billing-ops` | 300,648 | 5,501 | Evidence-first revenue, pricing, refunds, team-billing, and billing-model truth workflow for ECC. Use when… |
| 6 | contract-first | `affaan-m/ecc@contract-first` | 300,648 | 4,257 | Coordinate frontend/backend or service-to-service work through one authoritative machine-checkable contract… |
| 7 | persona-hr-coordinator | `googleworkspace/cli@persona-hr-coordinator` | 32,230 | 30,472 | Handle HR workflows — onboarding, announcements, and employee comms. |
| 8 | operator-approval-loop | `affaan-m/ecc@operator-approval-loop` | 300,648 | 2,720 | Operator approval contract with internal filing notices for agent-drafted outbound messages, hashed drafts,… |
| 9 | backtesting-frameworks | `wshobson/agents@backtesting-frameworks` | 42,393 | 17,579 | Build robust backtesting systems for trading strategies with proper handling of look-ahead bias, survivorship… |
| 10 | startup-financial-modeling | `wshobson/agents@startup-financial-modeling` | 42,393 | 13,161 | Build comprehensive 3-5 year financial models with revenue projections, cost structures, cash flow analysis,… |
| 11 | startup-metrics-framework | `wshobson/agents@startup-metrics-framework` | 42,393 | 11,683 | Track, calculate, and optimize key performance metrics for SaaS, marketplace, consumer, and B2B startups from… |
| 12 | pci-compliance | `wshobson/agents@pci-compliance` | 42,393 | 10,961 | Implement PCI DSS compliance requirements for secure handling of payment card data and payment systems. Use… |
| 13 | employment-contract-templates | `wshobson/agents@employment-contract-templates` | 42,393 | 10,897 | Create employment contracts, offer letters, and HR policy documents following legal best practices. Use when… |
| 14 | defi-protocol-templates | `wshobson/agents@defi-protocol-templates` | 42,393 | 10,826 | Implement DeFi protocols with production-ready templates for staking, AMMs, governance, and flash loans. Use… |
| 15 | team-composition-analysis | `wshobson/agents@team-composition-analysis` | 42,393 | 10,731 | Design optimal team structures, hiring plans, compensation strategies, and equity allocation for early-stage… |

## Video

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | hyperframes-cli | `heygen-com/hyperframes@hyperframes-cli` | 82,153 | 1,499,957 | The HyperFrames CLI by job - scaffold, check, look at frames, edit the timeline, preview, render locally or… |
| 2 | hyperframes | `heygen-com/hyperframes@hyperframes` | 82,153 | 1,461,339 | Read first to make, edit, animate or render any video with HyperFrames (HTML rendered to video), including… |
| 3 | hyperframes-registry | `heygen-com/hyperframes@hyperframes-registry` | 82,153 | 1,251,100 | About 450 ready-made HyperFrames blocks and components installed as editable source - transitions, overlays,… |
| 4 | hyperframes-core | `heygen-com/hyperframes@hyperframes-core` | 82,153 | 931,075 | The HyperFrames composition contract — build one renderable project. Use for composition structure, the… |
| 5 | hyperframes-creative | `heygen-com/hyperframes@hyperframes-creative` | 82,153 | 917,127 | Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling,… |
| 6 | hyperframes-keyframes | `heygen-com/hyperframes@hyperframes-keyframes` | 82,153 | 754,806 | Use when a HyperFrames composition needs a punch-in, punch-out, zoom, reframe, Ken Burns treatment, camera… |
| 7 | hyperframes-audio | `heygen-com/hyperframes@hyperframes-audio` | 82,153 | 663,877 | Use when audio already placed in a HyperFrames composition needs to be mixed: fade-in/fade-out, crossfade,… |
| 8 | general-video | `heygen-com/hyperframes@general-video` | 82,153 | 661,760 | Author or edit a custom HyperFrames composition when no specialized workflow fits, or when BRIEF.md sets… |
| 9 | remotion-to-hyperframes | `heygen-com/hyperframes@remotion-to-hyperframes` | 82,153 | 593,602 | Bring existing video code or footage into HyperFrames and verify it frame by frame against the original -… |
| 10 | product-launch-video | `heygen-com/hyperframes@product-launch-video` | 82,153 | 539,328 | Turn a product or marketing URL, pasted script, or brief into a product launch / promo video — SaaS promos,… |
| 11 | faceless-explainer | `heygen-com/hyperframes@faceless-explainer` | 82,153 | 522,033 | Turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video: there is no site… |
| 12 | embedded-captions | `heygen-com/hyperframes@embedded-captions` | 82,153 | 453,936 | Add captions or subtitles to an existing single-subject talking-head video without editing the footage. Use… |
| 13 | hyperframes-studio | `heygen-com/hyperframes@hyperframes-studio` | 82,153 | 451,648 | Use when working with a person on a HyperFrames project in Studio: first, whether their message asks for a… |
| 14 | talking-head-recut | `heygen-com/hyperframes@talking-head-recut` | 82,153 | 407,957 | Package an existing talking-head / interview / podcast video with timed, designed GRAPHIC OVERLAY cards —… |
| 15 | hyperframes-media | `heygen-com/hyperframes@hyperframes-media` | 82,153 | 141,731 | Audio and media assets for HyperFrames compositions, produced by one shared audio engine… |

## Debugging

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | diagnosing-bugs | `mattpocock/skills@diagnosing-bugs` | 320,638 | 916,300 | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or… |
| 2 | systematic-debugging | `obra/superpowers@systematic-debugging` | 315,588 | 327,657 | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| 3 | diagnose | `mattpocock/skills@diagnose` | 320,638 | 227,598 | Disciplined diagnosis loop for hard bugs and performance regressions. Reproduce → minimise → hypothesise →… |
| 4 | investigate-first | `juliusbrussee/caveman@investigate-first` | 118,839 | 120,995 | Diagnose ambiguous failures before editing. Use for unknown causes, intermittent behavior, performance… |
| 5 | diagnosing-superpowers | `obra/superpowers@diagnosing-superpowers` | 315,588 | 31,620 | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored… |
| 6 | optimize | `pbakaus/impeccable@optimize` | 107,410 | 81,054 | Diagnoses and fixes UI performance across loading speed, rendering, animations, images, and bundle size. Use… |
| 7 | debugging-and-error-recovery | `addyosmani/agent-skills@debugging-and-error-recovery` | 114,962 | 72,880 | Guides systematic root-cause debugging. Use when tests fail, builds break, something that worked yesterday… |
| 8 | turborepo | `vercel/turborepo@turborepo` | 31,323 | 89,541 | Configure and troubleshoot Turborepo repositories. Use when working with turbo.json, task pipelines, caching,… |
| 9 | agent-introspection-debugging | `affaan-m/ecc@agent-introspection-debugging` | 300,648 | 5,745 | Structured self-debugging workflow for AI agent failures using capture, diagnosis, contained recovery, and… |
| 10 | product-lens | `affaan-m/ecc@product-lens` | 300,648 | 5,542 | Validate the why before building through four product diagnostics — a YC-style product diagnostic that… |
| 11 | terminal-ops | `affaan-m/ecc@terminal-ops` | 300,648 | 5,498 | Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI… |
| 12 | network-interface-health | `affaan-m/ecc@network-interface-health` | 300,648 | 5,455 | Diagnose interface errors, drops, CRCs, duplex mismatches, flapping, speed negotiation issues, and counter… |
| 13 | homelab-pihole-dns | `affaan-m/ecc@homelab-pihole-dns` | 300,648 | 5,447 | Pi-hole installation, blocklist management, DNS-over-HTTPS setup, DHCP integration, local DNS records, and… |
| 14 | network-bgp-diagnostics | `affaan-m/ecc@network-bgp-diagnostics` | 300,648 | 5,428 | Diagnostics-only BGP troubleshooting patterns for neighbor state, route exchange, prefix policy, AS path… |
| 15 | orca-per-workspace-env | `stablyai/orca@orca-per-workspace-env` | 121,250 | 12,543 | Set up, review, debug, or validate an Orca per-workspace environment recipe: the on-demand, disposable… |

## 3D & games

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | three | `heygen-com/hyperframes@three` | 82,153 | 69,320 | Three.js and WebGL adapter patterns for HyperFrames. Use when creating deterministic Three.js scenes, WebGL… |
| 2 | godot-gdscript-patterns | `wshobson/agents@godot-gdscript-patterns` | 42,393 | 18,284 | Master Godot 4 GDScript patterns including signals, scenes, state machines, and optimization. Use when… |
| 3 | game-engine | `github/awesome-copilot@game-engine` | 41,011 | 13,421 | Expert skill for building web-based game engines and games using HTML5, Canvas, WebGL, and JavaScript. Use… |
| 4 | unity-ecs-patterns | `wshobson/agents@unity-ecs-patterns` | 42,393 | 12,483 | Master Unity ECS (Entity Component System) with DOTS, Jobs, and Burst for high-performance game development.… |
| 5 | threejs | `nexu-io/open-design@threejs` | 106,999 | 3,553 | Three.js skills for creating 3D elements and interactive experiences in the browser — scenes, materials,… |
| 6 | metal-kernel | `pytorch/pytorch@metal-kernel` | 105,318 | 3,189 | Write Metal/MPS kernels for PyTorch operators. Use when adding MPS device support to operators, implementing… |
| 7 | shader-dev | `nexu-io/open-design@shader-dev` | 106,999 | 2,945 | GLSL shader techniques for ray marching, fluid simulation, particle systems, and procedural generation.… |
| 8 | fal-3d | `nexu-io/open-design@fal-3d` | 106,999 | 2,928 | Generate 3D models from text or images via fal.ai. Useful for game assets, AR previews, product mockups, and… |
| 9 | mockup-device-3d | `nexu-io/open-design@mockup-device-3d` | 106,999 | 2,831 | Static iPhone and MacBook 3D-style showcase with real HTML embedded on screens, glass-lens refraction, and… |
| 10 | gcode | `earthtojake/text-to-cad@gcode` | 25,975 | 10,528 | Slice 3D models into printer-ready G-code with OrcaSlicer, the open-source slicer with built-in profiles for… |
| 11 | 3d-web-experience | `sickn33/agentic-awesome-skills@3d-web-experience` | 49,484 | 5,262 | Use when building or debugging web 3D scenes, product configurators or portfolios with Three.js, React Three… |
| 12 | game-development | `sickn33/agentic-awesome-skills@game-development` | 49,484 | 3,872 | Game development orchestrator. Routes by platform, dimension, and engine fit (web 2D/3D, hybrid DOM+canvas,… |
| 13 | p5js | `nousresearch/hermes-agent@p5js` | 262,370 | 572 | p5.js sketches: gen art, shaders, interactive, 3D. |
| 14 | implicit-cad | `earthtojake/text-to-cad@implicit-cad` | 25,975 | 5,523 | Create, edit, render, and snapshot browser-native implicit CAD `.implicit.js` and `.implicit.mjs` files using… |
| 15 | game-feel | `gamedev-skills/awesome-gamedev-agent-skills@game-feel` | 8,155 | 14,933 | Add "juice" and game feel that makes actions satisfying — screen shake, hit-stop/freeze frames, tweened/eased… |

## Images & graphics

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | image-to-code | `leonxlnx/taste-skill@image-to-code` | 112,904 | 385,945 | Moved to github.com/Leonxlnx/imagegen-skills. Runs only when called by name. |
| 2 | imagegen-frontend-web | `leonxlnx/taste-skill@imagegen-frontend-web` | 112,904 | 380,152 | Moved to github.com/Leonxlnx/imagegen-skills. Runs only when called by name. |
| 3 | motion-graphics | `heygen-com/hyperframes@motion-graphics` | 82,153 | 514,339 | Use when creating a short, design-led motion graphic where motion is the message — kinetic typography, stat… |
| 4 | imagegen-frontend-mobile | `leonxlnx/taste-skill@imagegen-frontend-mobile` | 112,904 | 373,799 | Moved to github.com/Leonxlnx/imagegen-skills. Runs only when called by name. |
| 5 | canvas-design | `anthropics/skills@canvas-design` | 192,031 | 130,207 | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill… |
| 6 | banner-design | `nextlevelbuilder/ui-ux-pro-max-skill@banner-design` | 147,710 | 47,459 | Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction… |
| 7 | image | `coreyhaines31/marketingskills@image` | 59,560 | 95,592 | When the user wants to create, generate, edit, or optimize marketing images, or asks how to make one look… |
| 8 | popups | `coreyhaines31/marketingskills@popups` | 59,560 | 78,216 | When the user wants to create or improve popups, modals, slide-ins, sticky bars, and banners, or asks whether… |
| 9 | json-canvas | `kepano/obsidian-skills@json-canvas` | 51,529 | 76,985 | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when working with… |
| 10 | graphic-overlays | `heygen-com/hyperframes@graphic-overlays` | 82,153 | 29,124 | Package an existing talking-head / interview / podcast video by layering timed, designed GRAPHIC OVERLAY… |
| 11 | diagram-design | `cathrynlavery/diagram-design@diagram-design` | 66,285 | 26,994 | Create branded architecture, architecture delta, IT current-state, flowchart, sequence, state machine,… |
| 12 | excalidraw-diagram-generator | `github/awesome-copilot@excalidraw-diagram-generator` | 41,011 | 34,441 | Generate Excalidraw diagrams from natural language descriptions. Use when asked to "create a diagram", "make… |
| 13 | plan-canvas | `affaan-m/ecc@plan-canvas` | 300,648 | 4,463 | Open plans and HTML artifacts in a local browser canvas where the human annotates elements, chats, and… |
| 14 | baoyu-image-gen | `jimliu/baoyu-skills@baoyu-image-gen` | 27,453 | 34,187 | AI image generation with OpenAI GPT Image 2.5, Azure OpenAI, Google, OpenRouter, DashScope, Z.AI GLM-Image,… |
| 15 | baoyu-cover-image | `jimliu/baoyu-skills@baoyu-cover-image` | 27,453 | 32,581 | Generates article cover images with 5 dimensions (type, palette, rendering, text, mood) combining 11 color… |

## Productivity & integrations

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | obsidian-vault | `mattpocock/skills@obsidian-vault` | 320,638 | 195,522 | Search, create, and manage notes in the Obsidian vault with wikilinks and index notes. Use when user wants to… |
| 2 | slack-gif-creator | `anthropics/skills@slack-gif-creator` | 192,031 | 79,699 | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation… |
| 3 | lark-doc | `larksuite/cli@lark-doc` | 18,041 | 491,504 | 飞书云文档（Docx / Wiki）内容操作：读取、创建、编辑文档，插入或下载图片附件，以及操作思维笔记。用户提供文档 URL/token（包括 doubao.com 的 /docx/、/wiki/）时使用；按 URL… |
| 4 | lark-base | `larksuite/cli@lark-base` | 18,041 | 488,773 | 飞书多维表格（Base）操作：建表、字段、记录、视图、统计、公式/lookup、表单、仪表盘、应用模式（BaseApp/AppMode 页面与组件）、Workspace… |
| 5 | lark-shared | `larksuite/cli@lark-shared` | 18,041 | 487,824 | Use for lark-cli setup/auth tasks: auth login/status/logout, user vs bot identity, business-domain… |
| 6 | lark-drive | `larksuite/cli@lark-drive` | 18,041 | 485,581 | 飞书云空间（云盘/云存储）：管理 Drive 文件和文件夹，包含上传/下载、创建文件夹、复制/移动/删除、查看元数据、查询权限设置、评论/权限/订阅、标题、版本、飞书文档密级标签（secure… |
| 7 | lark-im | `larksuite/cli@lark-im` | 18,041 | 485,545 | 飞书即时通讯：收发消息和管理群聊。发送和回复消息、搜索聊天记录、管理群聊成员、上传下载图片和文件、管理表情回复、发送应用内/短信/电话加急、发送和处理交互卡片（Interactive… |
| 8 | lark-sheets | `larksuite/cli@lark-sheets` | 18,041 | 484,807 | 飞书电子表格：创建和操作电子表格。支持工作表与行列结构（增删/合并/尺寸/隐藏/冻结/分组）、单元格读写（值/公式/样式/批注/单元格图片）、区域复制移动排序填充、查找替换、批量更新，图表、透视表、条件格式、筛选器与筛选… |
| 9 | lark-wiki | `larksuite/cli@lark-wiki` | 18,041 | 484,297 | 飞书知识库：管理知识空间、空间成员和文档节点。创建和查询知识空间、查看和管理空间成员、管理节点层级结构、在知识库中组织文档和快捷方式。当用户需要在知识库中查找或创建文档、浏览知识空间结构、查看或管理空间成员、移动或复制节… |
| 10 | lark-whiteboard | `larksuite/cli@lark-whiteboard` | 18,041 | 482,558 | 飞书画板：查询和编辑飞书云文档中的画板。支持导出画板为预览图片、导出原始节点结构、使用多种格式更新画板内容。 当用户需要查看画板内容、导出画板图片、编辑画板时使用此… |
| 11 | lark-task | `larksuite/cli@lark-task` | 18,041 | 482,490 | 飞书任务：管理任务、清单和任务智能体。创建待办任务、查看和更新任务状态、拆分子任务、组织任务清单、分配协作成员、上传任务附件、注册或注销任务智能体、更新任务智能体的主页数据、写入智能体任务记录。当用户需要创建待办事项、查… |
| 12 | lark-calendar | `larksuite/cli@lark-calendar` | 18,041 | 481,501 | 飞书日历：管理日历日程和会议室。查看/搜索日程、创建/更新日程、管理参会人、查询忙闲和推荐时段、预定会议室。当用户需要查看日程安排、创建/修改会议、查询/预定会议室时使用。不负责：查询过去的视频会议记录（走… |
| 13 | lark-mail | `larksuite/cli@lark-mail` | 18,041 | 479,880 | 飞书邮箱：Use when user mentions 起草邮件、写邮件、草稿、发送/回复/转发邮件、查阅邮件、看邮件、搜索邮件、邮件文件夹、邮件标签、邮件联系人、监听新邮件、邮件收信规则等；use for… |
| 14 | lark-event | `larksuite/cli@lark-event` | 18,041 | 479,191 | Lark/Feishu real-time event listening / subscribing / consuming: stream events as NDJSON via `lark-cli event… |
| 15 | lark-contact | `larksuite/cli@lark-contact` | 18,041 | 478,965 | 飞书 / Lark 通讯录:按姓名 / 邮箱解析成 open_id,或按 open_id 反查姓名 / 部门 / 邮箱 / 联系方式 / 个人状态 / 签名,以及按关键词搜索当前用户可见的机器人 /… |

## Languages & frameworks

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | setup-ts-deep-modules | `mattpocock/skills@setup-ts-deep-modules` | 320,638 | 417,899 | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden… |
| 2 | launch | `coreyhaines31/marketingskills@launch` | 59,560 | 86,737 | When the user wants to plan product and feature launches: Product Hunt, feature announcements, beta and early… |
| 3 | typescript-advanced-types | `wshobson/agents@typescript-advanced-types` | 42,393 | 98,949 | Master TypeScript's advanced type system including generics, conditional types, mapped types, template… |
| 4 | python-patterns | `affaan-m/ecc@python-patterns` | 300,648 | 6,724 | Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and… |
| 5 | golang-patterns | `affaan-m/ecc@golang-patterns` | 300,648 | 6,412 | Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go… |
| 6 | rust-patterns | `affaan-m/ecc@rust-patterns` | 300,648 | 6,186 | Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building… |
| 7 | error-handling | `affaan-m/ecc@error-handling` | 300,648 | 5,860 | Patterns for robust error handling across TypeScript, Python, and Go. Covers typed errors, error boundaries,… |
| 8 | dotnet-patterns | `affaan-m/ecc@dotnet-patterns` | 300,648 | 5,601 | Idiomatic C# and .NET patterns, conventions, dependency injection, async/await, and best practices for… |
| 9 | tinystruct-patterns | `affaan-m/ecc@tinystruct-patterns` | 300,648 | 5,392 | Expert guidance for developing with the tinystruct Java framework. Use when working on the tinystruct… |
| 10 | python-performance-optimization | `wshobson/agents@python-performance-optimization` | 42,393 | 37,603 | Profile and optimize Python code using cProfile, memory profilers, and performance best practices. Use when… |
| 11 | generating-python-installer | `affaan-m/ecc@generating-python-installer` | 300,648 | 4,689 | Commercial-grade Python installer expert for Windows: Nuitka extreme compilation, dist slimming, DLL… |
| 12 | python-design-patterns | `wshobson/agents@python-design-patterns` | 42,393 | 23,706 | Python design patterns including KISS, Separation of Concerns, Single Responsibility, and composition over… |
| 13 | modern-javascript-patterns | `wshobson/agents@modern-javascript-patterns` | 42,393 | 23,328 | Master ES6+ features including async/await, destructuring, spread operators, arrow functions, promises,… |
| 14 | rust-async-patterns | `wshobson/agents@rust-async-patterns` | 42,393 | 21,894 | Master Rust async programming with Tokio, async traits, error handling, and concurrent patterns. Use when… |
| 15 | async-python-patterns | `wshobson/agents@async-python-patterns` | 42,393 | 18,821 | Master Python asyncio, concurrent programming, and async/await patterns for high-performance applications.… |

## Coding quality & refactoring

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | scaffold-exercises | `mattpocock/skills@scaffold-exercises` | 320,638 | 530,174 | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting.… |
| 2 | request-refactor-plan | `mattpocock/skills@request-refactor-plan` | 320,638 | 202,443 | Create a detailed refactor plan with tiny commits via user interview, then file it as a GitHub issue. Use… |
| 3 | impeccable | `pbakaus/impeccable@impeccable` | 107,410 | 398,548 | Use when the user wants to design, redesign, shape, critique, audit, polish, simplify, harden, animate, or… |
| 4 | ponytail | `dietrichgebert/ponytail@ponytail` | 188,256 | 125,370 | Lazy senior dev mode: the smallest change that fully solves the task, and a reply a busy human understands in… |
| 5 | safe-refactor | `juliusbrussee/caveman@safe-refactor` | 118,839 | 122,055 | Restructure code while preserving behavior. Use for extraction, consolidation, ownership moves, or cleanup… |
| 6 | ponytail-audit | `dietrichgebert/ponytail@ponytail-audit` | 188,256 | 55,988 | Quality audit of a whole repo: bugs, security holes, what breaks under real load, risky code without tests,… |
| 7 | ponytail-debt | `dietrichgebert/ponytail@ponytail-debt` | 188,256 | 52,943 | List every `shortcut:` comment (and older `ponytail:` ones) as a debt ledger. One-shot report, changes… |
| 8 | ponytail-help | `dietrichgebert/ponytail@ponytail-help` | 188,256 | 52,877 | Quick reference for ponytail levels, skills and commands. One-shot display. Use for /ponytail-help, "ponytail… |
| 9 | ponytail-gain | `dietrichgebert/ponytail@ponytail-gain` | 188,256 | 50,738 | Show ponytail's measured savings (code, cost, speed) from the benchmark. One-shot display. Use for… |
| 10 | distill | `pbakaus/impeccable@distill` | 107,410 | 79,457 | Strip designs to their essence by removing unnecessary complexity. Great design is simple, powerful, and… |
| 11 | code-simplification | `addyosmani/agent-skills@code-simplification` | 114,962 | 73,050 | Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code… |
| 12 | coding-standards | `affaan-m/ecc@coding-standards` | 300,648 | 7,048 | Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. Use… |
| 13 | oracle | `openclaw/openclaw@oracle` | 394,301 | 5,203 | Oracle CLI second-model review/debug/refactor/design with selected files, dry-run token checks, API or… |
| 14 | cpp-coding-standards | `affaan-m/ecc@cpp-coding-standards` | 300,648 | 6,292 | C++ coding standards based on the C++ Core Guidelines (isocpp.github.io). Use when writing, reviewing, or… |
| 15 | java-coding-standards | `affaan-m/ecc@java-coding-standards` | 300,648 | 6,210 | Java coding standards for Spring Boot and Quarkus services: naming, immutability, Optional usage, streams,… |

## Data & analytics

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | analytics | `coreyhaines31/marketingskills@analytics` | 59,560 | 93,257 | When the user wants to set up, improve, or audit analytics tracking: tracking plans, event taxonomies, GA4,… |
| 2 | analytics-tracking | `coreyhaines31/marketingskills@analytics-tracking` | 59,560 | 57,817 | When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user… |
| 3 | dashboard-builder | `affaan-m/ecc@dashboard-builder` | 300,648 | 5,794 | Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms.… |
| 4 | data-scraper-agent | `affaan-m/ecc@data-scraper-agent` | 300,648 | 5,609 | Build a fully automated AI-powered data collection agent for any public source — job boards, prices, news,… |
| 5 | latency-critical-systems | `affaan-m/ecc@latency-critical-systems` | 300,648 | 5,396 | Optimize and verify latency-sensitive systems — realtime dashboards, market data feeds, streaming agents,… |
| 6 | data-throughput-accelerator | `affaan-m/ecc@data-throughput-accelerator` | 300,648 | 5,347 | Diagnose and accelerate large data movement — ingestion, backfill, export, ETL, warehouse loading, manifest… |
| 7 | recipe-backup-sheet-as-csv | `googleworkspace/cli@recipe-backup-sheet-as-csv` | 32,230 | 31,759 | Export a Google Sheets spreadsheet as a CSV file for local backup or processing. |
| 8 | nature-data | `yuan1z0825/nature-skills@nature-data` | 53,059 | 16,242 | Draft or audit manuscript Data/Code Availability statements, dataset access routes, repository plans, and… |
| 9 | data-storytelling | `wshobson/agents@data-storytelling` | 42,393 | 17,622 | Transform data into compelling narratives using visualization, context, and persuasive structure. Use when… |
| 10 | kpi-dashboard-design | `wshobson/agents@kpi-dashboard-design` | 42,393 | 17,204 | Design effective KPI dashboards with metrics selection, visualization best practices, and real-time… |
| 11 | nature-statistics | `yuan1z0825/nature-skills@nature-statistics` | 53,059 | 12,784 | Audit or improve manuscript statistical reporting, including experimental units, replication, uncertainty,… |
| 12 | gdpr-data-handling | `wshobson/agents@gdpr-data-handling` | 42,393 | 15,445 | Implement GDPR-compliant data handling with consent management, data subject rights, and privacy by design.… |
| 13 | grafana-dashboards | `wshobson/agents@grafana-dashboards` | 42,393 | 13,582 | Create and manage production Grafana dashboards for real-time visualization of system and application… |
| 14 | data-analyst | `shubhamsaboo/awesome-llm-apps@data-analyst` | 144,353 | 3,974 | SQL, pandas, and statistical analysis expertise for data exploration and insights. Use when: analyzing data,… |
| 15 | data-visualization | `anthropics/knowledge-work-plugins@data-visualization` | 35,331 | 14,493 | Create effective data visualizations with Python (matplotlib, seaborn, plotly). Use when building charts,… |

## Databases

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | migration | `juliusbrussee/caveman@migration` | 118,839 | 119,242 | Implement reversible compatibility-safe transitions. Use for schema, data, API, protocol, configuration, or… |
| 2 | deprecation-and-migration | `addyosmani/agent-skills@deprecation-and-migration` | 114,962 | 66,835 | Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users… |
| 3 | schema | `coreyhaines31/marketingskills@schema` | 59,560 | 87,520 | When the user wants to add, fix, and validate schema markup and structured data (JSON-LD): product, review,… |
| 4 | schema-markup | `coreyhaines31/marketingskills@schema-markup` | 59,560 | 55,479 | When the user wants to add, fix, or optimize schema markup and structured data on their site. Also use when… |
| 5 | database-migrations | `affaan-m/ecc@database-migrations` | 300,648 | 6,409 | Safe, reversible database migration patterns: forward-only production changes, expand-contract zero-downtime… |
| 6 | postgres-patterns | `affaan-m/ecc@postgres-patterns` | 300,648 | 6,403 | PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase… |
| 7 | claude-opus-4-5-migration | `anthropics/claude-code@claude-opus-4-5-migration` | 155,190 | 11,819 | Migrate prompts and code from Claude Sonnet 4.0, Sonnet 4.5, or Opus 4.1 to Opus 4.5. Use when the user wants… |
| 8 | redis-patterns | `affaan-m/ecc@redis-patterns` | 300,648 | 5,792 | Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection… |
| 9 | mysql-patterns | `affaan-m/ecc@mysql-patterns` | 300,648 | 5,723 | MySQL and MariaDB schema, query, indexing, transaction, replication, and connection-pool patterns for… |
| 10 | prisma-patterns | `affaan-m/ecc@prisma-patterns` | 300,648 | 5,578 | Prisma ORM patterns for TypeScript backends — schema design, query optimization, transactions, pagination,… |
| 11 | supabase-postgres-best-practices | `supabase/agent-skills@supabase-postgres-best-practices` | 3,040 | 480,625 | Postgres best practices maintained by Supabase, for Postgres running anywhere. Load this skill BEFORE writing… |
| 12 | postgresql-table-design | `wshobson/agents@postgresql-table-design` | 42,393 | 28,742 | Use this skill when designing or reviewing a PostgreSQL-specific schema. Covers best-practices, data types,… |
| 13 | supabase | `supabase/agent-skills@supabase` | 3,040 | 361,722 | Use when doing ANY task involving Supabase. Triggers: Supabase products (Database, Auth, Edge Functions,… |
| 14 | uspto-database | `affaan-m/ecc@uspto-database` | 300,648 | 3,244 | USPTO patent and trademark data workflow for official record lookup, PatentSearch queries, TSDR checks,… |
| 15 | sql-optimization-patterns | `wshobson/agents@sql-optimization-patterns` | 42,393 | 20,470 | Master SQL query optimization, indexing strategies, and EXPLAIN analysis to dramatically improve database… |

## Security & pentesting

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | security-and-hardening | `addyosmani/agent-skills@security-and-hardening` | 114,962 | 81,960 | Hardens code against vulnerabilities. Use when auditing an input handler for vulnerabilities, when handling… |
| 2 | security-audit | `cloudflare/security-audit-skill@security-audit` | 68,886 | 97,766 | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons.… |
| 3 | 1password | `openclaw/openclaw@1password` | 394,301 | 6,346 | Set up and use 1Password CLI for sign-in, desktop integration, and reading or injecting secrets. |
| 4 | security-review | `affaan-m/ecc@security-review` | 300,648 | 7,614 | Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints,… |
| 5 | perl-security | `affaan-m/ecc@perl-security` | 300,648 | 5,994 | Comprehensive Perl security covering taint mode, input validation, safe process execution, DBI parameterized… |
| 6 | security-scan | `affaan-m/ecc@security-scan` | 300,648 | 5,819 | Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and… |
| 7 | llm-trading-agent-security | `affaan-m/ecc@llm-trading-agent-security` | 300,648 | 5,638 | Security patterns for autonomous trading agents with wallet or transaction authority. Covers prompt… |
| 8 | security-bounty-hunter | `affaan-m/ecc@security-bounty-hunter` | 300,648 | 5,590 | Hunt for exploitable, bounty-worthy security issues in repositories. Focuses on remotely reachable… |
| 9 | defi-amm-security | `affaan-m/ecc@defi-amm-security` | 300,648 | 5,448 | Security checklist for Solidity AMM contracts, liquidity pools, and swap flows. Covers reentrancy, CEI… |
| 10 | quarkus-security | `affaan-m/ecc@quarkus-security` | 300,648 | 5,432 | Quarkus security implementation patterns: JWT and OIDC authentication, @RolesAllowed RBAC and… |
| 11 | fix-security-vulnerabilities-with-strix | `usestrix/strix@fix-security-vulnerabilities-with-strix` | 74,834 | 19,148 | Fix security vulnerabilities found by a Strix pentest (open-source CLI or app.strix.ai cloud) — triage by… |
| 12 | ci-security-scanning-with-strix | `usestrix/strix@ci-security-scanning-with-strix` | 74,834 | 18,727 | Add security scanning to CI/CD with Strix — GitHub Actions, GitLab CI, or any pipeline — so every pull… |
| 13 | managed-pentesting-with-strix | `usestrix/strix@managed-pentesting-with-strix` | 74,834 | 18,661 | Run a managed pentest of a web app, API, repository, or local workspace on the app.strix.ai platform with the… |
| 14 | web-app-penetration-testing | `usestrix/strix@web-app-penetration-testing` | 74,834 | 16,463 | Pentest a web app or website end to end — black-box testing of a live URL, staging environment, or local dev… |
| 15 | owasp-top-10-testing | `usestrix/strix@owasp-top-10-testing` | 74,834 | 16,343 | Test an application against the OWASP Top 10 with Strix — autonomous AI agents that attempt real exploits for… |

## Documents & office files

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | pptx | `anthropics/skills@pptx` | 192,031 | 252,430 | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This… |
| 2 | pdf | `anthropics/skills@pdf` | 192,031 | 226,577 | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting… |
| 3 | docx | `anthropics/skills@docx` | 192,031 | 216,043 | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or… |
| 4 | slideshow | `heygen-com/hyperframes@slideshow` | 82,153 | 499,552 | Build a HyperFrames slideshow to present live - slides, fragment reveals, branching hotspots and presenter… |
| 5 | xlsx | `anthropics/skills@xlsx` | 192,031 | 196,341 | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user… |
| 6 | lark-slides | `larksuite/cli@lark-slides` | 18,041 | 433,334 | 飞书幻灯片：创建和编辑幻灯片。创建演示文稿、读取幻灯片内容、管理幻灯片页面（创建、删除、读取、局部替换）。当用户需要创建或编辑幻灯片、读取或修改单个页面时使用。当用户给出 doubao.com 的 /slides/… |
| 7 | lark-markdown | `larksuite/cli@lark-markdown` | 18,041 | 398,007 | 飞书 Markdown：查看、创建、上传、编辑和比较飞书中的原生 Markdown 文件。当用户要操作飞书 Markdown 文件，或比较其远端版本及本地草稿时使用。纯本地 Markdown 文件操作不触发本… |
| 8 | slides | `nextlevelbuilder/ui-ux-pro-max-skill@slides` | 147,710 | 46,497 | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas,… |
| 9 | ultracave | `juliusbrussee/caveman@ultracave` | 118,839 | 42,143 | Caveman at maximum compression: fragments, one word when one word is enough, each fact once. Invoke only with… |
| 10 | defuddle | `kepano/obsidian-skills@defuddle` | 51,529 | 76,790 | Extract clean Markdown from HTML pages with Defuddle CLI. |
| 11 | referral-program | `coreyhaines31/marketingskills@referral-program` | 59,560 | 52,294 | When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth… |
| 12 | nano-pdf | `openclaw/openclaw@nano-pdf` | 394,301 | 7,161 | Edit PDFs with natural-language instructions using the nano-pdf CLI. |
| 13 | frontend-slides | `affaan-m/ecc@frontend-slides` | 300,648 | 6,558 | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when… |
| 14 | ppt-master | `hugohe3/ppt-master@ppt-master` | 75,609 | 22,460 | AI-driven presentation workflow for generating editable PPTX decks and slides, reconstructing page visuals,… |
| 15 | gws-sheets-read | `googleworkspace/cli@gws-sheets-read` | 32,230 | 52,084 | Google Sheets: Read values from a spreadsheet. |

## Animation & motion

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | hyperframes-animation | `heygen-com/hyperframes@hyperframes-animation` | 82,153 | 1,005,398 | All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene… |
| 2 | review-animations | `emilkowalski/skills@review-animations` | 55,720 | 297,163 | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering… |
| 3 | animation-vocabulary | `emilkowalski/skills@animation-vocabulary` | 55,720 | 275,922 | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact… |
| 4 | improve-animations | `emilkowalski/skills@improve-animations` | 55,720 | 262,735 | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit… |
| 5 | find-animation-opportunities | `emilkowalski/skills@find-animation-opportunities` | 55,720 | 245,990 | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't.… |
| 6 | animate | `emilkowalski/skills@animate` | 55,720 | 212,387 | Build an animation from scratch, making the decisions in the order that determines whether it feels right —… |
| 7 | animate-expo | `emilkowalski/skills@animate-expo` | 55,720 | 171,916 | Build animations in React Native and Expo, making the decisions in the order that determines whether they… |
| 8 | animate | `pbakaus/impeccable@animate` | 107,410 | 81,731 | Review a feature and enhance it with purposeful animations, micro-interactions, and motion effects that… |
| 9 | gsap | `heygen-com/hyperframes@gsap` | 82,153 | 92,062 | GSAP animation reference for HyperFrames. Covers gsap.to(), from(), fromTo(), easing, stagger, defaults,… |
| 10 | overdrive | `pbakaus/impeccable@overdrive` | 107,410 | 62,764 | Pushes interfaces past conventional limits with technically ambitious implementations — shaders, spring… |
| 11 | lottie | `heygen-com/hyperframes@lottie` | 82,153 | 69,051 | Lottie and dotLottie adapter patterns for HyperFrames. Use when embedding lottie-web JSON animations, .lottie… |
| 12 | waapi | `heygen-com/hyperframes@waapi` | 82,153 | 68,692 | Web Animations API adapter patterns for HyperFrames. Use when authoring element.animate() motion, Animation… |
| 13 | motion-doctrine | `heygen-com/hyperframes@motion-doctrine` | 82,153 | 62,287 | motion-doctrine — an installable skill for AI agents, published by heygen-com/hyperframes. |
| 14 | animation-performance | `emilkowalski/skills@animation-performance` | 55,720 | 73,994 | Keep web animations inside the frame budget — animate composite-only properties, keep motion off the main… |
| 15 | blender-motion-state-inspection | `affaan-m/ecc@blender-motion-state-inspection` | 300,648 | 6,218 | Use this skill when inspecting Blender characters, rigs, poses, animation retargeting, ground contact, facing… |

## Audio, voice & music

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | media-use | `heygen-com/hyperframes@media-use` | 82,153 | 1,371,189 | Get or make any media for a HyperFrames video - music, sound effects, images, icons, logos, voiceover, avatar… |
| 2 | caveman | `juliusbrussee/caveman@caveman` | 118,839 | 619,686 | Terse caveman voice: answer first, fluff gone, every technical fact kept. Use for /caveman, "caveman mode",… |
| 3 | music-to-video | `heygen-com/hyperframes@music-to-video` | 82,153 | 419,302 | Turn a music track (an audio file, a video to pull audio from, or a track generated from a mood brief) into a… |
| 4 | sherpa-onnx-tts | `openclaw/openclaw@sherpa-onnx-tts` | 394,301 | 5,349 | Local text-to-speech via sherpa-onnx (offline, no cloud) |
| 5 | sag | `openclaw/openclaw@sag` | 394,301 | 5,228 | ElevenLabs text-to-speech with mac-style say UX. |
| 6 | council | `affaan-m/ecc@council` | 300,648 | 5,687 | Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls. Use when multiple valid… |
| 7 | benchmark-methodology | `affaan-m/ecc@benchmark-methodology` | 300,648 | 4,852 | Score a scoped competitor set into comparable profile cards: nine weighted dimensions (positioning, voice,… |
| 8 | voice-call | `openclaw/openclaw@voice-call` | 394,301 | 3,172 | Start voice calls via the OpenClaw voice-call plugin. |
| 9 | no-ai-slop | `petergyang/no-ai-slop@no-ai-slop` | 13,345 | 30,500 | Edit drafts into sharper, more human writing while preserving the writer's personal voice, or detect AI-slop… |
| 10 | meeting-insights-analyzer | `composiohq/awesome-claude-skills@meeting-insights-analyzer` | 79,200 | 4,760 | Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and… |
| 11 | voicestudio | `debpalash/voicestudio@voicestudio` | 107,014 | 2,949 | Generate local speech with saved or designed voices, transcribe audio, and automate dubbing or narration… |
| 12 | venice-audio-music | `nexu-io/open-design@venice-audio-music` | 106,999 | 2,898 | Music generation queueing, retrieval, and completion endpoints via Venice.ai. Suited for jingles, background… |
| 13 | ai-music-album | `nexu-io/open-design@ai-music-album` | 106,999 | 2,871 | Full-lifecycle AI music album production — concept, lyric drafting, track sequencing, and export. Useful for… |
| 14 | speech | `nexu-io/open-design@speech` | 106,999 | 2,867 | Generate spoken audio from text using OpenAI's API with built-in voices. Useful for narrated explainers,… |
| 15 | venice-audio-speech | `nexu-io/open-design@venice-audio-speech` | 106,999 | 2,852 | Text-to-speech models, voices, formats, and streaming via Venice.ai. Useful for narration, voiceover, and… |

## Science & academia

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | healthcare-emr-patterns | `affaan-m/ecc@healthcare-emr-patterns` | 300,648 | 5,538 | EMR/EHR development patterns for healthcare applications. Clinical safety, encounter workflows, prescription… |
| 2 | healthcare-cdss-patterns | `affaan-m/ecc@healthcare-cdss-patterns` | 300,648 | 5,491 | Clinical Decision Support System (CDSS) development patterns. Drug interaction checking, dose validation,… |
| 3 | nature-polishing | `yuan1z0825/nature-skills@nature-polishing` | 53,059 | 18,666 | Polish, translate, or tighten existing academic prose while preserving facts, terminology, and evidence… |
| 4 | gget | `affaan-m/ecc@gget` | 300,648 | 3,244 | gget CLI and Python workflow for quick genomic database queries, sequence lookup, BLAST-style searches,… |
| 5 | scientific-thinking-literature-review | `affaan-m/ecc@scientific-thinking-literature-review` | 300,648 | 2,348 | Systematic literature-review workflow for academic, biomedical, technical, and scientific topics, including… |
| 6 | scientific-pkg-gget | `affaan-m/ecc@scientific-pkg-gget` | 300,648 | 2,140 | gget CLI and Python workflow for quick genomic database queries, sequence lookup, BLAST-style searches,… |
| 7 | academic-pipeline | `imbad0202/academic-research-skills@academic-pipeline` | 56,340 | 7,614 | Orchestrator for the full academic research pipeline: research -> write -> integrity check -> review ->… |
| 8 | math-olympiad | `anthropics/claude-plugins-official@math-olympiad` | 46,734 | 4,703 | Solve competition math problems (IMO, Putnam, USAMO, AIME) with adversarial verification that catches the… |
| 9 | directives | `vercel-labs/json-render@directives` | 19,546 | 8,088 | Pre-built custom directives for json-render — formatting, math, string manipulation, and i18n. Use when… |
| 10 | scientific-writing | `k-dense-ai/scientific-agent-skills@scientific-writing` | 56,722 | 2,609 | Drafts, revises, and audits scientific manuscripts or reports with explicit evidence provenance,… |
| 11 | scientific-visualization | `k-dense-ai/scientific-agent-skills@scientific-visualization` | 56,722 | 2,574 | Creates and audits truthful, accessible, publication-ready scientific figures with Matplotlib, Seaborn, or… |
| 12 | scientific-critical-thinking | `k-dense-ai/scientific-agent-skills@scientific-critical-thinking` | 56,722 | 2,529 | Evaluates scientific claims and evidence quality. Applies to experimental design validity, biases and… |
| 13 | scientific-brainstorming | `k-dense-ai/scientific-agent-skills@scientific-brainstorming` | 56,722 | 2,442 | Facilitates evidence-aware scientific ideation with independent generation, structured discussion, explicit… |
| 14 | matplotlib | `k-dense-ai/scientific-agent-skills@matplotlib` | 56,722 | 2,350 | Creates and customizes scientific plots with Matplotlib. Used for fine-grained control over plot elements,… |
| 15 | scientific-schematics | `k-dense-ai/scientific-agent-skills@scientific-schematics` | 56,722 | 2,328 | Generates scientific diagram drafts using Nano Banana 2 AI with smart iterative refinement. Uses Gemini 3.7… |

## Reverse engineering

| # | Skill | Install as | Stars | Installs | What it does |
|---:|---|---|---:|---:|---|
| 1 | reverse-engineer-anything | `morluto/rea@reverse-engineer-anything` | 449,333 | 16,989 | Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA, and… |
| 2 | protocol-reverse-engineering | `wshobson/agents@protocol-reverse-engineering` | 42,393 | 13,484 | Master network protocol reverse engineering including packet analysis, protocol dissection, and custom… |
| 3 | binary-analysis-patterns | `wshobson/agents@binary-analysis-patterns` | 42,393 | 11,417 | Master binary analysis patterns including disassembly, decompilation, control flow analysis, and code pattern… |
| 4 | m5-onboard | `anthropics/claude-plugins-official@m5-onboard` | 46,734 | 3,550 | End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer, Cardputer-Adv, Core, CoreS3,… |
| 5 | learn-reverse-engineering | `rohitg00/ai-engineering-from-scratch@learn-reverse-engineering` | 78,247 | 1,189 | Focused interactive tutor for the Reverse Engineering path in AI Engineering from Scratch. Start or resume… |
| 6 | iot-firmware | `ruvnet/ruflo@iot-firmware` | 81,415 | 903 | Orchestrate firmware rollouts with canary deployment and anomaly-gated advancement |
| 7 | ghidra-reverse | `zhaoxuya520/reverse-skill@ghidra-reverse` | 44,422 | 1,623 | Use for free/open reverse engineering with Ghidra (headless or GUI), including decompile, cross-refs, and… |
| 8 | radare2 | `zhaoxuya520/reverse-skill@radare2` | 44,422 | 1,511 | Use this skill whenever the user wants to analyze binaries with radare2/r2 from the command line, including… |
| 9 | binary-diff | `zhaoxuya520/reverse-skill@binary-diff` | 44,422 | 1,441 | 跨版本符号迁移与二进制差分。当你有旧版本的符号/逆向结果，需要快速迁移到新版本时使用。 适用场景：内核缺 PDB 用旧版符号推导、程序更新后批量迁移函数名、应用更新后快速定位新偏移。 核心方法：用 LLM… |
| 10 | iot-fleet | `ruvnet/ruflo@iot-fleet` | 81,415 | 766 | Create and manage Cognitum Seed device fleets with firmware policies |
| 11 | protocol-reverse | `zhaoxuya520/reverse-skill@protocol-reverse` | 44,422 | 1,340 | Use for authorized reverse engineering of custom binary protocols, Protobuf/gRPC, WebSocket frames, and… |
| 12 | friday-brief | `anthropics/knowledge-work-plugins@friday-brief` | 35,331 | 1,364 | Delivers the Friday end-of-week pulse — revenue vs prior week, top sellers, wins and watches. Accepts… |
| 13 | reverse-engineer | `sickn33/agentic-awesome-skills@reverse-engineer` | 49,484 | 915 | Expert reverse engineer specializing in binary analysis, disassembly, decompilation, and software analysis.… |
| 14 | binary-ninja-reverse | `zhaoxuya520/reverse-skill@binary-ninja-reverse` | 44,422 | 726 | Use for authorized binary analysis in Binary Ninja, including HLIL/MLIL/LLIL inspection,… |
| 15 | reverse-engineering | `rehan-remade/universal-modder@reverse-engineering` | 9,585 | 2,013 | Read how a game actually works so a mod can hook it. Decompile .NET/Mono (ILSpy), IL2CPP (Cpp2IL,… |
