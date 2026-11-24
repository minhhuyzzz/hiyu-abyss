# Bản Tuyên Bố Mục Đích (Statement of Intent): Tối Ưu Hóa Ảnh Siêu Tốc Bằng Edge WebP Proxy

> **Mã hồ sơ:** `INTENT-IMG-01`  
> **Ngày phê duyệt:** 2026-11-24  
> **Trạng thái:** ĐÃ XÁC NHẬN (CONFIRMED)

---

## 1. Bản sắc & Mục đích cốt lõi
- **Outcome:** Tối ưu hóa toàn bộ ảnh đại diện thẻ bên ngoài (`/library`, `/themes`, `/saved`, `/search`, `SavedDrawer`) thông qua Edge WebP Proxy (`wsrv.nl` chạy trên mạng lưới Cloudflare CDN toàn cầu), tự động nén và resize ảnh từ **~900KB xuống còn ~22KB/ảnh** (giảm 97.5% lưu lượng tải mạng).
- **User:** Độc giả lướt xem thư viện trên điện thoại hoặc mạng 4G/Wifi yếu, cuộn trang mượt mà không bị nghẽn mạng hay ngốn data.
- **Why now:** Kho tác phẩm hiện đã đạt 300+ triết ngôn (~1.2GB ảnh sơn dầu), tải trực tiếp file gốc JPEG 900KB ở trang danh sách làm chậm trải nghiệm duyệt web.
- **Success:** Thẻ bên ngoài hiển thị ảnh vuông WebP sắc nét 400x400 ~22KB tải trong chớp mắt; trang xem chi tiết bên trong (`/library/[slug]`) vẫn giữ nguyên bộ tranh sơn dầu Full HD 1080x1920; có cơ chế fallback tự động về ảnh gốc nếu proxy có sự cố.
- **Constraint:** Không làm tăng dung lượng lưu trữ của repository GitHub (không cần lưu thêm hàng nghìn file thumbnail vào Git).
- **Out of scope:** Không can thiệp hay làm giảm độ phân giải của các slide tranh sơn dầu gốc bên trong trang chi tiết.

---

## 2. Kiến trúc giải pháp (Edge Image Architecture)

### 2.1 Cơ chế phân tầng ảnh (Two-Tier Image Strategy)
1. **Tier 1 (Danh mục & Thẻ bài bên ngoài):**
   - Kích thước: `400x400` pixel vuông (`aspect-square`), định dạng WebP, chất lượng `q=75`.
   - Dung lượng trung bình: `~20 - 25 KB`.
   - Định tuyến qua Edge Proxy: `https://wsrv.nl/?url=https://hiyuabyss.vercel.app{path}&w=400&h=400&fit=cover&output=webp&q=75`.
   - Fallback: Nếu Edge Proxy gián đoạn, `onerror` tự động load trực tiếp đường dẫn gốc `artSrc`.
2. **Tier 2 (Chiêm nghiệm chi tiết bên trong `/library/[slug]`):**
   - Giữ nguyên ảnh gốc chất lượng cao Full HD (`1080x1920`) để bảo toàn hiệu ứng cọ sơn dầu, thớ vải toan và độ sâu bảo tàng theo tiêu chuẩn `HYA-08`.

---

## 3. Các điểm triển khai trong Codebase
- Helper tập trung: `website/src/lib/image-optimizer.ts`
- Thẻ thư viện: `website/src/components/QuoteCard.astro`
- Danh sách thư viện: `website/src/pages/library/index.astro`
- Danh mục chủ đề: `website/src/pages/themes/[slug].astro`
- Kho lưu trữ: `website/src/pages/saved.astro` & `website/src/components/SavedDrawer.astro`
- Tìm kiếm: `website/src/pages/search.astro`
