from pathlib import Path
from html.parser import HTMLParser
import re,json,sys
R=Path(__file__).resolve().parents[2];s=(R/"privacy/index.html").read_text()
class P(HTMLParser):
 def __init__(self):super().__init__();self.h1=0;self.links=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=="h1":self.h1+=1
  if t=="a" and d.get("href"):self.links.append(d["href"])
x=P();x.feed(s)
c={"doctype":len(re.findall(r"<!doctype",s,re.I))==1,"h1":x.h1==1,"lang":'<html lang="nl">' in s,"meta":bool(re.search(r'<meta name="description" content="[^"]{45,}"',s)),"canonical":'href="https://haken-breien-shop.nl/privacy/"' in s,"robots":'<meta name="robots" content="noindex,follow">' in s,"no_wrong_fr":'hreflang="fr-FR"' not in s,"internal":all((R/"index.html" if x=="/" else R/x.lstrip("/")/"index.html").exists() for x in x.links if x.startswith("/") and not x.startswith("//"))}
print(json.dumps(c,indent=2));sys.exit(not all(c.values()))
