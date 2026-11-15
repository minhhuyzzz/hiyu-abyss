# Kế Hoạch Triển Khai: Nghiên Cứu Học Thuật & Soạn Thảo 50 Bài Triết Ngôn Bổ Sung (TXT-0151 -> TXT-0200)

> **Căn cứ:** Quyết định thống nhất qua quá trình phỏng vấn `/grill-me` ngày 15/11/2026.  
> **Mục tiêu:** Cào và thu thập tài liệu học thuật đáng tin cậy từ đa nguồn (bách khoa triết học SEP/IEP, kho nghiên cứu thực nghiệm OpenAlex/Crossref, nguyên tác kinh điển Project Gutenberg), biên soạn 50 kịch bản triết ngôn TikTok chuẩn SEO sắc bén (`TXT-0151` $\rightarrow$ `TXT-0200`), nhúng trực tiếp vào Google Sheet thành tab "Kế Hoạch 200 Bài (TikTok Pipeline)" với chuẩn thẩm mỹ Dark Slate cao cấp.  
> **Quy chuẩn tuân thủ:** `HYA-01` (Bản sắc), `HYA-02` (Chuẩn nguồn học thuật), `HYA-03` (Văn phong sắc lạnh), `HYA-04` (Mô hình dữ liệu), `HYA-06` (6 Cổng kiểm định chất lượng), `HYA-08` (Mỹ thuật phôi ảnh).

---

## 1. Kiến Trúc Giải Pháp & Quyết Định Thiết Kế

1. **Chiến lược Nguồn Học Thuật Mở (Academic Harvesting):**
   - **Bách khoa Triết học SEP (Stanford) & IEP (Tennessee):** Khai thác các mục từ chuyên sâu về Đạo đức học, Hoài nghi luận, Bản ngã, Công lý và Tâm lý học đạo đức.
   - **Kho Dữ Liệu Nghiên Cứu Mở OpenAlex & Crossref:** Truy xuất tự động metadata, tóm tắt nghiên cứu (Abstract) và DOI của các công trình thực nghiệm kinh điển về hành vi: Stanley Milgram (Vâng lời quyền lực), Solomon Asch (Áp lực đồng thuận), Leon Festinger (Bất hòa nhận thức), Daniel Kahneman & Amos Tversky (Thiên kiến nhận thức), Delroy Paulhus (Dark Triad).
   - **Nguyên tác Kinh Điển Project Gutenberg & Wikisource:** Khai thác các tác phẩm triết học gốc: Jean-Paul Sartre (*Being and Nothingness* / *Existentialism is a Humanism*), Erich Fromm (*Escape from Freedom*), Gustave Le Bon (*The Crowd: A Study of the Popular Mind*), Hannah Arendt (*Eichmann in Jerusalem*), Albert Camus (*The Myth of Sisyphus*), Friedrich Nietzsche (*Beyond Good and Evil*), Arthur Schopenhauer (*Studies in Pessimism*).
   - **Lưu trữ tri thức:** Đúc kết thành các hồ sơ `SRC-0003` $\rightarrow$ `SRC-0015` tại `knowledge/sources/` với đầy đủ liên kết và bằng chứng minh bạch.

2. **Cơ cấu 5 Cụm Chủ Đề Sâu Sắc (10 Bài/Cụm = 50 Bài):**
   - **Cụm 1 (`TXT-0151` – `TXT-0160`):** *Thao Túng Tâm Lý & Khí Độc Quan Hệ* (Gaslighting, Silent Treatment, Dark Triad, Nợ ân tình, Tội lỗi gán ép).
   - **Cụm 2 (`TXT-0161` – `TXT-0170`):** *Tâm Lý Đám Đông & Sự Thoái Hóa Của Lương Tri* (Tâm lý bầy đàn, Sự tầm thường của cái ác - Arendt, Hiệu ứng bàng quan, Đồng thuận mù quáng).
   - **Cụm 3 (`TXT-0171` – `TXT-0180`):** *Ngụy Tín & Nỗi Sợ Tự Do* (Mauvaise Foi - Sartre, Trốn chạy tự do - Fromm, Nỗi âu lo hiện sinh - Kierkegaard).
   - **Cụm 4 (`TXT-0181` – `TXT-0190`):** *Thiên Kiến Nhận Thức & Cơ Chế Tự Biện Hộ* (Bất hòa nhận thức - Festinger, Thiên kiến xác nhận, Bẫy tự bào chữa - Tavris & Aronson).
   - **Cụm 5 (`TXT-0191` – `TXT-0200`):** *Nghịch Lý Hiện Sinh & Sức Bật Nội Tại* (Amor Fati - Nietzsche, Huyền thoại Sisyphus - Camus, Liệu pháp ý nghĩa - Frankl, Tĩnh lặng Khắc kỷ - Seneca).

3. **Chuẩn Hóa Kịch Bản TikTok Chuẩn SEO (17 Cột Chuẩn):**
   - **Hook đanh thép (< 10 từ):** Kết thúc bằng dấu lửng tò mò (`......`), ngắt nhịp ở điểm nút tâm lý kịch tính nhất.
   - **Cú lật bóc trần & Chiếc gương tự vấn:** Thấu thị hành vi thực tế, không giáo điều, không sáo ngữ AI.
   - **SEO TikTok tối ưu:** Tiêu đề kích thích nhấp chuột, Caption chuẩn SEO < 90 từ chứa câu hỏi tương tác đẩy bình luận, 5 hashtag mục tiêu có lưu lượng tìm kiếm cao.
   - **Phôi ảnh (`theme_151` – `theme_200`):** Điền tên tác phẩm sơn dầu bảo tàng nổi tiếng và danh họa cổ điển tương ứng để sẵn sàng cho đợt render tiếp theo.

4. **Tích Hợp Google Sheet & Thẩm Mỹ Dark Slate:**
   - Nối tiếp các dòng 151 đến 200 trực tiếp vào tab chính.
   - Đổi tên tab sheet thành `Kế Hoạch 200 Bài (TikTok Pipeline)`.
   - Giữ nguyên định dạng Dark Slate (#0F172A), wrap text, căn giữa mã và ngày giờ, dropdown Trạng Thái cột Q.

---

## 2. Danh Sách Nhiệm Vụ Chi Tiết (Task List)

### Phase 1: Thu Thập & Cào Nguồn Học Thuật Mở (Academic Research & Scraper Pipeline)

- [ ] **Task 1: Xây Dựng Bộ Thu Thập & Cào Nguồn Học Thuật Mở (`scripts/academic_source_harvester.py`)**
  - **Mô tả:** Viết kịch bản Python kết nối OpenAlex API, Crossref API, bách khoa triết học SEP và Project Gutenberg để truy xuất và tổng hợp tài liệu học thuật theo 5 cụm chủ đề trọng tâm.
  - **Tiêu chí nghiệm thu:**
    - Cào và tải về metadata, abstract, DOI và văn bản tác phẩm gốc đáng tin cậy.
    - Lưu dữ liệu nghiên cứu thô vào `scripts/academic_harvested_sources.json`.
  - **Xác minh:** `python scripts/academic_source_harvester.py` chạy thành công không lỗi, xuất dữ liệu học thuật đầy đủ.
  - **Files:** `scripts/academic_source_harvester.py`, `scripts/academic_harvested_sources.json`
  - **Scope:** S (2 files)

- [ ] **Task 2: Chuẩn Hóa Hồ Sơ Nguồn Học Thuật `SRC-0003` -> `SRC-0015` Vào `knowledge/sources/`**
  - **Mô tả:** Tạo tối thiểu 10 hồ sơ nguồn Markdown chuẩn YAML frontmatter (`HYA-02`), ghi nhận chính xác tác giả, tác phẩm, năm xuất bản, DOI/URL, và mức truy cập văn bản (`READ_SOURCE` hoặc `FOUND_METADATA`).
  - **Tiêu chí nghiệm thu:**
    - Vượt qua Hard Gate G1 (không bịa đặt nguồn, trích dẫn có vị trí kiểm chứng thực tế).
    - Có đủ các nguồn nền tảng: Sartre, Le Bon, Arendt, Fromm, Festinger, Kahneman, Frankl, Camus, Nietzsche, Seneca.
  - **Xác minh:** Kiểm tra cú pháp YAML và link của toàn bộ file `SRC-0003.md` đến `SRC-0015.md`.
  - **Files:** `knowledge/sources/SRC-0003.md` đến `SRC-0015.md`, `indexes/INDEX_SOURCES.md`
  - **Scope:** M (11 files)

### ❖ Checkpoint 1: Academic Foundations
- [ ] Dữ liệu học thuật được trích xuất minh bạch và lưu trữ chuẩn quy cách.
- [ ] Các hồ sơ nguồn `SRC` có đầy đủ thông tin xuất xứ và mức truy cập.

---

### Phase 2: Soạn Thảo 50 Kịch Bản Triết Ngôn TikTok Chuẩn SEO (`TXT-0151` -> `TXT-0200`)

- [ ] **Task 3: Biên Soạn Kịch Bản 50 Bài Triết Ngôn Sắc Lạnh Chuẩn SEO 17 Cột**
  - **Mô tả:** Viết kịch bản chi tiết cho 50 bài mới theo cấu trúc 17 cột, chia đều cho 5 cụm chủ đề (10 bài/cụm). Áp dụng triệt để quy tắc Hook ngắn (< 10 từ, dấu `......`), Cú lật bóc trần, Chiếc gương phản tư, Caption chuẩn SEO < 90 từ, 5 hashtag TikTok xu hướng và đề xuất phôi ảnh `theme_151` -> `theme_200`.
  - **Tiêu chí nghiệm thu:**
    - Đúng 50 bài, đánh số liên tục từ `TXT-0151` đến `TXT-0200`.
    - Văn phong đanh thép, sâu sắc, loại bỏ hoàn toàn sáo ngữ AI, tuân thủ `HYA-03`.
    - Xuất dữ liệu ra `scripts/posts_151_200_data.json` và cập nhật vào `scripts/tiktok_200_posts.csv`.
  - **Xác minh:** `python scripts/verify_50_new_posts.py` kiểm tra cấu trúc 17 cột, độ dài hook, caption và hashtag.
  - **Files:** `scripts/generate_50_academic_posts.py`, `scripts/posts_151_200_data.json`, `scripts/tiktok_200_posts.csv`
  - **Scope:** M (3 files)

- [ ] **Task 4: Thẩm Định Phản Biện Đa Tầng & Kiểm Định Trùng Lặp (Hard Gates G2, G3, G4)**
  - **Mô tả:** Chạy kiểm tra tính mới ngữ nghĩa (`semantic-novelty-review`) đối chiếu với 150 bài hiện hữu. Rà soát lỗi ngụy biện, sáo ngữ AI hoặc đạo đức giả theo chuẩn `editorial-critique`.
  - **Tiêu chí nghiệm thu:**
    - 0 bài trùng lặp ý tưởng với 150 bài trước.
    - 100% bài đạt tiêu chuẩn sắc bén của Hiyu Abyss.
  - **Xác minh:** Chạy script audit ngữ nghĩa và kiểm định chất lượng nội dung.
  - **Files:** `scripts/audit_semantic_novelty_151_200.py`
  - **Scope:** S (1 file)

### ❖ Checkpoint 2: Content & SEO Excellence
- [ ] Đủ 50 bài kịch bản đạt tiêu chuẩn vàng 17 cột.
- [ ] Vượt qua toàn bộ các cổng kiểm định chất lượng nội dung và SEO.

---

### Phase 3: Tích Hợp Google Sheet & Định Dạng Thẩm Mỹ Chuyên Nghiệp

- [ ] **Task 5: Nhúng 50 Bài Mới Vào Google Sheet & Đổi Tên Tab Thành "Kế Hoạch 200 Bài (TikTok Pipeline)"**
  - **Mô tả:** Đồng bộ 50 dòng mới (STT 151 -> 200) lên Google Sheet thông qua `gsheets mutate import-csv`. Đổi tên tab sheet từ `Kế Hoạch 150 Bài (TikTok Pipeline)` thành `Kế Hoạch 200 Bài (TikTok Pipeline)`.
  - **Tiêu chí nghiệm thu:**
    - Sheet hiển thị đúng 200 dòng dữ liệu liên tục từ STT 1 đến 200.
    - Tên tab được cập nhật chuẩn xác.
  - **Xác minh:** `gsheets readonly info 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY` và đọc kiểm tra dòng 151, dòng 200.
  - **Files:** `scripts/upload_200_to_sheet.py`
  - **Scope:** S (1 file)

- [ ] **Task 6: Tối Ưu Hóa Giao Diện & Thẩm Mỹ Bảng Tính (Dark Slate Polishing)**
  - **Mô tả:** Chạy script định dạng thẩm mỹ toàn diện cho 200 dòng: Tiêu đề Dark Slate (#0F172A), chữ trắng in đậm, căn chỉnh lề tối ưu, tự động wrap text, cài đặt Dropdown trạng thái cột Q cho toàn bộ 200 dòng.
  - **Tiêu chí nghiệm thu:**
    - Giao diện bảng tính sang trọng, chuyên nghiệp, không lỗi hiển thị hay tràn viền.
    - Dropdown hoạt động mượt mà trên tất cả 200 hàng.
  - **Xác minh:** Đọc định dạng và kiểm tra live trên Google Sheet.
  - **Files:** `scripts/polish_200_sheet.py`
  - **Scope:** S (1 file)

### ❖ Checkpoint 3: Live Sheet Synchronization
- [ ] Google Sheet cập nhật thành công 200 bài, đổi tên tab chuẩn.
- [ ] Định dạng thẩm mỹ Dark Slate hoàn hảo, sẵn sàng cho nhóm sản xuất nội dung.

---

### Phase 4: Đồng Bộ Kho Tri Thức Nội Bộ & Kiểm Thử Toàn Diện

- [ ] **Task 7: Đồng Bộ Kho Hồ Sơ Nội Bộ `editorial/content/` Cho 50 Bài Mới**
  - **Mô tả:** Tạo 50 file markdown `TXT-0151.md` đến `TXT-0200.md` trong `editorial/content/` kèm metadata YAML (`HYA-04`), liên kết đến các nguồn `SRC` tương ứng. Cập nhật bảng chỉ mục `indexes/INDEX_CONTENT.md`.
  - **Tiêu chí nghiệm thu:**
    - 50 file markdown mới có đầy đủ ID, chủ đề hạt nhân, nguồn học thuật, trạng thái DRAFT.
    - Bảng chỉ mục `indexes/INDEX_CONTENT.md` cập nhật đủ 200 mục.
  - **Xác minh:** Kiểm tra số lượng và tính toàn vẹn của các file trong `editorial/content/`.
  - **Files:** `editorial/content/TXT-0151.md` đến `TXT-0200.md`, `indexes/INDEX_CONTENT.md`
  - **Scope:** M (51 files)

- [ ] **Task 8: Kiểm Thử Toàn Diện & Đẩy Toàn Bộ Lên GitHub**
  - **Mô tả:** Chạy toàn bộ các bài kiểm thử hệ thống, build website, đảm bảo 0 lỗi hồi quy. Thực hiện commit và push lên nhánh `main` trên GitHub theo các lô an toàn.
  - **Tiêu chí nghiệm thu:**
    - Website build thành công 127 trang tĩnh, 22/22 bài kiểm tra WCAG AA đạt chuẩn.
    - Git status sạch sẽ, `origin/main` đồng bộ đầy đủ.
  - **Xác minh:** `cd website && npm run build && node test/verify-build.js` và `git status`.
  - **Files:** Git commits
  - **Scope:** S (0 code changes, validation only)

### ❖ Checkpoint 4: Complete & Production Ready
- [ ] 200 bài đăng hoàn chỉnh trên Google Sheet và kho dữ liệu nội bộ.
- [ ] Hệ thống hoạt động trơn tru, mã nguồn được lưu trữ an toàn trên GitHub.

---

## 3. Quản Lý Rủi Ro & Biện Pháp Giảm Thiểu

| Rủi ro | Mức độ | Biện pháp giảm thiểu |
|---|---|---|
| **Giới hạn tốc độ / Chặn truy cập khi cào dữ liệu học thuật (Rate limiting)** | Trung bình | Sử dụng các API học thuật mở có chứng thực User-Agent lịch sự (`HiyuAbyssResearchBot`), thêm độ trễ (delay 0.5s - 1s) giữa các yêu cầu, sử dụng endpoint chuẩn của OpenAlex và Crossref thay vì cào web thô. |
| **Bịa đặt nguồn hoặc trích dẫn sai ngữ cảnh (Hallucination)** | Cao | Tuân thủ tuyệt đối Hard Gate G1: Mọi nguồn tác giả đều phải liên kết đến DOI, ISBN hoặc đường dẫn nguyên tác Project Gutenberg/SEP có thật; không gán ghép lời tự sáng tác thành câu của triết gia. |
| **Trùng lặp ý tưởng với 150 bài trước** | Trung bình | Mở rộng sang 5 lãnh địa chủ đề mới và chạy script so khớp vector/từ khóa ngữ nghĩa (`semantic-novelty-review`) trước khi chốt kịch bản. |
| **Lỗi tải tệp lớn hoặc gián đoạn mạng khi đẩy Git** | Thấp | Chia nhỏ các gói commit và cấu hình buffer HTTP Git (`http.postBuffer 524288000`). |
