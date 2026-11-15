#!/usr/bin/env python3
# scripts/push_distinct_98_oil_themes_incrementally.py
import subprocess
import sys
import time

# 1. Commit scripts and manifests first
print("📦 Committing and pushing scripts and manifests...")
scripts_to_add = [
    "scripts/curate_98_distinct_oil_art.py",
    "scripts/curated_98_distinct_oil_art.json",
    "scripts/inspect_slides_text.py",
    "scripts/mass_produce_98_distinct_oil_suites.py",
    "scripts/posts_151_200_slides_detail.json",
    "scripts/resolve_98_distinct_oil_art.py",
    "scripts/resolved_98_distinct_oil_art.json",
    "scripts/update_oil_catalog_151_200_distinct.py",
    "scripts/verify_98_distinct_oil_suites.py",
    "scripts/push_distinct_98_oil_themes_incrementally.py",
    "website/src/data/asset-catalog.json"
]

subprocess.run(f"git add {' '.join(scripts_to_add)}", shell=True)
subprocess.run('git commit -m "feat(art): add manifests and scripts for 98 distinct oil masterpieces"', shell=True)
subprocess.run("git push origin main", shell=True)

# 2. Push image batches (5 themes per batch)
BATCHES = [
    (["theme_151", "theme_152", "theme_153", "theme_154", "theme_155"], "themes 151-155 (Manipulation batch 1)"),
    (["theme_156", "theme_157", "theme_158", "theme_159", "theme_160"], "themes 156-160 (Manipulation batch 2)"),
    (["theme_161", "theme_162", "theme_163", "theme_164", "theme_165"], "themes 161-165 (Crowd Psychology batch 1)"),
    (["theme_166", "theme_167", "theme_168", "theme_169", "theme_170"], "themes 166-170 (Crowd Psychology batch 2)"),
    (["theme_171", "theme_172", "theme_173", "theme_174", "theme_175"], "themes 171-175 (Bad Faith & Freedom batch 1)"),
    (["theme_176", "theme_177", "theme_178", "theme_179", "theme_180"], "themes 176-180 (Bad Faith & Freedom batch 2)"),
    (["theme_181", "theme_182", "theme_183", "theme_184", "theme_185"], "themes 181-185 (Cognitive Biases batch 1)"),
    (["theme_186", "theme_187", "theme_188", "theme_189", "theme_190"], "themes 186-190 (Cognitive Biases batch 2)"),
    (["theme_191", "theme_192", "theme_193", "theme_194", "theme_195"], "themes 191-195 (Existentialism batch 1)"),
    (["theme_196", "theme_197", "theme_198", "theme_199", "theme_200"], "themes 196-200 (Existentialism batch 2)"),
]

for themes, desc in BATCHES:
    print(f"\n📦 Processing batch: {desc}...")
    paths = []
    for t in themes:
        paths.append(f"assets/templates/multislides/{t}")
        paths.append(f"website/public/images/themes/{t}")

    # Use git add -A on paths so both modifications and deletions of old crops are staged
    add_cmd = f"git add -A {' '.join(paths)}"
    subprocess.run(add_cmd, shell=True)

    commit_msg = f"feat(art): replace cropped slides with distinct museum artworks for {desc}"
    commit_cmd = f'git commit -m "{commit_msg}"'
    subprocess.run(commit_cmd, shell=True)

    print(f"🚀 Pushing {desc} to origin main...")
    push_success = False
    for attempt in range(1, 4):
        push_res = subprocess.run("git push origin main", shell=True, capture_output=True, text=True)
        if push_res.returncode == 0:
            print(f"✅ Successfully pushed {desc}!")
            push_success = True
            break
        else:
            print(f"⚠️ Push attempt {attempt} failed ({push_res.stderr.strip()[:60]}), retrying in 4s...")
            time.sleep(4)

    if not push_success:
        print(f"❌ Failed to push batch {desc} after 3 attempts.")
        sys.exit(1)

print("\n🎉 ALL 50 DISTINCT OIL MASTERPIECE THEMES PUSHED SUCCESSFULLY!")
