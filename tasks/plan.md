# Kế Hoạch Triển Khai: Tái Thiết Toàn Diện Mỹ Học Bảo Tàng & Trải Nghiệm Đắm Chìm (Hiyu Abyss V3.1)

> **Căn cứ:** Bản Tuyên Bố Chủ Đích đã xác nhận ngày 15/11/2026.  
> **Mục tiêu:** Thoát khỏi cảm giác "web sơ sài" dạng blog phẳng; kiến tạo một **Bảo Tàng Số Sống Động về Tâm Lý Học Đen & Mỹ Học Cổ Điển (The Living Museum of Dark Psychology)**.  
> **Quy chuẩn tuân thủ:** `HYA-01` (Bản sắc), `HYA-02` (Chuẩn nguồn), `HYA-03` (Văn phong sắc bén), `HYA-08` (Mỹ thuật sơn dầu thuần túy, sạch tì vết AI).

---

## 1. Tổng Quan Kiến Trúc & Quyết Định Thiết Kế

1. **Header Tinh Gọn & Đa Ngữ (Lean Header & Bilingual Switcher):**
   - Thu nhỏ chiều cao Floating Header từ `h-16/20` xuống `h-12/14`, giảm padding, tạo cảm giác thanh mảnh như gờ viền kim loại đồng hồ cao cấp.
   - Thêm nút chuyển đổi ngôn ngữ `[VI | EN]` với từ điển giao diện `i18n.ts`.
   - Bổ sung nút trigger **"Kho Lưu Trữ"** kèm Badge số đếm tác phẩm đã lưu.
2. **Kho Lưu Trữ Cá Nhân (Saved Drawer):**
   - Xây dựng Drawer trượt từ cạnh phải màn hình hiển thị toàn bộ danh sách các tác phẩm người dùng đã đánh dấu trong `localStorage['hiyu_saved_quotes']`.
   - Cung cấp tính năng xem nhanh, điều hướng tới bài đọc sâu, và xóa khỏi kho lưu trữ.
3. **Nút "Lên Đầu Trang" (Floating Widget FAB):**
   - Tách khỏi footer; trở thành Floating Action Widget nằm cố định ở góc dưới phải (`fixed bottom-6 right-6 z-40`), có hiệu ứng fade-in mượt khi cuộn xuống quá 300px và smooth scroll lên đỉnh trang.
4. **Footer Tinh Giản & Thuần Việt:**
   - Xóa bỏ hoàn toàn cột "Minh bạch xuất xứ" theo đúng yêu cầu người dùng.
   - Bỏ toàn bộ các ngoặc đơn dịch ngữ `(Thư Viện)`, `(Chiếc Gương)`, chỉ giữ tiếng Việt chuẩn mực: `Thư Viện`, `Chiếc Gương`, `Chủ Đề`, `Tìm Kiếm`.
5. **Hero Giám Tuyển Độc Bản (Curated Masterpiece):**
   - Không gán cứng `TXT-0001` làm Hero. Thiết kế cơ chế giám tuyển tác phẩm tiêu biểu (Curated Masterpiece) hoặc luân phiên trong ngày.
   - Tách bạch cấu trúc Tiêu đề và Trích dẫn, xóa bỏ hiện tượng lặp lại nguyên văn giữa Headline và Blockquote.
6. **Custom Dropdown Tìm Kiếm (Khắc phục lỗi xổ lên trên):**
   - Thay thế thẻ `<select>` nguyên thủy của trình duyệt bằng Custom Dropdown có vị trí tuyệt đối (`top-full mt-1.5 z-30`), bảo đảm luôn mở hướng xuống dưới và đồng bộ mỹ học bảo tàng.
7. **Trang Chi Tiết Sâu Sắc & Chế Độ Thưởng Lãm (Exhibition Lightbox):**
   - Tẩy bỏ câu "Phản đề tự soi chiếu" cố định đại trà; cá thể hóa nội dung chiêm nghiệm cho từng tác phẩm.
   - Bổ sung chế độ **Thưởng Lãm Bảo Tàng Toàn Màn Hình (Exhibition Lightbox)** giúp người xem chiêm ngưỡng cận cảnh từng nét cọ sơn dầu cổ điển.
8. **Thiết Kế Lại Logo Monogram Ẩn Ý Hiện Đại:**
   - Thay thế biểu tượng hình thoi chữ H bằng Monogram tối giản mang chiều sâu vực thẳm và sự phản chiếu vô tận (Abyss & Mirror).

---

## 2. Danh Sách Nhiệm Vụ Triển Khai (Task Breakdown)

### Phase 1: Nền Tảng Giao Diện, Header, Ngôn Ngữ & Kho Lưu Trữ
- **Task 1:** Header Thanh Mảnh (`h-13/14`), Logo Monogram Ẩn Ý & Nút Gạt Ngôn Ngữ `[VI | EN]`
- **Task 2:** Xây Dựng Ngăn Kéo "Kho Lưu Trữ Cá Nhân" (Saved Drawer) & Quản Lý Bookmark
- **Task 3:** Floating Widget "Lên Đầu Trang" (FAB) & Tinh Giản Footer Thuần Việt

### ❖ Checkpoint 1: Header, Navigation & Saved Flow
- [ ] Header thanh thoát, không che khuất nội dung khi cuộn.
- [ ] Nút chuyển ngữ VI/EN hoạt động mượt mà.
- [ ] Nhấn "Lưu Chiêm Nghiệm" lập tức cập nhật Badge và hiển thị trong Saved Drawer.
- [ ] Floating Widget xuất hiện khi cuộn và cuộn mượt lên đỉnh. Footer sạch sẽ, thuần Việt.

---

### Phase 2: Chiều Sâu Giám Tuyển, Trải Nghiệm Thưởng Lãm & Khắc Phục Lỗi Tương Tác
- **Task 4:** Tái Thiết Section Hero: Giám Tuyển Linh Hoạt & Khử Trùng Lặp Headline/Quote
- **Task 5:** Xây Dựng Custom Dropdown Tìm Kiếm (Bảo Đảm Luôn Mở Hướng Xuống Dưới)
- **Task 6:** Nâng Cấp Chiều Sâu Trang Chi Tiết & Chế Độ Thưởng Lãm Toàn Cảnh (Exhibition Lightbox)

### ❖ Checkpoint 2: Editorial & Interactive Depth
- [ ] Hero không còn gán cứng tác phẩm 1, không còn lặp từ.
- [ ] Dropdown bộ lọc mở hướng xuống dưới 100%, không bị che lấp.
- [ ] Trang chi tiết có bóc tách tâm lý riêng biệt, bấm xem ảnh toàn màn hình với placard bảo tàng.

---

### Phase 3: Chuẩn Hóa SEO, Metadata & Kiểm Thử Toàn Diện
- **Task 7:** Chuẩn Hóa SEO Toàn Diện, Schema.org & Kiểm Thử Tĩnh 127 Trang

### ❖ Checkpoint 3: Complete & Production Ready
- [ ] 127 trang tĩnh build thành công trong thời gian < 3s.
- [ ] 100% kiểm thử trong `website/test/verify-build.js` vượt qua.
- [ ] Không có lỗi console hay đụng chạm file ảnh catalog.

---

## 3. Bảng Đánh Giá Rủi Ro & Biện Pháp Kiểm Soát

| Rủi ro kỹ thuật | Mức độ | Biện pháp kiểm soát |
|---|---|---|
| Đụng chạm tiến trình sinh ảnh của bên ngoài | Cao | Tuyệt đối không chạm vào `website/src/data/asset-catalog.json` hay thư mục ảnh nguồn `assets/templates/`. |
| Giao diện đa ngữ gây phình to mã tĩnh | Thấp | Sử dụng Client-side dictionary siêu nhẹ kết hợp data attributes để chuyển đổi tức thì không cần tải lại trang. |
| Drawer chiếm nhiều bộ nhớ trình duyệt | Thấp | Chỉ lưu mảng các ID (`["TXT-0001", ...]`) trong `localStorage`, hydrate dữ liệu từ search index có sẵn. |
