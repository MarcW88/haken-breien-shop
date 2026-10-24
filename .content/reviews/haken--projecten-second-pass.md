# Second-pass editorial review — /haken/projecten/ — 2026-10-24

Decision: LIGHT_UPDATE, QA_IN_PROGRESS pending GitHub Actions.

1. guide-analysis-workflow (AUDIT): retained project decision-support architecture and identified specific wording, tutorial arithmetic and material guidance gaps.
2. seo-keyword / search-intent: page serves project selection, not detailed stitch instructions or product rankings. No unverified search volumes.
3. fact-check: Craft Yarn Council Single Crochet corroborates starting in second chain; 21 chains result in 20 single crochet stitches. Craft Yarn Council pattern-reading page confirms turning chain 1 is not counted in this example. Standard yarn label documentation confirms dye-lot numbers.
4. content-and-copy: inserted standalone stitch-count explanation, corrected materials guidance.
5. humanizer: replaced inflated hero claim with a natural reader question about what they can currently make.
6. general-writing: reduced abstract introductory language, replaced the overlong amigurumi and scarf formulations.
7. anti-ai-slop: removed generic “first project” framing, made yarn planning instructions concrete and avoided false assurances about project time.
8. internal-linking-audit: links retained to existing /haken/voor-beginners/, /haken/steken/, /haken/technieken/, /garen/, /materialen/haaknaalden/.
9. seo-onpage, seo-technical, editorial-qa: original semantic headings, title, meta, canonical and noindex retained; no first-hand testing claims.
10. PUBLISH_REVIEW: to be completed after latest CI. No automatic indexation.

Sources: https://www.craftyarncouncil.com/node/461 ; https://www.craftyarncouncil.com/standards/how-to-read-crochet-pattern ; https://media.craftyarncouncil.com/files/CIP/CYC_CIP_Crochet_Program_2017.pdf .

## Final machine check and publication decision

- GitHub Actions run 40091640731: SUCCESS for commit `0f0b6e5b2aecdb9842c090d8a721380d3081d595`.
- PUBLISH_REVIEW: **PASS — READY_FOR_HUMAN_VALIDATION** for the scoped editorial update. This status does not mean an autonomous AI pipeline ran in GitHub Actions; the discrete review observations are recorded above.
- User confirmation still required. `noindex,follow` remains unchanged. No other Haken article modified in this cycle.
