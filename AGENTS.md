# HIYU ABYSS — AGENT OPERATING RULES

> **Vai trò:** Quy tắc vận hành bắt buộc dành cho mọi AI Agent hoạt động trong workspace `hiyu-abyss`.

---

## 1. Ràng buộc pháp quy & Thứ tự tra cứu

1. **Định danh & Bản sắc dự án:** Đọc [docs/01_HIYU_ABYSS_PROJECT_INPUT.md](file:///c:/hiyuabyss/docs/01_HIYU_ABYSS_PROJECT_INPUT.md) (`HYA-01`) để nắm vững triết lý *Dark Psychological Aphorism*, tuyên ngôn biên tập, 20 nhóm chủ đề hạt nhân và các cơ chế tư tưởng.
2. **Nghiên cứu & Chuẩn nguồn:** Tuân thủ tuyệt đối [docs/02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md](file:///c:/hiyuabyss/docs/02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md) (`HYA-02`). Phân biệt rạch ròi giữa quan sát văn bản gốc (`observed_text`), luận điểm tác giả (`author_argument`) và suy luận dự án (`project_interpretation`).
3. **Quy chuẩn văn phong biên tập:** Tuân thủ [docs/03_HIYU_ABYSS_EDITORIAL_STYLE_BIBLE.md](file:///c:/hiyuabyss/docs/03_HIYU_ABYSS_EDITORIAL_STYLE_BIBLE.md) (`HYA-03`). Câu phải sắc, đúng mực, nén, gợi, có nhịp và có bản sắc; loại bỏ hoàn toàn sáo ngữ AI và ẩn dụ rỗng.
4. **Mô hình dữ liệu & Quản lý phiên bản:** Tuân thủ [docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md](file:///c:/hiyuabyss/docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md) (`HYA-04`). Mọi thực thể (`SRC`, `NOTE`, `CON`, `IDEA`, `TXT`, `RUN`) phải có YAML frontmatter chuẩn, ID bất biến, liên kết toàn vẹn và lịch sử lưu trong Git.
5. **Quy trình & Kỹ năng tác tử:** Sử dụng các skill chuyên môn tại `.agents/skills/` theo [docs/05_HIYU_ABYSS_AGENT_SKILLS_WORKFLOW.md](file:///c:/hiyuabyss/docs/05_HIYU_ABYSS_AGENT_SKILLS_WORKFLOW.md) (`HYA-05`). Không chạy tràn lan các skill không liên quan.
6. **Cổng kiểm định & Tiêu chí nghiệm thu:** Đánh giá mọi bản thảo và bằng chứng theo [docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md](file:///c:/hiyuabyss/docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md) (`HYA-06`). Vượt qua 6 hard gates trước khi trình duyệt.

---

## 2. Các ranh giới cấm vượt (Hard Boundaries)

- **Tuyệt đối không bịa đặt nguồn:** Không bao giờ tự bịa tên sách, số trang, số chương, tác giả, DOI, trích đoạn hay kết quả nghiên cứu khoa học.
- **Không nâng trạng thái truy cập ảo:** Chỉ gán `READ_SOURCE` hoặc `CONTEXT_CHECKED` khi đã thực sự đọc văn bản. Nếu chỉ có kết quả tìm kiếm/metadata, dừng ở `FOUND_METADATA`. Nếu chỉ đọc preview/đoạn trích, chỉ ghi `PARTIAL_TEXT`.
- **Không đồng nhất nhân vật với tác giả:** Lời nhân vật hoặc người kể chuyện trong văn học hư cấu không mặc nhiên là triết lý của tác giả.
- **Không tự phê duyệt hay tự xuất bản:** Agent được phép chuyển trạng thái `DRAFT ↔ IN_REVIEW`, đề xuất `PASS_EDITORIAL`, `REVISE`, `REJECT`, nhưng **nghiêm cấm tự đổi sang `APPROVED` hoặc `PUBLISHED`** khi chưa có xác nhận từ người phụ trách.
- **Không gán tên triết gia cho câu sáng tác mới:** Câu mới lấy cảm hứng từ chủ đề phải đánh dấu `INSPIRED_ORIGINAL`; câu phân tích độc lập phải là `INDEPENDENT_ORIGINAL`. Tuyệt đối không mượn danh Nietzsche, Jung, Freud, Dostoevsky, Pascal... cho câu chữ của dự án.
- **Không đánh đồng kỹ năng và nguồn:** Các kho Agent Skills bên ngoài (GitHub) là tài liệu kỹ thuật/phương pháp thao tác, không phải nguồn tư tưởng hay bằng chứng tâm lý.

---

## 3. Quy trình bàn giao & Báo cáo kết quả

Khi hoàn thành bất kỳ lượt nghiên cứu hay biên tập nào, Agent phải báo cáo rõ ràng:
1. **Các file đã tạo/chỉnh sửa:** Đường dẫn tuyệt đối, ID và trạng thái.
2. **Điều xác minh được:** Bằng chứng văn bản, URL thực tế, mức truy cập và vị trí đối chiếu.
3. **Điều chưa xác minh:** Rõ ràng, minh bạch, không che giấu khoảng trống tri thức.
4. **Bản thảo cần duyệt:** Nội dung hiện tại kèm đánh giá 6 chiều và lý do biên tập.
5. **Các việc còn mở:** Những việc cần người phụ trách phê duyệt hoặc cần thêm nguồn bổ sung.
