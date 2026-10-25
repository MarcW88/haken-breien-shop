# CSS and responsive correction review — 25 October 2026

## Scope

User explicitly authorized site-wide CSS and responsive corrections after the visual audit. Baseline main commit: 597ec642f1484bd9b91e5c09886b3dec264651bd. Applied the installed site-design-review workflow principles. No DESIGN.md exists in this repository. No editorial rewriting or content-generation workflow was run: this change concerns presentation and table wrappers only.

## Changes

- Shared rules in assets/style.css override legacy page-local spacing: readable title scales, consistent mobile gutters, restrained heading spacing and neutral inner-page heroes.
- Long Dutch words wrap without widening the document. Grid items may shrink to their available width.
- Added accessible horizontal-scroll wrappers to the previously uncontained tables in garen/acryl/index.html and haken/steken/index.html.
- Editorial figures are limited to 780px; responsive sizing, radius and caption tokens are defined. The homepage hero retains its dedicated image treatment.
- Footer links now use the correct direct-child selector and an explicit two-column grid.
- Homepage cards use a balanced 2/2/3 desktop arrangement, more compact mobile cards and a smaller decorative feature. Existing wording and links are retained.
- Editorial paragraph links and keyboard focus are visible. Two decorative wavy symbols use a widely supported fallback glyph.

## Executed verification

Actual local Chromium launched through Playwright. The default Playwright browser download returned an unusable archive; a packaged Chromium binary was used instead. This was a real browser render, not a code-only audit.

- All 35 routes tested at 1440x1000 and 390x844: 70 views, all HTTP 200, no page JavaScript errors, all 14 images loaded in each viewport.
- Horizontal document overflows at 390px: 7 before, 0 after.
- All 35 routes additionally tested at 320px and 768px: 70 additional views, 0 horizontal document overflows in the final pass. An initially detected long word on Privacy at 320px was corrected before the final pass.
- Opened desktop/mobile screenshots of homepage, hubs and guides, including corrected titles, gutters, image size and footer. Captured top views for every route; supplemental middle/bottom/image captures for eight representative routes in both viewports. Used viewport captures for long-page inspection because full-page browser rasterization was unreliable on very long pages in this environment.
- Verified the native FAQ interaction during the audit. Keyboard focus is visible; table wrappers are focusable scroll regions.
- Local validators for Haken, Breien, Garen, Materialen, Patronen, Koopadvies and Inspiratie all passed.
- Compared parsed HTML text before/after on both edited HTML files: identical. Existing metadata, links, robots directives and generated image assets remain unchanged.

Screenshots and measurement JSON are local verification artifacts under .artifacts/design-review-before/ and .artifacts/design-review-after/; they are not part of this commit. This is not a full accessibility certification. GitHub Actions and deployment status are checked after publication and must not be inferred from this pre-publication record.
