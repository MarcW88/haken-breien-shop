# Haken & Breien — editorial agent orchestration

Read `docs/content-maintenance.md` before changing any editorial URL. Agents are sourced verbatim from Bloc-Notes Numériques under `.agents/skills/`; the local routing, targets and publish policies live here and in `maintenance.config.json`.

**Never run the copied Bloc-Notes `_generate.py`, `apply_hreflang.py`, or `apply_section_indexation.py` on this website.** They target a different site. Likewise, legacy YAML workflows are preserved only under `workflow-templates/`.

For each URL: `maintenance prepare` -> guide/comparison analysis AUDIT -> SERP/source evidence -> unique brief -> content and copy -> humanizer -> general writing -> anti-ai-slop -> fact check/links/technical QA -> analysis PUBLISH_REVIEW -> machine validation -> push main -> **user approval**. Explicitly record any stage not performed. Only one page per cycle, never proceed without user approval.

Use `.content/briefs/<section>--<slug>.md` and `.content/reviews/<section>--<slug>.md`. Keep drafts noindex. No quotas of word count, H2 or FAQs. Dutch-language editorial website, not a hard-sell shop. Do not claim first-hand tests or source verification not performed. No Playwright requirement.

## Mandatory independent passes and attestation
Read `docs/skill-execution.md` before treating any page as complete. `humanizer`, `general-writing`, and `anti-ai-slop` MUST be executed separately by the chat agent, with concrete edits and individually documented evidence. Never substitute CI PASS for those executions. `scripts/haken/editorial_gate.py` prevents false ready claims; missing attestations mean PENDING, not a quality pass.
