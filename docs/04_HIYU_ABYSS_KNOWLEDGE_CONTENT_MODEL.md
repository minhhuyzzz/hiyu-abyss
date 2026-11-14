# HYA-04 — KNOWLEDGE & CONTENT MODEL

| Trường | Giá trị |
|---|---|
| Dự án | Hiyu Abyss |
| Mã tài liệu | `HYA-04` |
| Phiên bản | `1.0` |
| Ngày chuẩn hóa | `2026-11-13` |
| Phụ thuộc | `HYA-01`, `HYA-02`, `HYA-03` |
| Mục đích | Cách lưu, liên kết, kiểm tra và quản lý phiên bản tri thức / nội dung bằng Markdown |

> **Nguồn chân lý của hệ thống là file Markdown có ID bất biến và lịch sử Git.** Không đặt nội dung vào bảng tính hoặc thư mục chỉ dựa vào trạng thái; không lấy tên file làm tên tác phẩm. Trạng thái thay đổi trong metadata, đường dẫn không cần đổi.

## 1. Nguyên tắc kiến trúc thông tin

1. **Một thực thể — một hồ sơ chuẩn.** Không lập hai hồ sơ nguồn cho cùng một ấn bản chỉ vì xuất hiện ở hai URL.
2. **Có liên kết có nghĩa.** `SOURCE → NOTE → CONCEPT/IDEA → CONTENT` là tuyến truy nguyên, không chỉ gắn nhiều hashtag tùy ý.
3. **Định danh độc lập với tên.** Đổi nhan đề/đổi câu không làm thay ID.
4. **Không bịa dữ liệu thiếu.** Trường chưa biết dùng `null` hoặc trạng thái chưa kiểm; không điền giả trang, năm hoặc tên người dịch.
5. **Văn bản nguyên gốc khác ghi chú nghiên cứu.** Phân biệt câu trích, luận điểm của nguồn và suy luận riêng.
6. **Phê duyệt là hành động của người.** Agent có thể đánh giá, đề xuất trạng thái, nhưng không tự ghi `APPROVED` khi không có xác nhận của chủ dự án.
7. **Lưu lịch sử ngay trong Git.** Không tạo các bản `final-final-v2` bên cạnh một file chính.

## 2. Sáu loại hồ sơ chính

| Mã | Loại | Công dụng | ID mẫu |
|---|---|---|---|
| `SRC` | Source | Một tác phẩm, ấn bản, bài nghiên cứu hoặc bài viết công khai định danh | `SRC-0001` |
| `NOTE` | Reading Note | Tóm ý và đối chiếu một phần nội dung nguồn đã đọc | `NOTE-0001` |
| `CON` | Concept | Khái niệm/nghịch lý có thể khai thác qua nhiều nguồn | `CON-0001` |
| `IDEA` | Idea | Một quan sát, câu hỏi hoặc góc nhìn đủ rõ để phát triển câu | `IDEA-0001` |
| `TXT` | Content | Một câu/bài triết ngôn có bản thảo và vòng đời biên tập | `TXT-0001` |
| `RUN` | Research Run | Nhật ký một đợt tìm kiếm/nghiên cứu, kể cả trường hợp thất bại | `RUN-0001` |

Mỗi ID là chuỗi duy nhất trong repository. Không tái sử dụng ID đã xóa; nếu loại bỏ hồ sơ, nên để trạng thái/archive để giữ liên kết.

## 3. Cấu trúc thư mục chuẩn đề xuất

```text
hiyu-abyss/
├── README.md
├── AGENTS.md
├── docs/
│   ├── 01_HIYU_ABYSS_PROJECT_INPUT.md
│   ├── 02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md
│   ├── 03_HIYU_ABYSS_EDITORIAL_STYLE_BIBLE.md
│   ├── 04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md
│   ├── 05_HIYU_ABYSS_AGENT_SKILLS_WORKFLOW.md
│   └── 06_HIYU_ABYSS_QUALITY_EVALUATION.md
├── .agents/
│   └── skills/
│       └── <skill-name>/SKILL.md
├── knowledge/
│   ├── sources/SRC-0001.md
│   ├── notes/NOTE-0001.md
│   ├── concepts/CON-0001.md
│   └── runs/RUN-0001.md
├── editorial/
│   ├── ideas/IDEA-0001.md
│   └── content/TXT-0001.md
├── indexes/
│   ├── sources.md
│   ├── ideas.md
│   └── editorial-board.md
├── templates/
│   ├── source.md
│   ├── note.md
│   ├── idea.md
│   └── content.md
└── tests/
    ├── cases/
    └── fixtures/
```

Có thể thêm các thư mục khác khi có nhu cầu, nhưng giữ định danh và các tuyến liên kết này.

## 4. Quy tắc YAML frontmatter

Mọi hồ sơ `SRC`, `NOTE`, `CON`, `IDEA`, `TXT`, `RUN` dùng YAML frontmatter; phần nội dung viết Markdown thuần. Quy ước:

- Ngày dạng ISO `YYYY-MM-DD`; ngày/giờ lưu sự kiện nếu cần dạng ISO 8601 có múi giờ.
- ID tham chiếu là chuỗi, danh sách là mảng chuỗi, không nhúng toàn bộ hồ sơ khác.
- Các giá trị enum viết **chữ in hoa** như phần định nghĩa.
- Các trường không biết hoặc chưa áp dụng dùng `null`; danh sách rỗng là `[]`.
- Chuỗi tiếng Việt cần dấu câu rõ ràng; giá trị có dấu `:` hoặc `#` nên đặt trong dấu nháy.
- Không dùng URL chứa khóa truy cập hoặc thông tin đăng nhập trong hồ sơ.

## 5. Hồ sơ SOURCE (`SRC`)

Các trường bắt buộc: `id`, `record_type`, `title`, `source_type`, `access_level`, `created_at`, `links`. Các trường điều kiện: `author`, `edition`, `language`, `translator`, `publication_year`, `locator_scheme`, `rights_notes`, `retrieved_at`.

```markdown
---
id: SRC-0001
record_type: SOURCE
title: "[Tên tác phẩm xác định từ nguồn]"
source_type: BOOK
author: "[Tác giả đã đối chiếu]"
edition: null
translator: null
language: null
publication_year: null
access_level: FOUND_METADATA
locator_scheme: null
links:
  - "https://example.org/book-record"
rights_notes: "Chưa kiểm tra quyền sử dụng toàn văn"
created_at: 2026-11-13
retrieved_at: 2026-11-13
---

## Nguồn và phạm vi truy cập
- Đã xác nhận: hồ sơ thư mục.
- Chưa xác nhận: nội dung toàn văn, chương liên quan.

## Những câu hỏi cần đọc
- ...
```

`source_type`: `BOOK`, `PRIMARY_TEXT`, `STUDY`, `ACADEMIC_OVERVIEW`, `ESSAY`, `SOCIAL_POST`, `OTHER`. `access_level`: `FOUND_METADATA`, `PARTIAL_TEXT`, `READ_SOURCE`, `CONTEXT_CHECKED`.

**Một ấn bản khác nhau về dịch giả hoặc đoạn văn quan trọng có thể cần SRC riêng** và liên kết `related_source_ids`; không gộp lẫn chữ từ hai bản dịch rồi đánh dấu nguyên văn.

## 6. Hồ sơ READING NOTE (`NOTE`)

Ghi chép theo một nguồn và phạm vi cụ thể; với nhiều nguồn có thể có nhiều NOTE và một CON chung.

```markdown
---
id: NOTE-0001
record_type: READING_NOTE
source_id: SRC-0001
access_level: READ_SOURCE
locator: "[Tên chương / mục / số đoạn / trang]"
concept_ids: []
evidence_status: VERIFIED_IDEA
created_at: 2026-11-13
---

## Luận đề của tác giả
...

## Bằng chứng / lập luận trong phần đã đọc
...

## Ngữ cảnh và cách hiểu khác
...

## Giới hạn
...

## Cách Hiyu Abyss khai thác (suy luận riêng)
...
```

Không dùng `VERIFIED_TEXT` nếu chưa có đối chiếu nguyên văn và vị trí cụ thể. Nếu cần dịch, ghi đoạn nguyên ngữ ngắn và bản dịch của người viết ở hai trường tách biệt; tuân thủ giới hạn trích dẫn.

## 7. Hồ sơ CONCEPT (`CON`)

`CON` là nút khái niệm: có định nghĩa làm việc, các cách hiểu, nguồn, phản ví dụ và liên hệ chủ đề. Không phải mọi CON đều là chân lý đã được chứng minh.

```markdown
---
id: CON-0001
record_type: CONCEPT
name: "Đạo đức như tín hiệu địa vị"
topic_codes: [HYPOCRISY, STATUS]
source_ids: []
note_ids: []
related_concept_ids: []
created_at: 2026-11-13
---

## Định nghĩa làm việc
...

## Góc nhìn đối lập / phản ví dụ
...

## Câu hỏi mở
...
```

`topic_codes` là các mã trong bảng chủ đề HYA-01; nếu thêm mã mới, phải cập nhật bảng chủ đề và ghi định nghĩa để tránh hai tag cùng nghĩa.

## 8. Hồ sơ IDEA (`IDEA`)

Đây là **phát hiện chưa phải câu cuối cùng**. Nên giữ dữ liệu ý tưởng ngay cả khi bản câu bị loại.

```markdown
---
id: IDEA-0001
record_type: IDEA
title: "Khi sự giúp đỡ biến thành quyền đòi hỏi"
topic_codes: [HYPOCRISY, POWER]
concept_ids: [CON-0001]
note_ids: []
source_ids: []
status: CAPTURED
created_at: 2026-11-13
---

## Quan sát / vấn đề
...

## Nghịch lý trung tâm
- Tuyên bố: ...
- Điều kiện khiến tuyên bố đổi nghĩa: ...
- Phản ví dụ: ...

## Giá trị mới của góc nhìn
...

## Những hướng viết có thể có
...
```

`IDEA.status`: `CAPTURED`, `RESEARCHED`, `SELECTED`, `PARKED`, `REJECTED`. Chỉ dùng `RESEARCHED` nếu đã có công việc đối chiếu thực sự; một ý tưởng độc lập có thể không có nguồn sách cụ thể nhưng phải ghi lý do.

## 9. Hồ sơ CONTENT (`TXT`)

Một TXT là một tác phẩm biên tập độc lập. Nội dung hiển thị là phần `## Văn bản hiện tại`; phần còn lại chỉ dành cho kho biên tập.

```markdown
---
id: TXT-0001
record_type: CONTENT
title: "Ân huệ và món nợ"
idea_ids: [IDEA-0001]
source_ids: []
topic_codes: [HYPOCRISY, POWER]
content_type: INDEPENDENT_ORIGINAL
evidence_status: UNVERIFIED
status: DRAFT
created_at: 2026-11-13
updated_at: 2026-11-13
approved_by: null
approved_at: null
published_at: null
scores:
  insight: null
  coherence: null
  precision: null
  imagery: null
  resonance: null
  originality: null
---

## Văn bản hiện tại
Có những ân huệ chỉ trở thành món nợ khi người nhận bắt đầu nói không.

## Vì sao câu này đáng giữ
- Quan hệ giữa ân huệ, quyền đòi hỏi và ranh giới.

## Bằng chứng, nguồn và giới hạn
- Đây là câu sáng tác mới; không phải lời trích một triết gia.

## Đánh giá / lý do sửa
- ...
```

Các mã `content_type`: `DIRECT_QUOTE`, `PARAPHRASE`, `INSPIRED_ORIGINAL`, `INDEPENDENT_ORIGINAL`. `evidence_status`: `VERIFIED_TEXT`, `VERIFIED_IDEA`, `NEEDS_REVIEW`, `UNVERIFIED`, `DISPUTED`.

**Lưu ý:** `INDEPENDENT_ORIGINAL` có thể không có nguồn ngoài; `UNVERIFIED` trong trường hợp này không có nghĩa “câu bị sai”, chỉ có nghĩa không khẳng định bằng chứng trích dẫn. Khi thiết kế bảng kiểm có thể dùng `not_applicable` ở các nhận xét, nhưng không tự thay enum `evidence_status`.

## 10. Hồ sơ RESEARCH RUN (`RUN`)

Ghi lại cuộc tìm kiếm, nhất là khi không tìm được nguồn:

```markdown
---
id: RUN-0001
record_type: RESEARCH_RUN
question: "[Câu hỏi khảo sát]"
search_date: 2026-11-13
channels: [BOOK_CATALOG, WEB_SEARCH]
found_source_ids: []
created_note_ids: []
status: PARTIAL
---

## Truy vấn và nơi đã thử
...

## Những gì thực sự truy cập được
...

## Khoảng trống / trở ngại
...

## Bước tiếp theo
...
```

`RUN.status`: `COMPLETE`, `PARTIAL`, `BLOCKED`. Ghi lại trang không đọc được thay vì tự bịa trích đoạn.

## 11. Vòng đời nội dung và quyền hạn

`TXT.status` là một trong: `DRAFT`, `IN_REVIEW`, `NEEDS_SOURCE`, `APPROVED`, `PUBLISHED`, `REJECTED`, `ARCHIVED`.

```text
DRAFT ──> IN_REVIEW ──> APPROVED ──> PUBLISHED ──> ARCHIVED
              │             ▲
              ├──> NEEDS_SOURCE ──> DRAFT
              ├──> DRAFT (yêu cầu sửa)
              └──> REJECTED
```

- Agent được chuyển `DRAFT ↔ IN_REVIEW`, chuyển sang `NEEDS_SOURCE`, đề xuất `REJECTED`, ghi đánh giá và bản sửa.
- Agent **không được tự chuyển sang `APPROVED` hoặc `PUBLISHED`** nếu thiếu hành động rõ ràng của chủ dự án. `approved_by`, `approved_at` phải có giá trị thật khi APPROVED.
- `PUBLISHED` chỉ khi được người phụ trách xác nhận đã đăng hoặc giao quyền cụ thể cho thao tác ghi trạng thái, với ngày có chứng cứ. Không suy luận từ lịch dự kiến.
- Khi bản đã duyệt bị sửa nội dung chính, quay lại `IN_REVIEW`, yêu cầu phê duyệt mới.
- `REJECTED` nên lưu lý do. Nếu tái sử dụng một hướng mới, có thể tạo TXT mới liên kết `derived_from`.

## 12. Tính toàn vẹn liên kết

Trước mỗi đề xuất duyệt, kiểm:

- ID đúng tiền tố và duy nhất; tên file trùng chính xác ID.
- Mọi `source_ids`, `note_ids`, `concept_ids`, `idea_ids` đều trỏ đến hồ sơ tồn tại.
- `DIRECT_QUOTE` phải có nguồn, locator, trạng thái `VERIFIED_TEXT` và thông tin văn bản/bản dịch phù hợp.
- `PARAPHRASE` phải có ghi chú đọc/nguồn và `VERIFIED_IDEA` hoặc `NEEDS_REVIEW` (nếu chưa đủ).
- `APPROVED` phải có `approved_by` và `approved_at`; `PUBLISHED` phải có `published_at`.
- Không để cùng một `source_id` chỉ hai tác phẩm khác nhau.
- Một nguồn `FOUND_METADATA` không được diễn đạt trong NOTE như đã `CONTEXT_CHECKED`.
- Mã topic sử dụng bảng HYA-01 hoặc cập nhật bảng kèm lý do.
- Các file Markdown không được chứa bí mật, dữ liệu cá nhân riêng tư hoặc nguyên văn sách dài có bản quyền.

## 13. Index và khả năng tra cứu

`indexes/sources.md`: ID, tên nguồn, tác giả, truy cập, ghi chú gần nhất. `indexes/ideas.md`: ID, nhãn, trạng thái, các nguồn liên quan. `indexes/editorial-board.md`: ID TXT, nhãn, trạng thái, điểm đánh giá, ngày cập nhật.

Index là **bản xem dẫn xuất** từ hồ sơ gốc, không sửa trực tiếp. Đừng tạo hai phiên bản sự thật. Có thể tạo chỉ mục qua script nhỏ khi kho lớn; ở MVP chỉ cần file tĩnh được cập nhật có kiểm tra. Dùng Git search/grep để tìm, không cần hệ truy vấn phức tạp.

## 14. Định nghĩa hoàn thành của mô hình dữ liệu

- [ ] Tạo thử mỗi loại hồ sơ `SRC/NOTE/CON/IDEA/TXT/RUN` bằng template.
- [ ] Có ít nhất một chuỗi liên kết từ nguồn đến bản câu chữ hoặc ghi rõ câu độc lập.
- [ ] Kiểm tra được enum, link ID, và quyền duyệt.
- [ ] Thay trạng thái không cần di chuyển file.
- [ ] Truy nguyên được bản sửa qua Git.
- [ ] Index không mâu thuẫn với hồ sơ chuẩn.

**Handoff:** HYA-05 dùng những hồ sơ/đường dẫn này làm hợp đồng dữ liệu khi phối hợp skill. HYA-06 kiểm các điều kiện trước khi phê duyệt.
