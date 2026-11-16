#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Incremental Git Push for Themes 201 - 250 (115 Distinct Museum Oil Suites)
Đẩy 50 bộ kiệt tác sơn dầu (115 slides x 2 thư mục) lên GitHub theo 10 đợt (5 themes/đợt)
để tránh lỗi quá tải RPC / HTTP 408 Timeout.
"""

import subprocess
import sys
import time

BATCHES = [
    (["theme_201", "theme_202", "theme_203", "theme_204", "theme_205"], "themes 201-205 (Toxic Scripts Part 1)"),
    (["theme_206", "theme_207", "theme_208", "theme_209", "theme_210"], "themes 206-210 (Toxic Scripts Part 2)"),
    (["theme_211", "theme_212", "theme_213", "theme_214", "theme_215"], "themes 211-215 (Toxic Scripts 3 & Boundaries 1)"),
    (["theme_216", "theme_217", "theme_218", "theme_219", "theme_220"], "themes 216-220 (Boundaries & Sacrifice Trap 2)"),
    (["theme_221", "theme_222", "theme_223", "theme_224", "theme_225"], "themes 221-225 (Boundaries & Personal Dignity 3)"),
    (["theme_226", "theme_227", "theme_228", "theme_229", "theme_230"], "themes 226-230 (Boundaries 4 & Mind-Reading 1)"),
    (["theme_231", "theme_232", "theme_233", "theme_234", "theme_235"], "themes 231-235 (Mind-Reading & Unspoken Expectations 2)"),
    (["theme_236", "theme_237", "theme_238", "theme_239", "theme_240"], "themes 236-240 (Expectations 3 & Scarcity Principle 1)"),
    (["theme_241", "theme_242", "theme_243", "theme_244", "theme_245"], "themes 241-245 (Scarcity & Social Magnetism 2)"),
    (["theme_246", "theme_247", "theme_248", "theme_249", "theme_250"], "themes 246-250 (Scarcity & Stoic Self-Mastery 3)")
]

def run_cmd(cmd: str, desc: str = ""):
    print(f"👉 {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"❌ Error in {desc}: {res.stderr.strip()[:200]}")
        return False, res.stdout + "\n" + res.stderr
    return True, res.stdout

def main():
    print("=== ĐẨY GIAI ĐOẠN 1: SCRIPTS & KIỂM ĐỊNH ===")
    scripts_to_add = [
        "scripts/produce_batch_1_themes_201_213.py",
        "scripts/produce_batch_2_themes_214_226.py",
        "scripts/produce_batch_3_themes_227_238.py",
        "scripts/produce_batch_4_themes_239_250.py",
        "scripts/produce_remaining_10_slides.py",
        "scripts/refine_specific_artworks.py",
        "scripts/verify_115_distinct_oil_suites_201_250.py"
    ]
    run_cmd(f"git add {' '.join(scripts_to_add)}", "add scripts")
    run_cmd('git commit -m "feat(pipeline): add production & verification scripts for 115 distinct oil suites (201-250)"', "commit scripts")
    run_cmd("git push origin feat/the-agora-forum-v2", "push scripts")

    print("\n=== ĐẨY GIAI ĐOẠN 2: 10 ĐỢT ẢNH SƠN DẦU (5 THEMES/ĐỢT) ===")
    for idx, (themes, desc) in enumerate(BATCHES, 1):
        print(f"\n📦 [ĐỢT {idx}/10] Chuẩn bị đẩy: {desc}")
        
        patterns = []
        for t in themes:
            patterns.append(f"assets/templates/multislides/{t}/")
            patterns.append(f"website/public/images/themes/{t}/")
        
        add_cmd = f"git add {' '.join(patterns)}"
        ok, out = run_cmd(add_cmd, f"Stage batch {idx}")
        if not ok:
            print(f"Bỏ qua batch {idx} do lỗi stage.")
            continue
        
        commit_msg = f'feat(art): add museum oil suites batch {idx}/10 ({desc})'
        ok, out = run_cmd(f'git commit -m "{commit_msg}"', f"Commit batch {idx}")
        if not ok and "nothing to commit" in out:
            print(f"Batch {idx} không có thay đổi mới.")
            continue
            
        print(f"🚀 Pushing batch {idx}/10 to GitHub...")
        push_ok = False
        for attempt in range(3):
            ok, out = run_cmd("git push origin feat/the-agora-forum-v2", f"Push batch {idx} (attempt {attempt+1})")
            if ok:
                push_ok = True
                print(f"✅ Đợt {idx}/10 thành công!")
                break
            else:
                print(f"⚠️ Push attempt {attempt+1} failed, retrying in 5s...")
                time.sleep(5)
                
        if not push_ok:
            print(f"❌ Không thể đẩy batch {idx} sau 3 lần thử. Dừng lại.")
            sys.exit(1)
            
        time.sleep(1)

    print("\n🎉 TOÀN BỘ 10 ĐỢT (50 THEMES / 115 KIỆT TÁC SƠN DẦU) ĐÃ ĐƯỢC ĐẨY LÊN GITHUB HOÀN TẤT!")

if __name__ == '__main__':
    main()
