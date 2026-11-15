#!/usr/bin/env python3
# scripts/organize_generated_oil_suites.py - Tự động quét, khử dấu vết AI và đồng bộ ảnh sơn dầu
import os
import glob
import shutil
import json
import re
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

BRAIN_DIR = r"C:\Users\CPS\.gemini\antigravity\brain\5a62bc38-8751-4208-9565-f6754b88d3e6"
OUTPUT_DIR = r"c:\hiyuabyss\assets\templates\multislides"
WEBSITE_PUBLIC = r"c:\hiyuabyss\website\public\images\themes"

TARGET_W, TARGET_H = 1080, 1920

def remove_ai_sheen_and_enhance(im: Image.Image) -> Image.Image:
    """
    Khử hoàn toàn dấu vết AI bóng bẩy (anti-AI-slop):
    1. Đưa về kích thước chuẩn 1080x1920 bằng Lanczos.
    2. Cân bằng sắc tố sơn dầu: giảm độ bão hòa kỹ thuật số quá mức (saturation -5%), tăng nhẹ độ tương phản vật lý.
    3. Thêm lớp hạt vi mô hữu cơ (organic canvas grain) để phá vỡ bề mặt mịn nhựa (plastic waxy texture) của AI.
    4. Unsharp Mask tinh tế để nổi rõ vân cọ và thớ vải toan tự nhiên.
    """
    # 1. Resize to 1080x1920 keeping aspect ratio with crop if needed
    w, h = im.size
    target_ratio = TARGET_W / TARGET_H
    current_ratio = w / h
    
    if abs(current_ratio - target_ratio) > 0.01:
        if current_ratio > target_ratio:
            new_w = int(h * target_ratio)
            left = (w - new_w) // 2
            im = im.crop((left, 0, left + new_w, h))
        else:
            new_h = int(w / target_ratio)
            top = (h - new_h) // 2
            im = im.crop((0, top, w, top + new_h))
            
    resized = im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    
    # 2. Color grading: Reduce synthetic saturation slightly, boost warm oil contrast
    sat = ImageEnhance.Color(resized).enhance(0.96)
    contrast = ImageEnhance.Contrast(sat).enhance(1.04)
    
    # 3. Add organic micro-grain (eliminates waxy AI plastic look)
    arr = np.array(contrast, dtype=np.float32)
    noise = np.random.normal(0, 2.5, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    grained = Image.fromarray(arr)
    
    # 4. Enhance physical paint impasto edge sharpness
    sharpened = grained.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=2))
    return sharpened

def sync_images():
    print("=== SYNCHRONIZING & PURIFYING GENERATED OIL PAINTING SUITES ===")
    pattern = os.path.join(BRAIN_DIR, "theme_*_slide_*_*.jpg")
    found_files = glob.glob(pattern)
    print(f"Total candidate files found in brain directory: {len(found_files)}")
    
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
            continue
        
        target_dir = os.path.join(OUTPUT_DIR, theme_id)
        os.makedirs(target_dir, exist_ok=True)
        target_file = os.path.join(target_dir, f"slide_{slide_idx}.jpg")
        
        # Purify and save
        try:
            raw_im = Image.open(fpath).convert("RGB")
            purified_im = remove_ai_sheen_and_enhance(raw_im)
            purified_im.save(target_file, "JPEG", quality=95, optimize=True)
            
            # Copy to website public
            web_target_dir = os.path.join(WEBSITE_PUBLIC, theme_id)
            os.makedirs(web_target_dir, exist_ok=True)
            purified_im.save(os.path.join(web_target_dir, f"slide_{slide_idx}.jpg"), "JPEG", quality=95, optimize=True)
            
            synced[key] = target_file
            print(f"  -> Purified & Synced {key} ({TARGET_W}x{TARGET_H}, {os.path.getsize(target_file)} bytes)")
        except Exception as e:
            print(f"  ❌ Error processing {fpath}: {e}")

    print(f"\nTotal synced & purified slides: {len(synced)}")

if __name__ == "__main__":
    sync_images()
