---
name: book-insight-summarization
description: "Trích xuất và tóm ý phân tích từ các chương sách hoặc bài luận đã đọc được thực tế. Tách bạch luận đề tác giả, lập luận, phản đề và suy luận khai thác của Hiyu Abyss vào hồ sơ NOTE."
---

# Book Insight Summarization (Tóm ý phân tích sách & tiểu luận)

## Mục đích & Ranh giới
Kỹ năng này chịu trách nhiệm đọc sâu phần văn bản nguồn đã tiếp cận hợp lệ, trích xuất cấu trúc lập luận của tác giả và đề xuất góc nhìn cho Hiyu Abyss.
- **Ranh giới:** Chỉ tóm tắt trong phạm vi phần văn bản thực tế đã đọc (`READ_SOURCE` hoặc `CONTEXT_CHECKED`). Phân biệt tuyệt đối giữa lời của tác giả và lời suy diễn của dự án.

## Tài liệu tham chiếu bắt buộc
- [docs/01_HIYU_ABYSS_PROJECT_INPUT.md](file:///c:/hiyuabyss/docs/01_HIYU_ABYSS_PROJECT_INPUT.md) — Mục 6 (Tuyến đọc khởi đầu), Mục 7 (Xác minh nguồn).
- [docs/02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md](file:///c:/hiyuabyss/docs/02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md) — Mục 3 (Quy trình R3, R4), Mục 8 (Quy tắc tóm ý sách).
- [docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md](file:///c:/hiyuabyss/docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md) — Mục 6 (`NOTE`).
- [docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md](file:///c:/hiyuabyss/docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md) — Ca kiểm thử T02, T04, T05.

## Quy trình thực hiện (Workflow)

### Bước 1: Tiếp nhận nguồn & Định vị văn bản
1. Xác định hồ sơ `SRC-xxxx` đã tồn tại và có `access_level` tối thiểu là `PARTIAL_TEXT` hoặc `READ_SOURCE`.
2. Ghi rõ `locator`: Số chương, tên mục, số đoạn (aphorism number), hoặc trang trong ấn bản cụ thể.

### Bước 2: Trích xuất 5 thành phần phân tích cốt lõi
1. **Thesis (Luận đề):** Tác giả khẳng định điều gì? Bản chất của mệnh đề là gì?
2. **Evidence & Reasoning (Lập luận):** Tác giả dùng logic nào, quan sát nào hoặc ví dụ nào để nâng đỡ luận đề?
3. **Context (Bối cảnh):** Hoàn cảnh phát biểu, đối tượng hướng tới, trường phái tư tưởng đang đối thoại hoặc phê phán.
4. **Counterpoint & Limitations (Phản đề & Giới hạn):** Trường hợp nào luận đề này sụp đổ? Có cách giải thích nào vô hại hoặc nhân văn hơn không?
5. **Original Insight (Góc nhìn Hiyu Abyss):** Nghịch lý tâm lý nào có thể rút ra cho đời sống đương đại? Đánh dấu rõ: *Đây là suy luận của Hiyu Abyss, không phải lời tác giả*.

### Bước 3: Tạo hồ sơ `NOTE` & Liên kết
1. Tạo file `knowledge/notes/NOTE-xxxx.md` theo mẫu `templates/note.md`.
2. Ghi nhận `evidence_status`:
   - `VERIFIED_TEXT`: Đã có nguyên văn chính xác của đoạn trích từ ấn bản xác định.
   - `VERIFIED_IDEA`: Đã đọc nguồn và xác nhận tác giả bàn về ý tưởng này, nhưng bản ghi là diễn giải.
3. Liên kết `source_id: SRC-xxxx`, các `concept_ids` nếu có.

## Điều kiện dừng & Cấm đoán (Stop Conditions & Forbidden)
- **Cấm tóm tắt khi chưa đọc:** Tuyệt đối không viết `NOTE` nếu nguồn chỉ mới dừng ở `FOUND_METADATA`.
- **Cấm đồng nhất hư cấu:** Khi đọc văn học (Dostoevsky, Camus, Tolstoy...), lời thoại nhân vật hoặc độc thoại nội tâm không được tự động đồng nhất với lập trường tác giả (Ca T05).
- **Cấm gộp lẫn bản dịch:** Khi đọc bản dịch tiếng Anh của một nguyên tác tiếng Pháp/Đức/Nga, ghi rõ người dịch và ấn bản; không nhận câu dịch tiếng Việt tự làm là câu của dịch giả nổi tiếng (Ca T04).
