"""Prevent an editorial page being marked publish-review PASS without independently recorded skill evidence.
No AI model is executed by this script. Missing reviews remain PENDING, not false PASS.
"""
from pathlib import Path
import hashlib, json, re, sys
ROOT=Path(__file__).resolve().parents[2]
PASSES=("fact-check","internal-linking-audit","humanizer","general-writing","anti-ai-slop","seo-onpage","seo-technical","editorial-qa","PUBLISH_REVIEW")
REPORT=ROOT/".artifacts/haken/editorial-passes.json"
REPORT.parent.mkdir(parents=True,exist_ok=True)
rows=[];errors=[]
for p in sorted((ROOT/"haken").glob("*/index.html")):
 slug=p.parent.name
 review=ROOT/".content/reviews"/f"haken--{slug}.json"
 status="PENDING_HUMAN_REVIEW"
 if review.exists():
  try:
   j=json.loads(review.read_text(encoding="utf-8"))
   status=j.get("status","DRAFT")
   if status in ("READY_FOR_HUMAN_VALIDATION","HUMAN_APPROVED","PUBLISHABLE"):
    missing=[step for step in PASSES if not isinstance(j.get("passes",{}).get(step),dict) or j["passes"][step].get("outcome")!="PASS" or not j["passes"][step].get("evidence")]
    if j.get("page_sha256")!=hashlib.sha256(p.read_bytes()).hexdigest():missing.append("stale_page_fingerprint")
    if missing:errors.append(f"{slug}: invalid READY claim: "+", ".join(missing))
   elif status not in ("DRAFT","QA_IN_PROGRESS","REVISION_REQUIRED","PENDING_HUMAN_REVIEW"):
    errors.append(f"{slug}: unknown editorial state {status}")
  except (ValueError,KeyError) as ex:errors.append(f"{slug}: invalid review JSON: {ex}")
 rows.append({"slug":slug,"status":status,"attestation_file":str(review.relative_to(ROOT)) if review.exists() else None})
REPORT.write_text(json.dumps({"pages":rows,"errors":errors},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(REPORT.read_text(encoding="utf-8"))
if errors:sys.exit(1)
