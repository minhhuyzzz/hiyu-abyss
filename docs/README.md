# Hiyu Abyss — Bộ tài liệu nền tảng cho Antigravity

**Phiên bản bộ tài liệu:** 1.0 · **Ngày:** 2026-11-13 · **Ngôn ngữ:** Tiếng Việt

Đây là **bộ tài liệu kiến trúc biên tập**, dùng để Google Antigravity hiểu và thiết lập hệ thống nghiên cứu, phân tích và sáng tác triết ngôn Hiyu Abyss. Các file 02–06 được xây dựa trên tài liệu đầu vào 01; chúng không phải thành phẩm đã triển khai trong workspace và không thay thế các file `SKILL.md` sẽ được tạo sau.

## Đọc theo thứ tự

| Mã | Tài liệu | Trả lời câu hỏi |
|---|---|---|
| HYA-01 | [Project Input](01_HIYU_ABYSS_PROJECT_INPUT.md) | Hiyu Abyss là gì? Theo đuổi chủ đề, nguồn và phẩm chất câu chữ nào? |
| HYA-02 | [Research & Source Standard](02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md) | Nghiên cứu, đọc/tóm ý sách, kiểm nguồn và phản biện như thế nào? |
| HYA-03 | [Editorial Style Bible](03_HIYU_ABYSS_EDITORIAL_STYLE_BIBLE.md) | Viết câu chữ tiếng Việt ra sao để sắc, có logic, có ẩn dụ mà không sáo? |
| HYA-04 | [Knowledge & Content Model](04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md) | Lưu hồ sơ, ID, trạng thái, liên kết và lịch sử tư tưởng thế nào? |
| HYA-05 | [Agent Skills & Workflow](05_HIYU_ABYSS_AGENT_SKILLS_WORKFLOW.md) | Trong Antigravity cần những skill nào và phối hợp theo trình tự nào? |
| HYA-06 | [Quality Evaluation](06_HIYU_ABYSS_QUALITY_EVALUATION.md) | Câu nào đạt, bị loại, phải sửa? Làm sao kiểm nghiệm skill? |

## Quy trình tối giản

```text
HYA-01 (định vị)
   └─> HYA-02 (nghiên cứu và nguồn)
        └─> HYA-03 (biên tập tiếng Việt)
             └─> HYA-04 (dữ liệu và trạng thái)
                  └─> HYA-05 (skill và quy trình)
                       └─> HYA-06 (kiểm thử và người duyệt)
```

**Một quy tắc xuyên suốt:** không bịa văn bản nguồn, không đồng nhất lời nhân vật với lập trường tác giả, không đưa câu sáng tác mới dưới tên triết gia, không tự phê duyệt bài thay chủ dự án.

## Cách sử dụng trong Google Antigravity

1. Tạo workspace dự án `hiyu-abyss`, đặt cả sáu file vào thư mục `docs/`.
2. Yêu cầu agent **đọc HYA-01 đến HYA-06 theo thứ tự**, kiểm tra sự nhất quán rồi lập danh sách công việc ưu tiên.
3. Yêu cầu agent thực hiện **mốc P0** của HYA-05 và kiểm thử tương ứng HYA-06.
4. Kiểm tra các file và kết quả thực tế trước khi triển khai tiếp P1.

### Lệnh giao cho Antigravity

> Đọc toàn bộ thư mục `docs/` theo thứ tự HYA-01 → HYA-06. Hãy dùng HYA-01 làm ngữ cảnh dự án, HYA-02/03 làm chuẩn nghiên cứu và biên tập, HYA-04 làm hợp đồng dữ liệu, HYA-05 làm yêu cầu xây dựng skill, HYA-06 làm tiêu chí nghiệm thu. Đầu tiên hãy kiểm tra tính nhất quán, sau đó triển khai mốc P0 thành các file và skill thật trong workspace. Tạo một ví dụ từ nguồn có thể truy cập, chạy ca kiểm thử liên quan và báo cáo file nào đã được tạo, bằng chứng đã kiểm và những phần còn chưa hoàn tất. Không thay quyền phê duyệt nội dung của tôi.

## Giới hạn của bộ này

Đây là đặc tả để *triển khai*, không phải một dự án phần mềm đã chạy, cũng chưa phải kho sách đã được thu thập. Các nguồn và skill bên ngoài trong HYA-01/HYA-05 là **tài liệu tra cứu có chỉ dẫn**; chỉ được tuyên bố đã kiểm tra một câu trích khi công việc đối chiếu thực sự xảy ra.

## Tài liệu chính thức để đối chiếu khi triển khai

- Google Antigravity Agent Skills: https://antigravity.google/docs/skills
- Chuẩn Agent Skills: https://agentskills.io/
- Project Gutenberg — robot access: https://www.gutenberg.org/policy/robot_access.html
- Open Library API: https://openlibrary.org/developers/api

---

**Tài liệu nguồn:** `01_HIYU_ABYSS_PROJECT_INPUT.md` v1.1 (giữ nguyên bản được cung cấp); `HYA-02`–`HYA-06` v1.0 (soạn dựa trên HYA-01).
