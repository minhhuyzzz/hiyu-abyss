---
name: semantic-novelty-review
description: "Kiểm tra tính mới ngữ nghĩa và phát hiện trùng lặp tư tưởng so với toàn bộ kho triết ngôn trong editorial/content. Ngăn chặn sao chép trá hình (Hard Gate G2)."
---

# Semantic Novelty Review (Kiểm tra tính mới ngữ nghĩa)

## Mục đích & Ranh giới
Kỹ năng này bảo vệ tính độc bản của kho nội dung Hiyu Abyss, phát hiện những câu viết lại (paraphrase) câu cũ bằng cách thay từ đồng nghĩa, đổi đại từ hoặc đảo cấu trúc ngữ pháp nhưng không mang lại phát hiện mới.
- **Ranh giới:** Không chỉ so khớp chuỗi ký tự (exact string match). Phải phân tích cú chuyển nghĩa và phát hiện tư tưởng cốt lõi.

## Tài liệu tham chiếu bắt buộc
- [docs/01_HIYU_ABYSS_PROJECT_INPUT.md](file:///c:/hiyuabyss/docs/01_HIYU_ABYSS_PROJECT_INPUT.md) — Mục 1.2, Mục 10 (`ORIGINALITY`).
- [docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md](file:///c:/hiyuabyss/docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md) — Mục 12 (Tính toàn vẹn).
- [docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md](file:///c:/hiyuabyss/docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md) — Hard Gate G2, Ca kiểm thử T09.

## Quy trình kiểm tra trùng lặp

### Bước 1: Quét từ khóa và Chủ đề
1. Xác định `topic_codes` của bản thảo `TXT-xxxx` đang duyệt.
2. Đọc toàn bộ các file `TXT-xxxx.md` trong `editorial/content/` có chung mã chủ đề hoặc từ khóa hạt nhân (ví dụ: `ân huệ`, `món nợ`, `mặt nạ`, `tha thứ`, `khiêm nhường`).

### Bước 2: So sánh cơ chế tư tưởng & Cú chuyển nghĩa
Phân tích xem bản mới có rơi vào tình trạng "bình mới rượu cũ" không:
- *Câu đã có:* "Ta dễ tha cho mình lỗi mà ta lên án ở người khác."
- *Câu mới nộp:* "Điều ta kết tội người đời thường được miễn trừ khi mang tên chính ta."
- -> **Đánh giá:** Dù từ ngữ khác nhau hoàn toàn, cơ chế tâm lý và phát hiện tư tưởng là **hoàn toàn trùng lặp** (Tiêu chuẩn kép trong việc tha thứ cho bản thân).

### Bước 3: Phân loại mức độ trùng lặp
- `CLEAR`: Câu mang phát hiện mới, góc nhìn mới hoặc khai thác một khía cạnh chưa từng xuất hiện trong kho.
- `RELATED`: Câu chia sẻ cùng một chủ đề hoặc đối tượng, nhưng cú lật hoặc điều kiện kiểm tra khác biệt. Có thể giữ lại nếu bổ sung giá trị.
- `DUPLICATE`: Câu gần như trùng khớp về mặt ý niệm và phát hiện tâm lý; chỉ là một cách diễn đạt khác (Ca T09).

### Bước 4: Xử lý vi phạm Hard Gate G2
- Nếu kết quả là `DUPLICATE`: Kích hoạt **Hard Gate G2 (Sao chép trá hình)**. Chặn chuyển trạng thái sang `IN_REVIEW`.
- Đề xuất: Hoặc sáp nhập làm biến thể (variant) trong hồ sơ cũ, hoặc từ chối (`REJECTED`) kèm ID của câu trùng lặp để đối chiếu.
