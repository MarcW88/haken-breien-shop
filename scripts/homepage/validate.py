from pathlib import Path
from html.parser import HTMLParser
import re,sys
R=Path(__file__).resolve().parents[2];s=(R/"index.html").read_text()
class P(HTMLParser):
 def __init__(self):super().__init__();self.h1=0;self.links=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=="h1":self.h1+=1
  if t=="a" and d.get("href"):self.links.append(d["href"])
p=P();p.feed(s)
checks=[len(re.findall(r"<!doctype",s,re.I))==1,p.h1==1,'<html lang="nl">' in s,'name="robots" content="index,follow"' in s,'href="https://haken-breien-shop.nl/"' in s,'hreflang="fr-FR"' not in s,all((R/"index.html" if u=="/" else R/u.lstrip("/")/"index.html").exists() for u in p.links if u.startswith("/") and not u.startswith("//"))]
print(checks);sys.exit(not all(checks))
