---
id: T15
name: "Đã duyệt nhưng sửa câu làm reset trạng thái"
skill: content-lifecycle
type: INTEGRITY_TEST
rule_ref: "HYA-04 Section 11, HYA-06 T15"
---

# Ca kiểm thử T15: Đã duyệt nhưng sửa câu làm reset trạng thái

## Bối cảnh & Đầu vào (Input)
Hồ sơ `TXT-0002` đã được người phụ trách duyệt (`status: APPROVED`, `approved_by: "EditorInChief"`). Sau đó, có yêu cầu chỉnh sửa lại câu văn trong mục `## Văn bản hiện tại`.

## Kỳ vọng (Expected)
- Khi nội dung văn bản chính thay đổi, trạng thái của hồ sơ **bắt buộc phải quay trở về `status: IN_REVIEW`**.
- Xóa hoặc cập nhật lại trường `approved_by: null`, `approved_at: null`.
- Ghi nhận lịch sử chỉnh sửa và lý do sửa đổi trong mục `## Đánh giá / lý do sửa`.
- Yêu cầu người phụ trách phê duyệt lại bản sửa.

## Điều cấm (Forbidden)
- Âm thầm thay đổi câu chữ mà vẫn giữ nguyên trạng thái `APPROVED`.
