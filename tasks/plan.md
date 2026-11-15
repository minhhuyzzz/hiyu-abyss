# Kế Hoạch Triển Khai: Chế Tác 50 Bộ Ảnh Sơn Dầu Cổ Điển Bảo Tàng (Theme 151 -> 200)

> **Căn cứ:** Nhiệm vụ mở rộng quy mô từ bài 151 đến 200 (`TXT-0151` $\rightarrow$ `TXT-0200`).  
> **Mục tiêu:** Chế tác trọn vẹn **50 bộ ảnh sơn dầu bảo tàng mới (`theme_151` $\rightarrow$ `theme_200`)**, mỗi bộ gồm đủ **3 slide dọc 9:16 (`1080x1920`)** đạt chuẩn **HYA-08 Anti-AI Standard**:
> - Slide 1: Toàn cảnh tác phẩm sơn dầu (Establishing Shot 1.0x).
> - Slide 2: Cận cảnh tâm điểm nghệ thuật & biểu cảm (Closeup Shot 1.65x).
> - Slide 3: Siêu cận thớ vải toan, vệt cọ impasto & chiaroscuro (Macro Shot 2.5x).  
> **Tổng sản lượng:** Đúng **150 slide hoàn chỉnh** (50 themes x 3 slides), đồng bộ 100% vào `assets/templates/multislides/` và `website/public/images/themes/`.

---

## 1. Nguyên Tắc Mỹ Thuật Bắt Buộc (HYA-08 Anti-AI Standard)

1. **100% Danh Tác Cổ Điển Đích Thực:** Sử dụng nguồn tranh công khai (Public Domain / CC0) từ các bảo tàng lớn qua Wikimedia Commons & Google Art Project (Louvre, Rijksmuseum, Prado, Hermitage, National Gallery...).
2. **Khử Triệt Để Tì Vết AI (Banned AI Artifacts):**
   - Không bề mặt nhựa/sáp CGI (`NO 3D plastic/waxy sheen`).
   - Không ánh sáng neon phát quang ảo (`NO airbrushed glow / fantasy sparkles`).
   - Không ký tự hay hoa văn nguệch ngoạc giả tạo (`NO pseudo-text / runes`).
   - Tỷ lệ cơ thể và giải phẫu tự nhiên theo trường phái cổ điển.
3. **Quy Trình Hậu Kỳ Khử AI Vật Lý (Organic Canvas Normalization):**
   - Cắt chuẩn dọc 9:16 (1080x1920) bằng thuật toán Lanczos.
   - Cân bằng màu khoáng tự nhiên: Giảm nhẹ độ bão hòa (-4%) trở về màu đất son, hổ phách, xanh Prussian, đỏ thẫm.
   - Phủ lớp hạt vải toan vi mô (*Organic Canvas Grain*) phá vỡ bề mặt nhẵn bóng kỹ thuật số.
   - Tinh chỉnh *Micro-contrast Unsharp Mask* làm nổi rõ thớ vải toan và gờ sơn dầu impasto vật lý.
4. **Chuẩn Hóa Bộ 3 Slide Đa Tầng Thu Phóng (3-Slide Visual Progression):**
   Mỗi chủ đề đều có trọn vẹn 3 slide để phục vụ đăng TikTok dạng Carousel hoặc Single-Punch mà không bao giờ bị thiếu ảnh.

---

## 2. Danh Mục 5 Cụm Chủ Đề & 50 Kiệt Tác Giám Tuyển

| Cụm Chủ Đề (10 theme/cụm) | Dải Theme | Phong Cách Mỹ Thuật | Danh Họa & Tác Phẩm Tiêu Biểu |
|---|---|---|---|
| **1. Thao Túng Tâm Lý & Khí Độc Quan Hệ** | `theme_151` $\rightarrow$ `theme_160` | Chiaroscuro u tối, ánh nến le lói giữa đêm đen, ánh mắt toan tính, phản chiếu gương. | Georges de La Tour (*The Penitent Magdalen*), Caravaggio (*Narcissus*, *The Cardsharps*), John William Waterhouse, Francisco Goya (*Saturn*), Vilhelm Hammershøi, Quentin Matsys. |
| **2. Tâm Lý Đám Đông & Thoái Hóa Lương Tri** | `theme_161` $\rightarrow$ `theme_170` | Biển người cuồng loạn, hàng súng vô cảm, người mù dắt nhau, chàng hề trầm tư giữa dạ tiệc. | Honoré Daumier (*The Uprising*), Francisco Goya (*The Third of May 1808*), Rembrandt (*Dr. Nicolaes Tulp*), Pieter Bruegel (*The Blind*), J.M.W. Turner (*The Slave Ship*), Jacques-Louis David, Jan Matejko (*Stańczyk*), Edvard Munch, James Ensor. |
| **3. Ngụy Tín & Nỗi Sợ Tự Do** | `theme_171` $\rightarrow$ `theme_180` | Người suy ngẫm trĩu nặng, ánh mắt u uẩn của cô hầu bàn, thiên thần u uất giữa dụng cụ vô nghĩa, tiếng thét hiện sinh. | Auguste Rodin (*The Thinker*), William Blake, Édouard Manet (*A Bar at the Folies-Bergère*), Edvard Munch (*The Scream*), Fernand Léger, Hieronymus Bosch, Albrecht Dürer (*Melencolia I*), Caspar David Friedrich, Salvador Dalí, Eugène Delacroix. |
| **4. Thiên Kiến Nhận Thức & Tự Biện Hộ** | `theme_181` $\rightarrow$ `theme_190` | Ngón tay hoài nghi kiểm chứng vết thương, chiếc gương soi phản chiếu, học giả giữa kho tàng tri thức, đứa con hoang đàng hối cải, nàng Ophelia chìm trong tiếc nuối. | Caravaggio (*The Incredulity of Saint Thomas*), William Hogarth, Diego Velázquez (*Las Meninas*), John Everett Millais (*Ophelia*), Artemisia Gentileschi, Rembrandt (*Self-Portrait*, *The Prodigal Son*), Johannes Vermeer (*The Astronomer*), Carl Spitzweg, Titian. |
| **5. Nghịch Lý Hiện Sinh & Sức Bật Nội Tại** | `theme_191` $\rightarrow$ `theme_200` | Sisyphus oằn mình nâng khối đá, con tàu vượt qua tâm bão tuyết dữ dội, người khổng lồ thức tỉnh giữa chân trời, con thuyền trở về bến đỗ hoàng hôn (Amor Fati). | Titian (*Sisyphus*), Vincent van Gogh (*Prisoners' Round*), Odilon Redon, Caspar David Friedrich (*The Sea of Ice*, *The Stages of Life*), Claude Monet (*Impression, Sunrise*), Rembrandt (*Jeremiah*), J.M.W. Turner (*Snow Storm*), Gustave Courbet (*The Wave*), Francisco Goya (*Colossus*). |

---

## 3. Lộ Trình Triển Khai 4 Pha Chi Tiết

### Phase 1: Đặc Tả Mỹ Thuật HYA-08 & Manifest 50 Danh Tác
- [ ] **Task 1: Tạo Đặc Tả Mỹ Thuật `docs/10_HIYU_ABYSS_OIL_PAINTING_SUITES_151_200_SPEC.md` & Manifest JSON**
  - Viết kịch bản `scripts/build_oil_spec_151_200.py` xuất đặc tả đầy đủ 50 theme và `scripts/oil_suites_151_200_prompts_manifest.json`.
  - **Tiêu chí:** Đúng 50 mục, có tên tranh, tác giả, năm, bảo tàng, ý niệm thị giác và prompt chuẩn.

### Phase 2: Phân Giải Nguồn Ảnh Bảo Tàng Siêu Phân Giải (Wikimedia Commons API)
- [ ] **Task 2: Tìm Kiếm & Tải Bản Scan Gốc (3.000px–5.000px) Về `assets/templates/raw_cache/`**
  - Viết và chạy `scripts/resolve_50_master_oil_art.py` truy vấn Wikimedia API (User-Agent chuẩn, delay 0.5s).
  - Tải và lưu các bản scan độ phân giải cao vào bộ đệm cache.
  - **Tiêu chí:** 100% 50 tác phẩm được phân giải và tải về đầy đủ.

### Phase 3: Chế Tác Hàng Loạt 150 Slide Chuẩn HYA-08 & 3 Tầng Thu Phóng
- [ ] **Task 3: Xuất Trọn Bộ 150 Slide Sơn Dầu Khử AI (50 Themes x 3 Slides)**
  - Viết và chạy `scripts/mass_produce_oil_suites_151_200.py`:
    - Slide 1: Toàn cảnh 1080x1920 (1.0x).
    - Slide 2: Cận cảnh tâm điểm kịch tính (1.65x).
    - Slide 3: Siêu cận thớ toan và vết cọ impasto (2.5x).
    - Khử bão hòa -4%, phủ Organic Canvas Grain, tăng sắc nét Micro-contrast.
    - Lưu vào `assets/templates/multislides/theme_151..200/` và `website/public/images/themes/theme_151..200/`.
  - **Tiêu chí:** Đúng 150 file JPG chất lượng cao, 0 tì vết AI.

### Phase 4: Cập Nhật Asset Catalog, Kiểm Thử Toàn Diện & Đồng Bộ Git
- [ ] **Task 4: Cập Nhật `asset-catalog.json`, Build Thư Viện Sống & Đẩy Git**
  - Cập nhật thông tin tác phẩm bảo tàng vào `website/src/data/asset-catalog.json`.
  - Chạy `npm run build && node test/verify-build.js` (đảm bảo 22 PASS).
  - Đẩy Git theo các gói chia nhỏ an toàn lên `origin main`.
  - **Tiêu chí:** Website cập nhật đủ 200 theme, git sạch sẽ.

---

## 4. Quản Lý Rủi Ro Kỹ Thuật

1. **Lỗi Rate Limit / Chặn IP từ Wikimedia Commons:** Giữ User-Agent định danh rõ ràng kèm email liên hệ, thêm độ trễ 0.5s - 1.0s giữa các lượt tải và cơ chế thử lại (exponential backoff 3 lần).
2. **Ảnh scan gốc bị thiếu hoặc sai tên:** Thiết lập cơ chế fallback với danh mục tác phẩm thay thế cùng chủ đề và thời kỳ của danh họa.
3. **Lỗi timeout HTTP 408 khi đẩy Git:** Chia nhỏ lệnh commit/push thành các lô 10-15 theme (~8-10MB mỗi lô).
