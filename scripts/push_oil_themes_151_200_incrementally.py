#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Incremental Git Push for Themes 151 - 200 (HYA-08 Oil Suites)
Đẩy 50 bộ kiệt tác sơn dầu (150 slides x 2 thư mục = 300 tệp ảnh) lên GitHub theo 10 đợt (5 themes/đợt)
để tránh lỗi quá tải RPC / HTTP 408 Timeout.
"""

import subprocess
import sys
import time

BATCHES = [
    (["theme_151", "theme_152", "theme_153", "theme_154", "theme_155"], "themes 151-155 (Manipulation & Dark Triad 1)"),
    (["theme_156", "theme_157", "theme_158", "theme_159", "theme_160"], "themes 156-160 (Manipulation 2 & Dark Triad)"),
    (["theme_161", "theme_162", "theme_163", "theme_164", "theme_165"], "themes 161-165 (Crowd Psychology & Power 1)"),
    (["theme_166", "theme_167", "theme_168", "theme_169", "theme_170"], "themes 166-170 (Crowd Psychology & Power 2)"),
    (["theme_171", "theme_172", "theme_173", "theme_174", "theme_175"], "themes 171-175 (Bad Faith & Freedom 1)"),
    (["theme_176", "theme_177", "theme_178", "theme_179", "theme_180"], "themes 176-180 (Bad Faith & Freedom 2)"),
    (["theme_181", "theme_182", "theme_183", "theme_184", "theme_185"], "themes 181-185 (Cognitive Biases & Rationalization 1)"),
    (["theme_186", "theme_187", "theme_188", "theme_189", "theme_190"], "themes 186-190 (Cognitive Biases & Rationalization 2)"),
    (["theme_191", "theme_192", "theme_193", "theme_194", "theme_195"], "themes 191-195 (Existential Paradox & Resilience 1)"),
    (["theme_196", "theme_197", "theme_198", "theme_199", "theme_200"], "themes 196-200 (Existential Paradox & Resilience 2)")
]

def run_cmd(cmd: str, desc: str = ""):
    print(f"👉 {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"❌ Error in {desc}: {res.stderr.strip()[:200]}")
        return False, res.stdout + "\n" + res.stderr
    return True, res.stdout

def main():
    print("=== ĐẨY GIAI ĐOẠN 1: METADATA, SCRIPTS & ASSET CATALOG ===")
    meta_files = [
        "docs/10_HIYU_ABYSS_OIL_PAINTING_SUITES_151_200_SPEC.md",
        "docs/ideas/",
        "scripts/build_oil_spec_151_200.py",
        "scripts/download_last_3_artworks.py",
        "scripts/mass_produce_oil_suites_151_200.py",
        "scripts/oil_suites_151_200_prompts_manifest.json",
        "scripts/resolve_50_master_oil_art.py",
        "scripts/resolved_50_master_oil_art.json",
        "scripts/update_oil_catalog_151_200.py",
        "scripts/push_oil_themes_151_200_incrementally.py",
        "website/src/data/asset-catalog.json",
        "website/test/e2e-smoke.mjs",
        "editorial/content/TXT-0001.md",
        "tasks/plan.md",
        "tasks/todo.md"
    ]
    
    # Thêm các tệp code/spec trước
    run_cmd(f"git add {' '.join(meta_files)}", "add metadata")
    commit_meta = 'git commit -m "feat(spec): add 50 oil suites specification, metadata and catalog update (themes 151-200)"'
    run_cmd(commit_meta, "commit metadata")
    
    # Push metadata
    print("🚀 Pushing metadata commit...")
    for attempt in range(1, 4):
        ok, out = run_cmd("git push origin main", "push metadata")
        if ok:
            print("✅ Metadata pushed successfully!")
            break
        print(f"⚠️ Push retry {attempt} in 4s...")
        time.sleep(4)

    print("\n=== ĐẨY GIAI ĐOẠN 2: 10 ĐỢT ẢNH SƠN DẦU (5 THEMES/ĐỢT) ===")
    
    for idx, (themes, desc) in enumerate(BATCHES, 1):
        print(f"\n📦 [{idx}/10] Xử lý đợt: {desc}...")
        files_to_add = []
        for t in themes:
            files_to_add.append(f"assets/templates/multislides/{t}")
            files_to_add.append(f"website/public/images/themes/{t}")
            
        add_cmd = f"git add {' '.join(files_to_add)}"
        ok, _ = run_cmd(add_cmd, f"git add {desc}")
        if not ok:
            sys.exit(1)
            
        commit_msg = f"feat(art): add HYA-08 oil painting suites for {desc}"
        commit_cmd = f'git commit -m "{commit_msg}"'
        ok, out = run_cmd(commit_cmd, f"git commit {desc}")
        if not ok and "nothing to commit" in out:
            print("⏩ Nothing to commit, continuing...")
            continue
            
        print(f"🚀 Đang đẩy {desc} lên GitHub origin main...")
        push_success = False
        for attempt in range(1, 4):
            push_ok, push_out = run_cmd("git push origin main", f"push {desc}")
            if push_ok:
                print(f"✅ Đẩy thành công đợt {idx}/10: {desc}!")
                push_success = True
                break
            else:
                print(f"⚠️ Đẩy thất bại lượt {attempt}, thử lại sau 5s...")
                time.sleep(5)
                
        if not push_success:
            print(f"❌ Không thể đẩy đợt {desc} sau 3 lần thử.")
            sys.exit(1)
            
        time.sleep(1)

    print("\n=======================================================")
    print("🎉 TẤT CẢ 50 THEMES (151 - 200) ĐÃ ĐƯỢC PUSH THÀNH CÔNG LÊN GITHUB!")
    print("=======================================================")

if __name__ == "__main__":
    main()
