---
name: source-discovery
description: "Khám phá, tra cứu và đánh giá nguồn tri thức (sách, nghiên cứu, bách khoa triết học) theo câu hỏi nghiên cứu của Hiyu Abyss. Xác định chính xác mức độ truy cập thực tế và ghi nhận vào SRC, RUN."
---

# Source Discovery (Khám phá nguồn tri thức)

## Mục đích & Ranh giới
Kỹ năng này chịu trách nhiệm tìm kiếm các nguồn tư tưởng, ấn bản học thuật và công trình nghiên cứu phù hợp với câu hỏi nghiên cứu của dự án Hiyu Abyss.
- **Ranh giới:** Phân biệt rõ ràng giữa việc tìm thấy metadata và việc thực sự đọc được toàn văn. Không bao giờ suy đoán nội dung của tài liệu chưa được đọc.

## Tài liệu tham chiếu bắt buộc
- [docs/01_HIYU_ABYSS_PROJECT_INPUT.md](file:///c:/hiyuabyss/docs/01_HIYU_ABYSS_PROJECT_INPUT.md) — Mục 6 (Hệ sinh thái nguồn), Mục 7 (Chuẩn xác minh).
- [docs/02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md](file:///c:/hiyuabyss/docs/02_HIYU_ABYSS_RESEARCH_SOURCE_STANDARD.md) — Mục 2 (Thứ bậc bằng chứng), Mục 3 (Quy trình R0–R2), Mục 6 (Bản đồ kho sách).
- [docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md](file:///c:/hiyuabyss/docs/04_HIYU_ABYSS_KNOWLEDGE_CONTENT_MODEL.md) — Mục 5 (`SRC`), Mục 10 (`RUN`).
- [docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md](file:///c:/hiyuabyss/docs/06_HIYU_ABYSS_QUALITY_EVALUATION.md) — Ca kiểm thử T01, T02, T11.

## Quy trình thực hiện (Workflow)

### Bước 1: Chuẩn hóa câu hỏi & Truy vấn (R0)
1. Xác định câu hỏi nghiên cứu cụ thể gắn với 20 mã chủ đề (ví dụ: `HYPOCRISY`, `POWER`, `EGO`).
2. Tạo tối thiểu 3 truy vấn tìm kiếm bằng tiếng Việt, tiếng Anh và thuật ngữ học thuật tương ứng.
3. Mở hồ sơ nghiên cứu `knowledge/runs/RUN-xxxx.md` để ghi nhận nhật ký tìm kiếm.

### Bước 2: Dò tìm nguồn theo thứ tự ưu tiên (R1)
1. **Nguyên tác công cộng:** Project Gutenberg, Standard Ebooks, Wikisource.
2. **Bình giải học thuật & Bách khoa:** Stanford Encyclopedia of Philosophy (SEP), Internet Encyclopedia of Philosophy (IEP).
3. **Mục từ & Nghiên cứu mở:** PhilPapers, Directory of Open Access Books (DOAB), Crossref, OpenAlex.
4. **Metadata & Thư mục:** Open Library, Google Books.

### Bước 3: Xác định mức độ truy cập thực tế (R2)
Gán chính xác một trong bốn giá trị enum:
- `FOUND_METADATA`: Chỉ tìm thấy bản ghi thư mục, mục lục, ISBN hoặc bài giới thiệu; chưa đọc được nội dung.
- `PARTIAL_TEXT`: Đã xem được bản xem trước (preview), trích đoạn mục tiêu, abstract hoặc một chương lẻ.
- `READ_SOURCE`: Đã truy cập và đọc trực tiếp phần văn bản đầy đủ chứa luận điểm cần khai thác.
- `CONTEXT_CHECKED`: Đã đọc toàn bộ bối cảnh tác phẩm, đối chiếu bản dịch/nguyên ngữ và các tài liệu bình giải liên quan.

### Bước 4: Tạo hồ sơ & Lưu trữ (R6)
1. Tạo file `knowledge/sources/SRC-xxxx.md` theo mẫu `templates/source.md`.
2. Điền đầy đủ thông tin: `title`, `author`, `source_type`, `access_level`, `links`, `rights_notes`. Nếu chưa rõ dịch giả hay năm, để `null`.
3. Cập nhật ID nguồn vào `RUN-xxxx.md` và bảng chỉ mục `indexes/sources.md`.

## Điều kiện dừng & Cấm đoán (Stop Conditions & Forbidden)
- **Dừng ngay khi bị chặn:** Nếu gặp paywall, captcha hoặc trang yêu cầu đăng nhập, ghi nhận `UNAVAILABLE` trong `RUN` và giữ `access_level: FOUND_METADATA`. Không cố vượt rào cản kỹ thuật.
- **Cấm bịa đặt:** Tuyệt đối không bịa số trang, số chương, DOI hoặc tác giả.
- **Cấm phóng đại:** Tuyệt đối không tuyên bố "tác phẩm khẳng định rằng..." khi mới chỉ xem metadata hoặc đoạn trích ngắn (Hard Gate G4, Ca T01).
