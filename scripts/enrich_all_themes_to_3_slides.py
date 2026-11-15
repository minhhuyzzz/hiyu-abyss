#!/usr/bin/env python3
# scripts/enrich_all_themes_to_3_slides.py - Bổ sung crop soi vào (Closeup & Macro) để 100% theme có đủ 3 slide
import os
import glob
import json
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

OUTPUT_BASE = r"c:\hiyuabyss\assets\templates\multislides"
WEBSITE_PUBLIC = r"c:\hiyuabyss\website\public\images\themes"
CACHE_DIR = r"c:\hiyuabyss\assets\templates\raw_cache"

TARGET_W, TARGET_H = 1080, 1920
TARGET_RATIO = TARGET_W / TARGET_H  # 9/16 = 0.5625

def process_and_purify_oil_painting(raw_im: Image.Image) -> Image.Image:
    """Chuẩn hóa toan vải hữu cơ HYA-08"""
    resized = raw_im.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    sat = ImageEnhance.Color(resized).enhance(0.96)
    contrast = ImageEnhance.Contrast(sat).enhance(1.04)
    arr = np.array(contrast, dtype=np.float32)
    noise = np.random.normal(0, 2.5, arr.shape)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    grained = Image.fromarray(arr)
    sharpened = grained.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=2))
    return sharpened

def make_zoom_crop(im: Image.Image, zoom_factor: float, cx_ratio: float = 0.5, cy_ratio: float = 0.5) -> Image.Image:
    w, h = im.size
    if w / h > TARGET_RATIO:
        base_h = h
        base_w = int(h * TARGET_RATIO)
    else:
        base_w = w
        base_h = int(w / TARGET_RATIO)
        
    crop_w = max(10, int(base_w / zoom_factor))
    crop_h = max(10, int(base_h / zoom_factor))
    
    cx = int(w * cx_ratio)
    cy = int(h * cy_ratio)
    
    left = max(0, min(w - crop_w, cx - crop_w // 2))
    top = max(0, min(h - crop_h, cy - crop_h // 2))
    
    cropped = im.crop((left, top, left + crop_w, top + crop_h))
    return cropped

def main():
    print("=== BẮT ĐẦU BỔ SUNG SLIDE CLOSEUP & MACRO ĐẠT CHUẨN 3 SLIDE (THEME 91 - 150) ===")
    
    created_count = 0
    
    for stt in range(91, 151):
        theme_id = f"theme_{stt:02d}"
        theme_dir = os.path.join(OUTPUT_BASE, theme_id)
        web_dir = os.path.join(WEBSITE_PUBLIC, theme_id)
        os.makedirs(theme_dir, exist_ok=True)
        os.makedirs(web_dir, exist_ok=True)
        
        slide_1_path = os.path.join(theme_dir, "slide_1.jpg")
        slide_2_path = os.path.join(theme_dir, "slide_2.jpg")
        slide_3_path = os.path.join(theme_dir, "slide_3.jpg")
        
        # Check source raw image
        raw_1_path = os.path.join(CACHE_DIR, f"{theme_id}_slide_1_raw.jpg")
        raw_2_path = os.path.join(CACHE_DIR, f"{theme_id}_slide_2_raw.jpg")
        
        src_im_1 = None
        if os.path.exists(raw_1_path) and os.path.getsize(raw_1_path) > 1000:
            try:
                src_im_1 = Image.open(raw_1_path).convert("RGB")
            except Exception:
                pass
        if src_im_1 is None and os.path.exists(slide_1_path):
            try:
                src_im_1 = Image.open(slide_1_path).convert("RGB")
            except Exception:
                pass
                
        src_im_2 = None
        if os.path.exists(raw_2_path) and os.path.getsize(raw_2_path) > 1000:
            try:
                src_im_2 = Image.open(raw_2_path).convert("RGB")
            except Exception:
                pass
        if src_im_2 is None and os.path.exists(slide_2_path):
            try:
                src_im_2 = Image.open(slide_2_path).convert("RGB")
            except Exception:
                pass

        # Case 1: Thiếu slide_2 (Theme chỉ có 1 slide)
        if not os.path.exists(slide_2_path) and src_im_1:
            crop_2 = make_zoom_crop(src_im_1, zoom_factor=1.65, cx_ratio=0.50, cy_ratio=0.48)
            purified_2 = process_and_purify_oil_painting(crop_2)
            purified_2.save(slide_2_path, "JPEG", quality=95, optimize=True)
            purified_2.save(os.path.join(web_dir, "slide_2.jpg"), "JPEG", quality=95, optimize=True)
            created_count += 1
            print(f"✅ {theme_id}/slide_2.jpg (Closeup 1.65x)")

        # Case 2: Thiếu slide_3 (Theme có 1 slide hoặc 2 slide)
        if not os.path.exists(slide_3_path):
            base_src = src_im_2 if src_im_2 else src_im_1
            if base_src:
                zoom_f = 2.4 if src_im_2 else 2.6
                crop_3 = make_zoom_crop(base_src, zoom_factor=zoom_f, cx_ratio=0.50, cy_ratio=0.42)
                purified_3 = process_and_purify_oil_painting(crop_3)
                purified_3.save(slide_3_path, "JPEG", quality=95, optimize=True)
                purified_3.save(os.path.join(web_dir, "slide_3.jpg"), "JPEG", quality=95, optimize=True)
                created_count += 1
                print(f"✅ {theme_id}/slide_3.jpg (Macro {zoom_f}x)")

    print(f"\n🎉 HOÀN TẤT: Đã tạo thêm {created_count} slide cận cảnh & macro!")

if __name__ == "__main__":
    main()
