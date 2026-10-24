from pathlib import Path
from html.parser import HTMLParser
import re,sys,json
R=Path(__file__).resolve().parents[2]
p=R/"over-ons/index.html"
s=p.read_text(encoding="utf-8")
class P(HTMLParser):
 def __init__(self):super().__init__();self.h1=0;self.links=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=="h1":self.h1+=1
  if tag=="a" and d.get("href"):self.links.append(d["href"])
x=P();x.feed(s)
checks={"doctype":len(re.findall(r"<!doctype",s,re.I))==1,"h1":x.h1==1,"lang":'<html lang="nl">' in s,"title":bool(re.search(r"<title>.{12,}</title>",s)),"description":bool(re.search(r'<meta name="description" content="[^"]{45,}"',s)),"canonical":'href="https://haken-breien-shop.nl/over-ons/"' in s,"robots":'<meta name="robots" content="noindex,follow">' in s,"hreflang":'hreflang="fr-FR"' not in s,"links":all((R/"index.html" if h=="/" else R/h.lstrip("/")/"index.html").exists() for h in x.links if h.startswith("/") and not h.startswith("//"))}
print(json.dumps(checks,indent=2))
sys.exit(not all(checks.values()))
