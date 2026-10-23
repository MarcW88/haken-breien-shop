# Haken & Breien — one-page-at-a-time editorial orchestration

## Scope
Site: Dutch SEO/GEO portal. Editorial directory: `/haken/`. This file supersedes the Bloc-Notes site-specific AGENTS.md for this repository; upstream skills stay byte-identical in `.agents/skills/`.

## Strict order — one URL per cycle
1. Read `.agents/skills/guide-analysis-workflow/SKILL.md` and use AUDIT for the selected `/haken/` URL. Treat its Bloc-Notes sections as **conceptual only**: do not route to /guides/, /marques/, /usages/, or /comparatifs/.
2. Research the specific Dutch-language search intent, evidence, competing pages, adjacent Haken pages and information gain. Output a page-specific brief. Never invent evidence or products.
3. Follow `.agents/skills/guide-content-workflow/SKILL.md`, using content-and-copy, humanizer, general-writing, anti-ai-slop, fact-check, internal-linking-audit, seo-onpage, seo-technical and editorial-qa in that sequence where applicable.
4. Modify **only the selected HTML page** and associated assets essential to it. Retain layout and navigation.
5. Run `python scripts/haken/validate.py` (or `HAKEN_PAGE=voor-beginners python scripts/haken/validate.py`), then GitHub Actions `Haken editorial quality and visual checks`. Inspect screenshots.
6. Submit final review using guide-analysis-workflow PUBLISH_REVIEW, publish to main, verify checks, and **ask the user to approve the page**. Never start the next page until approval.
7. Subpages remain noindex until a full evidence-based editorial review approves publication. Removing noindex also requires updating validator behavior and sitemap deliberately.

## Absolute safeguards
- Never execute copied Bloc-Notes Python generators to build this website: they target different source data and routes.
- Never use /guides/, /marques/, /comparatifs/, /usages/, /bons-plans/ paths as output.
- Do not invent personal experience, product tests, measurements, prices or citations.
- Dutch language, appropriate spelling and user-focused tutorials; mark affiliate links sponsored/no-follow.
- GitHub Actions validates and screenshots only. It does not run an LLM or automatically certify factual accuracy.
- Keep all upstream workflows in `workflow-templates/` for reference; only adapted actions in `.github/workflows/` are executable.
