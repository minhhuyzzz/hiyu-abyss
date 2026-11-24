import json
import os
import glob

with open("scripts/oil_suites_101_300_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

assets_dir = "assets/templates/multislides"
web_dir = "website/public/images/themes"

complete_themes = []
incomplete_themes = []

for theme in manifest.values():
    stt = theme["stt"]
    key = f"theme_{stt}"
    
    missing_slides = []
    for s in theme["slides"]:
        s_idx = s["slide_index"]
        fn = f"slide_{s_idx}.jpg"
        p_asset = os.path.join(assets_dir, key, fn)
        p_web = os.path.join(web_dir, key, fn)
        
        if not os.path.exists(p_asset) or os.path.getsize(p_asset) < 10000:
            missing_slides.append(f"assets/{key}/{fn}")
        if not os.path.exists(p_web) or os.path.getsize(p_web) < 10000:
            missing_slides.append(f"web/{key}/{fn}")
            
    if missing_slides:
        incomplete_themes.append((stt, missing_slides))
    else:
        complete_themes.append(stt)

print(f"Complete themes: {len(complete_themes)} / 200")
print(f"Incomplete themes: {len(incomplete_themes)} / 200")
if incomplete_themes:
    print("Incomplete sample:")
    for stt, m in incomplete_themes[:10]:
        print(f"  Theme {stt}: {m}")
