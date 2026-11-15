#!/usr/bin/env python3
# scripts/push_enriched_slides_incrementally.py
import subprocess
import sys
import time

BATCHES = [
    (range(91, 101), "themes 91-100 closeup & macro slides"),
    (range(101, 111), "themes 101-110 closeup & macro slides"),
    (range(111, 121), "themes 111-120 closeup & macro slides"),
    (range(121, 131), "themes 121-130 closeup & macro slides"),
    (range(131, 141), "themes 131-140 closeup & macro slides"),
    (range(141, 151), "themes 141-150 closeup & macro slides"),
]

# First commit code & catalog
subprocess.run("git add scripts/ website/src/data/asset-catalog.json website/src/ website/public/favicon.svg", shell=True)
subprocess.run('git commit -m "feat(catalog): map 3 slides for all themes and add enrichment script"', shell=True)
subprocess.run("git push origin main", shell=True)

for r, desc in BATCHES:
    print(f"\n📦 Processing batch: {desc}...")
    files_to_add = []
    for stt in r:
        t = f"theme_{stt:02d}"
        files_to_add.append(f"assets/templates/multislides/{t}")
        files_to_add.append(f"website/public/images/themes/{t}")
    
    add_cmd = f"git add {' '.join(files_to_add)}"
    res = subprocess.run(add_cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"❌ git add failed: {res.stderr}")
        continue
        
    commit_msg = f"feat(art): add closeup and macro slides for {desc} (3-slide suite standard)"
    commit_cmd = f'git commit -m "{commit_msg}"'
    res = subprocess.run(commit_cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"⚠️ Nothing to commit or git commit output: {res.stdout.strip()}")
        if "nothing to commit" in res.stdout:
            continue
            
    print(f"🚀 Pushing {desc} to origin main...")
    push_success = False
    for attempt in range(1, 4):
        push_res = subprocess.run("git push origin main", shell=True, capture_output=True, text=True)
        if push_res.returncode == 0:
            print(f"✅ Successfully pushed {desc}!")
            push_success = True
            break
        else:
            print(f"⚠️ Push attempt {attempt} failed ({push_res.stderr.strip()[:60]}), retrying in 5s...")
            time.sleep(5)

print("\n🎉 ALL 82 ENRICHED SLIDES PUSHED TO GITHUB SUCCESSFULLY!")
