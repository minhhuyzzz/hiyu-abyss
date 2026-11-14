# Cương Lĩnh Kiến Trúc & Kế Hoạch Triển Khai: Thư Viện Nghệ Thuật & Hệ Thống Xuất Bản Hiyu Abyss (The Living Art Library & Publishing System)

> **Dự án:** Hiyu Abyss  
> **Tuyên ngôn tư duy:** *Chuyển dịch triệt để từ tư duy "xây 100 trang triết ngôn" sang "kiến tạo một Thư viện Nghệ thuật đương đại với hệ thống xuất bản đáng tin cậy".*  
> **Căn cứ pháp quy:** `HYA-01` (Bản sắc) $\rightarrow$ `HYA-02` (Chuẩn nguồn) $\rightarrow$ `HYA-03` (Văn phong) $\rightarrow$ `HYA-04` (Mô hình dữ liệu) $\rightarrow$ `HYA-06` (Cổng kiểm định) $\rightarrow$ `HYA-07` (Đặc tả Thư viện & Trải nghiệm)  
> **Mã nguồn hệ thống:** `website/` (Không gian kiến trúc cô lập, an toàn tại gốc dự án)  
> **Phiên bản:** `3.0 — The Living Library Edition`  

---

## 1. Triết Lý & Chuyển Dịch Tư Duy Nền Tảng

```
TƯ DUY CŨ (Page-Factory / Churn):
Kho bài TikTok ──→ Xuất HTML hàng loạt ──→ 100 trang web na ná nhau ──→ Đếm số lượng

                    ▼ BƯỚC CHUYỂN DỊCH TƯ DUY ▼

TƯ DUY MỚI (Art-Directed Library & Trusted Publishing System):
Tư tưởng triết học   +   Mỹ học Old Masters & Bảo tàng
        │                          │
        └──────────────┬───────────┘
                       ▼
        HỆ THỐNG XUẤT BẢN ĐÁNG TIN CẬY (Publishing Engine)
        - Cổng phê duyệt 2 lớp (Publication Gate G5)
        - Xác minh xuất xứ văn bản & tác giả (HYA-02)
        - Catalog bản quyền & nguồn gốc tranh ảnh (ART-xxxx)
        - Taxonomy chủ đề mở linh hoạt (Open Seed Ontology)
                       ▼
        THƯ VIỆN NGHỆ THUẬT SỐNG (The Living Library & The Mirror)
        - Nhịp điệu mỹ thuật: Monument, Reading, Index
        - Đối thoại bình đẳng giữa Chữ và Hình
        - Hai điều kiện chiếu sáng: Black Archive / Pale Archive
        - Không gian phản tư riêng tư, bảo mật tuyệt đối
```

### 4 Trụ Cột Của "Hệ Thống Xuất Bản Đáng Tin Cậy":
1. **Đáng tin cậy về Tri thức & Học thuật (Scholarly & Philosophical Integrity):**  
   Mọi văn bản đều minh bạch về bản chất: đâu là câu nguyên văn (`DIRECT_QUOTE`), đâu là diễn giải (`PARAPHRASE`), đâu là sáng tác lấy cảm hứng (`INSPIRED_ORIGINAL`) hay sáng tác nội bộ (`INDEPENDENT_ORIGINAL`). Tuyệt đối không mượn danh triết gia cho câu tự nghĩ; nguồn gốc xuất xứ được truy xuất về tài liệu thực tế.
2. **Đáng tin cậy về Mỹ học & Bản quyền Hình ảnh (Curated Visual Provenance):**  
   Tranh ảnh không phải là "ảnh nền lấp chỗ trống". Mỗi bức tranh là một chứng tích nghệ thuật được giám tuyển (Old Masters, tranh khắc đồng, kiến trúc cổ), có hồ sơ `ART-xxxx` ghi nhận bảo tàng lưu trữ (The Met, Art Institute of Chicago, Rijksmuseum...), trạng thái bản quyền (Public Domain / CC0) và văn bản alt mô tả tiếp cận.
3. **Đáng tin cậy về Kỹ thuật & Bảo mật Dữ liệu (Publishing Infrastructure Gate):**  
   Cơ chế kiểm soát 2 lớp: Chỉ xuất bản những nội dung nằm trong `publication-manifest.yaml` VÀ đạt trạng thái `APPROVED`/`PUBLISHED`. Bộ điều hợp xuất bản (Publishing Adapter) tự động thanh lọc dữ liệu (data sanitization), ngăn chặn 100% rò rỉ ghi chú nghiên cứu nội bộ ra tệp HTML công khai.
4. **Đáng tin cậy về Trải nghiệm Độc giả (Humanity & Privacy):**  
   The Mirror không phải quiz tâm lý hay trò bói toán tính cách. Đó là một buồng chiêm nghiệm tĩnh lặng (Contemplative Sanctuary), nơi người đọc chủ động đối diện với các nghịch lý và tự rút ra kết luận cho riêng mình. 100% xử lý tại trình duyệt của người dùng (zero tracking, zero profiling).

---

## 2. Quyết Định Công Nghệ & Kiến Trúc Kỹ Thuật

| Hạng mục | Quyết định kỹ thuật | Lý do bảo vệ chất lượng & bản sắc |
|---|---|---|
| **Engine xuất bản** | **Astro v5 (Static-First)** | Tạo ra các trang HTML tĩnh thuần túy, tốc độ tức thì, tối ưu SEO, không cồng kềnh JS. |
| **Lớp tương tác** | **React Islands (`client:visible`)** | Chỉ nạp JavaScript tại thành phần thực sự cần tương tác: Trình phản tư *The Mirror* và bộ phát audio/bốc bài ngẫu nhiên. |
| **Hệ thống ánh sáng** | **Black Archive / Pale Archive** | Hai điều kiện ánh sáng hoàn chỉnh, cùng một lưới và tỷ lệ vàng; chuyển đổi mượt bằng inline boot script chống FOUC. |
| **Typography** | **Cormorant Garamond + Literata + Be Vietnam Pro** | 3 tầng chữ: Nhận diện thương hiệu cổ điển $\rightarrow$ Đọc sách tiếng Việt êm ái $\rightarrow$ Điều hướng UI sắc sảo. |
| **Đường dẫn dữ liệu** | **Cross-Platform Relative Resolution** | Dùng `import.meta.url` và `path.resolve`, bảo đảm tính di động tuyệt đối giữa Windows và Linux hosting. |
| **Hạ tầng hình ảnh** | **Astro `<Image />` / `<Picture />` Pipeline** | Tự động sinh WebP/AVIF, responsive `srcset`, chống layout shift (CLS), placeholder màu pigment. |
| **Tìm kiếm nội dung** | **Pagefind Static Search** | Chỉ mục tìm kiếm tĩnh tốc độ cao sau build, hỗ trợ tiếng Việt có dấu, tìm kiếm toàn văn không cần server. |
| **Đa thiết bị & Màn hình** | **Mobile-First & Fluid Editorial Matrix** | Viewport từ 320px đến 1920px+; touch targets $\ge 44\times 44\text{px}$; safe-area insets (`env(safe-area-inset-*)`) cho tai thỏ/dynamic island; giới hạn `max-w-6xl` cho màn hình siêu rộng chống kéo dãn dòng chữ. |

---

## 3. Bản Đồ Năng Lực & 5 Giai Đoạn Triển Khai (16 Tasks)

```
Giai Đoạn 1: Nền Tảng Kỹ Thuật & Nhận Diện Bản Sắc (Astro, Tokens, 3 Fonts, Vector Logo)
   │
   ▼ ❖ Checkpoint 1: Môi trường build hoàn chỉnh, chuyển đổi theme hoàn hảo, typography chuẩn mực
Giai Đoạn 2: Publishing Engine & Chuẩn Hóa Kho Tri Thức (Catalog ART-xxxx, Manifest Gate, Adapter)
   │
   ▼ ❖ Checkpoint 2: Dữ liệu 100 tác phẩm đạt chuẩn HYA-04, bảo mật nội bộ 100%, dynamic taxonomy
Giai Đoạn 3: Trụ Cột The Library — Không Gian Giám Tuyển (Hero Chiaroscuro, Catalog, Reader, Surprise Me)
   │
   ▼ ❖ Checkpoint 3: Thư viện nghệ thuật hoạt động mượt mà, nhịp điệu ấn phẩm, không rập khuôn card AI
Giai Đoạn 4: Trụ Cột The Mirror — Buồng Chiêm Nghiệm (Hành trình MIR-0001, Client-side React Island)
   │
   ▼ ❖ Checkpoint 4: Luồng phản tư 5 nhịp sâu lắng, không lưu dữ liệu, bảo mật quyền riêng tư
Giai Đoạn 5: Tìm Kiếm Toàn Văn, Audit Tiếp Cận WCAG AA & Xuất Bản Production
   │
   ▼ ❖ Checkpoint 5: Nghiệm thu toàn diện 100% tiêu chí HYA-07, sẵn sàng vận hành & mở rộng dài hạn
```

---

## 4. Chi Tiết Kế Hoạch Từng Giai Đoạn

### Giai Đoạn 1: Nền Tảng Kỹ Thuật & Nhận Diện Bản Sắc (`web-foundation`)
- **Task 1: Khởi tạo Kiến trúc Astro v5 tại `website/`**  
  Thiết lập môi trường build tĩnh độc lập, TypeScript strict mode, React Integration, và cấu hình build đa nền tảng không phụ thuộc hệ điều hành.
- **Task 2: Hệ Thống Theme Tokens & Typography 3 Tầng**  
  Cài đặt bảng màu độc bản (*Lampblack, Bone Paper, Oxide, Patina*), nạp 3 font qua `@fontsource` với đầy đủ ký tự tiếng Việt có dấu, và cấu hình script chặn FOUC ngay tại `<head>`.
- **Task 3: Thiết Kế Bộ Nhận Diện Vector Logo Monogram & Favicon**  
  Sử dụng quy chuẩn `taste-skill` để vẽ monogram tối giản (biểu tượng hố sâu tri thức / chiếc gương hình học) định dạng SVG siêu nhẹ, tự đổi sắc tố theo Dark/Light.
- **❖ Checkpoint 1:** Build tĩnh chạy trơn tru, chuyển theme tức thì không nháy trắng, font tiếng Việt hiển thị sắc nét.

### Giai Đoạn 2: Publishing Engine & Chuẩn Hóa Kho Tri Thức (`publishing-engine`)
- **Task 4: Chuẩn Hóa Dữ Liệu 100 Tác Phẩm Sang Markdown Chuẩn `HYA-04`**  
  Đồng bộ 100 bài viết xuất sắc từ pipeline vào thư mục lưu trữ vĩnh viễn `editorial/content/TXT-0001.md` $\rightarrow$ `TXT-0100.md` với đầy đủ Frontmatter: ID, loại trích dẫn, tác giả, chủ đề, trạng thái `APPROVED`.
- **Task 5: Thiết Lập Publication Manifest & Catalog Mỹ Thuật `ART-xxxx`**  
  Tạo `website/publication-manifest.yaml` kiểm soát danh sách xuất bản công khai. Xây dựng catalog `ART-xxxx` lưu trữ thông tin tranh bảo tàng, họa sĩ, niên đại, license và văn bản alt mô tả thị giác.
- **Task 6: Xây Dựng Publishing Adapter & Dynamic Open Taxonomy Engine**  
  Viết module `website/src/lib/content-publisher.ts` thực thi: đường dẫn tương đối, xác thực cổng kiểm duyệt 2 lớp, thanh lọc dữ liệu nội bộ (data sanitization), và tự động trích xuất taxonomy chủ đề mở từ các tác phẩm được duyệt.
- **❖ Checkpoint 2:** Adapter nạp đúng 100 tác phẩm, tự sinh danh mục chủ đề mở, loại bỏ hoàn toàn các bài nháp và ghi chú nhạy cảm.

### Giai Đoạn 3: Trụ Cột The Library — Không Gian Giám Tuyển (`the-library`)
- **Task 7: Khung Giao Diện Ấn Phẩm Nghệ Thuật (`BaseLayout`, `Header`, `Footer`)**  
  Xây dựng thanh điều hướng tối giản (*Library · Mirror · Themes · Search · ThemeToggle*) và chân trang mang tuyên ngôn triết học và ghi công xuất xứ.
- **Task 8: Trang Chủ Art-Directed Hero & Editorial Mosaic (`src/pages/index.astro`)**  
  Thiết kế trang chủ theo cấu trúc ấn phẩm nghệ thuật: Hero artwork khổ lớn ánh sáng chiaroscuro, khối trích dẫn mở màn, và cụm Editorial Mosaic dẫn dắt vào các dòng tư tưởng.
- **Task 9: Danh Mục Thư Viện Đa Nhịp Điệu (`src/pages/library/index.astro`)**  
  Bố cục tạp chí nghệ thuật (xen kẽ tranh lớn, thẻ đọc, khoảng lặng), bộ lọc chủ đề mở động không cần tải lại trang, và tính năng *Surprise Me* (Bốc ngẫu nhiên một tác phẩm chiêm nghiệm).
- **Task 10: Trang Đọc Chi Tiết Tác Phẩm (`src/pages/library/[slug].astro`)**  
  Không gian đọc tĩnh lặng với tranh nền bảo tàng mờ ảo, nhãn minh bạch bản chất trích dẫn (`DIRECT_QUOTE`, `PARAPHRASE`, `INSPIRED_ORIGINAL`), chú thích tác giả và công cụ chia sẻ trích dẫn.
- **Task 11: Trang Bản Đồ Chủ Đề Mở (`src/pages/themes/[slug].astro`)**  
  Sinh tự động các không gian tập hợp tác phẩm theo từng luồng tư tưởng mở (Thao túng, Đạo đức giả, Bản ngã, Khắc kỷ, Ranh giới...).
- **❖ Checkpoint 3:** Toàn bộ 100 trang tác phẩm và trang chủ đề hoạt động trơn tru trên mọi độ phân giải màn hình.

### Giai Đoạn 4: Trụ Cột The Mirror — Buồng Chiêm Nghiệm Tĩnh Lặng (`the-mirror`)
- **Task 12: Soạn Thảo Kịch Bản Hành Trình `MIR-0001` ("Sự thật và bình yên")**  
  Tạo hồ sơ `website/journeys/MIR-0001.yaml` với cấu trúc 5 bước triết học: Khởi đầu $\rightarrow$ Câu hỏi $\rightarrow$ Lựa chọn góc nhìn $\rightarrow$ Phản đề thức tỉnh $\rightarrow$ Kết thúc mở để tự vấn.
- **Task 13: Xây Dựng React Island `MirrorJourney.tsx`**  
  Component tương tác client-side với nhịp chuyển động chậm rãi, tĩnh lặng, hỗ trợ quay lại (Back), thoát (Exit), bắt đầu lại (Restart), bảo mật tuyệt đối thông tin người đọc.
- **Task 14: Trang Trải Nghiệm The Mirror (`src/pages/mirror/index.astro` & `[journey].astro`)**  
  Không gian trải nghiệm phản tư với tranh mở màn huyền ảo và lối dẫn dắt trang nghiêm.
- **❖ Checkpoint 4:** Người đọc hoàn thành trọn vẹn hành trình phản tư mà không gặp bất kỳ lỗi logic hay gián đoạn trải nghiệm nào.

### Giai Đoạn 5: Tìm Kiếm, Bộ Kiểm Thử Tiếp Cận WCAG AA & Hoàn Tất (`search-and-audit`)
- **Task 15: Tích Hợp Tìm Kiếm Toàn Văn Pagefind (`src/pages/search.astro`)**  
  Đánh chỉ mục tĩnh kho 100 tác phẩm, tìm kiếm tức thì tiếng Việt có dấu, hỗ trợ lọc theo chủ đề và tác giả.
- **Task 16: Bộ Kiểm Thử Tự Động & Đóng Gói Production Build**  
  - *Accessibility Audit:* Đo tương phản màu đạt chuẩn WCAG AA ($\ge 4.5:1$ chữ thường, $\ge 3:1$ chữ lớn) trên CẢ 2 THEME.
  - *Integrity & Security Test:* Kiểm tra tự động tính hợp lệ của toàn bộ route tĩnh và xác nhận không rò rỉ dữ liệu nháp ra bản build.
  - *Production Build:* Chạy `npm run build` xuất ra thư mục tĩnh `website/dist/` hoàn hảo.
- **❖ Checkpoint 5:** 16/16 tasks hoàn thành và kiểm định đạt chuẩn, sẵn sàng đưa lên hosting toàn cầu (Cloudflare Pages / Vercel).
