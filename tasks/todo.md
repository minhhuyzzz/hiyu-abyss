# Hiyu Abyss — Thư Viện Nghệ Thuật & Hệ Thống Xuất Bản (Task List v3.0)

> **Cương lĩnh kiến trúc:** [tasks/plan.md](file:///c:/hiyuabyss/tasks/plan.md)  
> **Tuyên ngôn tư duy:** *Xây dựng một Thư viện Nghệ thuật có Hệ thống Xuất bản Đáng tin cậy.*  
> **Căn cứ pháp quy:** `HYA-01` $\rightarrow$ `HYA-07`

---

## Phase 1: Nền Tảng Kỹ Thuật & Nhận Diện Bản Sắc (`web-foundation`)

- [x] **Task 1: Khởi tạo Kiến trúc Astro v5 tại `website/`**
  - **Mô tả:** Khởi tạo project Astro v5 độc lập tại `website/`, cài đặt `@astrojs/react`, Tailwind CSS tương thích Astro 5, TypeScript strict mode, và cấu hình đường dẫn tương đối đa nền tảng.
  - **Tiêu chí nghiệm thu:**
    - `website/package.json` độc lập với root, cấu hình build chạy tốt trên cả Windows và Linux.
    - `website/.gitignore` bỏ qua `node_modules/` và `dist/`.
    - Lệnh build tĩnh thử nghiệm thành công không lỗi.
  - **Xác minh:** `cd website && npm run build`
  - **Files:** `website/package.json`, `website/astro.config.mjs`, `website/tsconfig.json`, `website/.gitignore`
  - **Scope:** Medium (4 files)

- [x] **Task 2: Hệ Thống Theme Tokens (Black/Pale Archive) & 3 Tầng Typography**
  - **Mô tả:** Thiết lập CSS Variables cho 2 theme (*Black Archive* & *Pale Archive*), nạp 3 font qua `@fontsource` (Cormorant Garamond cho Brand, Literata cho Quote, Be Vietnam Pro cho UI), và tạo inline script chống FOUC trong `<head>`.
  - **Tiêu chí nghiệm thu:**
    - Màu sắc đạt chuẩn: Dark `#090A09` (Lampblack) / Light `#ECE9E1` (Bone Paper), Accent `#C29A77` / `#76513D`, Oxide `#B47862` / `#8A4D43`.
    - Chuyển đổi theme mượt qua nút bấm, lưu `localStorage`, không nháy trắng khi F5.
    - Hiển thị hoàn hảo mọi ký tự tiếng Việt có dấu phức tạp (`ắ`, `ễ`, `ộ`, `ượ`, `ỵ`).
  - **Xác minh:** Inspect DOM và CSS variables trên cả 2 theme trong browser.
  - **Files:** `website/src/styles/tokens.css`, `website/src/components/ThemeToggle.astro`, `website/src/layouts/BaseLayout.astro`
  - **Scope:** Medium (3 files)

- [x] **Task 3: Thiết Kế Bộ Nhận Diện Vector Logo Monogram & Favicon**
  - **Mô tả:** Sử dụng quy chuẩn `taste-skill` để vẽ monogram tối giản (biểu tượng hố sâu tri thức / chiếc gương hình học) định dạng SVG siêu nhẹ (< 5KB), tự động đổi sắc tố theo Dark/Light.
  - **Tiêu chí nghiệm thu:**
    - Vector SVG tinh xảo, sắc nét ở mọi kích thước màn hình.
    - Hiển thị hài hòa trên thanh Header và Favicon tab trình duyệt ở cả 2 chế độ nền.
  - **Xác minh:** Kiểm tra hiển thị favicon trên tab và logo trên thanh Header.
  - **Files:** `website/public/favicon.svg`, `website/src/components/BrandLogo.astro`
  - **Scope:** Small (2 files)

### ❖ Checkpoint 1: Foundation Complete
- [x] `cd website && npm run build` thành công 100%.
- [x] Theme Dark/Light chuyển đổi tức thì không chớp trắng.
- [x] 3 font chữ hiển thị đúng vai trò và chuẩn mực tiếng Việt.

---

## Phase 2: Publishing Engine & Chuẩn Hóa Kho Tri Thức (`publishing-engine`)

- [x] **Task 4: Chuẩn Hóa Dữ Liệu 100 Tác Phẩm Sang Markdown Chuẩn `HYA-04`**
  - **Mô tả:** Xuất bản đồng bộ 100 bài đăng từ pipeline vào thư mục lưu trữ vĩnh viễn `editorial/content/TXT-0001.md` $\rightarrow$ `TXT-0100.md` với đầy đủ Frontmatter: ID, loại trích dẫn, tác giả, chủ đề, trạng thái `APPROVED`.
  - **Tiêu chí nghiệm thu:**
    - Đủ đúng 100 file markdown với ID bất biến từ `TXT-0001` đến `TXT-0100`.
    - 100% file đều có trạng thái `status: APPROVED` và nhãn loại trích dẫn minh bạch theo `HYA-04`.
  - **Xác minh:** Chạy script xác thực frontmatter 100 file trong `editorial/content/`.
  - **Files:** `editorial/content/TXT-0001.md` $\rightarrow$ `TXT-0100.md`, `scripts/sync_100_markdown_content.py`
  - **Scope:** Medium (script + generated files)

- [x] **Task 5: Thiết Lập Publication Manifest & Catalog Mỹ Thuật `ART-xxxx`**
  - **Mô tả:** Tạo file manifest `website/publication-manifest.yaml` phê duyệt xuất bản 100 tác phẩm, và xây dựng catalog `ART-xxxx` ghi nhận bản quyền, xuất xứ bảo tàng của các bộ phôi ảnh cổ điển.
  - **Tiêu chí nghiệm thu:**
    - Cấu trúc YAML chuẩn xác theo đặc tả HYA-07 Mục 3.8 và Mục 8.
    - Minh bạch nguồn tranh (The Met, Rijksmuseum...), license rõ ràng.
  - **Xác minh:** Kiểm tra cú pháp YAML và schema kiểm định asset.
  - **Files:** `website/publication-manifest.yaml`, `website/src/data/asset-catalog.json`
  - **Scope:** Small (2 files)

- [x] **Task 6: Xây Dựng Publishing Adapter & Dynamic Open Taxonomy Engine**
  - **Mô tả:** Module TypeScript `website/src/lib/content-publisher.ts` thực thi đường dẫn tương đối (cross-platform), cổng kiểm duyệt 2 lớp (Manifest + Status), thanh lọc dữ liệu nội bộ (data sanitization), và trích xuất taxonomy chủ đề mở.
  - **Tiêu chí nghiệm thu:**
    - Không hardcode đường dẫn tuyệt đối Windows.
    - Loại bỏ triệt để các bài nháp (`DRAFT`) hoặc không nằm trong manifest.
    - Tự động trích xuất taxonomy mở động từ các tác phẩm được duyệt.
  - **Xác minh:** Chạy test adapter kiểm tra danh sách bài và taxonomy trả về.
  - **Files:** `website/src/lib/content-publisher.ts`, `website/src/lib/types.ts`
  - **Scope:** Medium (2 files)

### ❖ Checkpoint 2: Publishing Engine Complete
- [x] 100 tác phẩm đã duyệt được nạp trơn tru vào build system.
- [x] Không có bất kỳ dữ liệu nháp hay ghi chú nội bộ nào bị lọt qua adapter.
- [x] Danh mục chủ đề mở được sinh tự động từ metadata.

---

## Phase 3: Trụ Cột The Library — Không Gian Giám Tuyển (`the-library`)

- [x] **Task 7: Khung Giao Diện Ấn Phẩm Nghệ Thuật (`BaseLayout`, `Header`, `Footer`)**
  - **Mô tả:** Hoàn thiện `Header.astro` (Logo + Menu + Theme Toggle) và `Footer.astro` (Tuyên ngôn triết học, xuất xứ và liên kết mạng xã hội).
  - **Tiêu chí nghiệm thu:**
    - Menu điều hướng tối giản: *Library · Mirror · Themes · Search*.
    - Co giãn hoàn hảo trên mọi thiết bị: Touch targets $\ge 44\times 44\text{px}$; safe-area insets (`env(safe-area-inset-*)`) cho màn hình tai thỏ/dynamic island; tuyệt đối không có thanh cuộn ngang (horizontal scroll).
  - **Xác minh:** Kiểm tra hiển thị header/footer trên các viewport 320px, 375px, 768px và 1280px.
  - **Files:** `website/src/layouts/BaseLayout.astro`, `website/src/components/Header.astro`, `website/src/components/Footer.astro`
  - **Scope:** Small (3 files)

- [x] **Task 8: Trang Chủ Art-Directed Hero & Editorial Mosaic (`src/pages/index.astro`)**
  - **Mô tả:** Thiết kế trang chủ theo chuẩn ấn phẩm nghệ thuật: Hero artwork khổ lớn (sơn dầu Phục Hưng / ánh sáng chiaroscuro), câu triết ngôn tiêu biểu, và cụm Editorial Mosaic dẫn dắt vào các dòng tư tưởng.
  - **Tiêu chí nghiệm thu:**
    - Bố cục bất đối xứng nghệ thuật, có nhịp thở, không rập khuôn template AI.
    - Hero artwork tải nhanh, tối ưu hóa qua thẻ `<Image />` của Astro.
  - **Xác minh:** Mở trang chủ trên local dev server và kiểm tra trực quan.
  - **Files:** `website/src/pages/index.astro`, `website/src/components/HeroArtwork.astro`, `website/src/components/EditorialMosaic.astro`
  - **Scope:** Medium (3 files)

- [x] **Task 9: Danh Mục Thư Viện Đa Nhịp Điệu (`src/pages/library/index.astro`)**
  - **Mô tả:** Bố cục tạp chí nghệ thuật hiển thị 100 tác phẩm (xen kẽ tranh lớn, thẻ đọc, khoảng lặng), bộ lọc dynamic taxonomy theo chủ đề mở, và nút *Surprise Me* (Bốc bài ngẫu nhiên).
  - **Tiêu chí nghiệm thu:**
    - Bộ lọc chủ đề hoạt động mượt mà không cần reload trang.
    - Nút *Surprise Me* chuyển hướng tức thì đến 1 tác phẩm ngẫu nhiên kèm hiệu ứng êm dịu.
  - **Xác minh:** Thao tác thử các bộ lọc chủ đề và bấm nút *Surprise Me*.
  - **Files:** `website/src/pages/library/index.astro`, `website/src/components/QuoteCard.astro`
  - **Scope:** Medium (2 files)

- [x] **Task 10: Trang Đọc Chi Tiết Tác Phẩm (`src/pages/library/[slug].astro`)**
  - **Mô tả:** Không gian đọc tĩnh lặng với tranh nền bảo tàng mờ ảo, nhãn nguồn minh bạch (`DIRECT_QUOTE`, `PARAPHRASE`, `INSPIRED_ORIGINAL`), trích dẫn tác giả, và nút sao chép trích ngôn.
  - **Tiêu chí nghiệm thu:**
    - Sinh tĩnh đúng 100 trang HTML cho 100 tác phẩm.
    - Văn bản hiển thị rõ ràng ngay cả khi ảnh nền bị tắt hoặc chưa tải xong.
  - **Xác minh:** Mở thử các trang `/library/txt-0001`, `/library/txt-0050`, `/library/txt-0100`.
  - **Files:** `website/src/pages/library/[slug].astro`, `website/src/components/SourceAttribution.astro`
  - **Scope:** Medium (2 files)

- [x] **Task 11: Trang Bản Đồ Chủ Đề Mở (`src/pages/themes/[slug].astro`)**
  - **Mô tả:** Sinh tự động các trang tập hợp tác phẩm theo từng luồng tư tưởng mở (Thao túng, Đạo đức giả, Bản ngã, Khắc kỷ, Ranh giới...).
  - **Tiêu chí nghiệm thu:**
    - Sinh tĩnh danh mục trang cho tất cả chủ đề có tác phẩm thực tế được duyệt.
  - **Xác minh:** Truy cập thử `/themes/hypocrisy`, `/themes/ego`.
  - **Files:** `website/src/pages/themes/[slug].astro`, `website/src/pages/themes/index.astro`
  - **Scope:** Small (2 files)

### ❖ Checkpoint 3: The Library Complete
- [x] Toàn bộ 100 trang tác phẩm, trang chủ, trang thư viện và các trang chủ đề hoạt động trơn tru.
- [x] Nút *Surprise Me* bốc bài ngẫu nhiên hoạt động chính xác.

---

## Phase 4: Trụ Cột The Mirror — Buồng Chiêm Nghiệm Tĩnh Lặng (`the-mirror`)

- [x] **Task 12: Soạn Thảo Kịch Bản Hành Trình `MIR-0001` ("Sự thật và bình yên")**
  - **Mô tả:** Soạn thảo hồ sơ `website/journeys/MIR-0001.yaml` theo cấu trúc 5 bước của HYA-07: Mở đầu $\rightarrow$ Câu hỏi $\rightarrow$ Lựa chọn $\rightarrow$ Phản đề $\rightarrow$ Kết thúc mở.
  - **Tiêu chí nghiệm thu:**
    - Cấu trúc YAML chuẩn xác, không có nhánh mồ côi hay vòng lặp vô tận.
    - Ngôn từ phản tư sâu sắc, tôn trọng góc nhìn người đọc, không chẩn đoán tâm lý.
  - **Xác minh:** Kiểm tra cú pháp YAML và logic rẽ nhánh qua script validator.
  - **Files:** `website/journeys/MIR-0001.yaml`
  - **Scope:** Small (1 file)

- [x] **Task 13: Xây Dựng React Island `MirrorJourney.tsx`**
  - **Mô tả:** Thành phần React tương tác client-side với nhịp chuyển động chậm rãi, tĩnh lặng, hỗ trợ quay lại (Back), thoát (Exit), bắt đầu lại (Restart), bảo mật tuyệt đối thông tin người đọc.
  - **Tiêu chí nghiệm thu:**
    - Tương tác 100% tại trình duyệt, không gửi dữ liệu lựa chọn cá nhân lên máy chủ.
    - Animation chuyển cảnh trầm tĩnh, không giật màn hình.
  - **Xác minh:** Thử hoàn thành hành trình qua cả 2 nhánh lựa chọn.
  - **Files:** `website/src/components/MirrorJourney.tsx`
  - **Scope:** Medium (1 file)

- [x] **Task 14: Trang Trải Nghiệm The Mirror (`src/pages/mirror/index.astro` & `[journey].astro`)**
  - **Mô tả:** Không gian trải nghiệm phản tư với tranh mở màn huyền ảo và lối dẫn dắt trang nghiêm.
  - **Tiêu chí nghiệm thu:**
    - Không khí tĩnh lặng, artwork mở đầu phù hợp tinh thần chiêm nghiệm.
  - **Xác minh:** Truy cập trực tiếp `/mirror` và `/mirror/su-that-va-binh-yen`.
  - **Files:** `website/src/pages/mirror/index.astro`, `website/src/pages/mirror/[journey].astro`
  - **Scope:** Small (2 files)

### ❖ Checkpoint 4: The Mirror Complete
- [x] Hành trình phản tư tương tác mượt mà, logic rẽ nhánh chính xác.
- [x] Nút Exit và Restart hoạt động tin cậy.

---

## Phase 5: Tìm Kiếm, Bộ Kiểm Thử Tiếp Cận WCAG AA & Hoàn Tất (`search-and-audit`)

- [x] **Task 15: Tích Hợp Tìm Kiếm Toàn Văn Pagefind (`src/pages/search.astro`)**
  - **Mô tả:** Cài đặt Pagefind để tự động đánh chỉ mục tĩnh sau khi build và xây dựng giao diện tìm kiếm tại `src/pages/search.astro`.
  - **Tiêu chí nghiệm thu:**
    - Tìm kiếm tức thì từ khóa tiếng Việt (có dấu và không dấu).
    - Hiển thị kết quả tìm kiếm gồm trích đoạn và link tới bài đọc.
  - **Xác minh:** Chạy build và thử tìm kiếm các từ khóa: "thao túng", "giả tạo", "bản ngã".
  - **Files:** `website/src/pages/search.astro`, `website/package.json`
  - **Scope:** Small (1–2 files)

- [x] **Task 16: Bộ Kiểm Thử E2E, Kiểm Định WCAG AA & Production Build Đa Thiết Bị**
  - **Mô tả:** Xây dựng script kiểm thử tự động kiểm tra tương phản màu WCAG AA trên cả 2 theme, kiểm tra tính toàn vẹn của tất cả URL, kiểm định hiển thị trên 5 mốc viewport (320px, 375px/390px, 768px, 1280px, 1920px+), và chạy production build hoàn chỉnh.
  - **Tiêu chí nghiệm thu:**
    - Tỷ lệ tương phản màu chữ đạt chuẩn WCAG AA ($\ge 4.5:1$ chữ thường, $\ge 3:1$ chữ lớn) trên CẢ 2 THEME.
    - Hiển thị hoàn hảo trên 5 mốc viewport: 320px không vỡ chữ, tablet 768px bố cục tạp chí 2 cột, desktop ultrawide 1920px+ giới hạn `max-w-6xl` căn giữa độ dài dòng lý tưởng (60–75 ký tự).
    - Lệnh `npm run build` tạo thành công thư mục tĩnh `website/dist/` không có liên kết hỏng.
    - Tài liệu hướng dẫn deploy lên Cloudflare Pages / Vercel tại `website/README.md`.
  - **Xác minh:** `cd website && npm run build && node test/verify-build.js`
  - **Files:** `website/test/verify-build.js`, `website/README.md`
  - **Scope:** Medium (2 files)

### ❖ Checkpoint 5: Project Shipped & Ready to Deploy
- [x] 16/16 tasks hoàn thành và được kiểm định.
- [x] Toàn bộ thư viện nghệ thuật sống sẵn sàng xuất bản công khai lên hosting.
