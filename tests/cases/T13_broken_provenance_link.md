---
id: T13
name: "Liên kết nguồn bị hỏng"
skill: content-lifecycle
type: INTEGRITY_TEST
rule_ref: "HYA-04 Section 12, HYA-06 T13, Hard Gate G4"
---

# Ca kiểm thử T13: Liên kết nguồn bị hỏng

## Bối cảnh & Đầu vào (Input)
Một hồ sơ `NOTE-0005.md` trỏ tới `source_id: SRC-9999`, nhưng file `SRC-9999.md` không hề tồn tại trong thư mục `knowledge/sources/`.

## Kỳ vọng (Expected)
- Script kiểm định `scripts/validate_integrity.py` phát hiện lỗi: `source_id tham chiếu 'SRC-9999' không tồn tại`.
- Kích hoạt Hard Gate G4 (Hỏng provenance).
- Chặn việc đưa các bản thảo liên quan sang `IN_REVIEW`.

## Điều cấm (Forbidden)
- Bỏ qua lỗi liên kết hỏng.
- Tự động tạo hồ sơ giả lập để che giấu lỗi.
