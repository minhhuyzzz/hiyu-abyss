# Hiyu Abyss — Triết ngôn tâm lý sắc lạnh (Dark Psychological Aphorisms)

Dự án nghiên cứu, tuyển chọn, phân tích và sáng tác triết ngôn tâm lý bóc trần bằng tiếng Việt dựa trên phương pháp luận học thuật, kiểm chứng nguồn nghiêm ngặt và quy chuẩn biên tập đa tầng.

---

## 1. Cấu trúc Workspace

```text
hiyu-abyss/
├── README.md               # Tổng quan dự án và hướng dẫn vận hành
├── AGENTS.md               # Quy tắc vận hành và ranh giới bất biến cho AI Agents
├── docs/                   # Bộ tiêu chuẩn kiến trúc dự án (HYA-01 -> HYA-06)
│   ├── 01_HIYU_ABYSS_PROJECT_INPUT.md
│   ├── 02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md
│   ├── 03_HIYU_ABYSS_EDITORIAL_STYLE_BIBLE.md
│   ├── 04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md
│   ├── 05_HIYU_ABYSS_AGENT_SKILLS_WORKFLOW.md
│   ├── 06_HIYU_ABYSS_QUALITY_EVALUATION.md
│   └── README.md
├── .agents/
│   └── skills/             # 11 Agent Skills chuẩn hóa theo Google Antigravity
│       ├── source-discovery/
│       ├── book-insight-summarization/
│       ├── citation-and-quote-audit/
│       ├── aphorism-writing/
│       ├── editorial-critique/
│       ├── philosophical-argument-mapping/
│       ├── hypocrisy-paradox-mining/
│       ├── metaphor-and-subtext/
│       ├── semantic-novelty-review/
│       ├── social-insight-mining/
│       └── content-lifecycle/
├── knowledge/              # Kho lưu trữ tri thức nền tảng
│   ├── sources/            # Hồ sơ nguồn tư liệu (SRC-xxxx.md)
│   ├── notes/              # Ghi chú đọc và đối chiếu văn bản (NOTE-xxxx.md)
│   ├── concepts/           # Khái niệm và sơ đồ lập luận (CON-xxxx.md)
│   └── runs/               # Nhật ký các đợt nghiên cứu/tìm kiếm (RUN-xxxx.md)
├── editorial/              # Kho phát triển và biên tập nội dung
│   ├── ideas/              # Ý tưởng, quan sát và nghịch lý (IDEA-xxxx.md)
│   └── content/            # Bản thảo triết ngôn và lịch sử biên tập (TXT-xxxx.md)
├── indexes/                # Bản chỉ mục tra cứu dẫn xuất
│   ├── sources.md          # Danh mục nguồn và trạng thái truy cập
│   ├── ideas.md            # Danh mục ý tưởng và chủ đề
│   └── editorial-board.md  # Bảng điều phối biên tập và vòng đời bài viết
├── templates/              # Khuôn mẫu Markdown chuẩn cho 6 loại hồ sơ
│   ├── source.md
│   ├── note.md
│   ├── concept.md
│   ├── idea.md
│   ├── content.md
│   └── run.md
├── scripts/                # Bộ công cụ tự động kiểm định tính toàn vẹn và test runner
│   ├── validate_integrity.py
│   └── run_tests.py
└── tests/                  # Bộ ca kiểm thử chất lượng và chấp nhận (HYA-06)
    ├── cases/              # Ca kiểm thử từ T01 đến T18
    └── fixtures/           # Dữ liệu đối chiếu mẫu
```

---

## 2. Luồng vận hành chuẩn

1. **Khám phá & Thu thập nguồn (`source-discovery`):** Xác định câu hỏi, tìm nguồn hợp pháp, ghi nhận thực tế mức truy cập (`FOUND_METADATA` / `PARTIAL_TEXT` / `READ_SOURCE` / `CONTEXT_CHECKED`).
2. **Trích xuất luận điểm (`book-insight-summarization`):** Đọc phần văn bản, tách bạch thesis, reasoning, context, counterpoint và suy luận của Hiyu Abyss.
3. **Phân tích nghịch lý (`hypocrisy-paradox-mining`, `philosophical-argument-mapping`):** Soi chiếu khoảng cách giữa biểu hiện bề mặt và động cơ ẩn giấu.
4. **Sáng tác & Biên tập (`aphorism-writing`, `metaphor-and-subtext`, `editorial-critique`):** Viết câu chữ cô đọng tiếng Việt, loại bỏ sáo ngữ AI, kiểm tra tính logic và sắc thái.
5. **Kiểm tra nguồn & Trùng ý (`citation-and-quote-audit`, `semantic-novelty-review`):** Soát xét hard gates, xác định đúng `content_type` (`DIRECT_QUOTE`, `PARAPHRASE`, `INSPIRED_ORIGINAL`, `INDEPENDENT_ORIGINAL`) và kiểm tra trùng ý trong kho.
6. **Kiểm định & Trình duyệt (`content-lifecycle`, `validate_integrity.py`):** Kiểm tra liên kết toàn vẹn, cập nhật chỉ mục, đưa bài viết vào trạng thái `IN_REVIEW`.
7. **Phê duyệt cuối cùng:** Người phụ trách dự án trực tiếp duyệt (`APPROVED`).
