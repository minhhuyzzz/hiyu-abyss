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

---

# Danh Mục Nhiệm Vụ: Thiết Kế & Chế Tác 103 Slide Sơn Dầu Khử AI (Theme 251 -> 300)

## Phase 1: Đặc Tả Mỹ Thuật 103 Slide & Manifest JSON Generator

- [x] **Task 1: Thiết Kế Tài Liệu Đặc Tả Mỹ Thuật `docs/11_HIYU_ABYSS_HEALING_OIL_SUITES_251_300_SPEC.md`**
  - **Mô tả:** Viết tài liệu đặc tả mỹ thuật hoàn chỉnh cho 50 theme mới (103 slide độc lập). Mỗi slide gắn liền với danh tác/nghệ sĩ cảm hứng, ý niệm thị giác chuyển tải đúng nhịp điệu bài viết và prompt Master 9:16 khử AI.
  - **Tiêu chí:** Đúng 50 theme, đủ 103 slide, 0 tì vết AI, bảng màu ấm áp/tươi sáng.
  - **Xác minh:** Kiểm tra file tồn tại và đủ 50 mục theme (1.507 dòng, 166.591 ký tự).
  - **Files:** `docs/11_HIYU_ABYSS_HEALING_OIL_SUITES_251_300_SPEC.md`
  - **Scope:** L (1 spec document)

- [x] **Task 2: Lập Trình Script Khởi Tạo Manifest `scripts/build_oil_spec_251_300.py`**
  - **Mô tả:** Tạo script Python tự động tổng hợp dữ liệu kịch bản và xuất ra `scripts/oil_suites_251_300_manifest.json` chuẩn hóa 103 slide.
  - **Tiêu chí:** JSON chứa 50 theme keys, tổng cộng 103 slide.
  - **Xác minh:** `python scripts/build_oil_spec_251_300.py` thành công (103 slides).
  - **Files:** `scripts/build_oil_spec_251_300.py`, `scripts/oil_suites_251_300_manifest.json`
  - **Scope:** M (1 script + 1 JSON)

- [x] **Task 3: Viết & Chạy Bộ Kiểm Định Độc Bản Mỹ Thuật `scripts/audit_oil_spec_251_300.py`**
  - **Mô tả:** Script kiểm tra tính toàn vẹn của 103 prompt: 0 prompt trùng lặp, đúng tỷ lệ 9:16, không chứa từ khóa AI slop, đầy đủ thuộc tính toan vải và impasto.
  - **Tiêu chí:** Script chạy exit code 0, 100% PASS.
  - **Xác minh:** `python scripts/audit_oil_spec_251_300.py` đạt 0 Cảnh báo | 0 Lỗi (100% PASS).
  - **Files:** `scripts/audit_oil_spec_251_300.py`
  - **Scope:** S (1 script)

### ❖ Checkpoint 1: Art Spec & Manifest Sẵn Sàng
- [x] Đặc tả mỹ thuật `docs/11_HIYU_ABYSS_HEALING_OIL_SUITES_251_300_SPEC.md` hoàn thiện.
- [x] File manifest 103 slide độc lập đã sẵn sàng và vượt qua kiểm định (100% PASS).

---

## Phase 2: Khảo Sát Nguồn Bảo Tàng CCO & Curation Strategy

- [x] **Task 4: Thu Thập Bản Scan CCO Siêu Phân Giải & Cơ Chế Render Dự Phòng**
  - **Mô tả:** Viết script `scripts/resolve_healing_master_art.py` tìm kiếm bản scan 3.000px–5.000px từ Wikimedia Commons / Met Open Access / Rijksmuseum lưu vào `assets/templates/raw_cache/`.
  - **Tiêu chí:** Tìm và tải các kiệt tác tranh bảo tàng tương thích.
  - **Xác minh:** `python scripts/resolve_healing_master_art.py`
  - **Files:** `scripts/resolve_healing_master_art.py`, `scripts/resolved_healing_art.json`
  - **Scope:** M (1 script + raw cache)

### ❖ Checkpoint 2: Raw Master Scans & Prompts Sẵn Sàng
- [x] Bản scan bảo tàng chất lượng cao được lưu trong bộ đệm.
- [x] 0 lỗi tải, không dính rate-limit.

---

## Phase 3: Chế Tác Hàng Loạt 103 Slide & Hậu Kỳ Khử AI (5 Lô)

- [x] **Task 5: Chế tác Lô 1 (Theme 251 – 260 · 21 slides) — Cụm Tự Trắc Ẩn**
- [x] **Task 6: Chế tác Lô 2 (Theme 261 – 270 · 20 slides) — Tự Trắc Ẩn & Khắc Kỷ Điềm Tĩnh**
- [x] **Task 7: Chế tác Lô 3 (Theme 271 – 280 · 21 slides) — Khắc Kỷ & Kết Nối Lành Mạnh**
- [x] **Task 8: Chế tác Lô 4 (Theme 281 – 290 · 21 slides) — Kết Nối & Ý Nghĩa Sống**
- [x] **Task 9: Chế tác Lô 5 (Theme 291 – 300 · 20 slides) — Ý Nghĩa Sống & Cột Mốc 300**
- [x] **Task 10: Hậu Kỳ Khử Dấu Vết AI Hữu Cơ (`scripts/normalize_healing_suites.py`)**
  - **Mô tả:** Chạy bộ lọc quang học vật lý: tỷ lệ 9:16 (1080x1920), giảm -4% bão hòa, phủ hạt *Organic Canvas Grain*, tăng sắc nét micro-contrast.
  - **Tiêu chí:** Đủ 103 slide hoàn thiện, lưu vào `assets/templates/multislides/` và `website/public/images/themes/`.
  - **Xác minh:** Script verify 103 slide đạt 100% PASS.
  - **Files:** `scripts/normalize_healing_suites.py`, 103 ảnh
  - **Scope:** L (103 images + 1 script)

### ❖ Checkpoint 3: 103 Slide Hoàn Tất & Khử AI Đạt Chuẩn
- [x] 103 slide sơn dầu chất lượng cao đã xuất và kiểm định.
- [x] Đạt chuẩn mỹ thuật HYA-08.

---

## Phase 4: Tích Hợp Asset Catalog, Cập Nhật Google Sheet & Build Thư Viện

- [x] **Task 11: Cập Nhật `website/src/data/asset-catalog.json` Lên 300 Theme**
  - **Mô tả:** Mở rộng metadata hệ thống, liên kết 103 slide mới với các theme trên Living Museum.
  - **Tiêu chí:** Đủ 300 theme trong catalog, không lỗi cú pháp.
  - **Files:** `website/src/data/asset-catalog.json`
  - **Scope:** M (1 JSON file)

- [x] **Task 12: Cập Nhật Trạng Thái Ảnh Trên Google Sheet Pipeline**
  - **Mô tả:** Cập nhật cột P (`Gợi Ý Phôi Ảnh`) và cột Q (`Trạng Thái` -> `ĐÃ CÓ ẢNH`) cho hàng 252-301.
  - **Tiêu chí:** Google Sheet hiển thị đồng bộ trạng thái mới.
  - **Scope:** S (Google Sheet mutate)

- [x] **Task 13: Build Hệ Thống Thư Viện Tĩnh, Chạy 22 Test WCAG AA & Đồng Bộ Git**
  - **Mô tả:** Build website, chạy `node test/verify-build.js` đạt 22 PASS | 0 FAIL, commit và push lên GitHub.
  - **Tiêu chí:** Build sạch sẽ, Git clean.
  - **Scope:** S (Build & Git push)

### ❖ Checkpoint 4: Hoàn Thành Toàn Bộ 50 Bộ Ảnh Chữa Lành Mới
- [x] 103 ảnh sơn dầu đã nạp thành công vào hệ thống.
- [x] Google Sheet cập nhật trạng thái đồng bộ.
- [x] Toàn bộ kho lưu trữ Git đã được đẩy an toàn lên GitHub.

---

# Danh Mục Nhiệm Vụ: 50 Bài Lưu Đồ Tâm Lý & Ranh Giới Đời Thực (STT 301 -> 350)

## Phase 1: Lập Kế Hoạch & Xây Dựng Kịch Bản Lưu Đồ Tâm Lý
- [x] **Task 1: Xây Dựng 50 Kịch Bản Lưu Đồ & Decision Trees (`scripts/build_50_flowchart_posts_301_350.py`)**
  - **Mô tả:** Tạo 50 kịch bản chi tiết STT 301-350 tập trung vào các lưu đồ bóc tách thao túng, thiết lập ranh giới, phản ứng sang chấn và trí tuệ Khắc kỷ. Áp dụng skill `humanizer` khử sạch sáo ngữ AI.
  - **Tiêu chí:** Đúng 50 bài, phân bổ linh hoạt (12 Single-Punch, 7 Carousel 2 trang, 25 Carousel 3 trang, 6 Carousel 4 trang).
  - **Xác minh:** `python scripts/build_50_flowchart_posts_301_350.py` xuất ra `scripts/posts_301_350.json`.
  - **Files:** `scripts/build_50_flowchart_posts_301_350.py`, `scripts/posts_301_350.json`

## Phase 2: Kiểm Định Chất Lượng Biên Tập & Chuẩn SEO
- [x] **Task 2: Kiểm Định Toàn Diện Chất Lượng & SEO (`scripts/audit_posts_301_350.py`)**
  - **Mô tả:** Kiểm tra không trùng lặp tiêu đề, quy tắc Hook ngắn (< 10 từ kèm `...`), 5 hashtag chuẩn SEO 5 tầng, tác giả chuẩn xác và tuân thủ `humanizer`.
  - **Tiêu chí:** 100% PASS (0 lỗi).
  - **Xác minh:** `python scripts/audit_posts_301_350.py`

## Phase 3: Nạp Google Sheet & Chuẩn Hóa Định Dạng
- [x] **Task 3: Nạp 50 Bài & Đồng Bộ Định Dạng Google Sheet (`scripts/upload_and_polish_posts_301_350.py`)**
  - **Mô tả:** Ghi 50 hàng vào dải `'Kế Hoạch Đăng Bài (TikTok Pipeline)'!A302:Q351`, áp dụng `wrapStrategy: WRAP`, font Roboto 9pt, căn giữa `MIDDLE`, và sao chép data validation cho cột Q.
  - **Tiêu chí:** 50 hàng được nạp thành công, kiểm tra trực tiếp qua `scripts/verify_live_301_350.py`.
  - **Files:** `scripts/upload_and_polish_posts_301_350.py`, `scripts/verify_live_301_350.py`

## Phase 4: Đồng Bộ Git & Bàn Giao
- [x] **Task 4: Commit & Push Hệ Thống Lên GitHub**
  - **Mô tả:** Đẩy toàn bộ mã nguồn script, dữ liệu JSON và tài liệu kế hoạch lên GitHub `origin/main`.

