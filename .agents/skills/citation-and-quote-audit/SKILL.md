---
name: citation-and-quote-audit
description: "Kiểm tra, xác minh tính xác thực của trích dẫn và các khẳng định nguồn gốc qua 4 tầng đối chiếu (Thư mục, Văn bản, Ngữ cảnh, Diễn giải). Bảo vệ Hard Gate G1 của Hiyu Abyss."
---

# Citation and Quote Audit (Kiểm tra trích dẫn & Nguồn gốc)

## Mục đích & Ranh giới
Kỹ năng này là người gác cổng trung thực tri thức, chịu trách nhiệm xác minh mọi câu trích dẫn, phép gán tác giả hoặc khẳng định mang tính thực nghiệm.
- **Ranh giới:** Không nâng trạng thái nguồn vì câu nói nghe có vẻ sâu sắc hoặc được lan truyền rộng rãi trên mạng xã hội.

## Tài liệu tham chiếu bắt buộc
- [docs/01_HIYU_ABYSS_PROJECT_INPUT.md](file:///c:/hiyuabyss/docs/01_HIYU_ABYSS_PROJECT_INPUT.md) — Mục 7 (Chuẩn sử dụng và xác minh nguồn).
- [docs/02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md](file:///c:/hiyuabyss/docs/02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md) — Mục 4 (Phân loại xuất xứ), Mục 5 (Kiểm trích dẫn qua nhiều lớp).
- [docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md](file:///c:/hiyuabyss/docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md) — Mục 9, 12.
- [docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md](file:///c:/hiyuabyss/docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md) — Hard Gate G1, Ca kiểm thử T03, T04, T05, T18.

## Quy trình kiểm định 4 lớp (Multi-layer Audit)

### Lớp A — Thư mục (Bibliographical Layer)
- Tác phẩm này có thật không? Tác giả là ai?
- Bản in / ấn bản nào được sử dụng? Năm xuất bản?
- Người dịch là ai (nếu qua ngôn ngữ trung gian)?

### Lớp B — Văn bản (Textual Layer)
- Câu chữ có xuất hiện chính xác trong tác phẩm không?
- Vị trí cụ thể (Locator: chương, phần, số câu, số trang) ở đâu?
- Có bị cắt xén làm thay đổi bản chất ý nghĩa của câu không?

### Lớp C — Ngữ cảnh (Contextual Layer)
- Câu này là khẳng định nghiêm túc, một lời châm biếm (irony), hay một giả thuyết phản biện?
- Trong tác phẩm hư cấu: Đây là lời của nhân vật (ví dụ Underground Man của Dostoevsky) hay quan điểm của chính tác giả?

### Lớp D — Diễn giải (Interpretive Layer)
- Câu tiếng Việt trong bản thảo thuộc loại nào:
  - `DIRECT_QUOTE`: Trích nguyên văn (phải có vị trí và văn bản gốc).
  - `PARAPHRASE`: Diễn giải trung thành luận điểm.
  - `INSPIRED_ORIGINAL`: Sáng tác mới lấy cảm hứng từ chủ đề.
  - `INDEPENDENT_ORIGINAL`: Sáng tác độc lập của Hiyu Abyss.

## Phân định trạng thái bằng chứng (`evidence_status`)
- `VERIFIED_TEXT`: Đã đối chiếu chính xác nguyên văn, tác giả, tác phẩm, ấn bản và vị trí.
- `VERIFIED_IDEA`: Đã đọc nguồn hỗ trợ ý tưởng, nhưng bản câu chữ hiện tại là lời diễn giải.
- `NEEDS_REVIEW`: Còn nghi vấn hoặc thiếu đối chiếu văn bản đáng tin cậy.
- `UNVERIFIED`: Không có căn cứ xác nhận từ văn bản nguồn hợp lệ.
- `DISPUTED`: Tồn tại chứng cứ mâu thuẫn hoặc tranh cãi học thuật về tính xác thực của câu trích.

## Điều kiện dừng & Hard Gate G1
- **Kích hoạt Hard Gate G1:** Nếu một bản thảo gắn tên tác giả nhưng chỉ là câu lan truyền trên mạng không có văn bản chứng minh, hoặc câu tự sáng tác nhưng gán tên triết gia -> Đánh dấu `FAIL`, chuyển `content_type` về `INSPIRED_ORIGINAL` hoặc `INDEPENDENT_ORIGINAL` và loại bỏ tên tác giả (Ca T03).
- **Điểm cao không cứu được lỗi nguồn:** Bản thảo dù đạt 5/5 về văn phong nhưng gán sai nguồn thì vẫn bị chặn duyệt (Hard Gate G1, Ca T18).
