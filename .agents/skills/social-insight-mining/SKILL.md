---
name: social-insight-mining
description: "Khảo sát và ghi nhận các hiện tượng, câu chuyện, thảo luận xã hội công khai để tìm kiếm câu hỏi hoặc nghịch lý đời thực. Tuân thủ đạo đức dữ liệu và không quy chụp số đông."
---

# Social Insight Mining (Khảo sát hiện tượng & Thảo luận xã hội)

## Mục đích & Ranh giới
Kỹ năng này chịu trách nhiệm lắng nghe và phát hiện những căng thẳng tâm lý, tiêu chuẩn kép hoặc nghịch lý hành vi diễn ra trong đời sống thực tế thông qua các cuộc thảo luận công khai (Reddit, Threads, diễn đàn, mạng xã hội).
- **Ranh giới:** Thảo luận xã hội chỉ là nguồn gợi ý câu hỏi và tình huống, **không bao giờ là bằng chứng khoa học** về bản chất của mọi con người.

## Tài liệu tham chiếu bắt buộc
- [docs/01_HIYU_ABYSS_PROJECT_INPUT.md](file:///c:/hiyuabyss/docs/01_HIYU_ABYSS_PROJECT_INPUT.md) — Mục 6.2 (Nguồn quan sát xã hội), Mục 7.3.
- [docs/02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md](file:///c:/hiyuabyss/docs/02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md) — Mục 7 (Dùng bài đăng công khai và thảo luận xã hội).
- [docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md](file:///c:/hiyuabyss/docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md) — Mục 10 (`RUN`).
- [docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md](file:///c:/hiyuabyss/docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md) — Hard Gate G6, Ca kiểm thử T11, T12.

## Quy định đạo đức & Giới hạn dữ liệu bắt buộc (Hard Gate G6)
1. **Chỉ khảo sát dữ liệu công khai:** Tuyệt đối không xâm nhập các nhóm kín, tin nhắn riêng tư hoặc tài khoản có thiết lập bảo mật.
2. **Ẩn danh hóa hoàn toàn:** Không lưu tên tài khoản, địa chỉ cá nhân, hình ảnh hoặc bất kỳ dữ liệu định danh nào của người thật.
3. **Không sao chép nguyên văn dài:** Chỉ ghi nhận tóm tắt tình huống hoặc mô hình lập luận bằng ngôn từ phân tích của dự án.
4. **Không vượt rào kỹ thuật:** Nếu liên kết bị chặn, yêu cầu đăng nhập hoặc bot-check, đánh dấu `UNAVAILABLE` trong `RUN` và dừng lại (Ca T11).

## Quy trình khảo sát

### Bước 1: Tiếp nhận đề tài & Tạo hồ sơ `RUN-xxxx`
- Đặt câu hỏi khảo sát cụ thể: "Những tình huống nào khiến người ta cảm thấy sự giúp đỡ biến thành áp lực nợ nần?"
- Mở `knowledge/runs/RUN-xxxx.md` ghi nhận thời gian, kênh khảo sát và liên kết công khai.

### Bước 2: Bóc tách mẫu lập luận & Nghịch lý
- Rút ra 3–5 mẫu tình huống hoặc phản ứng tâm lý tiêu biểu.
- Xác định sự phân hóa: Có bao nhiêu luồng quan điểm trái ngược nhau? Đâu là phản ví dụ?

### Bước 3: Nhận diện thiên lệch của mẫu (Selection Bias)
- Nhận thức rõ ràng: Ý kiến trên mạng xã hội thường mang tính cực đoan, phân cực hoặc bức xúc tức thời.
- **Cấm đoán:** Tuyệt đối không kết luận "Đa số con người đều ích kỷ..." hay "Xã hội ngày nay đều..." chỉ từ vài bài đăng thảo luận (Ca T12).

### Bước 4: Chuyển giao câu hỏi sang nguồn sách / nghiên cứu
- Từ hiện tượng đời thực, tạo các câu hỏi nghiên cứu học thuật để chuyển giao cho skill `source-discovery` tìm kiếm nền tảng triết học hoặc tâm lý học hành vi.
