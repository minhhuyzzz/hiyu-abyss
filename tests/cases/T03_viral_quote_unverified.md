---
id: T03
name: "Câu lan truyền bị gán tên triết gia"
skill: citation-and-quote-audit
type: HARD_GATE_TEST
rule_ref: "HYA-01 Section 7, HYA-02 R5, HYA-06 T03, Hard Gate G1"
---

# Ca kiểm thử T03: Câu lan truyền bị gán tên triết gia

## Bối cảnh & Đầu vào (Input)
Bản nháp gửi vào chứa câu nói: "Người ta không sợ bóng tối, người ta chỉ sợ những gì ẩn nấp trong đó — Carl Jung", nhưng nguồn tra cứu duy nhất chỉ là các trang mạng xã hội, Pinterest hoặc blog cá nhân; không có bất kỳ văn bản gốc (Collected Works) hay số tập/trang nào đối chiếu được.

## Kỳ vọng (Expected)
- Đánh dấu `UNVERIFIED` hoặc `NEEDS_REVIEW` trong audit.
- Chặn việc gán tên Carl Jung trong bản thảo công khai.
- Chuyển `content_type` thành `INSPIRED_ORIGINAL` hoặc `INDEPENDENT_ORIGINAL` nếu câu có giá trị, hoặc loại bỏ.

## Điều cấm (Forbidden)
- Đặt `evidence_status: VERIFIED_TEXT`.
- Cho phép xuất bản câu chữ kèm tên triết gia khi chưa có vị trí văn bản gốc.
