# HYA-07 — HIYU ABYSS WEBSITE & EXPERIENCE SPECIFICATION

| Thuộc tính | Giá trị |
|---|---|
| Mã tài liệu | `HYA-07` |
| Phiên bản | `2.0` — Dual-theme, art-directed, image-rich |
| Loại | Product concept + UX + technical implementation specification |
| Môi trường thực hiện | Google Antigravity |
| Phụ thuộc | HYA-01 → HYA-06 |
| Phạm vi | Website công khai: The Library + The Mirror |
| Ngôn ngữ ưu tiên | Tiếng Việt; có đường mở rộng đa ngôn ngữ |
| Giao diện | **Dark mặc định + Light hoàn chỉnh**, cùng một hệ nhận diện thị giác |

> **Tầm nhìn:** Hiyu Abyss là một không gian đọc và khám phá tri thức mở, nơi người đọc có thể đi từ một câu chữ ngắn đến những tác phẩm, khái niệm, câu hỏi và hành trình phản tư. Website không phải bản sao của TikTok, blog châm ngôn rời rạc hay một công cụ chẩn đoán tâm lý.

---

## 1. Nguyên tắc sản phẩm

1. **Hai trụ cột cùng tồn tại:** `The Library` để khám phá nội dung; `The Mirror` để khám phá góc nhìn bằng trải nghiệm có lựa chọn.
2. **Phạm vi tri thức mở:** không giới hạn ở đạo đức giả, tâm lý học hay bóng tối nội tâm. HYA-01 cung cấp các hạt nhân chủ đề ban đầu; bộ phân loại được mở rộng có kiểm soát mỗi khi có ý tưởng xứng đáng.
3. **Image-rich editorial, not text-only:** mở trang là thấy ngay một ý tưởng có nội dung **và** hình ảnh mang ngữ nghĩa. Không dùng ảnh để lấn át khả năng đọc, cũng không biến trang thành danh sách chữ thuần.
4. **Sắc lạnh nhưng không một chiều:** cho phép mâu thuẫn, phản đề, hoài nghi, lòng trắc ẩn, tính phi lý, cái đẹp và sự bất định cùng tồn tại.
5. **Dẫn nguồn nghiêm túc:** câu nguyên văn, diễn giải, câu lấy cảm hứng và sáng tác độc lập phải phân biệt minh bạch, theo HYA-02/HYA-04.
6. **Độc giả có quyền tự diễn giải:** The Mirror không chấm điểm nhân cách, suy đoán bệnh lý, hoặc trình bày câu lựa chọn như kết luận về người dùng.
7. **Hiện thực hóa dần:** kiến trúc gọn, tốc độ nhanh, thiết bị di động là ưu tiên chính.

## 2. Định vị và các nhóm người đọc

- **Casual reader:** từ TikTok sang đọc một câu, lưu/chia sẻ nhanh, không bị ép đăng ký.
- **Explorer:** khám phá chủ đề lạ, theo đường dẫn liên quan giữa câu, câu hỏi, tác giả và tác phẩm.
- **Reflective reader:** tham gia trải nghiệm The Mirror, chủ động đối diện nhiều góc nhìn.
- **Deep reader:** tìm nguồn sách, đọc phân tích, tra cứu tác phẩm và trích dẫn có xuất xứ.

**Trải nghiệm mong muốn:** đọc ngay → tò mò → khám phá → tự suy ngẫm → muốn quay lại.

## 3. Hệ thống thị giác — Black Archive / Pale Archive

### 3.1. Tuyên ngôn mỹ thuật và quyết định đã chốt

**Art direction: "The Black Archive"** — một ấn phẩm mỹ thuật đương đại lưu giữ tư tưởng cổ xưa, chứ không phải theme "luxury gold" hoặc trang web trí tuệ nhân tạo đại trà. Nhịp bố cục lấy cảm hứng từ **editorial art books, tranh Old Masters, bản khắc cổ, phòng trưng bày đương đại**, kết hợp khoảng lặng với các bức hình lớn có chủ đích.

- Dark mode **mặc định**: gần đen mực (không phải xanh đen cyberpunk); điểm nhấn sắc pigment trầm.
- Light mode **đầy đủ**: mặt giấy khoáng ấm, không trắng tinh, không sepia phủ toàn màn hình.
- Một brand, hai điều kiện chiếu sáng: cùng lưới, typography, cách biên tập ảnh; thay ánh sáng, độ tương phản, bề mặt và xử lý overlay.
- **Không dùng** neon tím/xanh, gradient chuyển màu lớn, glassmorphism, bokeh, glow giả lập, chip/tag rực rỡ, golden-border toàn trang, icon AI não bộ/đám mây, hàng trăm card y hệt nhau, hiệu ứng 3D chỉ để khoe công nghệ.
- **Không dùng** hình đầu lâu/castle/đồng hồ cát lặp đi lặp lại như biểu tượng toàn bộ dự án. Vanitas chỉ là **một** ngữ pháp thị giác; kho ảnh phải mở theo mỹ học, thiên nhiên, khoa học, thân phận, lịch sử, kiến trúc, trừu tượng và đời sống.
- Màu sắc phản ánh tư tưởng chứ không máy móc ánh xạ "chủ đề buồn = ảnh đen". Ảnh có thể rực rỡ khi nội dung nói đến vẻ đẹp, tái sinh, niềm tin hoặc hy vọng.

### 3.2. Bảng màu được lựa chọn (không generic)

Tên vật liệu: **Lampblack / Bone Paper / Oxide / Patina / Ash**. Màu nhấn có nguồn cảm hứng từ sắc tố hội họa thay vì xu hướng sản phẩm công nghệ.

| Vai trò | Token | Dark: Black Archive | Light: Pale Archive |
|---|---|---|---|
| Canvas | `--bg` | `#090A09` | `#ECE9E1` |
| Surface | `--surface` | `#141614` | `#F6F2E9` |
| Elevated | `--surface-raised` | `#1D201C` | `#E3DED3` |
| Chữ chính | `--text` | `#EAE5DA` | `#24251F` |
| Chữ phụ | `--muted` | `#B2B0A6` | `#50534D` |
| Viền tinh tế | `--border` | `#393C36` | `#A7A69A` |
| Pigment chính | `--accent` | `#C29A77` | `#76513D` |
| Sắc đỏ oxit | `--oxide` | `#B47862` | `#8A4D43` |
| Màu patina phụ | `--patina` | `#96A79A` | `#536C60` |
| Chữ trên nút màu pigment | `--on-accent` | `#151713` | `#FFF7EA` |

**Quy tắc phân bổ thị giác:** gần đen/giấy 70–80%, typography & tranh 15–25%, các điểm pigment 3–5% theo cảm nhận bố cục (không phải chỉ tiêu pixel chính xác). `--oxide` dùng cho nhấn quan trọng; `--patina` dùng rất hiếm, không phải màu thứ ba xuất hiện khắp mọi card. Không biến mọi tiêu đề thành vàng.

**Kiểm tra tương phản tính toán:** chữ chính/nền Dark ≈ 15.8:1, chữ phụ/nền Dark ≈ 9.1:1; chữ chính/nền Light ≈ 12.7:1, chữ phụ/nền Light ≈ 6.5:1; accent/nền Light ≈ 5.7:1. Đây là phép tính cho các cặp token cơ sở, **không thay thế** kiểm tra trên component thật/ảnh/overlay. Mọi chữ thường phải đạt WCAG AA >= 4.5:1; chữ lớn >= 3:1; control/focus indicator quan trọng >= 3:1. Border trang trí không bắt buộc 3:1; khi border truyền tải trạng thái nhập liệu phải có cách phân biệt rõ hơn.

**Đánh giá phương án:**

| Phương án | Độ riêng biệt | Khả năng đọc | Hợp bản sắc | Quyết định |
|---|---|---|---|---|
| Đen + vàng kim luxury | Thấp | Khá | Chỉ có vẻ sang, dễ sáo | Loại |
| Đen + tím/xanh gradient AI | Thấp | Khá | Lệch bản sắc văn chương | Loại |
| Đen lạnh + trắng tinh | Trung bình | Tốt | Thiếu chất liệu/mỹ học | Không chọn |
| **Lampblack + Bone Paper + Oxide + Patina** | **Cao** | **Tốt (token kiểm tương phản)** | **Phù hợp** | **Chọn** |

Đây là đánh giá biên tập định tính, không phải khảo sát người dùng.

### 3.3. Tokens CSS khởi điểm

```css
:root,
:root[data-theme="dark"] {
  color-scheme: dark;
  --bg: #090A09;
  --surface: #141614;
  --surface-raised: #1D201C;
  --text: #EAE5DA;
  --muted: #B2B0A6;
  --border: #393C36;
  --accent: #C29A77;
  --oxide: #B47862;
  --patina: #96A79A;
  --on-accent: #151713;
}
:root[data-theme="light"] {
  color-scheme: light;
  --bg: #ECE9E1;
  --surface: #F6F2E9;
  --surface-raised: #E3DED3;
  --text: #24251F;
  --muted: #50534D;
  --border: #A7A69A;
  --accent: #76513D;
  --oxide: #8A4D43;
  --patina: #536C60;
  --on-accent: #FFF7EA;
}
html { background: var(--bg); color: var(--text); }
body { background: var(--bg); color: var(--text); }
::selection { background: var(--oxide); color: var(--on-accent); }
```

Đây là token nền cho implementation; developer phải kiểm tra `::selection`, button disabled, hover, focus, selection trên cả 2 mode và chỉnh khi cần. Không tự dùng `--accent` làm nền text nếu chưa kiểm contrast.

### 3.4. Theme switch — UX và kỹ thuật

- Nút chuyển theme **luôn thấy** ở header desktop và mobile; biểu tượng mặt trời/mặt trăng kèm `aria-label` văn bản rõ; không làm một theme ẩn.
- Dark là default lần đầu (đúng định hướng kênh); nếu đã chọn Light thì giữ lựa chọn bằng `localStorage` (chỉ lưu `theme`, không ghi nội dung đọc riêng tư). Nếu thiết lập hỗ trợ theo hệ điều hành được thêm sau, không ghi đè lựa chọn tay.
- Áp dụng `data-theme` trên `<html>` **trước khi render nội dung chính**, ví dụ inline boot script ngắn trong `<head>` để tránh nháy giao diện (FOUC).
- Thiết kế ảnh/overlay theo theme (độ mờ gradient tối ở Dark, đường viền và khoảng nền trong Light) chứ không phủ filter đảo màu lên ảnh hội họa.
- Kiểm contrast, hover, focus, icon, skeleton, ảnh có chữ phủ lên ở cả 2 theme; screen reader phải nhận biết trạng thái hiện tại (`aria-pressed` hoặc mô tả tương đương).
- Không làm hai site/route riêng; cùng URL, cùng nội dung, cùng component và tokens khác nhau.

### 3.5. Typography & bố cục chống "AI hóa"

- Chữ nội dung tiếng Việt: ưu tiên **Literata** (serif cho quote và essays, kiểm dấu tiếng Việt thực tế). UI: **Be Vietnam Pro** hoặc sans có độ tương phản nét cân bằng; không dùng quá 2 họ font nếu không có lý do biên tập.
- Tự kiểm các dấu phức như `ắ`, `ễ`, `ộ`, `ượ`, `ỵ` trên tất cả weight; nếu font thiếu glyph phải chọn fallback tương thích thay vì hiển thị lỗi.
- Layout **asymmetrical editorial**: ảnh full bleed ở một số section, caption nhỏ, masthead, đường chia mảnh, biên rộng, type scale có nhịp. Tránh grid 3 cột card đồng kích thước áp dụng cho toàn website.
- Có ba nhịp: **Monument** (ảnh lớn/ít chữ), **Reading** (cột văn bản hợp lý), **Index** (thư mục/raster tranh, có khoảng trắng). Thiết kế mobile như một ấn phẩm được tái biên tập, không chỉ co desktop xuống 375px.
- Text hiển thị dưới dạng HTML chọn được, copy được, tìm được; **không rasterize câu chữ vào ảnh**. Câu trên ảnh nên là overlay HTML có nền/gradient đảm bảo đọc, có phiên bản đọc độc lập.

### 3.6. Art direction — thư viện thị giác thực thụ

**Tranh ảnh là một cấu phần biên tập ngang hàng với câu chữ.** Mỗi ảnh phải có ít nhất một chức năng: đối thoại với luận điểm; xây dựng không khí; mở một liên tưởng mới; hoặc làm chứng tích nghệ thuật/lịch sử. Không lấy ảnh bất kỳ vì `cover image` còn trống.

**Ngữ pháp hình ảnh gồm:**

1. **Old Masters:** sơn dầu Baroque/Renaissance, ánh sáng chiaroscuro, chân dung, tĩnh vật, biểu tượng.
2. **Engravings:** bản khắc gỗ/đồng cổ, atlas, giải phẫu cổ, bản đồ thiên văn, sơ đồ khoa học có nguồn.
3. **Sculpture & architecture:** tượng đá phong hóa, hành lang cổ, cửa sổ, tường, bóng đổ, không gian trống.
4. **Nature & matter:** biển tối, địa chất, cây cối, bùn đất, rễ, đá, ánh sáng xuyên sương, chất liệu đời thực.
5. **Contemporary abstraction:** hình khối, nét khắc, bóng và khoảng trống; dùng có chủ đích, không giả làm "ảnh tác phẩm cổ".
6. **Original commissioned imagery:** ảnh minh họa mới, được tạo/biên tập riêng theo concept đã duyệt, giữ khác biệt với tranh thật.

**Tổ chức trên trang** (không phải mọi trang đều phải chứa tất cả):

| Khu vực | Tổ chức hình ảnh |
|---|---|
| Home | 1 **hero artwork** lớn có trọng tâm + một cụm 2–4 khung tác phẩm/khái niệm được giám tuyển; chuyển nhịp sang quote và Library |
| The Library index | Bố cục magazine: 1 thẻ ảnh lớn xen các thẻ văn bản, thumbnail có chủ đích ở danh mục. Không dùng 100% card chỉ chữ hoặc 100% bìa giả |
| Quote detail | 1 ảnh chủ đề khi phù hợp, đặt cạnh/trước/sau câu tùy độ dài. Khi không có ảnh đúng nghĩa, dùng type-only art direction chứ không bịa ảnh |
| The Mirror | Ảnh/cảnh riêng cho **mỗi chương hoặc ngã rẽ quan trọng**, chuyển cảnh trầm; không cần 1 ảnh cho mỗi nút chọn |
| Thinkers & Works | Chân dung/tác phẩm/ấn bản thật với nguồn và giấy phép; nếu không có ảnh hợp pháp, dùng artwork biểu trưng ghi rõ không phải chân dung thật |
| Essays | Ảnh mở đầu + các hình minh họa ở phần có luận điểm/giá trị thị giác, kèm caption có thông tin |
| About | Chân dung sơn dầu Hiyu đã được chọn và xử lý theo hai theme, không lặp ở mọi trang |

**Không bị khóa vào Gothic**. Gothic/vanitas là một nhánh phong cách, không phải bắt mọi câu về đạo đức, thiên nhiên, tình yêu, khoa học đều kèm đầu lâu, trăng, lâu đài. Phong cách riêng nằm ở **chất liệu, nhịp hình–chữ, ánh sáng, cấu trúc đối thoại**, không nằm ở 10 motif lặp lại.

### 3.7. Quy trình tạo và tuyển ảnh (editorial pipeline)

**Đầu ra mong muốn:** mỗi nội dung đủ điều kiện xuất bản có thể gắn 0–n asset; website có cơ chế tự hiển thị ảnh đã duyệt trên các trang phù hợp. Asset mới được tạo/giám tuyển **trong quy trình biên tập** bằng khả năng tạo ảnh sẵn có của agent khi môi trường có hỗ trợ, **không giả định trình duyệt web tự sinh ảnh tại runtime hoặc một công cụ tạo ảnh chắc chắn hiện hữu**.

1. **Brief tư tưởng**: xuất phát từ nội dung, lập 3–5 biểu tượng/chi tiết có thể chuyển hóa thành hình, đánh dấu motif đã dùng gần đây để tránh lặp.
2. **Chọn nguồn asset** theo thứ tự: ảnh gốc do chủ dự án sở hữu → tác phẩm public domain/CC0 có bằng chứng → ảnh mới tạo bằng công cụ sẵn có có quyền sử dụng phù hợp → artwork typography khi cần. Ảnh tạo tự động phải được người biên tập duyệt.
3. **Với ảnh thật/tác phẩm cổ:** tra cứu The Met Open Access, Art Institute of Chicago, Cleveland Museum of Art hoặc kho chính thức khác. Chỉ tải những asset có quyền dùng rõ ràng; metadata của cả bảo tàng không đồng nghĩa mọi ảnh đều CC0.
4. **Với hình sinh mới:** lập prompt theo brief (chủ thể, bố cục, ánh sáng, thời kỳ, bề mặt, palette, tỉ lệ, negative constraints), tạo nhiều phương án nếu có công cụ, chọn thủ công, đối chiếu lỗi hình thể và tính nhất quán. **Không tự nhận là tranh lịch sử hoặc gán tên họa sĩ thật cho ảnh sinh mới.**
5. **Biên tập sau tạo:** crop cho desktop/mobile, chỉnh vùng đặt chữ, xuất AVIF/WebP + nguồn gốc khi hợp lệ, tạo placeholder ảnh mờ, giữ file master ngoài public nếu cần.
6. **Duyệt quyền và thẩm mỹ:** kiểm nguồn, license, ghi công, motif đã lặp, có phục vụ nội dung không, có phù hợp hai mode không. Chỉ asset `APPROVED` được đưa vào publication manifest/asset manifest.
7. **Build:** dùng `<Picture />`/`<Image />` của Astro, kích thước và `sizes` hợp lý; preload duy nhất ảnh LCP quan trọng; lazy-load ảnh phụ. Nếu asset bị thiếu/không duyệt, fallback có chủ ý (không broken image).

Không được bỏ qua bước 2 bằng cách scrape ảnh Google Images/Threads/Pinterest rồi đưa lên site. Đó có thể là tư liệu tham khảo nghiên cứu, **không mặc định có quyền tái bản**.

**Nguồn ảnh mở ưu tiên:**

- The Met Open Access: https://www.metmuseum.org/hubs/open-access
- Art Institute of Chicago API: https://api.artic.edu/docs/
- Cleveland Museum of Art Open Access: https://www.clevelandart.org/open-access

### 3.8. Metadata ảnh & publication gate

Các file nguồn ở `website/assets/catalog/ART-xxxx.yaml` và file ảnh tại `website/assets/masters/` hoặc `website/public/images/` khi đã được phép. Hồ sơ website bổ sung này không thay thế hồ sơ `SRC/TXT` HYA-04.

```yaml
id: ART-0001
title: "Nội cảnh của một câu hỏi"
kind: GENERATED_ORIGINAL  # PUBLIC_DOMAIN_ARTWORK | LICENSED | OWNED | GENERATED_ORIGINAL
origin_url: null
creator_credit: "Hiyu Abyss"
license: "PROJECT_OWNED" # không được suy diễn nếu là ảnh bên thứ ba
rights_evidence: "internal-generation-record"
source_artwork_id: null
prompt_ref: "website/assets/briefs/ART-0001.md"
master_path: "website/assets/masters/ART-0001.png"
published_path: "website/public/images/ART-0001.webp"
alt_vi: "Một hành lang đá tối, ánh sáng rọi lên cánh cửa khép hờ."
focal_point: [0.52, 0.39]
topic_codes: []
related_content_ids: []
status: DRAFT  # DRAFT | IN_REVIEW | APPROVED | REJECTED
```

- Các giá trị trên là **minh họa schema**; tuyệt đối không xuất bản chính ví dụ này như asset đã được duyệt. `rights_evidence` cho ảnh sinh là nhật ký/quyền hợp đồng nếu có, không phải chứng minh pháp lý tuyệt đối; nếu không rõ quyền, cần rà soát.
- Metadata lưu **artwork gốc** tách biệt **file crop/biến thể** để không đánh mất provenance; nên có `original_artist`, `collection`, `accession`, `license_url`, `credit_line`, `retrieved_at` khi dùng tác phẩm bảo tàng.
- Cần build validator: không publish asset `DRAFT/REJECTED`, thiếu file, thiếu `alt_vi`, không có bằng chứng quyền dùng tối thiểu, hoặc không khớp ID nội dung public.
- **Những nguồn image reference chỉ dùng để tham khảo mỹ thuật không tự động được coi là nguồn ảnh thương mại hợp lệ**.

## 4. Sơ đồ thông tin và điều hướng

```text
/
├── /library                  # The Library: thư viện mở
│   ├── /library/:slug        # Trang đọc một nội dung
│   └── /library/random       # Một nội dung bất ngờ
├── /mirror                   # The Mirror: chọn hành trình
│   └── /mirror/:journey      # Trải nghiệm tương tác
├── /themes                   # Bản đồ chủ đề mở
│   └── /themes/:slug
├── /thinkers                 # Người viết, nhà tư tưởng
│   └── /thinkers/:slug
├── /works                    # Sách, tác phẩm, nghiên cứu
│   └── /works/:slug
├── /essays                   # Bài phân tích dài hơn
│   └── /essays/:slug
├── /search                   # Tìm kiếm toàn văn
└── /about                    # Tuyên ngôn & người sáng lập
```

**Navigation tối giản desktop:** `Library · Mirror · Explore · About · Search` + công tắc `Light/Dark` hiện diện. Trên mobile nút theme phải nằm trong top bar, không chôn trong submenu.

**Mobile:** menu gọn, truy cập Library/Mirror trong tối đa 1–2 lần chạm. Các phần `/thinkers`, `/works`, `/essays` là nhánh mở rộng theo mức độ dữ liệu đã chuẩn bị; không cần ép hiển thị trang rỗng ở MVP.

## 5. Trụ cột A — THE LIBRARY

### 5.1. Trang danh mục

- Bắt đầu bằng một **art-directed hero**: hình ảnh tuyển chọn + một câu nổi bật; ảnh không chèn chữ raster vào file. Không mở đầu bằng khẩu hiệu quảng cáo dài.
- Bố cục dạng **image-rich editorial library**: kết hợp những khung ảnh khổ lớn, những trích đoạn ngắn, mục lục và khoảng lặng. Không dùng duy nhất một dạng card đồng kích thước.
- Có tìm kiếm tiếng Việt, filter theo chủ đề, loại nội dung, tác giả/tác phẩm khi có dữ liệu; filter không ép vào một số nhóm cố định.
- Có `Surprise me` mở ngẫu nhiên một nội dung đã được xuất bản.
- Kết quả đọc liên quan dựa trên tag/khái niệm/nguồn đã có, không chỉ "câu đang thịnh hành".

### 5.2. Trang đọc một nội dung

Hiển thị: ảnh chủ đề **khi đã được tuyển chọn đúng nội dung** + văn bản chính → loại nội dung & ghi công chính xác → chủ đề → nội dung liên quan → truy nguồn (khi có) → chia sẻ/sao chép. Văn bản vẫn phải đọc đầy đủ nếu ảnh không tải.

Các `content_type` phải tôn trọng HYA-04:

| Mã chuẩn | Nhãn công khai |
|---|---|
| `DIRECT_QUOTE` | Trích dẫn đã xác minh |
| `PARAPHRASE` | Diễn giải tư tưởng |
| `INSPIRED_ORIGINAL` | Sáng tác lấy cảm hứng |
| `INDEPENDENT_ORIGINAL` | Sáng tác Hiyu Abyss |

- `DIRECT_QUOTE` chỉ xuất hiện dưới nhãn "đã xác minh" khi `evidence_status = VERIFIED_TEXT` và có định vị nguồn theo HYA-02.
- Luôn phân biệt ai là tác giả lời văn bản, tác giả tác phẩm nguồn, người dịch và người biên tập (nếu có).
- Không công khai ghi chú nghiên cứu thô, log truy cập, nhận xét nội bộ, điểm chất lượng nội bộ.

### 5.3. Nội dung có thể phát triển

Không chỉ "câu nói": triết ngôn, câu hỏi mở, đối thoại ngắn, mẩu suy tưởng, diễn giải luận điểm, bài luận nhỏ, và trang giới thiệu tác phẩm. Những dạng chưa có hồ sơ HYA-04 tương ứng phải được đặc tả ở lớp trình bày riêng; không sửa ngầm các enum của HYA-04.

## 6. Trụ cột B — THE MIRROR

### 6.1. Mục đích

The Mirror là **hành trình đọc tương tác**, không phải quiz đo tâm lý. Người dùng chọn một vấn đề hoặc câu hỏi; website dẫn tới những quan điểm khác nhau, kể cả phản đề và góc nhìn khiến người đọc xem xét lại câu trả lời ban đầu.

### 6.2. Cấu trúc một hành trình

```text
Enter → Question → Choice → Reflection → Counterpoint → Open Ending
```

- **Enter:** cảnh mở bằng artwork riêng và giới thiệu ngắn, không hù dọa/khẳng định sẽ "đọc vị bạn".
- **Question:** một câu hỏi nhiều cách hiểu.
- **Choice:** 2–4 lựa chọn như góc nhìn, không gán phân loại nhân cách.
- **Reflection:** một câu chữ hoặc lập luận liên quan đến lựa chọn, đi cùng ảnh/chi tiết thị giác nếu có ý nghĩa.
- **Counterpoint:** nêu phản đề, hoàn cảnh khiến góc nhìn trước không còn đủ.
- **Open Ending:** một câu hỏi để người đọc tự giữ lấy; liên kết qua Library / Works.

### 6.3. Một hành trình mẫu — "Sự thật và bình yên"

1. Hỏi: *Bạn muốn một sự thật làm mình bất an, hay một lời giải thích giúp mình yên lòng?*
2. Người đọc chọn một trong hai góc nhìn.
3. Website hiển thị đoạn suy tưởng đã được biên tập theo lựa chọn, không nói "Bạn là kiểu người...".
4. Tiếp theo hiển thị phản đề: *Có khi tìm sự thật là lòng can đảm; có khi cũng là một cách tự trừng phạt. Điều gì khiến hai hành vi khác nhau?*
5. Kết thúc bằng đường đọc mở về nhận thức, tự lừa dối, niềm tin, nỗi đau hoặc chủ đề liên quan.

Ví dụ chỉ để mô tả tương tác; không có nghĩa website chỉ xoay quanh chủ đề tâm lý.

### 6.4. Các mode có thể phát triển

| Mode | Mục đích | MVP? |
|---|---|---|
| `The Question` | Một câu hỏi, nhiều quan điểm | Có |
| `Two Sides` | Một luận đề và phản đề | Có |
| `The Passage` | Hành trình 4–6 chặng | Có (ít nội dung) |
| `The Contradiction` | Đặt hai câu tưởng đối lập cạnh nhau | Giai đoạn tiếp theo |
| `The Reflection Journal` | Người dùng tự viết ghi chú riêng, lưu trên máy | Giai đoạn tiếp theo |

Ở bản đầu, hành trình được **biên soạn trước và điều hướng ở client**. Cần luôn cho phép trở lại, bỏ qua, bắt đầu lại; không bắt người dùng đưa thông tin riêng tư.

### 6.5. Quy tắc an toàn, quyền riêng tư

- Không đưa ra chẩn đoán, kết luận về nhân cách, dự báo sức khỏe tâm thần hoặc giả định đau khổ của người dùng.
- Không tự lưu câu trả lời nhạy cảm lên máy chủ. Nếu có lưu nháp trên thiết bị, phải chủ động chọn và có cách xóa.
- Không ép người đọc tiếp tục khi chủ đề gây khó chịu; luôn có `Exit`/`Skip`.
- Không sử dụng các chiến thuật thao túng, gây lo âu hay tạo cảm giác agent biết bí mật người đọc.

## 7. Chủ đề — một ontology mở, không hardcode danh mục

Sử dụng mã `topic_codes` đang có ở HYA-01/HYA-04 làm điểm bắt đầu, nhưng xem chúng là **seed taxonomy**. Cho phép mở rộng sang các nhánh như: nghệ thuật, mỹ học, ký ức, thời gian, lịch sử, tri thức, khoa học, công nghệ, niềm tin, đạo đức, chính trị học dưới góc nhìn phân tích, văn chương, sự hữu hạn, tính phi lý, nghịch lý thường nhật, hy vọng, đức hạnh, sự cảm thông...

Mỗi chủ đề mới cần: `code`, `slug`, `title_vi`, `description`, `related_codes` và một nguyên tắc ranh giới (khi nào nên gắn tag này, khi nào không). Cập nhật tài liệu taxonomy chuẩn trước khi sử dụng mã mới, theo HYA-04.

UI không viết chết nút "Đạo đức giả / Bản ngã / Quyền lực". Nó tải danh mục từ metadata và chỉ hiện những chủ đề có nội dung công khai thực sự.

Mạng liên kết có thể dùng các quan hệ: `opposes`, `questions`, `extends`, `same_work`, `same_concept`, `related`, nhưng chỉ hiển thị khi được biên tập có căn cứ.

## 8. Nguồn dữ liệu và quy tắc xuất bản

HYA-04 đã quy định nơi lưu hồ sơ nội dung chuẩn. HYA-07 bổ sung hồ sơ **ảnh** riêng trong `website/assets/catalog/`, không nhân đôi nội dung TXT:

```text
knowledge/sources/SRC-xxxx.md
knowledge/notes/NOTE-xxxx.md
knowledge/concepts/CON-xxxx.md
editorial/ideas/IDEA-xxxx.md
editorial/content/TXT-xxxx.md
```

**Không tạo kho nội dung chuẩn thứ hai chỉ dành cho website.** Xây một lớp xuất bản (build adapter) đọc nội dung gốc đã duyệt rồi sinh ra trang web tĩnh.

Để tránh hiểu nhầm `APPROVED = tự động công khai`, đề xuất **file danh sách cho phép xuất bản** riêng do chủ dự án kiểm soát:

```yaml
# website/publication-manifest.yaml
public_content_ids:
  - TXT-0001
featured_content_ids:
  - TXT-0001
public_journey_ids:
  - MIR-0001
public_artwork_ids: []   # chỉ bổ sung ID ART-xxxx đã duyệt
```

**Quy tắc build:** chỉ xuất bản nội dung `TXT` khi ID có trong manifest VÀ `status` thuộc `APPROVED`/`PUBLISHED`, đồng thời không vi phạm quy tắc nguồn. Các ảnh tham chiếu bởi nội dung public cũng phải qua gate asset `APPROVED` và quyền sử dụng có bằng chứng. Một ID `DRAFT`, `IN_REVIEW`, `NEEDS_SOURCE`, `REJECTED`, `ARCHIVED` không được lên web dù xuất hiện nhầm trong manifest; build phải fail hoặc cảnh báo rõ. Sau khi triển khai thành công và được xác nhận, trạng thái `PUBLISHED` có thể được cập nhật theo HYA-04, không suy đoán trước.

Nguồn được đưa ra trang công khai với metadata lọc: chỉ nhan đề, tác giả, ấn bản/định vị nguồn kiểm chứng, URL công khai phù hợp, thông tin dịch/ghi công. Không vô tình đưa cả nhật ký nghiên cứu, private note hay bản sách có bản quyền vào gói client.

## 9. Hồ sơ riêng cho Mirror Journey

Đây là lớp sản phẩm web bổ sung, không thay thế `TXT`/`IDEA`/`CON` của HYA-04. Mỗi journey là file Markdown/YAML thuộc `website/journeys/`, có ID `MIR-xxxx` và liên kết tới TXT/CON/IDEA đã tồn tại.

```yaml
id: MIR-0001
title: "Sự thật và bình yên"
slug: "su-that-va-binh-yen"
status: DRAFT
topic_codes: [TRUTH, SELF_DECEPTION]
related_content_ids: [TXT-0001]
intro: "Một câu hỏi không có đáp án tiện lợi."
steps:
  - id: Q1
    type: QUESTION
    text: "Bạn mong được an ủi hay được nói thật?"
    options:
      - id: A
        text: "Được an ủi"
        next: R1
      - id: B
        text: "Được nói thật"
        next: R2
  - id: R1
    type: REFLECTION
    text: "Một đoạn phản tư do người biên tập viết."
    next: END
  - id: R2
    type: REFLECTION
    text: "Một đoạn phản tư khác, không phán xét người chọn."
    next: END
  - id: END
    type: ENDING
    text: "Câu hỏi còn mở."
```

Đây là **ví dụ hợp đồng**, không phải dữ liệu nội dung đã được duyệt. Khi xây, schema phải kiểm `id` duy nhất, `next` trỏ tới step tồn tại, mọi đường đi kết thúc hoặc có nút thoát, không tạo vòng lặp vô tận, không còn đường nhánh mồ côi. `status` của journey là quy tắc riêng của website, phải có duyệt rõ ràng trước khi thêm vào manifest.

## 10. Kiến trúc triển khai đề xuất

### 10.1. Quyết định công nghệ: Astro (không phải Next.js cho phiên bản hiện tại)

- **Astro**: lựa chọn chốt cho website xuất bản nội dung và triển lãm ảnh; Content Collections + `glob` loader đọc dữ liệu Markdown qua build adapter (không tái tạo kho chuẩn), dùng `<Image />`/`<Picture />` tối ưu ảnh.
- **TypeScript**: schema, publication pipeline, theme management và validation. **React Islands** chỉ dành cho các phần thực sự giàu tương tác như Mirror, gallery/lightbox có state; phần còn lại Astro/HTML tĩnh.
- **Pagefind**: chỉ mục tìm kiếm nội dung HTML tĩnh sau build; hỗ trợ filter/metadata.
- **GitHub + Git**: phiên bản nội dung, code và lịch sử phê duyệt.
- **Static hosting**: triển khai thông qua dịch vụ hỗ trợ Git, ví dụ Cloudflare Pages hoặc tương đương, tùy hạ tầng hiện có.

**Vì sao không chọn Next.js trước:** Next.js mạnh với server rendering linh hoạt và ứng dụng React đầy đủ (tài khoản, dashboard, dữ liệu người dùng thời gian thực). Với Hiyu Abyss hiện tại, nội dung tĩnh có kiểm duyệt chiếm trọng tâm; Astro giúp giảm JS/client surface và cho phép dùng React ở Mirror mà không bắt mọi trang thành ứng dụng React. **Nhiều ảnh không đòi Next.js:** Astro cũng có pipeline responsive image. Chỉ xem xét Next.js sau khi nhu cầu app thực tế vượt các islands (ví dụ hồ sơ đồng bộ, cộng đồng tương tác, cá nhân hóa đăng nhập, API thời gian thực).

Website runtime không cần agent để chọn câu phản tư hoặc sinh ảnh tại mỗi lượt xem. Agent Antigravity dùng khi *nghiên cứu, biên tập, giám tuyển/tạo artwork và cập nhật kho*, còn nội dung người đọc thấy là kết quả đã được duyệt.

### 10.2. Cấu trúc thư mục bổ sung (không thay HYA-04)

```text
hiyu-abyss/
├── docs/                              # HYA-01..HYA-07
├── knowledge/                         # Theo HYA-04
├── editorial/                         # Theo HYA-04
├── .agents/skills/                     # Theo HYA-05
└── website/
    ├── package.json
    ├── astro.config.mjs
    ├── publication-manifest.yaml
    ├── journeys/MIR-0001.yaml
    ├── assets/
    │   ├── briefs/                    # Art direction / prompt briefs
    │   ├── catalog/                   # ART-xxxx.yaml, quyền & nguồn
    │   └── masters/                   # Source master, không mặc định public
    ├── public/
    │   └── images/                    # Chỉ file ảnh đã duyệt, tối ưu
    ├── src/
    │   ├── components/
    │   │   ├── ArtworkFrame.astro
    │   │   ├── EditorialMosaic.astro
    │   │   ├── ThemeToggle.ts
    │   │   ├── QuoteCard.astro
    │   │   ├── SourceAttribution.astro
    │   │   ├── SearchPanel.astro
    │   │   └── MirrorJourney.tsx       # React island
    │   ├── layouts/
    │   ├── pages/
    │   ├── styles/tokens.css          # Dark + Light palettes
    │   ├── lib/content-publisher.ts
    │   ├── lib/artwork-publisher.ts
    │   ├── lib/journey-validator.ts
    │   └── generated/                 # Sinh tự động, không sửa tay
    └── tests/
        ├── content-publication.test.ts
        ├── artwork-publication.test.ts
        ├── theme-contrast.test.ts
        ├── mirror-journey.test.ts
        └── navigation.test.ts
```

Không bắt buộc React cho mọi thao tác. Tương tác Mirror có thể dùng React island; theme toggle đủ nhẹ để dùng JS thuần. Ưu tiên giảm JS và ổn định layout khi ảnh tải.

### 10.3. Hiệu năng và accessibility

- Responsive 320px đến desktop; không tràn chữ khi dùng tiếng Việt có dấu.
- Font có dự phòng và kiểm hỗ trợ Unicode Vietnamese.
- Có focus keyboard, label dễ hiểu, tương phản đủ và trạng thái hover/focus.
- `prefers-reduced-motion` phải vô hiệu các animation không thiết yếu.
- Nội dung chính server/static rendered để đọc được khi JavaScript bị tắt; riêng phần tương tác Mirror có hướng dẫn fallback.
- Metadata social share, canonical URL, sitemap, robots và OpenGraph cho từng trang public.
- Ảnh hero rõ kích thước và crop mobile; responsive `srcset`/`sizes`, AVIF/WebP khi phù hợp, lazy-load ảnh phụ, tránh layout shift. Không tải bản master nhiều MB cho ảnh thumbnail.
- Kiểm tra accessibility trên **cả dark và light**: độ tương phản text/control, focus rõ, alt ảnh có nội dung; art trang trí có alt rỗng nếu đúng vai trò.
- Giao diện vẫn đủ ý nghĩa với ảnh bị tắt/không tải; content layout không được sụp vì phụ thuộc vào ảnh.

## 11. User flows chủ đạo

### 11.1. Người đến từ TikTok

`Share link → /library/:slug → đọc ngay → xem chú thích nguồn → đọc liên quan → The Mirror (nếu muốn)`.

### 11.2. Người muốn khám phá

`/ → Library → filter/search → một nội dung → một chủ đề → nhà tư tưởng/tác phẩm → quay lại nội dung`.

### 11.3. Người muốn phản tư

`/ → Mirror → chọn hành trình → chọn góc nhìn → đọc phản đề → kết thúc mở → đọc thêm trong Library`.

## 12. Kế hoạch phiên bản

| Giai đoạn | Mục tiêu | Chức năng |
|---|---|---|
| `P0 — Foundation` | Đọc đẹp và nội dung công khai an toàn | **Dark + Light**, theme toggle, image-rich landing, artwork manifest/gate, Library list/detail, metadata, mobile |
| `P1 — Discovery` | Tìm được nội dung theo nhiều đường | Search + filters, random, theme pages, editorial imagery cho listing, trang nguồn/thinkers/works khi có hồ sơ duyệt |
| `P2 — Mirror` | Trải nghiệm tương tác bản đầu | 2–3 journey đã biên tập, mỗi journey có visual direction/ảnh mở phù hợp, choice/reflection/counterpoint/end, route validation, exit/restart |
| `P3 — Depth` | Mở rộng và cá nhân hóa có chừng mực | Essays giàu hình/ảnh có nguồn, gallery biên tập, journey khác, lưu dấu trang local, các liên kết ý tưởng sâu hơn |

Các cột mốc thể hiện thứ tự ưu tiên chứ không phải hứa về thời gian. Có thể triển khai P0–P2 trong cùng một đợt nếu nguồn lực cho phép; không công bố trang Mirror trống.

## 13. Tiêu chí nghiệm thu bắt buộc

1. **Dark & Light** hoạt động trên tất cả route, cùng một bố cục chất lượng; dark là mặc định. Theme đổi trực tiếp, giữ lựa chọn khi reload, không gây nháy nền trắng, không làm méo ảnh.
2. Cặp token và các component thật đạt **WCAG AA** về tương phản chữ; focus/control quan trọng phân biệt đủ rõ. Kiểm ở viewport 320px, 375px, 768px và desktop; kiểm dấu tiếng Việt.
3. **Không template AI đại trà**: không gradient tím/xanh, glassmorphism, card dashboard hàng loạt, bề mặt gold lấp lánh, motif đầu lâu/castle lạm dụng. Bố cục có nhịp editorial và khoảng trắng.
4. Home có **ít nhất một hero artwork được cấp quyền + một cụm ảnh giám tuyển có lý do**; Library kết hợp ảnh và chữ, không chỉ đăng quote thành grid chữ; The Mirror có ít nhất ảnh/cảnh mở cho hai journey. Tất cả ảnh phải phục vụ ý nghĩa, không nhồi ảnh cho đủ số.
5. Có `ART` schema, catalog, duyệt quyền, duyệt mỹ thuật và `publication-manifest` tách biệt với nội dung nguồn. Không xuất bản ảnh chưa duyệt hoặc thiếu quyền sử dụng.
6. Nội dung chủ đề là hệ mở; thêm topic hợp lệ mới không cần sửa UI danh mục thủ công.
7. Chỉ nội dung được chủ dự án duyệt và cho phép xuất bản mới xuất hiện công khai; tuyệt đối không lộ nghiên cứu nội bộ.
8. Trích dẫn phải có nhãn và nguồn đúng trạng thái kiểm chứng; hình tác phẩm/thư viện phải ghi công phù hợp, không gán tranh AI thành tranh bảo tàng.
9. The Library có danh mục, trang riêng, tìm kiếm/liên quan, share; The Mirror có ít nhất hai journey rẽ nhánh có phản đề, kết thúc, thoát và bắt đầu lại.
10. Có kiểm thử cho nội dung/asset gate, image fallback, theme persistence, route journey, link, source attribution; chạy `build` thực tế và không báo đạt khi chưa kiểm.
11. Ảnh hero/LCP tối ưu, ảnh ngoài màn hình tải trễ, không kéo ảnh khổng lồ vào gallery, không gây layout shift nghiêm trọng. Nội dung đọc được nếu ảnh không tải.
12. Agent báo cáo rõ những artwork đã thật sự tạo/tuyển chọn/cấp quyền, thành phần đã test, và thứ **chưa thể tạo do thiếu công cụ/quyền**; không biến placeholder thành sản phẩm hoàn chỉnh.

## 14. Nhiệm vụ giao Antigravity

> Đọc HYA-01..HYA-06 để nắm chuẩn nội dung/nguồn và HYA-07 v2.0 để triển khai website Hiyu Abyss. **Chọn Astro + TypeScript + React Islands**. Xây cả The Library và The Mirror với hai theme nhất quán: **Black Archive (Dark mặc định)** và **Pale Archive (Light)**; nút đổi theme hoạt động, lưu lựa chọn, không FOUC. Dùng palette/tokens/mood/typography đã chốt, tránh giao diện AI/template đại trà. Website phải **giàu ảnh**: hero artwork, editorial mosaic, ảnh trong Library, cảnh mở cho Mirror; chọn ảnh public-domain có bằng chứng hoặc tạo ảnh mới bằng công cụ sẵn có khi môi trường có hỗ trợ, tất cả qua quyền sử dụng và duyệt ảnh. Không tự nhận ảnh sinh là tác phẩm lịch sử. Chủ đề mở; data Markdown và publication gates theo HYA-04/HYA-07; không lộ hồ sơ nội bộ. Thực hiện P0/P1 rồi Mirror P2, có build/test và báo cáo evidence; nếu thiếu công cụ tạo ảnh, vẫn triển khai pipeline, asset catalog và một tập artwork hợp pháp/placeholder có ghi rõ trạng thái, không nói đã tạo ảnh khi chưa có.

## 15. Nguồn kỹ thuật / mỹ thuật tham khảo

- Astro Content Collections: https://docs.astro.build/en/guides/content-collections/
- Astro Islands architecture: https://docs.astro.build/en/concepts/islands/
- Astro images (`<Image />`, `<Picture />`): https://docs.astro.build/en/guides/images/
- React in Astro: https://docs.astro.build/en/guides/integrations-guide/react/
- Next.js App Router (để đối chiếu khi quy mô đổi): https://nextjs.org/docs/app
- Pagefind: https://pagefind.app/
- Cloudflare Pages: https://developers.cloudflare.com/pages/get-started/git-integration/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- The Met Open Access: https://www.metmuseum.org/hubs/open-access
- Art Institute of Chicago image docs: https://api.artic.edu/docs/
- Cleveland Museum of Art Open Access: https://www.clevelandart.org/open-access

Tài liệu kỹ thuật có thể đổi theo package version; khi triển khai phải đối chiếu phiên bản Astro/React/Image thực tế. Các nguồn mỹ thuật là **kho tra cứu**, không có nghĩa mọi bức ảnh đều được phép xuất bản; kiểm từng asset.

---

**Kết luận thiết kế v2.0:** Hiyu Abyss là một vũ trụ tri thức không bị giới hạn chủ đề, đồng thời là **một ấn phẩm có trí nhớ hình ảnh**: một thế giới sâu thẳm khi tắt đèn và một thế giới sáng rõ như trang giấy lưu trữ khi bật đèn. Không biến nó thành tường chữ, dashboard AI hay cuộc triển lãm hình ảnh vô căn cứ.
