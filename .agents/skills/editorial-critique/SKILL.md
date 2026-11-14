---
name: editorial-critique
description: "Biên tập phản biện đa tầng (Tư tưởng, Logic, Ngôn ngữ, Dấu ấn) và chấm điểm 6 chiều cho bản thảo triết ngôn. Phát hiện lỗi quy chụp, sáo rỗng hoặc lỏng lẻo lập luận."
---

# Editorial Critique (Biên tập & Phản biện triết ngôn)

## Mục đích & Ranh giới
Kỹ năng này hoạt động như một biên tập viên nghiêm khắc, rà soát bản thảo câu chữ qua 4 lượt độc lập, chỉ ra chính xác điểm yếu của câu và chấm điểm theo khung tiêu chí HYA-06.
- **Ranh giới:** Không khen ngợi chung chung ("câu rất hay, rất lạnh lùng"). Mọi nhận xét phải chỉ rõ từ ngữ, cấu trúc và lý do cụ thể.

## Tài liệu tham chiếu bắt buộc
- [docs/01_HIYU_ABYSS_PROJECT_INPUT.md](file:///c:/hiyuabyss/docs/01_HIYU_ABYSS_PROJECT_INPUT.md) — Mục 10 (Thước đo chất lượng).
- [docs/03_HIYU_ABYSS_EDITORIAL_STYLE_BIBLE.md](file:///c:/hiyuabyss/docs/03_HIYU_ABYSS_EDITORIAL_STYLE_BIBLE.md) — Mục 7 (Ví dụ đạt/chưa đạt), Mục 8 (Cấu trúc đánh giá và sửa bản thảo).
- [docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md](file:///c:/hiyuabyss/docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md) — Mục 2 (Bộ điểm văn bản 1–5), Mục 3 (Hard Gates G1–G6).

## Quy trình 4 lượt phản biện (Four Review Passes)

### Lượt 1: Lượt Tư tưởng (Philosophical Pass)
- Câu này thật sự phát hiện điều gì mới về tâm lý con người?
- Đây là một quy luật kiểm chứng được hay chỉ là cảm xúc bất mãn cá nhân?
- Động cơ được nói như một *khả năng* hay bị kết án như một *chân lý tuyệt đối*?

### Lượt 2: Lượt Logic & Lập luận (Logic Pass)
- Mệnh đề mở đầu có thực sự nâng đỡ mệnh đề kết luận không?
- Cú đảo chiều có hợp lý hay chỉ gây sốc nhân tạo?
- Phản ví dụ mạnh nhất chống lại câu này là gì? Câu có chịu được phản ví dụ đó không?

### Lượt 3: Lượt Ngôn ngữ & Nhịp điệu (Literary Pass)
- Có từ nào thừa có thể cắt bỏ mà câu không mất nghĩa?
- Động từ đã sắc bén chưa?
- Ẩn dụ có phục vụ ý nghĩa hay chỉ là trang trí? (Nếu không có ẩn dụ nhưng sắc, để `imagery = null`).
- Đọc to câu văn: có chỗ nào vấp thanh điệu hoặc trúc trắc không cần thiết không?

### Lượt 4: Lượt Dấu ấn & Độc bản (Voice Pass)
- Câu có bị ảnh hưởng bởi mô-típ châm ngôn quen thuộc trên mạng không?
- Câu có mang lại dư âm khiến người đọc quay lại soi chính mình (tính phản tư) hay chỉ khiến họ thỏa mãn đi phán xét người khác?

## Khung chấm điểm 6 chiều (Thang 1–5)
- `insight` (Độ sâu phát hiện): 1–5
- `coherence` (Tính chặt chẽ logic): 1–5
- `precision` (Độ chuẩn xác từ ngữ, tránh quy chụp): 1–5
- `imagery` (Sức gợi của ẩn dụ chức năng): 1–5 (hoặc `null` nếu câu trực diện)
- `resonance` (Độ đọng lại và khả năng phản tư): 1–5
- `originality` (Tính độc bản và góc nhìn riêng): 1–5

## Đề xuất kết luận biên tập
- `PASS_EDITORIAL`: Khi `insight`, `coherence`, `precision`, `originality` ≥ 4, `resonance` ≥ 3, điểm trung bình ≥ 4.0 và không vi phạm hard gate.
- `REVISE`: Khi ý tưởng có tiềm năng nhưng câu chữ còn lỗi logic, quy chụp hoặc sáo rỗng. Cung cấp hướng sửa cụ thể.
- `REJECT`: Khi ý tưởng trống rỗng, tự mâu thuẫn vô nghĩa, hoặc sao chép ý người khác.
