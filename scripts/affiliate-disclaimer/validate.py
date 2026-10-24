from pathlib import Path
from html.parser import HTMLParser
import re,json,sys
R=Path(__file__).resolve().parents[2];s=(R/"affiliate-disclaimer/index.html").read_text()
class P(HTMLParser):
 def __init__(self):super().__init__();self.h1=0;self.links=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=="h1":self.h1+=1
  if tag=="a" and d.get("href"):self.links.append(d["href"])
x=P();x.feed(s)
c={"doctype":len(re.findall(r"<!doctype",s,re.I))==1,"h1":x.h1==1,"lang":'<html lang="nl">' in s,"meta_description":bool(re.search(r'<meta name="description" content="[^"]{45,}"',s)),"canonical":'href="https://haken-breien-shop.nl/affiliate-disclaimer/"' in s,"robots":'<meta name="robots" content="noindex,follow">' in s,"no_fr_hreflang":'hreflang="fr-FR"' not in s,"links":all((R/"index.html" if u=="/" else R/u.lstrip("/")/"index.html").exists() for u in x.links if u.startswith("/") and not u.startswith("//"))}
print(json.dumps(c,indent=2));sys.exit(not all(c.values()))
