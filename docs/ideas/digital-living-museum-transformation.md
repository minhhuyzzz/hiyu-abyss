# HIYU ABYSS — TRANSFORMATION TO DIGITAL LIVING MUSEUM

> **Mã hồ sơ:** `IDEA-MUSEUM-TRANSFORMATION`  
> **Ngày khởi tạo:** 15/11/2026  
> **Căn cứ:** Phê chuẩn từ bản thẩm định độc lập `HIYU_ABYSS_INDEPENDENT_REVIEW_FOR_AGENT_2026-11-15.md` và phản hồi của Chủ dự án.  
> **Trạng thái:** APPROVED / READY FOR IMPLEMENTATION

---

## 1. Problem Statement (Tuyên ngôn bài toán)

> **How Might We:**  
> Làm thế nào để biến Hiyu Abyss từ một trang web hiển thị triết ngôn đơn thuần thành một **Bảo Tàng Triết Học & Mỹ Học Số (Digital Living Museum)** đạt chuẩn mực học thuật về nguồn gốc, mang lại trải nghiệm nội tâm điện ảnh sâu sắc, vận hành vĩnh cửu với chi phí **0đ/tháng** mà không cần bất kỳ hạ tầng phức tạp nào?

---

## 2. Recommended Direction (Chiến lược định hướng được duyệt)

### 2.1. Triết lý phát triển: "Trust First, Atmospheric Soul Second"
1. **Bảo tồn nền tảng kỹ thuật hiện có:** Tiếp tục duy trì 100% kiến trúc Astro static-first, React Island cho The Mirror, bộ đôi chủ đề Black Archive / Pale Archive, hệ thống kiểu chữ 3 tầng (Cormorant Garamond, Literata, Be Vietnam Pro). Tuyệt đối không viết lại (rewrite) hay chuyển sang Next.js.
2. **Chi phí cố định 0đ/tháng:** Không sử dụng cơ sở dữ liệu (PostgreSQL, Supabase, Firebase), không máy chủ backend, không tích hợp API trả phí. Mọi dữ liệu lưu trữ cá nhân đều được ủy nhiệm an toàn cho `localStorage` của người dùng.
3. **Thanh lọc học thuật (Academic Rigor):** Chấm dứt triệt để việc gán nhãn "Đã xác minh" mang tính hình thức. Minh bạch hóa 4 tầng xuất xứ (Tác phẩm, Năm ấn hành, Bản dịch, Tình trạng kiểm chứng) theo chuẩn `HYA-02`.
4. **Mỹ học điện ảnh không phô trương:** Loại bỏ các hiệu ứng hào nhoáng nhân tạo (AI glow, neon, pill badge lạm dụng). Tôn vinh vẻ đẹp của khoảng trống (negative space), tranh sơn dầu bảo tàng CCO và sức nặng của câu từ triết học.

---

## 3. Lộ trình Triển khai Phân kỳ (Phased Roadmap)

### Giai đoạn 1: Nền tảng Niềm Tin & An Toàn Kỹ Thuật (Sprint 1 — P0 Trust & Integrity)
- **P0-01 (Nguồn trích dẫn học thuật):**
  - Mở rộng schema dữ liệu tại `website/src/lib/types.ts`: thêm `source_work`, `source_url`, `source_location`, `translation_note`, `verification_status` (`VERIFIED_SOURCE`, `PENDING_VERIFICATION`, `INSPIRED_ORIGINAL`, `INDEPENDENT_ORIGINAL`).
  - Rà soát các bài viết, hạ nhãn "Đã xác minh" về "Chờ đối chiếu ấn bản" nếu chưa có bằng chứng trang sách thực tế.
- **P0-02 (Minh bạch Provenance hình ảnh):**
  - Cập nhật 120 mục tranh trong `asset-catalog.json`: phân định rõ `original_museum_image` (ảnh bảo tàng Public Domain), `transformed_public_domain` (phục dựng/chuẩn hóa hữu cơ), và `original_commissioned` (sáng tác nội bộ).
- **P0-03 (SEO Canonical & i18n Trung thực):**
  - Cấu hình canonical domain chuẩn xác theo môi trường thực tế.
  - Gỡ bỏ các thẻ `hreflang` song ngữ giả trỏ cùng một URL.
  - Khẳng định rõ phạm vi đa ngôn ngữ hiện tại là **UI Translation** (khung điều hướng, nút bấm), bảo vệ tính toàn vẹn của nội dung tiếng Việt chuẩn mực cho đến khi có bản dịch tiếng Anh chính thức.
- **P0-05 (Bảo mật Tìm kiếm):**
  - Viết lại hàm hiển thị kết quả trong `search.astro`: loại bỏ nội suy chuỗi qua `innerHTML`, chuyển sang DOM APIs an toàn (`textContent`, `createElement`) để miễn nhiễm với HTML injection.
- **P0-04 (Kiểm thử thực tế E2E & A11y):**
  - Thiết lập smoke test bằng Playwright & axe-core kiểm tra tương tác bàn phím, mobile 320px không bị tràn ngang, và tuân thủ `prefers-reduced-motion`.

### Giai đoạn 2: Trải nghiệm Nghệ thuật Sâu sắc (Sprint 2 — P1 Atmospheric UX)
- **P1-Mirror (The Mirror Scene Director):**
  - Xây dựng Scene Renderer kích hoạt đầy đủ thuộc tính `scenePreset` và `motionPreset` từ `MIR-0001.yaml`.
  - Thiết kế 5 dạng phòng tâm lý trực quan: `threshold` (ngưỡng cửa hé sáng), `observation` (quan sát), `silence` (khoảng lặng), `confrontation` (đối diện phản đề), `ending` (bản kết đúc kết).
  - Tối ưu 4 nhánh kịch bản với góc máy tranh và ánh sáng riêng biệt.
- **P1-Landing (Ấn phẩm Nghệ thuật 10-11 nhịp):**
  - Chuyển đổi Landing Page từ cấu trúc khối card đồng dạng sang nhịp điệu ấn phẩm bảo tàng: The Entrance $\rightarrow$ Inscription of the Day $\rightarrow$ Curator's Note $\rightarrow$ Selected Works (bố cục magazine bất đối xứng) $\rightarrow$ Exhibition Wings $\rightarrow$ Mirror Threshold $\rightarrow$ Closing Invitation.
- **P1-Library & Detail:**
  - Chế độ xem `Editorial` mang nhịp điệu tạp chí thực thụ (1 tác phẩm lớn tiêu điểm, xen kẽ câu ngắn đanh thép).
  - Tối ưu nút Lưu chiêm nghiệm (Bookmark) hiển thị tự nhiên trên màn hình cảm ứng điện thoại di động.

---

## 4. Key Assumptions to Validate (Các giả định cốt lõi cần kiểm chứng)

- [ ] **Giả định về Sự minh bạch:** Độc giả trí thức đánh giá cao sự trung thực khi dự án thừa nhận "Chờ đối chiếu bản in" hơn là những tuyên bố xác minh hời hợt.
- [ ] **Giả định về Hiệu năng The Mirror:** Scene transitions thuần túy bằng CSS transforms và Web Animations API đạt mượt mà 60fps trên thiết bị di động tầm trung mà không cần thư viện 3D nặng.
- [ ] **Giả định về Ngôn ngữ:** Độc giả chấp nhận đọc giao diện tiếng Anh với bài viết tiếng Việt chất lượng cao thay vì một bản dịch máy cẩu thả.

---

## 5. Not Doing List (Những điều TUYỆT ĐỐI KHÔNG LÀM)

1. **KHÔNG** đập đi làm lại hoặc chuyển đổi sang framework khác (Next.js, Remix, Nuxt).
2. **KHÔNG** cài đặt thêm bất kỳ cơ sở dữ liệu nào (Postgres, MongoDB, Supabase, Firebase).
3. **KHÔNG** sử dụng API trả phí hoặc các dịch vụ đám mây phát sinh chi phí hàng tháng.
4. **KHÔNG** tự ý đổi nhãn "Đã xác minh" hàng loạt khi chưa có đối chiếu trang sách/ấn bản thực tế.
5. **KHÔNG** thêm âm thanh nền tự động phát gây quấy rầy người xem.
6. **KHÔNG** lạm dụng hiệu ứng cuộn trang (scroll hijacking) gây ức chế cho người dùng di động.

---

## 6. Open Questions (Các câu hỏi tiếp theo cần giải quyết)

1. **Quy chuẩn nguồn cho các câu sáng tác:** Câu nào trong 100 tác phẩm là danh ngôn cổ điển có xuất xứ đối chiếu, câu nào là sáng tác độc quyền lấy cảm hứng từ các nhà tư tưởng? (Cần chạy script phân loại dựa trên `knowledge/content/TXT-xxxx.md`).
2. **Hình ảnh phục dựng:** Có cần bổ sung một trang/modal ngắn giải thích về quy trình "Organic Canvas Normalization" (chuẩn hóa thớ vải toan và sắc tố sơn dầu tự nhiên) để minh bạch nghệ thuật với công chúng không?
