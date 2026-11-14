# HYA-05 — AGENT SKILLS & WORKFLOW

| Trường | Giá trị |
|---|---|
| Dự án | Hiyu Abyss |
| Mã tài liệu | `HYA-05` |
| Phiên bản | `1.0` |
| Ngày chuẩn hóa | `2026-11-13` |
| Môi trường mục tiêu | Google Antigravity |
| Phụ thuộc | `HYA-01` đến `HYA-04`; nghiệm thu theo `HYA-06` |
| Mục đích | Hợp đồng quy trình và bộ Agent Skills chuyên môn để agent tự nghiên cứu, sáng tác, kiểm nguồn, lưu kho |

> Tài liệu này quy định **kỹ năng nào làm việc gì, khi nào phải kích hoạt, tạo hồ sơ gì và trả kết quả nào**. Đây là đặc tả để Antigravity hiện thực hóa skill; không phải một skill duy nhất nhồi mọi nhiệm vụ.

## 1. Cách Antigravity tiếp nhận quy tắc và skills

- `AGENTS.md` ở root: nguyên tắc luôn đúng, cách đọc hệ tài liệu, quyền phê duyệt và ranh giới thao tác.
- `.agents/skills/<skill-name>/SKILL.md`: một năng lực chuyên môn có mô tả kích hoạt và quy trình riêng.
- `docs/HYA-01..06`: tài liệu chuẩn hóa; skills chỉ dẫn tới các mục liên quan, tránh chép lại cả bộ.
- `knowledge/`, `editorial/`, `indexes/`: thư viện và kết quả làm việc, theo HYA-04.

Antigravity hiện có tài liệu chính thức về `.agents/skills/` và `SKILL.md`: https://antigravity.google/docs/skills. Các skill có thể được chọn theo mô tả hoặc gọi theo tên; môi trường/phiên bản cụ thể quyết định giao diện. Thiết kế skill độc lập, không giả định mọi công cụ đều sẵn.

## 2. Nguyên tắc điều phối

**Một agent điều phối — nhiều skill chuyên trách.** Mỗi yêu cầu chọn đúng đường đi, không chạy cả 11 skill theo quán tính. Hướng làm việc là **tác vụ có trạng thái và có bằng chứng**: việc nào đã làm thì lưu, việc nào chưa làm phải ghi rõ.

Agent có thể đọc nguồn trên web bằng công cụ truy cập được cấp trong phiên. Khi nguồn bị chặn, không tạo trích dẫn hoặc ghi chú như thể đã đọc. Bài trên mạng xã hội là nguồn gợi câu hỏi, không phải chứng cứ học thuật tự thân.

## 3. Danh mục 11 skills

| Skill | Khi kích hoạt | Đầu ra chuẩn | Ưu tiên |
|---|---|---|---|
| `source-discovery` | Cần tìm sách, nghiên cứu, tác phẩm hoặc nguồn nền | `RUN`, `SRC` (metadata + truy cập thật) | P0 |
| `book-insight-summarization` | Có một phần tài liệu đã đọc, cần tóm luận điểm đúng | `NOTE`, cập nhật `SRC` | P0 |
| `citation-and-quote-audit` | Có trích dẫn/gán tác giả/luận điểm thực nghiệm | Audit bằng chứng, cập nhật `evidence_status` | P0 |
| `aphorism-writing` | Có IDEA hoặc luận điểm đã được chuẩn bị | Bản `TXT` nháp có `content_type` | P0 |
| `editorial-critique` | Có bản nháp hoặc cần sửa câu | Báo cáo lập luận/ngôn từ, bản sửa | P1 |
| `philosophical-argument-mapping` | Có luận điểm gây tranh luận, cần phân tích logic | `CON` hoặc `NOTE` mở rộng | P1 |
| `hypocrisy-paradox-mining` | Cần tìm khoảng cách lời nói–động cơ | `IDEA` với nghịch lý và phản đề | P1 |
| `metaphor-and-subtext` | Cần hình ảnh/ẩn dụ mới mà không làm sai ý | Phương án ẩn dụ kèm nghĩa đen và nghĩa chuyển | P1 |
| `semantic-novelty-review` | Chuẩn bị giữ/duyệt câu mới | Báo cáo trùng ý trong `TXT` và kho hiện có | P1 |
| `social-insight-mining` | Chủ động nghiên cứu thảo luận xã hội công khai | `RUN`, `IDEA`, câu hỏi đối chiếu | P1 |
| `content-lifecycle` | Cần tạo hồ sơ, liên kết, index, kiểm trạng thái | Hồ sơ/hồ sơ chỉ mục hợp lệ | P1 |

P0 là tập năng lực nhỏ cần dùng được trước; P1 mới mở rộng. Không diễn giải P0/P1 thành quyền tự triển khai xuất bản.

## 4. Chi tiết hợp đồng của các skill trọng tâm

### 4.1. `source-discovery`

**Input:** một câu hỏi nghiên cứu và chủ đề HYA-01. **Steps:** tạo truy vấn đa ngôn ngữ; tìm nguồn; phân loại (nguyên tác/danh mục/bình giải/nghiên cứu/thảo luận); xác định thực sự đã truy cập được gì; lưu `SRC`, nhật ký `RUN`. **Output:** danh sách 3–8 nguồn có lý do ưu tiên, ít nhất một hướng đọc tiếp. **Must not:** coi snippet hay mục lục là toàn văn; invent DOI/trang/chương.

### 4.2. `book-insight-summarization`

**Input:** nguồn `SRC`, phần văn bản truy cập được, mục tiêu đọc. **Steps:** tóm luận đề, các bước lập luận, chứng cứ, phản đề, bối cảnh, thuật ngữ; tách tác giả và suy luận Hiyu; lưu `NOTE`. **Output:** ghi chú có locator, access level và 2–3 câu hỏi phát triển. **Must not:** biến một đoạn preview thành kết luận về toàn cuốn sách.

### 4.3. `citation-and-quote-audit`

**Input:** câu/nhận định, phép gán tác giả, liên kết `SRC`/`NOTE`. **Steps:** xác nhận thư mục → so khớp nguyên văn → đọc ngữ cảnh → phân biệt lời nhân vật/bản dịch → đặt trạng thái nguồn. **Output:** `PASS`, `NEEDS_REVIEW`, `FAIL` kèm bằng chứng; trạng thái HYA-02. **Must not:** nâng nguồn vì nhiều website cùng lặp một câu nói.

### 4.4. `aphorism-writing`

**Input:** `IDEA` có nghịch lý/điểm nhìn; có thể có `NOTE`. **Steps:** phát biểu luận điểm bằng ngôn ngữ thô → kiểm phản đề → chọn góc nhìn → viết tối đa 3 biến thể khác cấu trúc → tự loại câu sáo → tạo TXT nháp. **Output:** câu chữ, lý do chọn, loại nội dung và link nguồn/cảm hứng. **Must not:** gán tên triết gia cho câu mới.

### 4.5. `editorial-critique`

**Input:** một `TXT` nháp. **Steps:** xem logic trước → soi mức khái quát/đọc ý nghĩ → soát từ sáo và ẩn dụ → đề xuất giữ/sửa/loại → ghi nhận xét. **Output:** nhận xét cụ thể từng vấn đề và bản sửa chỉ khi ý tưởng còn cứu được. **Must not:** chỉ khen “sâu sắc, sắc lạnh” hoặc phán xét bằng cảm giác mơ hồ.

### 4.6. `philosophical-argument-mapping`

**Input:** `SRC`/`NOTE` hoặc phát biểu lý thuyết. **Steps:** xác định tiền đề, kết luận, tiền giả định, phạm vi áp dụng, một cách diễn giải đối lập. **Output:** sơ đồ lập luận ngắn trong `CON` hay `NOTE`. **Must not:** đánh đồng lời của một trường phái với kiến thức thực nghiệm đã xác nhận.

### 4.7. `hypocrisy-paradox-mining`

**Input:** một tình huống/luận điểm. **Steps:** nêu giá trị được tuyên bố → mô tả hành vi thực tế → tìm động cơ khả dĩ → kiểm điều kiện làm đổi nghĩa → tìm phản ví dụ → ghi 2–5 `IDEA` khác biệt. **Must not:** tự tạo “đạo đức giả” bằng suy đoán động cơ không thể quan sát.

### 4.8. `metaphor-and-subtext`

**Input:** một luận điểm được hiểu rõ. **Steps:** tách quan hệ thực → chọn tối đa ba ẩn dụ → giải thích bản đồ tương ứng (ẩn dụ nào đại diện cái gì) → kiểm ẩn dụ có làm sai ý hay không → đề xuất câu rút gọn. **Must not:** thêm mặt nạ, vực sâu, bóng tối chỉ để trang trí.

### 4.9. `semantic-novelty-review`

**Input:** TXT đang duyệt và kho `editorial/content`. **Steps:** tìm trùng từ khóa và cụm; đọc các câu cùng topic; so khớp **phát hiện tư tưởng** và cú chuyển nghĩa, không chỉ từ ngữ; xuất `CLEAR`/`RELATED`/`DUPLICATE` kèm ID cụ thể. **Must not:** coi đổi đại từ hoặc thay từ đồng nghĩa là ý tưởng mới.

### 4.10. `social-insight-mining`

**Input:** một câu hỏi/đề tài xã hội. **Steps:** tìm thảo luận công khai truy cập hợp lệ → loại dữ liệu cá nhân → rút mẫu lập luận đối nghịch → ghi URL và giới hạn mẫu → tạo IDEA/chủ đề nghiên cứu thêm. **Must not:** vượt cơ chế chống bot, lấy thông tin không công khai, hoặc coi lời kể là đại diện số đông.

### 4.11. `content-lifecycle`

**Input:** trạng thái/ID của một hồ sơ. **Steps:** dùng template HYA-04 → tạo file đúng path → kiểm ID và liên kết → cập nhật chỉ mục → kiểm các thao tác cần người duyệt. **Output:** file hợp lệ và nhật ký thay đổi. **Must not:** tự gán `APPROVED`/`PUBLISHED`.

## 5. Vòng làm việc chuẩn: từ chủ đề đến câu nháp

```text
Câu hỏi nghiên cứu
   ├─> source-discovery → SRC/RUN
   ├─> book-insight-summarization → NOTE
   ├─> philosophical-argument-mapping → CON
   ├─> hypocrisy-paradox-mining → IDEA
   ├─> metaphor-and-subtext (nếu cần)
   ├─> aphorism-writing → TXT DRAFT
   ├─> editorial-critique
   ├─> citation-and-quote-audit (nếu có phép gán nguồn)
   ├─> semantic-novelty-review
   └─> content-lifecycle → TXT IN_REVIEW
                                    │
                                    ▼
                              Chủ dự án duyệt
```

Trình tự có thể rút ngắn khi đã có nguồn hoặc IDEA. Không rút ngắn **kiểm nguồn nếu có trích dẫn** hoặc **kiểm trùng/đánh giá trước khi trình duyệt**.

## 6. Ba tuyến nhiệm vụ cần hỗ trợ

### A. Bắt đầu từ một cuốn sách

1. Kiểm metadata và phần đọc được.
2. Ghi note theo chương/đoạn, giữ phản đề.
3. Chọn 1–3 luận điểm có sức khai thác.
4. Đưa vào IDEA/TXT theo HYA-04.
5. Báo rõ câu nào là diễn giải, câu nào là sáng tác mới.

### B. Bắt đầu từ một vấn đề xã hội

1. Tạo RUN với câu hỏi và nguồn công khai có thể truy cập.
2. Phân biệt phản ánh cá nhân với xu hướng có bằng chứng.
3. Liệt kê các cách giải thích, tìm phản ví dụ.
4. Ưu tiên đối chiếu với sách/nghiên cứu trước khi viết kết luận mạnh.
5. Tạo IDEA, chuyển sang quy trình sáng tác.

### C. Bắt đầu từ một câu văn sẵn có

1. Kiểm nó là trích dẫn, diễn giải hay câu sáng tác.
2. Phân tích tư tưởng và mức hợp lý.
3. Soát trùng ý/sao chép trá hình.
4. Đề xuất bản sửa, nêu điều được và mất; **không tự thay bản đã duyệt**.

## 7. Đầu ra cho mỗi yêu cầu người dùng

Một lần chạy phải báo ngắn gọn:

- **Đã làm:** những nguồn nào đã đọc, hồ sơ nào tạo/sửa, ID và đường dẫn.
- **Điều xác minh được:** bằng chứng, nguồn, mức truy cập.
- **Điều chưa xác minh:** rõ lý do, không che giấu.
- **Bản nháp cần duyệt:** bản câu chữ và nhận xét trọng tâm.
- **Việc còn mở:** cần người duyệt hoặc thêm nguồn gì.

Không tuyên bố “xong” nếu file chưa tồn tại hoặc không truy về được nguồn đã nêu.

## 8. Mẫu `SKILL.md` áp dụng cho Antigravity

Ví dụ dùng để agent tạo skill `book-insight-summarization`:

```markdown
---
name: book-insight-summarization
description: "Summarize accessible book chapters or essays into traceable argument notes for Hiyu Abyss. Use after a specific source and readable section are identified; preserve source locator, context and counterarguments."
---

# Book Insight Summarization

## Before starting
- Read docs/01_HIYU_ABYSS_PROJECT_INPUT.md sections 6–7.
- Read docs/02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md sections 3, 8.
- Read docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md section 6.

## Workflow
1. Identify the SRC record and actual accessible passage.
2. State precisely which passage has been read.
3. Extract thesis, reasoning, evidence, counterpoint, limitations.
4. Separate source claims from project interpretation.
5. Write or update NOTE; check links and locator.

## Stop conditions
- No accessible passage: report metadata-only and do not summarize.
- Uncertain author/edition: leave NEEDS_REVIEW instead of inventing.

## Deliverable
- A NOTE file and concise summary with factual provenance.
```

Mô tả kích hoạt cần **nói rõ khi nào sử dụng**. Nội dung skill nên ngắn, có tham chiếu tài liệu chi tiết, tránh đổ cả thư viện kiến thức vào mọi prompt.

## 9. Nội dung tối thiểu của `AGENTS.md`

Để đảm bảo agent hiểu hệ tài liệu, root `AGENTS.md` nên truyền đạt:

```markdown
# Hiyu Abyss — Agent Operating Rules

Read docs/01_HIYU_ABYSS_PROJECT_INPUT.md for project identity.
Follow HYA-02 for research and attribution; HYA-03 for writing;
HYA-04 for file format and state; HYA-05 for skills/routing;
HYA-06 for evaluation and approval gates.

Use project-local skills from .agents/skills when appropriate.
Keep source claims separate from project interpretations.
Never invent book passages, page numbers, authors, or study results.
Never self-approve or mark content as published.
For changed files, report paths, checks run, and remaining blockers.
```

Đây là **khung mẫu nội dung**. Người triển khai có thể viết tiếng Việt, miễn không làm đổi quy tắc.

## 10. Học hỏi từ GitHub Skills bên ngoài

Tuyển chọn theo **năng lực**, không nhập nguyên cả repository. Một số nguồn đã ghi trong HYA-01:

| Nguồn GitHub | Lợi ích học hỏi | Hướng tích hợp kiến thức |
|---|---|---|
| [jwynia — summarization](https://github.com/jwynia/agent-skills/blob/main/skills/general/writing/revision/summarization/SKILL.md) | Tóm tắt theo mục tiêu/phạm vi | Điều chỉnh thành `book-insight-summarization` |
| [tompulsarlabs — writing-voice-custom](https://github.com/tompulsarlabs/writing-voice-skill/blob/main/writing-voice-custom/SKILL.md) | Giữ giọng và chất lượng lập luận | `editorial-critique`, `aphorism-writing` |
| [alt-code-ai — fiction-writing-prose](https://github.com/alt-code-ai/agent/blob/main/skills/fiction-writing-prose/SKILL.md) | Ẩn dụ, nhịp điệu, subtext | `metaphor-and-subtext` |
| [KalarisLabs — citation-verification](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/citation-verification/SKILL.md) | Kiểm metadata nghiên cứu | `citation-and-quote-audit` (chỉ một phần) |
| [KalarisLabs — paper-lookup](https://github.com/KalarisLabs/research-agent-skills/blob/main/skills/paper-lookup/SKILL.md) | Khám phá nghiên cứu có provenance | `source-discovery` (nghiên cứu học thuật) |
| [Anthropic — skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | Soạn và kiểm thử skill | Khung tạo 11 skill dự án |

Trước khi tái sử dụng nội dung/code từ repository, kiểm license, phần phụ thuộc, quyền truy cập và nguy cơ thực thi script. **Skill bên ngoài không phải nguồn chứng minh triết học và không được thay thế nguồn sách.**

## 11. Quy tắc sử dụng trình duyệt và nguồn ngoài

- Ưu tiên nguồn có tác giả, xuất xứ, URL xác định; ghi ngày truy cập.
- Tôn trọng chính sách website, giới hạn truy cập, quyền riêng tư và quyền tác giả.
- Không chạy script lấy dữ liệu hoặc cài repo từ internet chỉ vì mô tả skill yêu cầu; cần xem xét an toàn trước.
- Nếu không có browser trong một phiên, làm việc với tài liệu đã có, đánh dấu thiếu nguồn; không tạo lời khẳng định đã nghiên cứu web.
- Trích dẫn phải được đối chiếu ở HYA-02 và qua kiểm tra HYA-06.

## 12. Trình tự hiện thực hóa skill

**Mốc 1 — năng lực tối thiểu:** tạo `source-discovery`, `book-insight-summarization`, `aphorism-writing`, `citation-and-quote-audit`. Thử một nguồn thật truy cập được và một trường hợp không thể truy cập. Mỗi skill phải có mô tả, hợp đồng đầu ra và stop condition.

**Mốc 2 — biên tập sâu:** bổ sung `editorial-critique`, `philosophical-argument-mapping`, `hypocrisy-paradox-mining`, `metaphor-and-subtext`. Thử các ví dụ HYA-03, yêu cầu câu mới khác cấu trúc.

**Mốc 3 — vận hành kho:** thêm `semantic-novelty-review`, `social-insight-mining`, `content-lifecycle`. Thử liên kết đầy đủ HYA-04, báo lỗi trùng ý và chặn thao tác tự duyệt.

Mỗi mốc **chỉ được coi là hoàn thành khi có đầu ra thực** và chạy các ca kiểm thử tương ứng trong HYA-06.

## 13. Hợp đồng hoàn thành HYA-05

- [ ] Các skill nằm đúng `.agents/skills/<name>/SKILL.md`, có frontmatter hợp lệ.
- [ ] Mô tả kích hoạt không quá mơ hồ hoặc trùng nhau.
- [ ] Skill đọc đúng tài liệu liên quan thay vì đoán lại quy tắc.
- [ ] Mỗi skill có input, output, stop conditions và ít nhất một ca kiểm thử.
- [ ] Đầu ra ghi đúng hồ sơ theo HYA-04, không tự phê duyệt.
- [ ] Một yêu cầu nghiên cứu/sáng tác đi qua được vòng từ nguồn/ý tưởng đến TXT `IN_REVIEW`.
- [ ] Mọi kết luận về trang sách hoặc công trình học thuật đều có bằng chứng truy nguyên được.

**Handoff:** HYA-06 xác định bộ ca kiểm thử, điểm chất lượng, điều kiện loại và chuẩn nghiệm thu vận hành.
