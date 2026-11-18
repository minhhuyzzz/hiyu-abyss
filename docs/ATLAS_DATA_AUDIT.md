# BÁO CÁO KIỂM TOÁN DỮ LIỆU ĐỒ THỊ THE ATLAS (V2.1)
**Hiyu Abyss — The Atlas Data Integrity & Graph Topology Audit**
*Thời gian thực hiện: 18/11/2026*
*Phiên bản Đồ thị: 2.1.0*

---

## 1. Tổng Quan Chỉ Số Đồ Thị

Toàn bộ dữ liệu của The Atlas được biên soạn tại `website/atlas/` và biên dịch tự động sang `website/src/data/atlas-graph.json` thông qua script kiểm toán `scripts/build-atlas-data.mjs`.

| Hạng mục thực thể | Yêu cầu Đặc tả V2.1 | Thực tế Đạt được | Đánh giá Tuân thủ |
|---|---|---|---|
| **Miền tư tưởng (Regions)** | Đúng 8 miền thiên văn | **8 miền** | **100% ĐẠT** |
| **Tọa độ tư tưởng (Published Nodes)** | Tối thiểu $\ge 80$ nodes | **86 nodes** độc bản | **VƯỢT CHỈ TIÊU (+6)** |
| **Mối liên hệ giám tuyển (Edges)** | Tối thiểu $\ge 110$ edges | **118 edges** có lý giải | **VƯỢT CHỈ TIÊU (+8)** |
| **Tuyến khám phá (Curated Trails)** | Tối thiểu $\ge 8$ trails | **8 trails** ($\ge 6$ chặng) | **100% ĐẠT** |
| **Liên kết mồ côi (Dangling Edges)** | Bắt buộc $0$ lỗi | **0 lỗi (100% toàn vẹn)** | **TUYỆT ĐỐI** |
| **Tọa độ cô lập (Orphan Nodes)** | Bắt buộc $0$ node | **0 node cô lập** | **TUYỆT ĐỐI** |

---

## 2. Phân Bổ 8 Miền Tư Tưởng Thiên Văn (Celestial Regions)

Hệ tọa độ đĩa thiên văn Renaissance Astrolabe được chuẩn hóa trên thang đo $1000 \times 1000$:

| ID Miền | Nhãn tiếng Việt | Nhãn tiếng Anh | Ký hiệu | Tọa độ tâm $(X, Y)$ | Số Nodes |
|---|---|---|---|---|---|
| `region-human-condition` | Bản Chất Con Người | The Human Condition | ☉ | $(280, 260)$ | 14 |
| `region-ego-and-illusion` | Bản Ngã & Sự Công Nhận | Ego & Recognition | ☽ | $(680, 220)$ | 12 |
| `region-freedom-and-order` | Tự Do & Giới Hạn | Freedom & Boundaries | ♄ | $(790, 480)$ | 11 |
| `region-solitude-and-communion` | Cô Độc & Gắn Kết | Solitude & Communion | ☿ | $(720, 760)$ | 11 |
| `region-power-and-machination` | Quyền Lực & Đạo Đức | Power & Machination | ♂ | $(490, 840)$ | 11 |
| `region-suffering-and-purpose` | Đau Khổ & Ý Nghĩa | Suffering & Purpose | ♃ | $(240, 740)$ | 11 |
| `region-masks-and-authenticity` | Mặt Nạ & Tính Chân Thực | Mask & Authenticity | ♅ | $(180, 470)$ | 10 |
| `region-aesthetics-and-worldview` | Thẩm Mỹ & Cái Nhìn Thế Giới | Aesthetics & Worldview | ♀ | $(500, 500)$ | 6 (Tâm đỉnh) |

---

## 3. Cấu Trúc Phân Loại Tọa Độ (86 Nodes)

Đồ thị đạt được sự đa dạng liên ngành giữa tâm lý học hành vi, triết học hiện sinh, kiệt tác mỹ thuật bảo tàng và văn học kinh điển:

- **29 Chủ đề hạt nhân (`kind: theme`):** Bao phủ toàn bộ 29 mã chủ đề của Hiyu Abyss (`TRUTH`, `EGO`, `MASK`, `SHADOW`, `POWER`, `SOLITUDE`, `SUFFERING`, `FREEDOM`...).
- **19 Ý tưởng triết học cốt lõi (`kind: idea`):** Các nghịch lý bản ngã như *Sự thật buốt giá & Cơn mê êm đềm*, *Ảo ảnh bản ngã & Nhu cầu hơn người*, *Bẫy tự do của Sartre*, *Nghịch lý cô độc của Pascal*, *Mặt nạ Persona & Burnout*, *Chiếc bẫy thao túng ngầm*...
- **10 Triết gia & Tác giả kinh điển (`kind: thinker`):** Friedrich Nietzsche, Arthur Schopenhauer, Marcus Aurelius, Blaise Pascal, Fyodor Dostoevsky, Carl Gustav Jung, Jean-Paul Sartre, Michel de Montaigne, Epictetus, Lucius Annaeus Seneca.
- **8 Kiệt tác mỹ thuật bảo tàng (`kind: artwork`):**
  - *Trường Học Athens* (Raffaello Sanzio, Vatican) — Tâm đỉnh đồ thị
  - *Kẻ Lãng Du Trên Biển Sương Mù* (Caspar David Friedrich, Hamburger Kunsthalle)
  - *Saturn Ăn Thịt Con Trai* (Francisco Goya, Museo del Prado)
  - *Nhà Thiên Văn Học* (Johannes Vermeer, Musée du Louvre)
  - *Judith Chặt Đầu Holofernes* (Caravaggio, Galleria Nazionale d'Arte Antica)
  - *Khu Vườn Khoái Lạc Trần Thế* (Hieronymus Bosch, Museo del Prado)
  - *Tử Thần Đánh Tráo Cán Cân* (Albrecht Dürer, Albertina Museum)
  - *Bữa Tiệc Của Belshazzar* (Rembrandt van Rijn, The National Gallery London)
- **20 Nhịp cầu hồ sơ tác phẩm Thư Viện (`kind: quote`):** Folio #0001 đến #0020, tạo cầu nối trực tiếp giữa The Atlas và trang đọc chuyên sâu `/library/txt-xxxx`.

---

## 4. Kiểm Toán 118 Mối Liên Hệ Giám Tuyển (Edges)

Toàn bộ 118 quan hệ đều tuân thủ nguyên tắc biên tập Hiyu Abyss: **Tuyệt đối không có cạnh vô nghĩa hoặc chỉ vẽ đường thẳng hình học**. Mỗi quan hệ đều chứa đựng:
1. `relation`: Phân loại quan hệ chuẩn (`explores`, `contrasts_with`, `influenced_by`, `illustrated_by`, `reframes`, `shares_question_with`, `contextualized_by`).
2. `why`: Đoạn văn ngắn 1–2 câu giải thích rành mạch căn nguyên tâm lý hoặc triết học.
3. `curatorNote`: Định vị học thuật của ban giám tuyển.

**Phân bổ loại quan hệ:**
- `explores`: 44 edges (Khám phá / Khơi mở)
- `contrasts_with`: 18 edges (Đối lập / Phản đề biện chứng)
- `influenced_by`: 16 edges (Dòng chảy tư tưởng & Kế thừa)
- `illustrated_by`: 12 edges (Minh họa kiệt tác bảo tàng)
- `shares_question_with`: 16 edges (Chung câu hỏi bản thể hiện sinh)
- `reframes`: 12 edges (Đặt lại góc nhìn nhận thức)

---

## 5. Danh Mục 8 Tuyến Thám Hiểm Giám Tuyển (Curated Trails)

Mỗi tuyến là một cuộc triển lãm có hướng dẫn với lộ trình từ 6 đến 8 chặng dừng, có câu hỏi khơi gợi (`introPrompt`) và câu hỏi đúc kết (`closingPrompt`):

1. **Bản Chất Chân Lý & Tự Lừa Dối** (`trail-nature-of-truth`): 7 chặng · 8 phút
2. **Bản Ngã & Sự Công Nhận** (`trail-ego-and-recognition`): 7 chặng · 8 phút
3. **Tự Do & Giới Hạn** (`trail-freedom-and-boundaries`): 7 chặng · 8 phút
4. **Cô Độc & Gắn Kết** (`trail-solitude-and-communion`): 8 chặng · 7 phút
5. **Quyền Lực & Đạo Đức** (`trail-power-and-machination`): 8 chặng · 8 phút
6. **Đau Khổ & Ý Nghĩa** (`trail-suffering-and-purpose`): 8 chặng · 8 phút
7. **Mặt Nạ & Tính Chân Thực** (`trail-mask-and-authenticity`): 8 chặng · 8 phút
8. **Thẩm Mỹ & Cái Nhìn Thế Giới** (`trail-aesthetics-and-worldview`): 7 chặng · 7 phút

---

## 6. Kết Luận Kiểm Toán

- **Toàn vẹn đồ thị:** 100% đạt chuẩn. Mã nguồn xác thực không tìm thấy bất kỳ ID nào bị sai lệch hoặc mồ côi.
- **Tương thích hoàn hảo với Astro 7:** Dữ liệu được nén thành bộ nhớ JSON tĩnh zero-I/O tại `website/src/data/atlas-graph.json`, loại bỏ hoàn toàn các lời gọi hệ thống tệp trong môi trường runtime Cloudflare Workers.
