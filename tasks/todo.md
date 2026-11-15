# Danh Mục Nhiệm Vụ: Chế Tác 50 Bộ Ảnh Sơn Dầu Cổ Điển Bảo Tàng (Theme 151 -> 200)

## Phase 1: Đặc Tả Mỹ Thuật HYA-08 & Manifest 50 Danh Tác

- [x] **Task 1: Tạo Đặc Tả Mỹ Thuật `docs/10_HIYU_ABYSS_OIL_PAINTING_SUITES_151_200_SPEC.md` & Manifest JSON**
  - **Mô tả:** Viết script `scripts/build_oil_spec_151_200.py` xuất đặc tả 50 theme và `scripts/oil_suites_151_200_prompts_manifest.json`.
  - **Tiêu chí:** Đúng 50 mục, có tên tranh, tác giả, năm, bảo tàng, ý niệm thị giác và prompt chuẩn.
  - **Xác minh:** `python scripts/build_oil_spec_151_200.py` (Đã hoàn thành 50 themes)
  - **Files:** `docs/10_HIYU_ABYSS_OIL_PAINTING_SUITES_151_200_SPEC.md`, `scripts/oil_suites_151_200_prompts_manifest.json`
  - **Scope:** S (2 files)

### ❖ Checkpoint 1: Art Specification Ready
- [x] Đặc tả mỹ thuật HYA-08 hoàn tất với đầy đủ 50 kiệt tác được chỉ định.
- [x] Manifest JSON sẵn sàng cho tiến trình phân giải ảnh.

---

## Phase 2: Phân Giải Nguồn Ảnh Bảo Tàng Siêu Phân Giải (Wikimedia API)

- [x] **Task 2: Tìm Kiếm & Tải Bản Scan Gốc (3.000px–5.000px) Về `assets/templates/raw_cache/`**
  - **Mô tả:** Viết và chạy `scripts/resolve_50_master_oil_art.py` truy vấn Wikimedia API tải các bản scan bảo tàng chất lượng cao.
  - **Tiêu chí:** 100% 50 tác phẩm được tải về `assets/templates/raw_cache/`.
  - **Xác minh:** `python scripts/resolve_50_master_oil_art.py` (Đạt 50/50 tác phẩm)
  - **Files:** `scripts/resolve_50_master_oil_art.py`, `scripts/resolved_50_master_oil_art.json`
  - **Scope:** M (2 files + cache images)

### ❖ Checkpoint 2: Raw High-Res Master Scans Ready
- [x] Đủ 50 bản scan bảo tàng độ phân giải cao trong bộ đệm.
- [x] 0 lỗi tải, không dính rate-limit.

---

## Phase 3: Chế Tác Hàng Loạt 150 Slide Chuẩn HYA-08 & 3 Tầng Thu Phóng

- [x] **Task 3: Xuất Trọn Bộ 150 Slide Sơn Dầu Khử AI (50 Themes x 3 Slides)**
  - **Mô tả:** Viết và chạy `scripts/mass_produce_oil_suites_151_200.py` chế tác trọn vẹn 3 slide/theme:
    - Slide 1: Toàn cảnh 1080x1920 (1.0x).
    - Slide 2: Cận cảnh tâm điểm kịch tính (1.65x).
    - Slide 3: Siêu cận thớ toan và vết cọ impasto (2.5x).
    - Hậu kỳ: Giảm bão hòa -4%, phủ hạt Organic Canvas Grain, tăng sắc nét Micro-contrast.
    - Lưu vào `assets/templates/multislides/` và `website/public/images/themes/`.
  - **Tiêu chí:** Đủ 150 slide chất lượng cao, 0 tì vết AI.
  - **Xác minh:** Kiểm thử tự động 300 tệp tin đạt 0 lỗi (100% PASS).
  - **Files:** `scripts/mass_produce_oil_suites_151_200.py`, thư mục `assets/templates/multislides/theme_151..200/`
  - **Scope:** L (150 images generated)

### ❖ Checkpoint 3: 150 Slides Produced & Verified
- [x] 150/150 slide sơn dầu bảo tàng hoàn thiện, tỷ lệ dọc 9:16 sắc nét.
- [x] Đạt chuẩn khử AI vật lý HYA-08.

---

## Phase 4: Cập Nhật Asset Catalog, Kiểm Thử Toàn Diện & Đồng Bộ Git

- [x] **Task 4: Cập Nhật `asset-catalog.json`, Build Thư Viện Sống & Đẩy Git**
  - **Mô tả:** Cập nhật `website/src/data/asset-catalog.json` từ 150 lên 200 theme. Build website tĩnh 127 trang và chạy test WCAG AA. Push git theo lô nhỏ an toàn.
  - **Tiêu chí:** Build 127 trang thành công, 22/22 test PASS, Git sạch sẽ đồng bộ `origin/main`.
  - **Xác minh:** `cd website && npm run build && node test/verify-build.js` (22 PASS | 0 FAIL) và `git push` hoàn tất.
  - **Files:** `website/src/data/asset-catalog.json`, Git commits
  - **Scope:** M (code & commits)

### ❖ Checkpoint 4: Complete & Production Ready
- [x] Hệ thống ảnh 200 bộ hoàn chỉnh trên cả kho tài nguyên và website.
- [x] Toàn bộ mã nguồn và tài nguyên ảnh được đẩy lên GitHub an toàn (commit `9ce6e39`).
