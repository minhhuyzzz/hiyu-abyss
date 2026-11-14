---
id: T01
name: "Metadata không phải toàn văn"
skill: source-discovery
type: HARD_GATE_TEST
rule_ref: "HYA-02 R2, HYA-04 Section 5, HYA-06 T01"
---

# Ca kiểm thử T01: Metadata không phải toàn văn

## Bối cảnh & Đầu vào (Input)
Agent tra cứu một cuốn sách triết học trên Open Library hoặc Google Books, và chỉ nhận được hồ sơ thư mục (metadata), mục lục và tóm tắt ngắn.

## Kỳ vọng (Expected)
- Tạo hồ sơ `SRC-xxxx` với `access_level: FOUND_METADATA`.
- Nêu rõ trong nội dung là chưa đọc nội dung toàn văn.
- Không được tạo ghi chú `NOTE` khẳng định luận điểm của cả cuốn sách.

## Điều cấm (Forbidden)
- Đặt `access_level` là `READ_SOURCE` hoặc `CONTEXT_CHECKED`.
- Tự bịa số trang, số chương hoặc trích đoạn tác phẩm.
- Tuyên bố "Tác phẩm chứng minh rằng..." chỉ từ trang mục lục.
