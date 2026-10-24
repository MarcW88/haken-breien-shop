# PUBLISH_REVIEW — section /haken/ — 2026-10-24

## Source of truth and checks
Head inspected: `1e8b12c2bd083638476d90f3dadc03dc63164edd`.
- GitHub Actions editorial validation: https://github.com/MarcW88/haken-breien-shop/actions/runs/40090488732 — **SUCCESS**.
- GitHub Pages deployment: https://github.com/MarcW88/haken-breien-shop/actions/runs/40090488625 — **SUCCESS**.
- Five checked pages: exactly one DOCTYPE, one H1, non-placeholder title and canonical. Validated HTML metadata and existing local links by CI.
- Robots: `Allow: /`; sitemap lists /haken/ and omits four current noindex subpages.

## Page-by-page decisions
| URL | Editorial role | Robots in main | Owner status recorded | PUBLISH_REVIEW |
| --- | --- | --- | --- | --- |
| /haken/ | Category hub and learning route | index,follow | Explicitly approved in chat, 2026-10-24 | **PASS for documented technical checks; approved hub content** |
| /haken/voor-beginners/ | First stitches and exercise | noindex,follow | No explicit indexation approval | **FAIL — KEEP_NOINDEX**: incomplete individual skill attestation |
| /haken/steken/ | Reference for crochet stitches | noindex,follow | Prior review requests further QA; no explicit indexation approval | **FAIL — KEEP_NOINDEX**: review explicitly says independent humanizer/anti-ai-slop not demonstrated |
| /haken/technieken/ | Rounds, shaping and techniques | noindex,follow | Prior page feedback positive; no explicit indexation approval | **FAIL — KEEP_NOINDEX**: unresolved prior full PUBLISH_REVIEW and incomplete linked-source attestation |
| /haken/projecten/ | Projects by ability | noindex,follow | Explicitly approved in chat, 2026-10-24 | **FAIL — KEEP_NOINDEX** for publish gate: review is still QA_IN_PROGRESS; approval of content is not an instruction to change indexation |

## Technical limitations and corrective actions
1. `scripts/haken/validate.py` checks HTML metadata, internal href existence and current robots rules, not sources, language quality or full skill execution.
2. `scripts/haken/editorial_gate.py` accepts absent page attestation files as pending. The absence is not equivalent to passing humanizer/general-writing/anti-ai-slop. JSON evidence files have not been supplied for each page.
3. Four detailed subpages remain `noindex,follow`. This review makes **no indexation changes**. A separate explicit owner instruction and passed editorial review should precede changes.
4. Source links have not all been live-verified in this consolidated review; no claims of exhaustive reference auditing.
5. Design preview and user-experience testing are out of scope at the owner's request (no Playwright).

## Overall verdict
**Hub /haken/: accepted and technical checks PASS.**
**Full section: FAIL — KEEP_NOINDEX for the four subpages pending per-page evidence and publish review.**

This report is an honest audit of existing artifacts and user approvals, not a claim that all editorial agents have run. No content HTML modified.
