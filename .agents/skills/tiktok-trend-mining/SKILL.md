---
name: tiktok-trend-mining
description: "Cào và khai thác dữ liệu xu hướng TikTok, bộ từ khóa TikTok SEO, phân tích hashtag thịnh hành và tối ưu hóa khả năng tìm kiếm cho nội dung tâm lý, triết học."
---

# TikTok Trend & Hashtag Mining Skill (Khai Thác Xu Hướng & TikTok SEO)

> **Mục đích:** Khảo sát, cào và trích xuất dữ liệu xu hướng thực tế trên TikTok (Hashtags thịnh hành, cụm từ tìm kiếm tự nhiên của người dùng, âm nhạc nền và cấu trúc nội dung chuẩn SEO) để tối ưu hóa khả năng hiển thị và giữ chân người xem cho kênh Hiyu Abyss.

---

## 1. Bản Chất Của Thuật Toán TikTok SEO

TikTok đã chuyển dịch từ một nền tảng giải trí lướt ngẫu nhiên sang **Công cụ tìm kiếm thế hệ mới (Search Engine)** của giới trẻ. Thuật toán tìm kiếm của TikTok xếp hạng bài đăng dựa trên 5 yếu tố cốt lõi:

1. **Văn bản trên video (On-Screen Text / OCR):** TikTok quét chữ trên ảnh slide/video qua công nghệ nhận diện quang học. Trang 1 (Hook) chứa từ khóa tìm kiếm sẽ được ưu tiên xếp hạng cao.
2. **Tiêu đề & Dòng đầu Caption:** 100–150 ký tự đầu tiên của phần mô tả là nơi bot TikTok xác định chủ đề và mục đích tìm kiếm (Search Intent).
3. **Cấu trúc 5 Tầng Hashtag Đa Dạng (Không Rập Khuôn):**
   - **Tầng 1 (Niche High-Intent Keyword):** Từ khóa chính của vấn đề người xem đang tìm kiếm (`#thaotungtamly`, `#daoducgia`, `#triethockhacky`, `#aiky`, `#ranhgioicanhan`...).
   - **Tầng 2 (Broad Category):** Danh mục lớn (`#tamlyhoc`, `#triethoc`, `#phattrienbanthan`...).
   - **Tầng 3 (Life Situation / Pain Point):** Vấn đề đời sống thực tế (`#suthatcuocsong`, `#gocnhincuocsong`, `#moiquanhe`, `#chualanh`...).
   - **Tầng 4 (Discovery / Viral Format):** Định dạng nội dung hoặc triết gia liên quan (`#baihoccanhan`, `#trichdanhay`, `#carljung`, `#nietzsche`...).
   - **Tầng 5 (Brand Anchor):** Nhận diện kênh (`#hiyuabyss`).
4. **Từ khóa trong Bình Luận (Keyword in Comments):** Đặt câu hỏi kết thúc video khéo léo để người xem bình luận có chứa từ khóa mục tiêu, đẩy điểm SEO video lên Top tìm kiếm.
5. **Thời gian xem trung bình (Watch Time & Retention):** Slide 1 (Hook gián đoạn suy nghĩ) $\rightarrow$ Slide 2 (Twist bóc trần) $\rightarrow$ Slide 3 (Phản tư).

---

## 2. Quy Trình Cào & Khai Thác Dữ Liệu Hashtag & SEO

### Bước 1: Thu Thập Dữ Liệu Xu Hướng Hợp Pháp & Ổn Định
Do TikTok chặn các scraper không chính thức, kỹ năng này định tuyến thu thập qua các nguồn mở bền vững:
- **TikTok Creative Center:** Tra cứu trực tiếp bảng xếp hạng Hashtag và BGM theo ngành hàng (*Education, Self-Improvement, Society*).
- **Search Auto-Complete Mining:** Truy vấn các cụm từ tìm kiếm tự nhiên của người dùng Việt Nam (ví dụ gõ *"tâm lý học..."*, *"dấu hiệu..."*, *"tại sao người ta..."* để lấy các gợi ý tìm kiếm hot nhất).
- **Công cụ hỗ trợ:** Script `scripts/mine_tiktok_trending_seo.py` giúp phân tích và sinh bộ từ khóa SEO tự động cho từng chủ đề.

### Bước 2: Phân Tích & Phân Loại Cụm Từ Khóa (Keyword Clustering)
Gán từ khóa tương ứng với 20 nhóm chủ đề hạt nhân của Hiyu Abyss:
- **Nhóm Thao túng & Ái kỷ:** `#thaotungtamly`, `#aiky`, `#gaslighting`, `#tamlyhocden`, `#nhandienkethaotung`.
- **Nhóm Đạo đức giả & Mặt nạ:** `#daoducgia`, `#matnaxahoi`, `#nguoithu3`, `#bocchuan`, `#suthatphatlong`.
- **Nhóm Khắc kỷ & Nội tâm:** `#triethockhacky`, `#marcusaurelius`, `#ngungquantam`, `#noidoc`, `#binhyentamhon`.
- **Nhóm Ranh giới & Lòng tốt:** `#ranhgioicanhan`, `#longtotbimat`, `#hoccachetloi`, `#tuchoi`.

### Bước 3: Đưa Vào Pipeline Google Sheets
- Mỗi bài đăng phải sở hữu bộ 5 hashtag riêng biệt, không copy-paste đồng loạt.
- Tiêu đề gắn tiền tố SEO nhận diện rõ ràng (*[Tâm Lý Học]*, *[Nghịch Lý]*, *[Sự Thật Đời Sống]*, *[Khắc Kỷ]*) để khớp truy vấn tìm kiếm của người dùng.

---

## 3. Checklist Kiểm Định SEO Trước Khi Đăng (SEO Gate)

| Yếu tố | Tiêu chuẩn Đạt | Cảnh báo Vi phạm |
|---|---|---|
| **Tiêu đề** | Có từ khóa tìm kiếm tự nhiên + Dưới 90 từ | Đặt tên quá hàn lâm hoặc không ai gõ tìm |
| **Mô tả** | Chứa từ khóa mục tiêu trong 2 câu đầu + Có câu hỏi CTA | Mô tả chung chung, không có từ khóa |
| **Hashtags** | Đúng 5 tag, kết hợp đa tầng, độc nhất theo chủ đề | Copy 5 tag giống hệt nhau qua nhiều bài |
| **Slide 1** | Có Hook rõ ràng, chữ to, OCR nhận diện được | Slide 1 chữ quá nhỏ hoặc không nêu vấn đề |
