---
name: philosophical-argument-mapping
description: "Phân tích và sơ đồ hóa cấu trúc lập luận triết học (tiền đề, kết luận, tiền giả định, phản đề, giới hạn áp dụng) vào hồ sơ CON hoặc NOTE."
---

# Philosophical Argument Mapping (Lập bản đồ lập luận triết học)

## Mục đích & Ranh giới
Kỹ năng này chịu trách nhiệm mổ xẻ các luận điểm phức tạp trong triết học đạo đức, hiện sinh và tâm lý học chiều sâu thành cấu trúc logic tường minh, phục vụ việc xây dựng hồ sơ khái niệm `CON-xxxx` hoặc đào sâu `NOTE-xxxx`.
- **Ranh giới:** Không đánh đồng tuyên ngôn của một trường phái với chân lý thực nghiệm phổ quát.

## Tài liệu tham chiếu bắt buộc
- [docs/01_HIYU_ABYSS_PROJECT_INPUT.md](file:///c:/hiyuabyss/docs/01_HIYU_ABYSS_PROJECT_INPUT.md) — Mục 6 (Tuyến đọc), Mục 6.6 (Năng lực đặc thù).
- [docs/02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md](file:///c:/hiyuabyss/docs/02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md) — Mục 3 (Quy trình R3, R4).
- [docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md](file:///c:/hiyuabyss/docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md) — Mục 7 (`CON`).

## Quy trình lập bản đồ lập luận

### Bước 1: Xác định hạt nhân luận đề
- Tác giả hoặc tư tưởng gia thực sự tuyên bố điều gì?
- Luận đề này thuộc chủ đề nào trong 20 mã chủ đề HYA-01 (`MORALITY`, `EGO`, `POWER`, `FREEDOM`...)?

### Bước 2: Bóc tách cấu trúc tiền đề (Premises)
1. **Tiền đề 1 (P1):** Giả định cơ bản về bản tính con người hoặc hoàn cảnh xã hội.
2. **Tiền đề 2 (P2):** Mâu thuẫn phát sinh khi hành vi được thực hiện.
3. **Tiền giả định ngầm (Hidden assumptions):** Điều tác giả không nói ra nhưng bắt buộc phải đúng để lập luận đứng vững.
4. **Kết luận (Conclusion):** Mệnh đề sau cùng được rút ra.

### Bước 3: Tìm kiếm phản biện & Cách hiểu đối lập
- Trường phái đối lập (ví dụ: Chủ nghĩa Khắc kỷ vs Chủ nghĩa Hoài nghi, Freud vs Jung, Nietzsche vs Kant) sẽ nhìn nhận vấn đề này ra sao?
- Đâu là phản ví dụ thực tế dễ làm sụp đổ kết luận này?

### Bước 4: Tạo hoặc cập nhật hồ sơ Khái niệm (`CON-xxxx`)
1. Tạo file `knowledge/concepts/CON-xxxx.md` theo mẫu `templates/concept.md`.
2. Định nghĩa làm việc (Working definition) ngắn gọn, sắc nét.
3. Liệt kê các câu hỏi mở và liên kết các nguồn `source_ids`, `note_ids`.
