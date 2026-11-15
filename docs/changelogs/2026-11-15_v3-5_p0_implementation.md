# HIYU ABYSS — V3.5 P0 IMPLEMENTATION CHANGELOG & AUDIT REPORT

**Ngày thực thi:** 15/11/2026  
**Nhánh làm việc (Feature Branch):** `feat/v3.5-museum-transformation`  
**Căn cứ đặc tả:** `c:\Users\CPS\Downloads\HIYU_ABYSS_V3_5_UIUX_REVIEW_AGENT_SPEC (1).md`  
**Trạng thái:** HOÀN THÀNH PHA P0 (Awaiting Owner Review - Không tự ý merge vào main)

---

## 1. Tóm tắt các hạng mục P0 đã giải quyết

| ID | Hạng mục | Hiện trạng trước | Giải pháp kiến trúc mới (V3.5) | File chỉnh sửa |
|---|---|---|---|---|
| **F01 & F02** | **Vật lý Sách Mở Hero** | Sách chỉ là card 2 cột phẳng, trang giấy đổi thành nền đen `dark:bg-[#151412]`, mất chất cảm bản thảo. | Dựng hình học sách cổ (Codex of the Abyss) với bìa da `#14120E`, gáy sách lõm có bóng đổ trục giữa, ruy-băng lụa vàng `#B88960`. Dùng bộ token riêng `book-paper` (`#F5EFE4`) & `book-ink` (`#201C16`) giữ nguyên chất giấy ấm ở cả Dark và Light mode. | `src/components/HeroArtwork.astro`, `src/styles/tokens.css` |
| **F01** | **Bố cục Tranh/Chữ trong Sách** | Tranh ở trang phải, chữ trang trái. | Đảo chuẩn logic sách mỹ thuật: **Trang TRÁI là Kiệt tác bảo tàng thu nhỏ (TABULA PICTA)** kèm khung và bảng chú thích; **Trang PHẢI là Văn tự & Trích tuyển (CODEX ABYSSI)**. | `src/components/HeroArtwork.astro` |
| **F03** | **Minh bạch Gán nhãn Biên tập** | Đoạn `curatorInsight` cắt từ diễn giải nhưng ký `— {quote.author}`, dễ gây hiểu nhầm câu nói của triết gia. | Gắn nhãn chuẩn xác: `— Bình giải · Hiyu Abyss`. Câu trích dẫn của triết gia được đặt trang trọng trong trang sách bên phải. | `src/components/HeroArtwork.astro` |
| **F04** | **Tuyên ngôn H1 Thương hiệu** | `h1` lấy câu quote dài ngoặc thay đổi theo ngày, mất nhận diện thương hiệu. | Cố định H1 thương hiệu: **"Đọc để nhìn thế giới khác đi."** kèm Dek: **"Suy ngẫm để hiểu mình rõ hơn."** Câu quote nằm bên trong cuốn sách. | `src/components/HeroArtwork.astro` |
| **F05 & F06** | **The Mirror Portal UX** | Layout `grid-cols-2` nhưng chỉ có 1 hành trình khiến nửa trang bên phải trống hoác. Copy nặng tính kỹ thuật (`DIRECTED SCENE GRAPH`, `14 phân cảnh`, `Zero Profiling`). | Chuyển sang bố cục **Featured Editorial Full-Width 100%**: Trái 45% là cửa tranh nghệ thuật, Phải 55% là tình huống thực tế + tương tác xem trước 2 lựa chọn + timeline 4 bước (`Tình huống → Lựa chọn → Phản đề → Kết thúc mở`). Chuyển toàn bộ copy sang ngôn ngữ người đọc. | `src/pages/mirror/index.astro`, `src/components/MirrorPortalSection.astro` |
| **F10** | **Mobile Library Bookmark & Filters** | Nút lưu trái tim ẩn (`opacity-0`) chỉ hiện khi hover (điện thoại không có hover). 20 nút chủ đề xếp hàng chục dòng chiếm 2 màn hình cuộn. | Nút trái tim hiển thị tự nhiên trên mobile (`opacity-90` trên mobile, hover trên desktop), có `aria-pressed`. 20 nút chủ đề chuyển thành thanh trượt ngang vuốt mượt mà 1 hàng (swipe ribbon). | `src/pages/library/index.astro` |

---

## 2. Kết quả kiểm thử tự động (Verification & QA)

1. **Astro Static Production Build:**
   - Đạt: **127/127 trang tĩnh** biên dịch hoàn tất trong 10.05s, không có cảnh báo hoặc lỗi cú pháp.
2. **WCAG AA Accessibility & Contrast:**
   - Black Archive Contrast: **15.79:1** (vượt chuẩn AA 4.5:1).
   - Pale Archive Contrast: **12.73:1** (vượt chuẩn AA 4.5:1).
   - Đạt: **22/22 tiêu chí** trong `test/verify-build.js`.
3. **E2E Playwright Smoke Suite:**
   - 5 Viewports kiểm tra tràn ngang: **320px, 360px, 390px, 1024px, 1440px** đều đạt `scrollWidth <= innerWidth` (0px horizontal overflow).
   - An toàn XSS Search: Không thực thi script trong DOM.
   - Thử nghiệm 4 nhánh rẽ của The Mirror: Cả 4 kết thúc độc lập đều dẫn tới trang thành công.
   - Đạt: **26/26 tests PASS (100%)**.
4. **Bộ ảnh thực nghiệm (Visual Proofs):**
   - Đã xuất vào `website/test-artifacts/`:
     - `01_hero_desktop_dark.png` (1440px Desktop Dark Mode)
     - `02_hero_desktop_light.png` (1440px Desktop Light Mode)
     - `03_mirror_portal_desktop.png` (1440px Mirror Full-Width Portal)
     - `04_hero_mobile_dark.png` (375px Mobile Hero)
     - `05_library_mobile_dark.png` (375px Mobile Library Cards & Swipe Ribbon)

---

## 3. Rủi ro & Kế hoạch Rollback

- **Rủi ro:** Không có rủi ro về cơ sở dữ liệu hay chi phí vì dự án thuần static SSG.
- **Kế hoạch Rollback:**
  Toàn bộ mã nguồn mới nằm trên nhánh riêng `feat/v3.5-museum-transformation`.
  Nếu muốn hủy bỏ hoặc trở về trạng thái cũ bất cứ lúc nào, chỉ cần chuyển nhánh:
  ```bash
  git checkout main
  ```
