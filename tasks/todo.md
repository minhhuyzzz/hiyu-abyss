# Danh Mục Nhiệm Vụ: Hiyu Abyss Digital Living Museum Transformation

## Master Track: Nâng Cấp Bảo Tàng Tư Tưởng & Thẩm Định Độc Lập (Sprints 0 -> 2)

- [x] **Sprint 0: Audit & Baseline**
  - Chạy bản build, kiểm tra hệ thống, chụp và đo đạc toàn diện.
- [x] **Sprint 1: Trust & QA (P0 - Minh Bạch Xuất Xứ & An Toàn Kỹ Thuật)**
  - [x] **P0-01:** Bổ sung schema `ScholarlySource` và `verification_status` trong `types.ts` & `content-publisher.ts`. Hạ nhãn verified ảo về `PENDING_VERIFICATION`, đối chiếu mẫu `TXT-0001`.
  - [x] **P0-02:** Khai báo `ArtworkProvenanceType` cho tranh bảo tàng CCO và tranh phục dựng hữu cơ HYA-08 trong `SourceAttribution.astro`.
  - [x] **P0-03:** Khắc phục canonical domain (fallback `https://hiyuabyss.vercel.app`), gỡ bỏ hoàn toàn thẻ `hreflang="en"` trỏ cùng trang tiếng Việt.
  - [x] **P0-04:** Xử lý triệt để lỗi tràn ngang trên mobile 320px/360px (Header compact spacing, SavedDrawer `invisible` khi đóng, `overflow-x: hidden`).
  - [x] **P0-05:** Viết lại cơ chế hiển thị Search: dùng DOM API an toàn (`document.createElement`, `textContent`), chặn XSS, đồng bộ URL parameters.
- [x] **Sprint 2: The Mirror Cinematic (P1 - Trải Nghiệm Chiêm Nghiệm)**
  - [x] Xây dựng Scene Renderer với 5 Room Archetypes (`threshold`, `observation`, `silence`, `confrontation`, `ending`).
  - [x] Tích hợp Transition Director với hiệu ứng chuyển động có hướng (`lateral-reveal`, `reveal-slow`, `crossfade`, `stillness`), tôn trọng `prefers-reduced-motion`.
  - [x] Bổ sung bộ kiểm thử E2E Playwright (`website/test/e2e-smoke.mjs`) kiểm tra thực tế trên trình duyệt Chromium: 26/26 tests PASS, đi qua trọn vẹn cả 4 nhánh rẽ và 4 kết thúc mở.
- [x] **Sprint 3: Landing Editorial (P1 - Minh Bạch Mỹ Thuật)**
  - [x] Bổ sung section `ArtProvenanceSection.astro` trên Landing Page minh bạch quy chuẩn HYA-02 và HYA-08.
  - [x] Đẩy nhánh riêng `feat/digital-living-museum-transformation` lên GitHub để chủ dự án xem xét PR.

---

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


---

# Danh Mục Nhiệm Vụ: 50 Bài Nội Dung Chữa Lành, Ánh Sáng & Sức Bật Nội Tâm (STT 251 -> 300)

## Phase 1: Đặc Tả Tri Thức & Khởi Tạo Kịch Bản

- [x] **Task 1: Xây Dựng Tập Dữ Liệu Kịch Bản 50 Bài Chuẩn (`scripts/build_50_healing_posts_251_300.py`)**
  - **Mô tả:** Viết script Python chứa toàn bộ 50 kịch bản chi tiết với 17 trường thông tin chuẩn theo 4 cụm chủ đề chữa lành & sức bật tinh thần.
  - **Tiêu chí:** Đủ 50 bài STT 251-300, đa dạng slide, 100% caption bespoke, concept tranh ánh sáng/ấm áp.
  - **Xác minh:** `python scripts/build_50_healing_posts_251_300.py` xuất ra `scripts/posts_251_300.json`.
  - **Files:** `scripts/build_50_healing_posts_251_300.py`, `scripts/posts_251_300.json`
  - **Scope:** M (1 script + 1 JSON)

- [x] **Task 2: Sinh 50 Tệp Markdown Lưu Trữ Chuẩn HYA-04 (`TXT-0251.md` đến `TXT-0300.md`)**
  - **Mô tả:** Tạo 50 file độc lập tại `editorial/content/` với YAML frontmatter chuẩn và nội dung đầy đủ.
  - **Tiêu chí:** 50 file hợp lệ, không lỗi YAML.
  - **Xác minh:** Kiểm tra 50 file tồn tại trong `editorial/content/`.
  - **Files:** `editorial/content/TXT-0251.md` -> `TXT-0300.md`
  - **Scope:** L (50 markdown files)

### ❖ Checkpoint 1: Kịch Bản & Lưu Trữ Đã Sẵn Sàng
- [x] File `scripts/posts_251_300.json` tồn tại đủ 50 bài.
- [x] 50 file Markdown đã tạo thành công trong `editorial/content/` (đồng thời bổ sung đầy đủ `TXT-0201.md` -> `TXT-0250.md` đạt 300/300 file).

---

## Phase 2: Kiểm Định Chất Lượng Biên Tập & Độc Bản Ngữ Nghĩa

- [x] **Task 3: Chạy Bộ Kiểm Định Toàn Diện (`scripts/audit_posts_251_300.py`)**
  - **Mô tả:** Viết script kiểm tra 0 trùng lặp mở đầu với 250 bài trước, 0 sáo ngữ AI, kiểm tra độ dài caption và tác giả học thuật xác thực.
  - **Tiêu chí:** 100% PASS kiểm định G1, G2, HYA-03.
  - **Xác minh:** `python scripts/audit_posts_251_300.py` exit code 0.
  - **Files:** `scripts/audit_posts_251_300.py`
  - **Scope:** S (1 script)

### ❖ Checkpoint 2: Vượt Qua Cổng Kiểm Định Chất Lượng
- [x] 100% không trùng lặp mở đầu bài viết.
- [x] 100% caption bespoke đạt chuẩn độ dài và văn phong.

---

## Phase 3: Cập Nhật Dữ Liệu & Nạp Google Sheet Pipeline

- [x] **Task 4: Mở Rộng Dữ Liệu CSV Lên 300 Hàng**
  - **Mô tả:** Cập nhật `scripts/tiktok_200_posts.csv` thành 300 dòng và tạo `scripts/tiktok_300_posts.csv`.
  - **Tiêu chí:** CSV chứa đúng 301 dòng.
  - **Xác minh:** Kiểm tra 301 dòng trong CSV (`scripts/live_sheet_300.csv` và `scripts/tiktok_300_posts.csv`).
  - **Files:** `scripts/tiktok_200_posts.csv`, `scripts/tiktok_300_posts.csv`
  - **Scope:** S (2 CSV files)

- [x] **Task 5: Nạp Đồng Bộ Hàng Loạt Vào Google Sheet (Hàng 252 – 301)**
  - **Mô tả:** Ghi 50 hàng vào Google Sheet tab `Kế Hoạch 200 Bài (TikTok Pipeline)` range `A252:Q301`. Đồng bộ định dạng Roboto 9pt, Wrap Text, căn Middle và menu Trạng Thái.
  - **Tiêu chí:** Dữ liệu hiển thị đẹp mắt, không tràn dòng, không co dòng.
  - **Xác minh:** Đọc lại các hàng 252, 275, 301 bằng `gsheets readonly read`. Đã sửa triệt để lỗi mất format từ hàng 205 trở xuống.
  - **Files:** `scripts/upload_and_polish_posts_251_300.py`, `scripts/batch_write_251_300.json`, `scripts/polish_sheet_205_301.json`
  - **Scope:** M (1 script + 2 JSON + Google Sheet sync)

### ❖ Checkpoint 3: Google Sheet Cập Nhật Hoàn Hảo Đến Bài 300
- [x] Dữ liệu 50 bài hiển thị đầy đủ trên Google Sheet từ hàng 252 đến 301.
- [x] Định dạng ô đồng nhất với các bài trước (khắc phục toàn diện hàng 205-301).

---

## Phase 4: Kiểm Thử Toàn Diện Website & Đồng Bộ Git

- [x] **Task 6: Kiểm Thử Build Hệ Thống Thư Viện Tĩnh & WCAG AA**
  - **Mô tả:** Build website và chạy bộ kiểm định tính toàn vẹn 22 PASS | 0 FAIL.
  - **Tiêu chí:** Build sạch, không lỗi schema.
  - **Xác minh:** `cd website && npm run build && node test/verify-build.js` đạt 22 PASS | 0 FAIL.
  - **Scope:** S (Test verification)

- [x] **Task 7: Đồng Bộ Git Lên Nhánh `main` & GitHub Remote**
  - **Mô tả:** Stage toàn bộ các file mới, tạo commit rõ ràng và push lên GitHub.
  - **Tiêu chí:** Working tree sạch sẽ, commit đẩy lên GitHub an toàn.
  - **Xác minh:** `git status` clean, commit hoàn tất.
  - **Scope:** S (Git push)

### ❖ Checkpoint 4: Hoàn Thành Toàn Bộ Kế Hoạch 50 Bài Mới
- [x] 50 bài nội dung chữa lành đã nạp thành công vào Google Sheet (đồng thời sửa triệt để format từ hàng 205-301).
- [x] Hệ thống mã nguồn, kho lưu trữ Git và website test đạt 100% chuẩn xuất bản.
