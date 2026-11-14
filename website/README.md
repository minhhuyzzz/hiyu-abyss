# Hiyu Abyss — Thư Viện Nghệ Thuật Sống & Hệ Thống Xuất Bản (v2.0)

> **Tuyên ngôn tư duy:** *Xây dựng một Thư viện Nghệ thuật có Hệ thống Xuất bản Đáng tin cậy.*  
> **Căn cứ quy chuẩn:** Tuân thủ triết lý và kiến trúc `HYA-01` $\rightarrow$ `HYA-07`.

---

## 1. Tổng Quan Kiến Trúc

Hiyu Abyss Website được phát triển theo kiến trúc **Static-First với Astro v5**, kết hợp **React 19 Islands** cho trụ cột chiêm nghiệm tương tác *The Mirror*, và hệ thống phân phối tĩnh (zero-latency static publishing) cho 100 tác phẩm triết ngôn, danh ngôn tâm lý học cùng các bộ kiệt tác hội họa bảo tàng cổ điển.

- **Framework:** [Astro v5](https://astro.build/) (`output: "static"`).
- **Styling:** Tailwind CSS v3 + Hệ thống CSS Tokens `tokens.css` chuẩn bảo tàng.
- **Dual-Theme:** 
  - *Black Archive (Mặc định):* Nền đen mực muội Lampblack `#090A09`, chữ kem lụa `#EAE5DA`, điểm xuyết đồng thau cổ `#C29A77` và gỉ sắt Chiaroscuro `#B47862`.
  - *Pale Archive:* Nền giấy ngà Bone Paper `#ECE9E1`, chữ mực nâu sẫm `#24251F`, điểm xuyết hạt dẻ chín `#76513D` và đất sét nung `#8A4D43`.
  - **Zero-FOUC:** Inline boot script trong `<head>` chặn hoàn toàn hiện tượng nháy trắng khi tải trang.
- **Hệ Thống 3 Tầng Typography:**
  - *Brand & Display:* **Cormorant Garamond** (serif cổ điển trang trọng).
  - *Quotes & Body:* **Literata** (serif đọc chuyên dụng được tối ưu cho văn bản triết luận).
  - *UI & Metadata:* **Be Vietnam Pro** (sans-serif hình học rõ ràng, tối ưu hiển thị dấu thanh tiếng Việt).
- **Trụ Cột The Mirror:** React 19 Interactive Island tĩnh lặng, hỗ trợ rẽ nhánh tư tưởng, bảo mật 100% client-side không lưu trữ hay gửi dữ liệu cá nhân lên máy chủ.
- **Tìm Kiếm Toàn Văn:** Tra cứu tức thì tiếng Việt (bỏ dấu thông minh) không độ trễ, lọc đa chiều theo chủ đề và phân loại tác phẩm.

---

## 2. Cổng Kiểm Duyệt Xuất Bản (2-Layer Security Gating)

Để ngăn chặn tuyệt đối việc rò rỉ bản thảo chưa hoàn thiện (`DRAFT`) hoặc ghi chú nghiên cứu nội bộ, hệ thống áp dụng cơ chế bảo vệ 2 lớp tại `src/lib/content-publisher.ts`:

1. **Lớp 1 — Publication Manifest (`website/publication-manifest.yaml`):** Chỉ những ID nằm trong danh sách `public_content_ids`, `public_journey_ids` mới được đưa vào hàng đợi nạp.
2. **Lớp 2 — Trạng thái Frontmatter:** Tác phẩm bắt buộc phải có `status: APPROVED` hoặc `status: PUBLISHED` trong tệp Markdown gốc tại `editorial/content/`.

Dữ liệu nội bộ (điểm số đánh giá 6 chiều, log phê duyệt, từ khóa nội bộ) được thanh lọc hoàn toàn trước khi tạo trang HTML công khai.

---

## 3. Cấu Trúc Tuyến Đường (Static Routes)

Tổng cộng **126 trang HTML tĩnh** được sinh ra sẵn trong thư mục `dist/`:

| Tuyến đường | Mục đích | Số lượng |
|---|---|---|
| `/` | Trang chủ Art-Directed Hero, Tuyên ngôn & Editorial Mosaic | 1 |
| `/library` | Danh mục toàn bộ 100 tác phẩm, dynamic taxonomy filter & *Surprise Me* | 1 |
| `/library/txt-0001` $\rightarrow$ `/library/txt-0100` | Trang chi tiết tác phẩm, tranh bảo tàng đa góc nhìn, trích dẫn & sao chép | 100 |
| `/mirror` | Cổng giới thiệu không gian The Mirror | 1 |
| `/mirror/su-that-va-binh-yen` | Hành trình chiêm nghiệm 5 chặng `MIR-0001` (React Island) | 1 |
| `/themes` | Bản đồ toàn bộ 20 dòng tư tưởng mở | 1 |
| `/themes/[slug]` | 20 trang chuyên đề (Đạo đức giả, Bản ngã, Sự thật, Quyền lực, Cô độc...) | 20 |
| `/search` | Tìm kiếm toàn văn tiếng Việt có gợi ý từ khóa | 1 |

---

## 4. Kiểm Thử Chất Lượng & Chuẩn Tiếp Cận (WCAG AA)

Hệ thống tích hợp bộ kiểm thử tự động tại `test/verify-build.js`:

```bash
cd website
npm run build
node test/verify-build.js
```

**Kết quả kiểm định:**
- **Tương phản màu WCAG AA:**
  - Black Archive Text: **15.79:1** (Vượt xa chuẩn tối thiểu 4.5:1).
  - Pale Archive Text: **12.73:1** (Vượt xa chuẩn tối thiểu 4.5:1).
  - Accent / Large Text: **7.73:1** (Đạt chuẩn Large Text 3.0:1).
- **Toàn vẹn tuyến đường:** 126/126 trang tĩnh và toàn bộ ảnh tranh bảo tàng `theme_01` $\rightarrow$ `theme_60` tồn tại đầy đủ.
- **Đa thiết bị:** Chuẩn hóa Touch targets $\ge 44\times 44\text{px}$, `safe-area-inset` cho iPhone/Android tai thỏ và responsive co giãn từ 320px đến màn hình 4K.

---

## 5. Hướng Dẫn Triển Khai Hosting (Deployment Guide)

### Cách 1: Triển khai lên Cloudflare Pages (Khuyên dùng - Nhanh nhất)
1. Kết nối kho lưu trữ GitHub `hiyuabyss`.
2. Tạo dự án mới trong **Cloudflare Pages**.
3. Cấu hình Build Settings:
   - **Framework preset:** `Astro`
   - **Root directory:** `website`
   - **Build command:** `npm run build`
   - **Build output directory:** `dist`
4. Bấm **Save and Deploy**. Toàn bộ 126 trang sẽ được phân phối tức thì trên mạng lưới CDN toàn cầu của Cloudflare với thời gian phản hồi < 50ms.

### Cách 2: Triển khai lên Vercel
1. Import kho lưu trữ GitHub vào **Vercel Dashboard**.
2. Chọn Root Directory là `website`.
3. Vercel sẽ tự động nhận diện Astro và thiết lập:
   - **Build Command:** `astro build`
   - **Output Directory:** `dist`
4. Bấm **Deploy**.

### Cách 3: Chạy Kiểm Thử Cục Bộ
```bash
cd website
npm run dev      # Khởi chạy máy chủ phát triển tại http://localhost:4321
npm run build    # Biên dịch tĩnh production ra thư mục dist/
npm run preview  # Xem thử bản build tĩnh tại http://localhost:4321
```
