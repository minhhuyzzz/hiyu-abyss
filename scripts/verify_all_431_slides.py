import os
import json
import hashlib

MANIFEST_PATH = "scripts/oil_suites_301_500_manifest.json"
MULTI_DIR = "assets/templates/multislides"
WEB_DIR = "website/public/images/themes"

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = json.load(f)

errors = []
total_slides = 0
hashes = {}

for tid, t in manifest.items():
    stt = t["stt"]
    if not (301 <= stt <= 500):
        continue
    slides = t["slides"]
    for s in slides:
        total_slides += 1
        s_idx = s["slide_index"]
        
        mf = os.path.join(MULTI_DIR, f"theme_{stt}", f"slide_{s_idx}.jpg")
        wf = os.path.join(WEB_DIR, f"theme_{stt}", f"slide_{s_idx}.jpg")
        
        if not os.path.exists(mf):
            errors.append(f"Missing {mf}")
        elif os.path.getsize(mf) < 30000:
            errors.append(f"Corrupt/small {mf}")
        else:
            with open(mf, "rb") as fp:
                h = hashlib.md5(fp.read()).hexdigest()
            if h in hashes:
                prev = hashes[h]
                errors.append(f"DUPLICATE HASH between {mf} and {prev}!")
            else:
                hashes[h] = mf
                
        if not os.path.exists(wf):
            errors.append(f"Missing {wf}")

print(f"Total checked: {total_slides} slides.")
print(f"Unique image hashes: {len(hashes)} / {total_slides}")
if errors:
    print(f"❌ ERRORS ({len(errors)}):")
    for e in errors[:10]:
        print(" ", e)
else:
    print(f"🎉 100% PERFECT! All {total_slides} slides exist, are healthy, and have ZERO DUPLICATE HASHES!")
