---
id: T06
name: "Nghịch lý giả"
skill: aphorism-writing
type: LOGIC_TEST
rule_ref: "HYA-03 Section 2 & 4, HYA-06 T06"
---

# Ca kiểm thử T06: Nghịch lý giả

## Bối cảnh & Đầu vào (Input)
Bản thảo câu chữ: "Con người chỉ thích nói dối vì chân lý là bóng tối của linh hồn."

## Kỳ vọng (Expected)
- Biên tập viên (`editorial-critique`) bắt lỗi: Hai vế không có quan hệ nhân quả hay logic nội tại; đây là một nghịch lý gượng ép, dùng từ ngữ trừu tượng ("bóng tối", "linh hồn") để ngụy trang sự thiếu vắng lập luận.
- Trả về `REVISE` hoặc `REJECT`, yêu cầu xác định lại luận điểm cốt lõi.

## Điều cấm (Forbidden)
- Chấm điểm cao hoặc cho qua chỉ vì câu nghe có vẻ bí hiểm hoặc u tối.
