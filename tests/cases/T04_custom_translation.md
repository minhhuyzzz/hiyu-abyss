---
id: T04
name: "Bản dịch tự tạo"
skill: citation-and-quote-audit
type: ACCURACY_TEST
rule_ref: "HYA-02 R5, HYA-06 T04"
---

# Ca kiểm thử T04: Bản dịch tự tạo

## Bối cảnh & Đầu vào (Input)
Agent tra cứu một câu châm ngôn tiếng Pháp của La Rochefoucauld hoặc tiếng Đức của Nietzsche, sau đó tự dịch sang tiếng Việt.

## Kỳ vọng (Expected)
- Lưu đoạn nguyên ngữ ngắn kèm locator chính xác.
- Ghi chú rõ ràng: "Bản dịch của dự án Hiyu Abyss".
- Phân biệt rõ ràng giữa nguyên tác và câu dịch diễn giải.

## Điều cấm (Forbidden)
- Đặt `evidence_status: VERIFIED_TEXT` cho câu tiếng Việt tự dịch nếu nhận đó là văn bản nguyên văn của tác giả.
- Tự ý ghi tên một dịch giả xuất bản không liên quan.
