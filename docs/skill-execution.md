# Mandatory per-page skills execution protocol

The upstream `bloc-notes-numerique` guide-content-workflow does **not** call an LLM in GitHub Actions. Its chat agent must carry out `humanizer`, then `general-writing`, then `anti-ai-slop` as **separate passes**, not a generic re-read. No GitHub Action PASS is evidence that a language-model skill ran.

## Before declaring the page ready

1. Read the FULL matching `.agents/skills/guide-analysis-workflow/SKILL.md` and `guide-content-workflow/SKILL.md`, their relevant references, and the separate `humanizer`, `general-writing`, `anti-ai-slop` instructions.
2. Analyze search intent, competitive gaps, facts and page neighbors; create a distinct brief.
3. Produce the page using content-and-copy.
4. Independently run factual verification and internal-linking-audit, then **humanizer → general-writing → anti-ai-slop**, revising the actual HTML after each pass. Record specific observations and changes for each pass.
5. Run seo-onpage, seo-technical, editorial-qa and the machine validator. Repeat any pass invalidated by later changes.
6. Run guide-analysis-workflow PUBLISH_REVIEW and record a separate decision. Do not allow automatic publication/indexation merely because CI passes.
7. Write `.content/reviews/haken--SLUG.json` with `status`, SHA256 hash of final HTML at `page_sha256`, and `passes` entries. Every entry needs `outcome: PASS` and nonempty truthful `evidence`; never pre-populate PASS fields or simulate skills. GitHub verifies state integrity, not substantive quality. Existing missing reports mean PENDING, NOT PASS.

The CI `editorial_gate.py` rejects false READY/PUBLISHABLE states and stale page fingerprints. Drafts and missing attestations remain PENDING and `noindex`. The user explicitly requested no Playwright dependency.
