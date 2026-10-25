# Atelier textile — sitewide rollout

User explicitly approved the two-page visual pilot and requested rollout to the entire site.

All 35 HTML pages now load assets/atelier.css and carry the atelier body class. Existing page components receive shared role classes for intros, notes, cards, contents navigation and sidebars. Table, heading, image, button, header and footer styling follows the approved cream/forest/sage direction. Existing local layout structures are retained, with previous responsive fixes.

Verification: real Chromium/Playwright, 35 routes at 1440/768/390/320 px (140 views). All HTTP 200, no JavaScript errors, images loaded, no horizontal document overflow. Desktop/mobile viewport screenshots created for all pages. Representative captures opened and examined across hubs, buying guides, pattern guides, inspiration and material articles. Text, links and metadata compared programmatically against repository baseline: preserved on all 35 pages. Seven section technical validators PASS; diff whitespace check PASS.

Artifacts: .artifacts/atelier-rollout/ (not versioned). No SEO/editorial rewrite, no new image generation and no indexation changes. This is visual rollout verification, not a full accessibility certification.
