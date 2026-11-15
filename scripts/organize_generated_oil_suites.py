#!/usr/bin/env python3
# scripts/organize_generated_oil_suites.py - Tự động quét và đồng bộ các ảnh sơn dầu đã render
import os
import glob
import shutil
import json
import re

BRAIN_DIR = r"C:\Users\CPS\.gemini\antigravity\brain\5a62bc38-8751-4208-9565-f6754b88d3e6"
OUTPUT_DIR = r"c:\hiyuabyss\assets\templates\multislides"
WEBSITE_PUBLIC = r"c:\hiyuabyss\website\public\images\themes"

with open("scripts/oil_suites_prompts_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

def sync_images():
    print("=== SYNCHRONIZING GENERATED OIL PAINTING SUITES ===")
    pattern = os.path.join(BRAIN_DIR, "theme_*_slide_*_*.jpg")
    found_files = glob.glob(pattern)
    print(f"Total candidate files found in brain directory: {len(found_files)}")
    
    # Sort by mtime descending to get latest
    found_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    
    synced = {}
    for fpath in found_files:
        fname = os.path.basename(fpath)
        m = re.match(r"(theme_\d+)_slide_(\d+)_\d+\.jpg", fname)
        if not m:
            continue
        theme_id = m.group(1)
        slide_idx = m.group(2)
        key = f"{theme_id}_slide_{slide_idx}"
        if key in synced:
            continue  # already got latest
        
        target_dir = os.path.join(OUTPUT_DIR, theme_id)
        os.makedirs(target_dir, exist_ok=True)
        target_file = os.path.join(target_dir, f"slide_{slide_idx}.jpg")
        
        # Copy to multislides
        shutil.copyfile(fpath, target_file)
        
        # Also copy to website public if directory exists
        web_target_dir = os.path.join(WEBSITE_PUBLIC, theme_id)
        os.makedirs(web_target_dir, exist_ok=True)
        shutil.copyfile(fpath, os.path.join(web_target_dir, f"slide_{slide_idx}.jpg"))
        
        synced[key] = target_file
        print(f"  -> Synced {key} ({os.path.getsize(target_file)} bytes)")

    print(f"\nTotal synced slides: {len(synced)}")

if __name__ == "__main__":
    sync_images()
