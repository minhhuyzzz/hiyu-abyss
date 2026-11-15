# Danh Sách Nhiệm Vụ: Tái Thiết Toàn Diện Hiyu Abyss V3.1 (The Living Museum)

> **Cương lĩnh kiến trúc:** [tasks/plan.md](file:///c:/hiyuabyss/tasks/plan.md)  
> **Căn cứ pháp quy:** `HYA-01` $\rightarrow$ `HYA-08`  
> **Mục tiêu:** Chuyển hóa toàn diện sang phong cách Bảo Tàng Số, khắc phục dứt điểm 8 lỗi giao diện đã ghi nhận.

---

## Phase 1: Nền Tảng Giao Diện, Header, Ngôn Ngữ & Kho Lưu Trữ

- [ ] **Task 1: Header Thanh Mảnh (`h-13/14`), Logo Monogram Ẩn Ý & Nút Gạt Ngôn Ngữ `[VI | EN]`**
  - **Mô tả:** Giảm chiều cao thanh Floating Header từ `h-16/20` xuống `h-12 sm:h-14` (48-56px), giảm đệm ngang, giữ nét thanh mảnh như viền đồng hồ cao cấp. Vẽ lại Monogram trong `BrandLogo.astro` theo phong cách ẩn ý hiện đại (hai vòng cung đối thoại / sự phản chiếu vô tận của gương và vực thẳm). Bổ sung nút gạt ngôn ngữ `[VI | EN]` và nút mở "Kho Lưu Trữ" kèm badge số lượng tác phẩm đã lưu.
  - **Tiêu chí nghiệm thu:**
    - Header mỏng, gọn, không chiếm diện tích màn hình hay che khuất chữ khi cuộn.
    - Logo Monogram mới tối giản, sang trọng, mang biểu tượng sâu lắng của vực thẳm và chiếc gương.
    - Nút `VI | EN` chuyển đổi ngôn ngữ mượt mà cho các nhãn điều hướng chính.
    - Nút icon "Kho Lưu Trữ" hiển thị số lượng bài đã lưu (VD: `Kho (3)`).
  - **Xác minh:** Kiểm tra hiển thị header trên cả desktop/mobile ở Light & Dark mode.
  - **Files:** `website/src/components/Header.astro`, `website/src/components/BrandLogo.astro`, `website/public/favicon.svg`, `website/src/lib/i18n.ts`
  - **Scope:** Medium (4 files)

- [ ] **Task 2: Xây Dựng Ngăn Kéo "Kho Lưu Trữ Cá Nhân" (Saved Drawer)**
  - **Mô tả:** Tạo component `SavedDrawer.astro` (hoặc React drawer) mở từ cạnh màn hình khi người dùng bấm vào nút Kho Lưu Trữ trên Header hoặc sau khi bấm "Lưu Chiêm Nghiệm". Hiển thị danh sách các tác phẩm đã lưu từ `localStorage['hiyu_saved_quotes']`, có thumbnail tranh nhỏ, tiêu đề, tác giả, nút đọc sâu và nút gỡ khỏi kho lưu trữ.
  - **Tiêu chí nghiệm thu:**
    - Giải quyết dứt điểm câu hỏi "khi nhấn lưu kho thì nó lưu ở đâu?".
    - Mở trượt êm ái, hiển thị danh sách đầy đủ, có trạng thái trống (Empty State) thơ mộng khi chưa lưu tác phẩm nào.
    - Cập nhật số đếm badge trên Header theo thời gian thực mỗi khi thêm/xóa bài.
  - **Xác minh:** Nhấn "Lưu Chiêm Nghiệm" trên trang chi tiết $\rightarrow$ mở drawer kiểm tra có xuất hiện bài vừa lưu hay không.
  - **Files:** `website/src/components/SavedDrawer.astro`, `website/src/layouts/BaseLayout.astro`
  - **Scope:** Small (2 files)

- [ ] **Task 3: Floating Action Widget "Lên Đầu Trang" (FAB) & Tinh Giản Footer Thuần Việt**
  - **Mô tả:** Tạo component `BackToTop.astro` dạng Floating Action Widget ở góc dưới bên phải màn hình (`fixed bottom-6 right-6 z-40`), chỉ hiện lên khi cuộn quá 300px, bấm vào lướt mượt mà lên đỉnh. Cải tạo `Footer.astro`: xóa bỏ hoàn toàn cột "Minh bạch xuất xứ", loại bỏ các cụm mở ngoặc dịch nghĩa `(Thư Viện)`, `(Chiếc Gương)` để tiếng Việt gãy gọn, chuẩn mực.
  - **Tiêu chí nghiệm thu:**
    - Widget "Lên đầu trang" nổi ở góc màn hình, có hoạt họa tinh tế khi hover, hoạt động mượt mà trên cả điện thoại và máy tính.
    - Footer chỉ còn 2 khối cân đối (Brand & Điều Hướng), không còn cột thừa, không còn ngoặc đơn tiếng Anh.
  - **Xác minh:** Cuộn trang xuống và click widget để kiểm tra cuộn mượt; kiểm tra Footer sạch sẽ.
  - **Files:** `website/src/components/BackToTop.astro`, `website/src/components/Footer.astro`, `website/src/layouts/BaseLayout.astro`
  - **Scope:** Medium (3 files)

### ❖ Checkpoint 1: Header, Navigation & Saved Flow
- [ ] Header thanh thoát, không che khuất nội dung.
- [ ] Bấm nút Lưu kho mở ngay Drawer hiển thị bài đã lưu.
- [ ] Widget "Lên đầu trang" hoạt động tốt, Footer tinh gọn thuần Việt.

---

## Phase 2: Chiều Sâu Giám Tuyển, Trải Nghiệm Thưởng Lãm & Khắc Phục Lỗi Tương Tác

- [ ] **Task 4: Tái Thiết Section Hero: Giám Tuyển Linh Hoạt & Khử Trùng Lặp Headline/Quote**
  - **Mô tả:** Bỏ cơ chế fix cứng `TXT-0001` làm Hero tại `index.astro`. Thiết kế cơ chế giám tuyển tác phẩm tiêu biểu (Curated Masterpiece) hoặc luân phiên trong ngày. Đồng thời, cấu trúc lại văn bản Hero: phân biệt rõ Tiêu Đề Dẫn Nhập (Curator's Inscription) và Nội Dung Trích Dẫn để chấm dứt hoàn toàn hiện tượng câu trên câu dưới lặp lại nhau như trong ảnh chụp màn hình 1.
  - **Tiêu chí nghiệm thu:**
    - Section Hero toát lên vẻ trang trọng của một phòng trưng bày chính.
    - Không bị trùng lặp chữ giữa tiêu đề lớn và đoạn trích dẫn.
    - Lựa chọn tác phẩm đắt giá nhất của bảo tàng làm điểm mở màn.
  - **Xác minh:** Kiểm tra hiển thị trang chủ `/` không còn lặp từ và bố cục hài hòa.
  - **Files:** `website/src/components/HeroArtwork.astro`, `website/src/pages/index.astro`, `website/src/lib/content-publisher.ts`
  - **Scope:** Medium (3 files)

- [ ] **Task 5: Xây Dựng Custom Dropdown Tìm Kiếm (Bảo Đảm Luôn Mở Hướng Xuống Dưới)**
  - **Mô tả:** Thay thế thẻ `<select>` mặc định của trình duyệt tại `search.astro` bằng Custom Dropdown chuẩn mỹ học bảo tàng. Định vị tuyệt đối `top-full mt-1.5 z-30` với thanh cuộn tinh tế, bảo đảm menu luôn luôn mở xổ xuống dưới, khắc phục triệt để hiện tượng bị trình duyệt đẩy ngược lên trên như ảnh chụp màn hình 3.
  - **Tiêu chí nghiệm thu:**
    - Menu bộ lọc chủ đề và phân loại luôn mở hướng xuống dưới 100%.
    - Phong cách thiết kế đồng bộ với nền tối/sáng của bảo tàng, có trạng thái hover và chọn rõ ràng.
    - Đóng dropdown khi click ra ngoài hoặc bấm phím Escape.
  - **Xác minh:** Mở `/search`, click vào cả 2 dropdown bộ lọc và xác nhận hướng xổ xuống dưới.
  - **Files:** `website/src/pages/search.astro`
  - **Scope:** Small (1 file)

- [ ] **Task 6: Nâng Cấp Chiều Sâu Trang Chi Tiết & Chế Độ Thưởng Lãm Toàn Cảnh (Exhibition Lightbox)**
  - **Mô tả:** Xóa bỏ câu "Phản đề tự soi chiếu" cố định đại trà trong `[slug].astro`. Đa dạng hóa tầng nghĩa chiêm nghiệm theo từng chủ đề. Tích hợp tính năng **Chế Độ Thưởng Lãm Toàn Cảnh (Museum Lightbox)**: người dùng có thể nhấp vào bức tranh sơn dầu để mở chế độ xem cận cảnh toàn màn hình với nền tối tĩnh lặng và bảng thông tin Placard của bảo tàng.
  - **Tiêu chí nghiệm thu:**
    - Phần "Bóc Tách Tâm Lý & Chiêm Nghiệm" không còn bị lặp lại các câu rập khuôn giữa các bài.
    - Click vào tranh sơn dầu mở ra giao diện thưởng lãm tĩnh lặng toàn màn hình, có phím bấm đóng hoặc Esc.
  - **Xác minh:** Kiểm tra một số trang chi tiết `/library/txt-0001`, `/library/txt-0002`... xác nhận nội dung riêng biệt và lightbox hoạt động mượt mà.
  - **Files:** `website/src/pages/library/[slug].astro`, `website/src/components/MuseumLightbox.astro`
  - **Scope:** Medium (2 files)

### ❖ Checkpoint 2: Editorial & Interactive Depth
- [ ] Hero trang chủ đẳng cấp, không lặp câu chữ.
- [ ] Dropdown bộ lọc tìm kiếm mở xuống dưới thanh lịch.
- [ ] Trang chi tiết có chiều sâu riêng biệt và chế độ xem tranh toàn cảnh.

---

## Phase 3: Chuẩn Hóa SEO, Metadata & Kiểm Thử Toàn Diện

- [ ] **Task 7: Chuẩn Hóa SEO Toàn Diện, Schema.org & Kiểm Thử Tĩnh 127 Trang**
  - **Mô tả:** Chuẩn hóa toàn bộ thẻ Meta, OpenGraph tags, cấu trúc JSON-LD Schema.org (`Article`, `ExhibitionEvent`), thẻ `hreflang` hỗ trợ đa ngữ. Chạy kiểm thử tự động toàn bộ 127 trang tĩnh, đảm bảo 0 lỗi build và 0 broken links.
  - **Tiêu chí nghiệm thu:**
    - Thẻ meta tiêu chuẩn bảo tàng nghệ thuật, xem trước link Facebook/Zalo/X sắc nét.
    - Chạy `node website/test/verify-build.js` vượt qua 100% các tiêu chí.
    - Lệnh build tĩnh `npm run build` hoàn thành không cảnh báo lỗi.
  - **Xác minh:** `cd website && npm run build && node test/verify-build.js`
  - **Files:** `website/src/layouts/BaseLayout.astro`, `website/src/pages/index.astro`, `website/test/verify-build.js`
  - **Scope:** Medium (3 files)

### ❖ Checkpoint 3: Complete & Production Ready
- [ ] 127 trang tĩnh build thành công trong thời gian < 3s.
- [ ] Tất cả 8 lỗi người dùng báo cáo được giải quyết triệt để.
- [ ] Không có bất kỳ xung đột nào với tiến trình sinh ảnh bên ngoài.
