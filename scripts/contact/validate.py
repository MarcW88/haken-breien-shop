from pathlib import Path
from html.parser import HTMLParser
import re,sys,json
R=Path(__file__).resolve().parents[2]
s=(R/"contact/index.html").read_text()
class P(HTMLParser):
 def __init__(self):super().__init__();self.h1=0;self.links=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=="h1":self.h1+=1
  if tag=="a" and a.get("href"):self.links.append(a["href"])
x=P();x.feed(s)
checks={"doctype":len(re.findall(r"<!doctype",s,re.I))==1,"one_h1":x.h1==1,"lang":'<html lang="nl">' in s,"meta_description":bool(re.search(r'<meta name="description" content="[^"]{45,}"',s)),"canonical":'href="https://haken-breien-shop.nl/contact/"' in s,"robots":'<meta name="robots" content="noindex,follow">' in s,"no_false_fr":'hreflang="fr-FR"' not in s,"internal_links":all((R/"index.html" if u=="/" else R/u.lstrip("/")/"index.html").exists() for u in x.links if u.startswith("/") and not u.startswith("//"))}
print(json.dumps(checks,indent=2));sys.exit(not all(checks.values()))
