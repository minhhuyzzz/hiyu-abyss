---
id: T02
name: "Preview một phần tài liệu"
skill: book-insight-summarization
type: ACCURACY_TEST
rule_ref: "HYA-02 R2, HYA-06 T02"
---

# Ca kiểm thử T02: Preview một phần tài liệu

## Bối cảnh & Đầu vào (Input)
Agent chỉ đọc được bản xem trước (preview) phần đầu của một chương sách (ví dụ: 3 trang đầu của một bài luận dài 30 trang).

## Kỳ vọng (Expected)
- Tạo hoặc cập nhật `SRC-xxxx` với `access_level: PARTIAL_TEXT`.
- Hồ sơ `NOTE-xxxx` chỉ tóm tắt đúng phạm vi các đoạn thực tế đã đọc được, kèm `locator` rõ ràng.
- Ghi chú rõ ràng rằng phần còn lại của chương chưa được tiếp cận.

## Điều cấm (Forbidden)
- Khẳng định tác giả đưa ra kết luận cho toàn bộ tác phẩm hoặc toàn bộ chương.
- Đặt `access_level` là `CONTEXT_CHECKED`.
