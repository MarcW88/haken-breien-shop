"""Local stdlib validation for one or all Vergelijkingen pages. Does not run editorial AI skills."""
from pathlib import Path
from html.parser import HTMLParser
import os,re,sys,json
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/"vergelijkingen"
slug=os.getenv("VERGELIJKINGEN_PAGE","").strip("/")
pages=[BASE/"index.html"]+sorted(BASE.glob("*/index.html")) if not slug else [BASE/("index.html" if slug=="vergelijkingen" else slug+"/index.html")]
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=="h1":self.h1+=1
  if tag=="a" and d.get("href"):self.links.append(d["href"])
errors=[];rows=[]
for p in pages:
 if not p.exists():errors.append(f"missing {p}");continue
 s=p.read_text();u="/"+str(p.parent.relative_to(ROOT))+"/";doc=Links();doc.feed(s)
 checks={"one_doctype":len(re.findall(r"<!doctype",s,re.I))==1,"one_h1":doc.h1==1,"lang_nl":'<html lang="nl">' in s,"title":bool(re.search(r"<title>.{12,}</title>",s)),"meta_description":bool(re.search(r'<meta name="description" content="[^"]{45,}"',s)),"canonical":f'href="https://haken-breien-shop.nl{u}"' in s,"no_invalid_fr_hreflang":'hreflang="fr-FR"' not in s,"robots_kept":'name="robots" content="'+("index,follow" if p==BASE/"index.html" else "noindex,follow")+'"' in s}
 for href in doc.links:
  if href.startswith("/") and not href.startswith("//"):
   candidate=ROOT/href.lstrip("/")/"index.html"
   if not candidate.exists():checks["internal_links"]=False
 checks.setdefault("internal_links",True)
 if not all(checks.values()):errors.append(f"{p.relative_to(ROOT)}: "+str([k for k,v in checks.items() if not v]))
 rows.append({"path":str(p.relative_to(ROOT)),"checks":checks})
print(json.dumps({"pages":rows,"errors":errors},indent=2))
sys.exit(bool(errors))
