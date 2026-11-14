---
name: content-lifecycle
description: "Quản lý vòng đời hồ sơ Markdown, đồng bộ hóa các bảng chỉ mục (indexes), xác minh tính toàn vẹn liên kết và bảo vệ tuyệt đối cổng phê duyệt của con người (Hard Gate G5)."
---

# Content Lifecycle (Quản lý vòng đời & Toàn vẹn nội dung)

## Mục đích & Ranh giới
Kỹ năng này chịu trách nhiệm giám sát toàn bộ trạng thái của các thực thể (`SRC`, `NOTE`, `CON`, `IDEA`, `TXT`, `RUN`), đồng bộ các bảng chỉ mục dẫn xuất trong `indexes/`, và kiểm soát luồng phê duyệt nội dung.
- **Ranh giới:** Agent **tuyệt đối không bao giờ tự ý chuyển trạng thái sang `APPROVED` hoặc `PUBLISHED`** (Hard Gate G5). Quyền duyệt thuộc về người phụ trách dự án.

## Tài liệu tham chiếu bắt buộc
- [docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md](file:///c:/hiyuabyss/docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md) — Mục 11 (Vòng đời nội dung và quyền hạn), Mục 12 (Tính toàn vẹn liên kết), Mục 13 (Index).
- [docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md](file:///c:/hiyuabyss/docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md) — Hard Gate G5, Ca kiểm thử T13, T14, T15.

## Vòng đời trạng thái của bài viết (`TXT.status`)

```text
DRAFT ──> IN_REVIEW ──> APPROVED ──> PUBLISHED ──> ARCHIVED
              │             ▲
              ├──> NEEDS_SOURCE ──> DRAFT
              ├──> DRAFT (yêu cầu sửa)
              └──> REJECTED
```

### Quyền hạn chi tiết
1. **Agent được phép:**
   - Chuyển `DRAFT ↔ IN_REVIEW`.
   - Chuyển sang `NEEDS_SOURCE` khi thiếu chứng cứ nguồn.
   - Đề xuất `REJECTED` kèm lý do chi tiết.
   - Cập nhật điểm đánh giá `scores` và ghi chú biên tập.
2. **Agent KHÔNG ĐƯỢC PHÉP:**
   - Tự gán `status: APPROVED` hoặc `status: PUBLISHED`.
   - Tự điền `approved_by` hoặc `approved_at` mà không có văn bản xác nhận thực tế từ người dùng (Ca T14).
3. **Quy tắc sửa đổi sau duyệt (Reset Rule):**
   - Nếu một bài viết đã `APPROVED` mà bị chỉnh sửa nội dung văn bản (`## Văn bản hiện tại`), trạng thái **bắt buộc phải quay về `IN_REVIEW`**, xóa `approved_by` và `approved_at` để chờ phê duyệt lại (Ca T15).

## Kiểm tra tính toàn vẹn liên kết (Integrity Checks)
Trước khi đưa bất kỳ hồ sơ nào sang `IN_REVIEW`, phải kiểm tra:
1. **Khớp ID và Tên file:** File `knowledge/sources/SRC-0001.md` phải có `id: SRC-0001`.
2. **Tồn tại thực tế của các liên kết trỏ tới:** Mọi ID xuất hiện trong `source_ids`, `note_ids`, `concept_ids`, `idea_ids` đều phải có file tương ứng tồn tại trên ổ đĩa (Ca T13).
3. **Độ chính xác của Enum:** Tất cả các giá trị trạng thái, mức truy cập, loại nguồn phải đúng định dạng chữ in hoa như quy định trong `HYA-04`.

## Đồng bộ hóa bảng chỉ mục (Index Synchronization)
Sau khi tạo hoặc thay đổi hồ sơ, cập nhật file tương ứng:
- `indexes/sources.md`: Cập nhật khi có thay đổi trong `knowledge/sources/`.
- `indexes/ideas.md`: Cập nhật khi có thay đổi trong `editorial/ideas/`.
- `indexes/editorial-board.md`: Cập nhật khi có thay đổi trong `editorial/content/`.
