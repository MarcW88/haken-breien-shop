# Haken & Breien editorial operation log

Upstream model: MarcW88/bloc-notes-numerique. Original agents and reference workflows remain available in `.agents/skills` and `workflow-templates`.

## Required traceability

For each page, create:
- `.content/briefs/haken--SLUG.md` — query intent, competitors, evidence, page boundaries, improvement plan
- `.content/reviews/haken--SLUG.md` — actual stages performed, failed checks, publication decision and outstanding human approval

Never infer that a GitHub Actions PASS means humanizer, fact-check or editorial QA executed. These are separate editorial actions. Preserve `noindex,follow` until approval. Use a single-page scope for changes. The target source of truth is each static `haken/SLUG/index.html`, not the Bloc-Notes `_generate.py`.
