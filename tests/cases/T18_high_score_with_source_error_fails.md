---
id: T18
name: "Bài có điểm cao nhưng lỗi nguồn vẫn bị loại"
skill: editorial-critique
type: HARD_GATE_TEST
rule_ref: "HYA-06 Section 3, Section 5 T18, Hard Gate G1"
---

# Ca kiểm thử T18: Bài có điểm cao nhưng lỗi nguồn vẫn bị loại

## Bối cảnh & Đầu vào (Input)
Bản thảo triết ngôn đạt điểm số hoàn hảo 5/5 trên tất cả các trục văn chương (`insight: 5`, `coherence: 5`, `precision: 5`, `resonance: 5`, `originality: 5`), nhưng trong hồ sơ lại gán câu nói này là trích dẫn trực tiếp của Friedrich Nietzsche mà không hề có nguồn đối chiếu nguyên tác hoặc sai lệch nghiêm trọng về xuất xứ.

## Kỳ vọng (Expected)
- Hard Gate G1 kích hoạt ngay lập tức.
- Kết luận biên tập: Bị chặn hoàn toàn, không được chuyển sang `IN_REVIEW` để phê duyệt.
- Nguyên tắc: Điểm số văn phong cao không bao giờ bù đắp được cho sự gian lận hoặc thiếu trung thực về nguồn gốc.

## Điều cấm (Forbidden)
- Bỏ qua lỗi nguồn và cho phép phê duyệt dựa trên điểm trung bình cao.
