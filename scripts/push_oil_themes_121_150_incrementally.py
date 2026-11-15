#!/usr/bin/env python3
# scripts/push_oil_themes_121_150_incrementally.py
import subprocess
import sys
import time

BATCHES = [
    (["theme_121", "theme_122", "theme_123", "theme_124", "theme_125"], "themes 121-125 (Resilience & Connection part 1)"),
    (["theme_126", "theme_127", "theme_128", "theme_129", "theme_130"], "themes 126-130 (Connection part 2)"),
    (["theme_131", "theme_132", "theme_133", "theme_134", "theme_135"], "themes 131-135 (Connection 3 & Identity 1)"),
    (["theme_136", "theme_137", "theme_138", "theme_139", "theme_140"], "themes 136-140 (Identity part 2)"),
    (["theme_141", "theme_142", "theme_143", "theme_144", "theme_145"], "themes 141-145 (Identity 3 & Transcending Judgment 1)"),
    (["theme_146", "theme_147", "theme_148", "theme_149", "theme_150"], "themes 146-150 (Transcending Judgment part 2)"),
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

print("\n🎉 ALL THEMES 121-150 BATCHES PUSHED SUCCESSFULLY!")
