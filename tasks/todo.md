# Danh Mục Nhiệm Vụ: Nghiên Cứu Học Thuật & Soạn Thảo 50 Bài Triết Ngôn Bổ Sung (TXT-0151 -> TXT-0200)

## Phase 1: Thu Thập & Cào Nguồn Học Thuật Mở (Academic Research & Scraper Pipeline)

- [x] **Task 1: Xây Dựng Bộ Thu Thập & Cào Nguồn Học Thuật Mở (`scripts/academic_source_harvester.py`)**
  - **Mô tả:** Viết script kết nối OpenAlex, Crossref API, SEP và Gutenberg cào dữ liệu học thuật cho 5 cụm chủ đề.
  - **Tiêu chí:** Tải về và tổng hợp metadata, abstract, DOI và văn bản chuẩn xác vào `scripts/academic_harvested_sources.json`.
  - **Xác minh:** `python scripts/academic_source_harvester.py` (Đã hoàn thành)
  - **Files:** `scripts/academic_source_harvester.py`, `scripts/academic_harvested_sources.json`
  - **Scope:** S (2 files)

- [x] **Task 2: Chuẩn Hóa Hồ Sơ Nguồn Học Thuật `SRC-0003` -> `SRC-0015` Vào `knowledge/sources/`**
  - **Mô tả:** Tạo tối thiểu 10 hồ sơ nguồn Markdown chuẩn YAML frontmatter (`HYA-02`), xác định rõ tác giả, tác phẩm, DOI/URL, và mức truy cập.
  - **Tiêu chí:** Vượt qua Hard Gate G1 (không bịa nguồn, có link/DOI thật), cập nhật `indexes/INDEX_SOURCES.md` (15 nguồn).
  - **Xác minh:** Kiểm tra cấu trúc file và link của `SRC-0003.md` -> `SRC-0015.md`.
  - **Files:** `knowledge/sources/SRC-0003.md` đến `SRC-0015.md`, `indexes/INDEX_SOURCES.md`
  - **Scope:** M (11 files)

### ❖ Checkpoint 1: Academic Foundations
- [x] Dữ liệu học thuật được trích xuất minh bạch và lưu trữ chuẩn quy cách.
- [x] Các hồ sơ nguồn `SRC` có đầy đủ thông tin xuất xứ và mức truy cập.

---

## Phase 2: Soạn Thảo 50 Kịch Bản Triết Ngôn TikTok Chuẩn SEO (`TXT-0151` -> `TXT-0200`)

- [x] **Task 3: Biên Soạn Kịch Bản 50 Bài Triết Ngôn Sắc Lạnh Chuẩn SEO 17 Cột**
  - **Mô tả:** Soạn 50 bài kịch bản mới (`TXT-0151` -> `TXT-0200`) theo 5 cụm chủ đề (10 bài/cụm), đúng quy chuẩn Hook ngắn < 10 từ kèm dấu `......`, Cú lật, Chiếc gương, Caption SEO < 90 từ, 5 hashtag, phôi ảnh `theme_151` -> `theme_200`.
  - **Tiêu chí:** 50 bài chuẩn 17 cột, không sáo ngữ AI, lưu tại `scripts/posts_151_200_data.json` và `scripts/tiktok_200_posts.csv`.
  - **Xác minh:** `python scripts/generate_50_academic_posts.py` (Đã hoàn thành)
  - **Files:** `scripts/generate_50_academic_posts.py`, `scripts/posts_151_200_data.json`, `scripts/tiktok_200_posts.csv`
  - **Scope:** M (3 files)

- [x] **Task 4: Thẩm Định Phản Biện Đa Tầng & Kiểm Định Trùng Lặp (Hard Gates G2, G3, G4)**
  - **Mô tả:** Chạy kiểm tra tính mới ngữ nghĩa (`semantic-novelty-review`) với 150 bài cũ, rà soát tính sắc lạnh (`editorial-critique`).
  - **Tiêu chí:** 0 trùng lặp, 100% đạt chuẩn Hiyu Abyss.
  - **Xác minh:** `python scripts/audit_semantic_novelty_151_200.py` (Đã hoàn thành: 0 errors)
  - **Files:** `scripts/audit_semantic_novelty_151_200.py`
  - **Scope:** S (1 file)

### ❖ Checkpoint 2: Content & SEO Excellence
- [x] Đủ 50 bài kịch bản đạt tiêu chuẩn vàng 17 cột.
- [x] Vượt qua toàn bộ các cổng kiểm định chất lượng nội dung và SEO.

---

## Phase 3: Tích Hợp Google Sheet & Định Dạng Thẩm Mỹ Chuyên Nghiệp

- [x] **Task 5: Nhúng 50 Bài Mới Vào Google Sheet & Đổi Tên Tab Thành "Kế Hoạch 200 Bài (TikTok Pipeline)"**
  - **Mô tả:** Cập nhật 50 dòng mới (STT 151 -> 200) lên Google Sheet qua `gsheets mutate import-csv`, đổi tên tab thành `Kế Hoạch 200 Bài (TikTok Pipeline)`.
  - **Tiêu chí:** Tab chứa đủ 200 bài liên tục, tên tab đổi thành công.
  - **Xác minh:** `gsheets readonly info 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY` (Đã hoàn thành)
  - **Files:** `scripts/tiktok_200_posts.csv`
  - **Scope:** S (1 file)

- [x] **Task 6: Tối Ưu Hóa Giao Diện & Thẩm Mỹ Bảng Tính (Dark Slate Polishing)**
  - **Mô tả:** Định dạng Dark Slate (#0F172A), wrap text, căn giữa mã và ngày giờ, dropdown Trạng Thái cột Q cho toàn bộ 200 dòng.
  - **Tiêu chí:** Bảng tính sang trọng, không tràn viền, dropdown mượt mà.
  - **Xác minh:** Kiểm tra định dạng live trên Sheet qua `polish_200_sheet.py`. (Đã hoàn thành)
  - **Files:** `scripts/polish_200_sheet.py`
  - **Scope:** S (1 file)

### ❖ Checkpoint 3: Live Sheet Synchronization
- [x] Google Sheet cập nhật thành công 200 bài, đổi tên tab chuẩn.
- [x] Định dạng thẩm mỹ Dark Slate hoàn hảo, sẵn sàng cho nhóm sản xuất nội dung.

---

## Phase 4: Đồng Bộ Kho Tri Thức Nội Bộ & Kiểm Thử Toàn Diện

- [x] **Task 7: Đồng Bộ Kho Hồ Sơ Nội Bộ `editorial/content/` Cho 50 Bài Mới**
  - **Mô tả:** Tạo 50 file markdown `TXT-0151.md` đến `TXT-0200.md` trong `editorial/content/` kèm YAML (`HYA-04`), cập nhật `indexes/INDEX_CONTENT.md`.
  - **Tiêu chí:** 50 file mới có đủ ID, chủ đề, nguồn học thuật, bảng index có đủ 200 mục.
  - **Xác minh:** `python scripts/sync_all_200_editorial_content.py` (Đã hoàn thành 200 file)
  - **Files:** `editorial/content/TXT-0151.md` đến `TXT-0200.md`, `indexes/editorial-board.md`
  - **Scope:** M (51 files)

- [x] **Task 8: Kiểm Thử Toàn Diện & Đẩy Toàn Bộ Lên GitHub**
  - **Mô tả:** Chạy kiểm thử hệ thống, build website, đảm bảo 0 lỗi hồi quy. Commit và push lên `origin main`.
  - **Tiêu chí:** Website build thành công 127 trang tĩnh, 22/22 kiểm tra WCAG AA đạt chuẩn, git đồng bộ.
  - **Xác minh:** `cd website && npm run build && node test/verify-build.js` (22 PASS | 0 FAIL).
  - **Files:** Git commits
  - **Scope:** S (0 code changes, validation only)

### ❖ Checkpoint 4: Complete & Production Ready
- [x] 200 bài đăng hoàn chỉnh trên Google Sheet và kho dữ liệu nội bộ.
- [x] Hệ thống hoạt động trơn tru, mã nguồn được lưu trữ an toàn trên GitHub.
