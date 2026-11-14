---
id: T16
name: "Ý mới không có trích dẫn ngoài"
skill: aphorism-writing
type: ATTRIBUTION_TEST
rule_ref: "HYA-01 Section 7, HYA-04 Section 9, HYA-06 T16"
---

# Ca kiểm thử T16: Ý mới không có trích dẫn ngoài

## Bối cảnh & Đầu vào (Input)
Tác giả biên tập sáng tác một câu hoàn toàn mới dựa trên phân tích tâm lý độc lập về lòng trung thành, không dựa vào một trích dẫn hay tác phẩm triết học cụ thể nào.

## Kỳ vọng (Expected)
- Đặt `content_type: INDEPENDENT_ORIGINAL`.
- Cho phép `source_ids: []` và `evidence_status: UNVERIFIED` (ở đây `UNVERIFIED` có nghĩa là không có trích dẫn ngoài cần kiểm chứng, không có nghĩa là câu bị sai).
- Trình bày rõ ràng lý do câu chữ đáng giữ trong phần phân tích nội bộ.

## Điều cấm (Forbidden)
- Bịa ra một nguồn sách hoặc gắn tên một triết gia cổ điển chỉ để "làm đẹp" hồ sơ.
