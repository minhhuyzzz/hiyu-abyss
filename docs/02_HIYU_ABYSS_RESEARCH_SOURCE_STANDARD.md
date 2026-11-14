# HYA-02 — RESEARCH & SOURCE STANDARD

| Trường | Giá trị |
|---|---|
| Dự án | Hiyu Abyss |
| Mã tài liệu | `HYA-02` |
| Phiên bản | `1.0` |
| Ngày chuẩn hóa | `2026-11-13` |
| Phụ thuộc | `HYA-01` |
| Mục đích | Chuẩn tìm, đọc, đối chiếu, tóm lược và lưu nguồn tri thức |

> Tài liệu này quy định **cách đi từ một câu hỏi đến một ghi chú có thể truy nguyên nguồn**. HYA-03 chịu trách nhiệm viết câu chữ; HYA-04 định nghĩa trường dữ liệu; HYA-05 điều phối kỹ năng; HYA-06 kiểm định đầu ra.

## 1. Phạm vi nghiên cứu

Không giới hạn vào một trường phái. Ưu tiên các vấn đề: đạo đức giả, tiêu chuẩn kép, sự tự lừa dối, bản ngã, nhu cầu công nhận, quyền lực, mặt nạ xã hội, nghịch lý giữa lời nói và động cơ, tự do và nỗi sợ, phóng chiếu, gắn bó, đố kỵ, đám đông, trách nhiệm, ảo tưởng và sự thật. Khi mở rộng đề tài phải giữ cùng tiêu chuẩn nguồn.

**Phân tách ba việc:** (a) khám phá nguồn; (b) xác định tác phẩm thật sự nói gì; (c) phát triển ý tưởng mới. Không gộp ba việc thành một lời khẳng định thiếu dấu vết.

## 2. Thứ bậc bằng chứng

| Loại nguồn | Ví dụ | Có thể hỗ trợ | Không đủ để khẳng định |
|---|---|---|---|
| Nguyên tác/ấn bản định danh | Sách, thư, bài giảng, chương gốc | Câu trích, lập luận của tác giả trong ngữ cảnh | Tính đúng phổ quát của một lý thuyết |
| Nghiên cứu gốc | Bài báo, dữ liệu, phương pháp | Kết quả trong điều kiện nghiên cứu | Quy luật áp dụng cho mọi người |
| Tổng quan học thuật/bình giải | SEP, sách nghiên cứu, systematic review | Khái niệm, tranh luận, cách hiểu | Một câu văn nguyên văn không được kiểm trong nguồn gốc |
| Danh mục/bibliography | Open Library, Crossref, PhilPapers | Tên sách, tác giả, bản in, DOI, địa chỉ tiếp cận | Đã đọc toàn văn hoặc xác nhận được ý nghĩa của đoạn |
| Báo, blog, mạng xã hội công khai | Bài viết, Reddit, Threads, X | Gợi tình huống, từ khóa, câu hỏi, phản biện | Bằng chứng về bản chất của mọi người hoặc số liệu đại diện |

Không gán nhãn “nghiên cứu chứng minh” nếu chỉ đọc tóm tắt, tiêu đề hoặc nội dung mạng xã hội.

## 3. Quy trình nghiên cứu chuẩn

### R0 — Diễn đạt câu hỏi

Đầu vào là **một câu hỏi**, không chỉ một từ khóa. Ví dụ: “Khi nào hình ảnh đạo đức trở thành công cụ củng cố địa vị?” Xác định: phạm vi, các thuật ngữ gần nghĩa, phản đề và dạng bằng chứng cần có. Tối thiểu tạo 3 truy vấn tìm kiếm với từ đồng nghĩa tiếng Việt/Anh và tên khái niệm học thuật liên quan.

### R1 — Phát hiện nguồn

Tìm theo thứ tự linh hoạt: nguyên tác → sách nghiên cứu → bách khoa học thuật → nghiên cứu gốc/tổng quan → quan sát xã hội. Ghi **URL truy cập thực tế** và loại tài liệu; kiểm tra nhan đề, tác giả, thời điểm, ngôn ngữ và tính hợp pháp của việc đọc. Không giả định một kết quả tìm kiếm đồng nghĩa với toàn văn.

### R2 — Xác định mức truy cập

Dùng đúng một trong bốn giá trị: `FOUND_METADATA`, `PARTIAL_TEXT`, `READ_SOURCE`, `CONTEXT_CHECKED`.

- `FOUND_METADATA`: chỉ tìm thấy hồ sơ, chưa đọc nội dung.
- `PARTIAL_TEXT`: đã xem preview, trích đoạn, abstract hoặc một phần.
- `READ_SOURCE`: đã đọc phần văn bản cần dùng, có vị trí tương ứng.
- `CONTEXT_CHECKED`: đã đọc đủ ngữ cảnh và đối chiếu dị bản/cách hiểu khi cần.

Chỉ được tóm tắt **phạm vi đã đọc**, không nói “cuốn sách khẳng định” nếu mới có một đoạn nhỏ.

### R3 — Trích xuất ghi chú đọc

Mỗi `NOTE` cần chứa:

1. **Thesis**: luận đề chính tác giả thực sự đưa ra.
2. **Evidence**: câu/đoạn/quan sát hỗ trợ, hoặc cách tác giả lập luận.
3. **Context**: đối tượng, trường hợp, điều kiện, đối thoại đối lập.
4. **Counterpoint**: cách đọc khác, phản ví dụ hoặc giới hạn.
5. **Original insight**: một câu hỏi/góc khai thác của Hiyu Abyss, ghi rõ *đây là suy luận của dự án*.
6. **Locator**: chương, mục, số đoạn, trang/bản in hoặc URL đến phần được đọc.

Đoạn ghi chú không được thay thế nguồn gốc: từ `NOTE` phải lần về được `SRC` và vị trí.

### R4 — Phân tích và tìm phản đề

Trước khi biến một luận điểm thành nội dung “bóc trần”, agent phải tự hỏi: **Có lời giải thích vô hại hơn không? Câu này đúng trong trường hợp nào? Có đang lẫn tương quan với quan hệ nhân quả?** Tối thiểu ghi một phản đề đáng xem xét cho mỗi ý tưởng có tính kết án hoặc khái quát.

### R5 — Quyết định trạng thái bằng chứng

- `VERIFIED_TEXT`: đã đối chiếu nguyên văn, tác giả, tác phẩm, ấn bản và vị trí.
- `VERIFIED_IDEA`: đã đọc nguồn hỗ trợ ý tưởng, nhưng bản câu là diễn giải.
- `NEEDS_REVIEW`: cần đối chiếu thêm ngữ cảnh/bản dịch.
- `UNVERIFIED`: không đủ cơ sở xác nhận.
- `DISPUTED`: tồn tại chứng cứ mâu thuẫn hoặc tranh luận về phép gán.

`VERIFIED_TEXT` không dùng cho **câu tiếng Việt do agent tự dịch**, nếu nguyên văn của tác giả ở ngôn ngữ khác. Phải ghi rõ “bản dịch của dự án” và cung cấp bản gốc cùng thông tin người dịch nếu trích dẫn công khai.

### R6 — Lưu và liên kết

Tạo/điều chỉnh hồ sơ `SRC-xxxx`, ghi chú `NOTE-xxxx`, khái niệm `CON-xxxx` và nếu hình thành hướng viết thì `IDEA-xxxx`. Tham chiếu liên kết theo ID theo HYA-04; không tạo các bản sao cùng một nguồn chỉ vì URL khác.

## 4. Quy tắc phân loại câu chữ theo xuất xứ

| `content_type` | Dùng khi | Cách thể hiện công khai |
|---|---|---|
| `DIRECT_QUOTE` | Nguyên văn đúng từ một ấn bản đã đối chiếu | Ghi tác giả, tác phẩm, bản dịch/bản gốc và vị trí khi khả thi |
| `PARAPHRASE` | Diễn giải đúng ý của một đoạn nguồn | Ghi “diễn giải từ…”; không đặt trong ngoặc kép như chính lời tác giả |
| `INSPIRED_ORIGINAL` | Một câu mới nảy sinh từ chủ đề đã nghiên cứu | Chỉ lưu nguồn như cảm hứng, không gán nguyên văn cho tác giả |
| `INDEPENDENT_ORIGINAL` | Câu mới xuất phát từ phân tích riêng | Không cố gắn tên triết gia để tăng uy tín |

Nếu không quyết định được, để `NEEDS_REVIEW`; không dùng tên tác giả làm đồ trang trí cho câu chữ.

## 5. Kiểm trích dẫn qua nhiều lớp

**Lớp A — Thư mục:** xác nhận tên tác giả/tác phẩm/ấn bản/năm/người dịch. **Lớp B — Văn bản:** đúng từ, đúng câu và đúng vị trí. **Lớp C — Ngữ cảnh:** lời nhân vật hay tác giả? Phát biểu châm biếm hay khẳng định? **Lớp D — Diễn giải:** nội dung hiện tại có lấn quá điều nguồn cho phép không?

Ví dụ thường gặp:

- Lời nhân vật trong tiểu thuyết Dostoevsky **không tự động** là triết lý được tác giả tán thành.
- Đánh số mảnh trong *Pensées* thay đổi giữa ấn bản; phải ghi hệ thống đánh số hoặc chú thích bản dùng.
- Một “câu nói của Jung” lan truyền trên mạng chưa được xác nhận chỉ bằng việc nhiều website lặp lại.
- Kết quả thí nghiệm về *moral licensing* không chứng minh rằng mọi hành vi tử tế đều giả dối.

## 6. Nguồn bắt đầu và vai trò chính xác

| Kho | URL | Vai trò |
|---|---|---|
| Project Gutenberg | https://www.gutenberg.org/ | Khám phá văn bản toàn văn hợp pháp theo từng ấn bản; chú ý chính sách robot và bản quyền theo quốc gia |
| Standard Ebooks | https://standardebooks.org/ebooks | Ebook tuyển chọn, ấn bản tương đối dễ đọc |
| Wikisource | https://en.wikisource.org/ | Văn bản nguồn, kiểm chất lượng hiệu đính và xuất xứ |
| Open Library | https://openlibrary.org/ | Metadata tác phẩm/bản in; một phần có cơ chế đọc/mượn |
| DOAB | https://www.doabooks.org/ | Khám phá sách học thuật open access |
| SEP | https://plato.stanford.edu/ | Bình giải học thuật, thuật ngữ và lịch sử tranh luận |
| IEP | https://iep.utm.edu/ | Giải thích triết học có biên tập |
| PhilPapers | https://philpapers.org/ | Danh mục bài triết học, một phần có toàn văn |
| Crossref | https://search.crossref.org/ | So khớp metadata công trình |
| OpenAlex | https://openalex.org/ | Tìm quan hệ nghiên cứu, tác giả, công trình |

**Nguyên tắc thu thập:** dùng giao diện/bản tải hợp lệ hoặc cách truy cập được nhà cung cấp cho phép; không vượt đăng nhập, paywall, chống bot hay hạn chế riêng tư. Với Project Gutenberg, tham khảo https://www.gutenberg.org/policy/robot_access.html; với Open Library xem https://openlibrary.org/developers/api. Khối lượng đọc nhỏ theo mục tiêu nghiên cứu, không cào hàng loạt.

## 7. Dùng bài đăng công khai và thảo luận xã hội

Quan sát thảo luận trên Reddit/Threads/X chỉ nên tạo hồ sơ **insight về một lời kể/góc nhìn**, không tự biến thành kết luận tâm lý học. Chỉ nghiên cứu phần công khai truy cập hợp lệ; không lấy dữ liệu cá nhân riêng tư, không theo dõi cá nhân, không tái đăng nguyên văn dài, không suy diễn đặc điểm nhạy cảm từ bài viết.

Đầu ra từ mỗi đợt nghiên cứu xã hội:

- Chủ đề và phạm vi/khung thời gian tìm kiếm.
- Tối đa 5–10 ý quan sát nổi bật, có URL và thời gian truy cập nếu hợp lệ.
- Các luận điểm đối nghịch và khả năng thiên lệch của mẫu.
- Danh sách **câu hỏi cần đối chiếu với sách/nghiên cứu**.
- Mọi nguồn không truy cập được phải ghi `UNAVAILABLE`, không phỏng đoán nội dung.

Không coi sự lan truyền, số lượt thích hoặc sự phẫn nộ là bằng chứng sự thật.

## 8. Quy tắc tóm ý sách/bài luận

**Tóm ý phân tích** phải giữ: luận đề, cấu trúc lập luận, dẫn chứng, phản đề, thuật ngữ, phạm vi đã đọc và vị trí. Tóm tắt có thể dài hơn câu triết ngôn; không nén quá sớm. Khi dịch một thuật ngữ khó, lưu cả nguyên ngữ. Cố gắng nêu 2–3 cách ứng dụng vào đề tài Hiyu Abyss nhưng **không biến ứng dụng thành lời của tác giả**.

Mẫu đầu ra tối thiểu:

```markdown
# NOTE-0001 — [Tên luận điểm]
- source_id: SRC-0001
- access_level: READ_SOURCE
- locator: "Phần II, §..."
- thesis: ...
- reasoning: ...
- limitations: ...
- alternative_reading: ...
- terms: [...]
- hiyu_insight: ... # cách hiểu của dự án
```

## 9. Quy tắc bản quyền, chất lượng và liêm chính

Chỉ lưu đoạn trích cần thiết để nghiên cứu, ưu tiên diễn giải bằng lời riêng; không lưu tập tin sách có bản quyền trái quyền truy cập; không xuất bản văn bản dài có bản quyền từ nguồn khác. Khi có mâu thuẫn, giữ cả hai hướng bằng chứng thay vì tự chọn phương án có sức giật gân hơn. Không viện dẫn tác giả/nguồn mà chưa xem nội dung tương ứng.

Mỗi ghi chú nghiên cứu phải phân biệt `observed_text` (văn bản nguồn), `author_argument` (ý tác giả), `project_interpretation` (suy luận Hiyu Abyss).

## 10. Tiêu chí hoàn thành một lượt nghiên cứu

- [ ] Câu hỏi nghiên cứu rõ ràng và các từ khóa đã được ghi.
- [ ] Ít nhất một nguồn phù hợp đã **thực sự đọc được**; nếu không có, ghi lý do và dừng ở metadata.
- [ ] Có URL/ấn bản và locator đủ để đối chiếu.
- [ ] Có luận đề, phản đề, điều kiện và giới hạn.
- [ ] Có trạng thái truy cập và bằng chứng đúng với thực tế.
- [ ] Nếu tạo ý tưởng mới, có liên kết từ ý tưởng về nguồn/ghi chú.
- [ ] Không chuyển một trích dẫn chưa xác minh thành lời của tác giả.

**Handoff:** `HYA-04` xác định nơi lưu hồ sơ; `HYA-03` dùng luận điểm đã phân tích để viết; `HYA-06` kiểm tra bằng chứng và thành phẩm.
