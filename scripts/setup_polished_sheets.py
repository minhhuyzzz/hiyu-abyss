import csv
import subprocess

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"

# DỮ LIỆU TAB 1: KẾ HOẠCH 7 NGÀY
cal_headers = [
    "Lịch Đăng",
    "Mã ID",
    "Chủ đề hạt nhân",
    "Định dạng / Nhịp đọc",
    "Trang 1 (Hook / Mở màn)",
    "Trang 2 (Cú lật bóc trần)",
    "Trang 3 (Chiếc gương phản tư)",
    "Văn bản hoàn chỉnh",
    "Khung giờ vàng",
    "Gợi ý Visual & Âm thanh TikTok",
    "Trạng thái"
]

cal_rows = [
    cal_headers,
    [
        "Thứ Hai (16/11)",
        "TXT-0001",
        "HYPOCRISY / POWER (Ân huệ & Quyền lực)",
        "Slide 2 trang (Đọc 5s)",
        "Có những ân huệ...",
        "...chỉ trở thành món nợ khi bạn bắt đầu nói \"KHÔNG\".",
        "-",
        "Có những ân huệ chỉ trở thành món nợ khi người nhận bắt đầu nói không.",
        "11:30 - 12:30 (Trưa)",
        "Tone đen tối, nhạc piano chậm, chữ trắng tối giản sans-serif",
        "SẴN SÀNG"
    ],
    [
        "Thứ Ba (17/11)",
        "TXT-0002",
        "SELF_DECEPTION / SOLITUDE (Tự lừa dối & Cô đơn)",
        "Slide 2 trang (Đọc 6s)",
        "Người ta sẵn sàng nhận lấy mọi sự bận rộn khiến mình kiệt sức...",
        "...chỉ để không phải ở một mình với người mà họ đã dành cả đời để che giấu.",
        "-",
        "Người ta chấp nhận mọi sự bận rộn khiến mình kiệt sức, chỉ để không phải ở một mình với người mà họ đã dành cả đời để che giấu.",
        "19:30 - 20:30 (Tối)",
        "Nhạc ambient trầm, hình ảnh bóng lưng trong phòng tĩnh lặng",
        "SẴN SÀNG"
    ],
    [
        "Thứ Tư (18/11)",
        "TXT-0003",
        "HYPOCRISY / MASK (Mặt nạ thánh thiện)",
        "Slide 3 trang (Đọc lướt 7s)",
        "Kẻ xấu luôn thích khoác lên mình vẻ thánh thiện...",
        "Không phải vì họ muốn hướng thiện...",
        "...mà vì sự tử tế là tấm bình phong an toàn nhất.",
        "Kẻ xấu luôn thích khoác lên mình vẻ thánh thiện, không phải vì họ muốn hướng thiện, mà vì sự tử tế là tấm bình phong an toàn nhất.",
        "11:30 - 12:30 (Trưa)",
        "Slide chuyển cảnh chậm, nhấn mạnh chữ \"tấm bình phong an toàn nhất\"",
        "SẴN SÀNG"
    ],
    [
        "Thứ Năm (19/11)",
        "TXT-0004",
        "DOUBLE_STANDARD (Tiêu chuẩn kép tha thứ)",
        "Slide 2 trang (Đọc 5s)",
        "Ta thường gọi lỗi lầm của người khác là \"bản chất\"...",
        "...nhưng lại gọi chính lỗi lầm ấy ở mình là \"hoàn cảnh bắt buộc\".",
        "-",
        "Ta gọi lỗi lầm của người khác là bản chất, nhưng lại gọi chính lỗi lầm ấy ở bản thân là hoàn cảnh bắt buộc.",
        "19:30 - 20:30 (Tối)",
        "Hình ảnh cán cân nghiêng hoặc 2 nửa khuôn mặt đối lập",
        "SẴN SÀNG"
    ],
    [
        "Thứ Sáu (20/11)",
        "TXT-0005",
        "EGO / STATUS (Khiêm nhường trình diễn)",
        "Slide 2 trang (Đọc 5s)",
        "Sự khiêm nhường đôi khi chỉ là một cách để đứng cao hơn...",
        "...khi điều người ta chờ đợi là tiếng vỗ tay cho cái cúi đầu.",
        "-",
        "Sự khiêm nhường đôi khi chỉ là một cách để đứng cao hơn, khi điều người ta chờ đợi là tiếng vỗ tay cho cái cúi đầu.",
        "19:00 - 21:00 (Tối cuối tuần)",
        "Ánh đèn sân khấu chiếu vào bóng người đang cúi đầu, nhạc cello sâu lắng",
        "SẴN SÀNG"
    ],
    [
        "Thứ Bảy (21/11)",
        "TXT-0006",
        "TRUTH / SELF_DECEPTION (Sự thật & Tự bào chữa)",
        "Slide 2 trang (Đọc 6s)",
        "Điều đau nhất của sự thật không phải là điều nó nói ra...",
        "...mà là những lời tự bào chữa nó đã lấy mất của ta.",
        "-",
        "Điều khó chịu nhất của sự thật không nằm ở điều nó nói ra, mà ở những lời bào chữa nó lấy mất.",
        "21:00 - 22:30 (Đêm muộn)",
        "Tiếng mưa rơi hoặc đồng hồ tích tắc, phông nền cửa sổ thành phố về đêm",
        "SẴN SÀNG"
    ],
    [
        "Chủ Nhật (22/11)",
        "TXT-0007",
        "FREEDOM / RESPONSIBILITY (Cái giá của tự do)",
        "Lướt đọc ngay (Đọc 4s)",
        "Ta thường đòi quyền tự do lựa chọn...",
        "...cho đến khi lựa chọn ấy không còn ai để đổ lỗi.",
        "-",
        "Ta thường đòi quyền tự chọn, cho đến khi lựa chọn ấy không còn ai để đổ lỗi.",
        "20:00 - 21:30 (Tối Chủ Nhật)",
        "Ảnh typography tối giản, chuyển động zoom chậm vào chữ \"đổ lỗi\"",
        "SẴN SÀNG"
    ]
]

with open("scripts/calendar_7days.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(cal_rows)

# DỮ LIỆU TAB 2: KHO TRIẾT NGÔN (PIPELINE)
archive_headers = [
    "Mã ID",
    "Tiêu đề",
    "Chủ đề hạt nhân",
    "Phân loại xuất xứ",
    "Cấp độ bằng chứng",
    "Trạng thái biên tập",
    "Điểm đánh giá (TB)",
    "Văn bản triết ngôn tiếng Việt",
    "Nguồn tư tưởng / Triết gia",
    "Ngày tạo"
]

archive_rows = [
    archive_headers,
    [
        "TXT-0001",
        "Ân huệ và món nợ",
        "HYPOCRISY / POWER",
        "INSPIRED_ORIGINAL",
        "VERIFIED_IDEA",
        "APPROVED",
        "4.5 / 5.0",
        "Có những ân huệ chỉ trở thành món nợ khi người nhận bắt đầu nói không.",
        "La Rochefoucauld (Reflections & Maxims #298)",
        "2026-11-14"
    ],
    [
        "TXT-0002",
        "Sự bận rộn và nỗi sợ ở một mình",
        "SELF_DECEPTION / SOLITUDE",
        "INSPIRED_ORIGINAL",
        "VERIFIED_IDEA",
        "APPROVED",
        "4.8 / 5.0",
        "Người ta chấp nhận mọi sự bận rộn khiến mình kiệt sức, chỉ để không phải ở một mình với người mà họ đã dành cả đời để che giấu.",
        "Blaise Pascal (Pensées §139 - On Diversion)",
        "2026-11-14"
    ],
    [
        "TXT-0003",
        "Tấm bình phong thánh thiện",
        "HYPOCRISY / MASK",
        "INSPIRED_ORIGINAL",
        "VERIFIED_IDEA",
        "APPROVED",
        "4.8 / 5.0",
        "Kẻ xấu luôn thích khoác lên mình vẻ thánh thiện, không phải vì họ muốn hướng thiện, mà vì sự tử tế là tấm bình phong an toàn nhất.",
        "La Rochefoucauld (Maxim 218 - Chuẩn hóa Hiyu Abyss)",
        "2026-11-14"
    ],
    [
        "TXT-0004",
        "Tiêu chuẩn kép của sự tha thứ",
        "DOUBLE_STANDARD",
        "INDEPENDENT_ORIGINAL",
        "UNVERIFIED",
        "APPROVED",
        "4.7 / 5.0",
        "Ta gọi lỗi lầm của người khác là bản chất, nhưng lại gọi chính lỗi lầm ấy ở bản thân là hoàn cảnh bắt buộc.",
        "Tâm lý học hành vi (Fundamental Attribution Error)",
        "2026-11-14"
    ],
    [
        "TXT-0005",
        "Khiêm nhường trình diễn",
        "EGO / STATUS",
        "INSPIRED_ORIGINAL",
        "VERIFIED_IDEA",
        "APPROVED",
        "4.6 / 5.0",
        "Sự khiêm nhường đôi khi chỉ là một cách để đứng cao hơn, khi điều người ta chờ đợi là tiếng vỗ tay cho cái cúi đầu.",
        "Friedrich Nietzsche & Baltasar Gracián",
        "2026-11-14"
    ],
    [
        "TXT-0006",
        "Sự thật và lời bào chữa",
        "TRUTH / SELF_DECEPTION",
        "INSPIRED_ORIGINAL",
        "VERIFIED_IDEA",
        "APPROVED",
        "4.9 / 5.0",
        "Điều khó chịu nhất của sự thật không nằm ở điều nó nói ra, mà ở những lời bào chữa nó lấy mất.",
        "Søren Kierkegaard",
        "2026-11-14"
    ],
    [
        "TXT-0007",
        "Cái giá của tự do",
        "FREEDOM / RESPONSIBILITY",
        "INSPIRED_ORIGINAL",
        "VERIFIED_IDEA",
        "APPROVED",
        "4.8 / 5.0",
        "Ta thường đòi quyền tự chọn, cho đến khi lựa chọn ấy không còn ai để đổ lỗi.",
        "Jean-Paul Sartre / Erich Fromm (Escape from Freedom)",
        "2026-11-14"
    ]
]

with open("scripts/archive_pipeline.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(archive_rows)

print("Exported calendar_7days.csv and archive_pipeline.csv")
