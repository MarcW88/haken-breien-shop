"""Single-page Haken publication gate. Stdlib only. Content writing remains human-approved."""
from pathlib import Path
from html.parser import HTMLParser
import json, os, re, sys

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "haken"
ART = ROOT / ".artifacts" / "haken"
ART.mkdir(parents=True, exist_ok=True)
PAGES = [BASE / "index.html"] + sorted(BASE.glob("*/index.html"))
SLUG = os.getenv("HAKEN_PAGE", "").strip().strip("/")
if SLUG:
    if "/" in SLUG or SLUG in (".", ".."):
        raise SystemExit("Only one Haken page slug may be selected")
    PAGES = [BASE / ("index.html" if SLUG == "haken" else SLUG + "/index.html")]

class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_h1 = False
        self.h1 = 0
        self.links = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "h1": self.h1 += 1
        if tag == "a" and d.get("href"): self.links.append(d["href"])

failures = []
results = []
for page in PAGES:
    if not page.is_file():
        failures.append(f"Missing page: {page.relative_to(ROOT)}")
        continue
    html = page.read_text(encoding="utf-8")
    doc = Document()
    doc.feed(html)
    rel = page.relative_to(ROOT).as_posix()
    url = "/" + str(page.parent.relative_to(ROOT)).replace("\\", "/") + "/"
    is_hub = page == BASE / "index.html"
    checks = {
      "one_h1": doc.h1 == 1,
      "title": bool(re.search(r"<title>[^<]{8,}</title>", html, re.I)),
      "description": bool(re.search(r'<meta name="description" content="[^"]{30,}"', html, re.I)),
      "canonical": f'href="https://haken-breien-shop.nl{url}"' in html,
      "lang_nl": '<html lang="nl">' in html,
      "correct_indexation": ('name="robots" content="index,follow"' if is_hub else 'name="robots" content="noindex,follow"') in html or (not is_hub and '<!-- approved-index -->' in html),
      "stylesheet_exists": (ROOT / "assets/style.css").is_file(),
      "no_french_hreflang": 'hreflang="fr-FR"' not in html
    }
    for href in doc.links:
        if href.startswith("/") and not href.startswith("//") and not href.startswith("/#"):
            candidate = ROOT / href.lstrip("/") / "index.html"
            if href.endswith((".css", ".js", ".svg", ".png", ".jpg", ".xml", ".txt")):
                candidate = ROOT / href.lstrip("/")
            if not candidate.exists(): checks["internal_links"] = False
    checks.setdefault("internal_links", True)
    for key, ok in checks.items():
        if not ok: failures.append(f"{rel}: {key}")
    results.append({"page":rel,"checks":checks,"status":"PASS" if all(checks.values()) else "FAIL"})
report = {"pages":results,"failures":failures,"status":"PASS" if not failures else "FAIL"}
(ART / "report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
print(json.dumps(report,indent=2,ensure_ascii=False))
sys.exit(bool(failures))
