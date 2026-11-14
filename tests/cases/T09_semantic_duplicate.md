---
id: T09
name: "Trùng ý khác câu chữ"
skill: semantic-novelty-review
type: HARD_GATE_TEST
rule_ref: "HYA-03 Section 2, HYA-06 T09, Hard Gate G2"
---

# Ca kiểm thử T09: Trùng ý khác câu chữ

## Bối cảnh & Đầu vào (Input)
- Trong kho đã lưu câu TXT-0010: "Ta dễ tha thứ cho mình lỗi lầm mà ta sẵn sàng kết án ở người khác."
- Bản thảo mới nộp vào: "Điều ta phán xét gay gắt ở thiên hạ lại thường được miễn trừ khi chính ta phạm phải."

## Kỳ vọng (Expected)
- Skill `semantic-novelty-review` phát hiện: Mặc dù từ ngữ khác nhau, cơ chế tư tưởng và phát hiện tâm lý là giống nhau 100% (Tiêu chuẩn kép trong sự tha thứ).
- Đánh dấu `DUPLICATE` và kích hoạt Hard Gate G2. Chặn đưa vào danh sách duyệt độc lập.

## Điều cấm (Forbidden)
- Bỏ qua trùng lặp chỉ vì thuật toán so khớp chuỗi ký tự (exact string match) không tìm thấy chuỗi trùng.
- Coi việc thay từ đồng nghĩa là sáng tác ý tưởng mới.
