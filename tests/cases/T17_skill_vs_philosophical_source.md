---
id: T17
name: "Khác biệt giữa tài liệu kỹ thuật và nguồn triết học"
skill: citation-and-quote-audit
type: METHODOLOGY_TEST
rule_ref: "HYA-01 Section 6.7, HYA-06 T17"
---

# Ca kiểm thử T17: Khác biệt giữa tài liệu kỹ thuật và nguồn triết học

## Bối cảnh & Đầu vào (Input)
Agent tham khảo một kho GitHub skill hướng dẫn kỹ thuật viết văn (ví dụ: `summarization` của jwynia hoặc `writing-voice-skill`).

## Kỳ vọng (Expected)
- Xác định đây là tài liệu phương pháp thao tác kỹ thuật (Agent Skill), không phải là công trình tâm lý học hay tác phẩm triết học.
- Tuyệt đối không đưa repository GitHub này vào hồ sơ `knowledge/sources/SRC-xxxx.md` như một nguồn tri thức minh chứng cho bản chất con người.

## Điều cấm (Forbidden)
- Trích dẫn file README hoặc SKILL.md của một repository GitHub như là bằng chứng thực nghiệm hay lập luận triết học.
