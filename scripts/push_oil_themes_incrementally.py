#!/usr/bin/env python3
# scripts/push_oil_themes_incrementally.py
import subprocess
import sys
import time

BATCHES = [
    (["theme_97", "theme_98", "theme_99", "theme_100"], "themes 97-100 (Status series)"),
    (["theme_101", "theme_102", "theme_103", "theme_104"], "themes 101-104 (Boundaries part 1)"),
    (["theme_105", "theme_106", "theme_107", "theme_108"], "themes 105-108 (Boundaries part 2)"),
    (["theme_109", "theme_110", "theme_111", "theme_112"], "themes 109-112 (Serenity part 1)"),
    (["theme_113", "theme_114", "theme_115", "theme_116"], "themes 113-116 (Serenity part 2)"),
    (["theme_117", "theme_118", "theme_119", "theme_120"], "themes 117-120 (Resilience series)"),
]

for themes, desc in BATCHES:
    print(f"\n📦 Processing batch: {desc}...")
    files_to_add = []
    for t in themes:
        files_to_add.append(f"assets/templates/multislides/{t}")
        files_to_add.append(f"website/public/images/themes/{t}")
    
    add_cmd = f"git add {' '.join(files_to_add)}"
    res = subprocess.run(add_cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"❌ git add failed: {res.stderr}")
        sys.exit(1)
        
    commit_msg = f"feat(art): add oil painting suites for {desc}"
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
            
    if not push_success:
        print(f"❌ Failed to push batch {desc} after 3 attempts.")
        sys.exit(1)

print("\n🎉 ALL OIL PAINTING THEME BATCHES PUSHED SUCCESSFULLY!")
