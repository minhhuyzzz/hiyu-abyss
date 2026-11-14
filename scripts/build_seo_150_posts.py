# -*- coding: utf-8 -*-
"""
Script nâng cấp toàn diện TikTok SEO cho 150 bài đăng Hiyu Abyss:
1. Tiêu Đề (Title): Tích hợp Search Query Brackets chuẩn SEO TikTok (dưới 90 từ).
2. Mô Tả (Caption): Chèn từ khóa tìm kiếm tự nhiên ở 100 ký tự đầu + Phân tích tâm lý + CTA kích hoạt comment chứa từ khóa.
3. Hashtags (5 cái): 150 BỘ HOÀN TOÀN ĐỘC NHẤT, chuẩn 5 tầng SEO (Ngách -> Danh mục -> Đời sống -> Triết lý -> Brand).
"""

import csv
import json
import subprocess

INPUT_CSV = "c:/hiyuabyss/scripts/tiktok_150_posts.csv"
OUTPUT_CSV = "c:/hiyuabyss/scripts/tiktok_150_posts_seo.csv"

# Từ điển SEO Niche & Category cho 20 chủ đề gốc và 6 chủ đề mới
THEME_SEO_CONFIG = {
    # 20 CORE THEMES
    "HYPOCRISY (Đạo đức giả & Sự giả tạo)": {
        "prefix": [
            "[Nhận Diện Đạo Đức Giả]",
            "[Bẫy Lòng Tốt]",
            "[Tâm Lý Học Hành Vi]",
            "[Kẻ Hai Mặt]",
            "[Sự Thật Mất Lòng]"
        ],
        "niche_tags": [
            ["#daoducgia", "#tamlyhocden", "#nhandienkegiatạo", "#baihoccanhan"],
            ["#bocchuan", "#anhuengam", "#ranhgioicanhan", "#suthatcuocsong"],
            ["#nguoihaimat", "#tamlyhanhvi", "#daoly", "#gocnhincuocsong"],
            ["#phancap", "#tutuong", "#thauhiệubảnthân", "#trietlynhansinh"],
            ["#ketoi", "#suthatphatlong", "#tuduyphanbien", "#tinhthuc"]
        ],
        "category_tags": ["#tamlyhoc", "#triethoc", "#kynangsong", "#tamlyhoc", "#phattrienbanthan"]
    },
    "DOUBLE_STANDARD (Tiêu chuẩn kép trong phán xét)": {
        "prefix": [
            "[Tiêu Chuẩn Kép]",
            "[Thói Đạo Mạo]",
            "[Tâm Lý Phán Xét]",
            "[Cái Giá Của Lòng Tự Trọng]",
            "[Bản Chất Con Người]"
        ],
        "niche_tags": [
            ["#tieuchuankep", "#phanxet", "#nhansinhcảm", "#tuduyphanbien"],
            ["#daomao", "#gocnhincuocsong", "#suthatcuocsong", "#baihoccanhan"],
            ["#tamlyxahoi", "#tuduydoctiep", "#thauhiệubảnthân", "#sauhai"],
            ["#tutrong", "#ranhgioi", "#kynangsong", "#truongthanh"],
            ["#banchatconnguoi", "#trietlynhansinh", "#chualanh", "#tamsu"]
        ],
        "category_tags": ["#tamlyhoc", "#triethoc", "#phattrienbanthan", "#tamlyhoc", "#kynangsong"]
    },
    "MORALITY (Lòng tốt & Điều kiện ngầm)": {
        "prefix": [
            "[Nghịch Lý Lòng Tốt]",
            "[Ân Huệ Độc Hại]",
            "[Ranh Giới Cho Đi]",
            "[Sự Tử Tế Thật Sự]",
            "[Tâm Lý Học Nợ Nần]"
        ],
        "niche_tags": [
            ["#longtot", "#anhuengam", "#ranhgioicanhan", "#chualanh"],
            ["#anhuetocdai", "#bocchuan", "#suthatcuocsong", "#baihoccanhan"],
            ["#chodivacanthuan", "#kynangsong", "#thaucam", "#gocnhincuocsong"],
            ["#tutechânthành", "#tuduy", "#truongthanh", "#trietlynhansinh"],
            ["#nononnoitam", "#tamlyhanhvi", "#sauhai", "#tamsu"]
        ],
        "category_tags": ["#tamlyhoc", "#kynangsong", "#chualanh", "#triethoc", "#tamlyhoc"]
    },
    "EGO (Bản ngã & Nhu cầu hơn người)": {
        "prefix": [
            "[Hội Chứng Ái Kỷ]",
            "[Chiếc Bẫy Bản Ngã]",
            "[Tâm Lý Hơn Thua]",
            "[Hạ Cái Tôi]",
            "[Bản Chất Bản Ngã]"
        ],
        "niche_tags": [
            ["#aiky", "#bannga", "#caitoi", "#thauhiệubảnthân"],
            ["#baybannga", "#honthua", "#suthatcuocsong", "#chualanhnoitam"],
            ["#tamlyhonthua", "#tuduyphanbien", "#tinhthuc", "#phattrienbanthan"],
            ["#hacaitoi", "#khiemton", "#kynangsong", "#baihoccanhan"],
            ["#banchatcaitoi", "#trietlynhansinh", "#truongthanh", "#sauhai"]
        ],
        "category_tags": ["#tamlyhoc", "#phattrienbanthan", "#triethoc", "#chualanh", "#tamlyhoc"]
    },
    "SELF_DECEPTION (Sự tự lừa dối & Vùng an toàn)": {
        "prefix": [
            "[Tự Lừa Dối]",
            "[Vùng An Toàn Độc Hại]",
            "[Đối Diện Sự Thật]",
            "[Ảo Tưởng Bản Thân]",
            "[Tỉnh Thức Nội Tâm]"
        ],
        "niche_tags": [
            ["#tulua", "#vungan toan", "#doidiensuthat", "#tinhthuc"],
            ["#vungantoandoc", "#suthatcuocsong", "#thauhiệubảnthân", "#sauhai"],
            ["#doidiensuthat", "#tuduy", "#truongthanh", "#baihoccanhan"],
            ["#aotuongbanthan", "#gocnhincuocsong", "#kynangsong", "#chualanh"],
            ["#tinhthucnoitam", "#trietlynhansinh", "#tamlyhanhvi", "#phattrienbanthan"]
        ],
        "category_tags": ["#tamlyhoc", "#phattrienbanthan", "#triethoc", "#tamlyhoc", "#kynangsong"]
    },
    "SHADOW (Góc khuất nội tâm & Sự chối bỏ)": {
        "prefix": [
            "[Tâm Lý Học Carl Jung]",
            "[Bóng Tối Tâm Hồn]",
            "[Shadow Work]",
            "[Chấp Nhận Bản Thân]",
            "[Góc Khuất Nội Tâm]"
        ],
        "niche_tags": [
            ["#carljung", "#shadowwork", "#tamlyhocden", "#thauhiệubảnthân"],
            ["#bongtoitamhon", "#chualanhnoitam", "#suthatcuocsong", "#sauhai"],
            ["#gockhuatnoitam", "#tamlyhanhvi", "#tinhthuc", "#triethoc"],
            ["#chapnhanbanthan", "#yeubanthan", "#truongthanh", "#baihoccanhan"],
            ["#shadowself", "#trietlynhansinh", "#chualanh", "#tamsu"]
        ],
        "category_tags": ["#tamlyhoc", "#triethoc", "#chualanh", "#tamlyhoc", "#phattrienbanthan"]
    },
    "MASK (Mặt nạ xã hội & Sự gồng gánh)": {
        "prefix": [
            "[Mặt Nạ Xã Hội]",
            "[Làm Hài Lòng Người Khác]",
            "[Áp Lực Đồng Trang Lứa]",
            "[Dám Sống Thật]",
            "[Sự Kiệt Sức Nội Tâm]"
        ],
        "niche_tags": [
            ["#matnaxahoi", "#lamhailongnguoikhac", "#apluccuocsong", "#chualanh"],
            ["#peoplepleaser", "#suthatcuocsong", "#ranhgioicanhan", "#sauhai"],
            ["#peerpressure", "#kynangsong", "#thauhiệubảnthân", "#tamsu"],
            ["#damsongthat", "#yeubanthan", "#truongthanh", "#baihoccanhan"],
            ["#kietsucnoitam", "#trietlynhansinh", "#tinhthuc", "#gocnhincuocsong"]
        ],
        "category_tags": ["#tamlyhoc", "#chualanh", "#kynangsong", "#phattrienbanthan", "#tamlyhoc"]
    },
    "POWER (Quyền lực ngầm & Kiểm soát)": {
        "prefix": [
            "[Tâm Lý Học Quyền Lực]",
            "[Kẻ Thích Kiểm Soát]",
            "[Thao Túng Vi Mô]",
            "[Ranh Giới Quyền Lực]",
            "[Mối Quan Hệ Độc Hại]"
        ],
        "niche_tags": [
            ["#quyenlucngam", "#kiemsoat", "#toxicrelationships", "#nhandien"],
            ["#kethichkiemsoat", "#suthatcuocsong", "#ranhgioicanhan", "#bocchuan"],
            ["#thaotungvimo", "#tamlyhocden", "#kynangsong", "#baihoccanhan"],
            ["#ranhgioiquyenluc", "#tuduyphanbien", "#truongthanh", "#sauhai"],
            ["#moiquanhedochai", "#trietlynhansinh", "#chualanh", "#tamsu"]
        ],
        "category_tags": ["#tamlyhoc", "#kynangsong", "#tamlyhoc", "#triethoc", "#phattrienbanthan"]
    },
    "MANIPULATION (Cảm giác tội lỗi & Nợ ân tình)": {
        "prefix": [
            "[Dấu Hiệu Thao Túng Tâm Lý]",
            "[Gaslighting Là Gì]",
            "[Thao Túng Tội Lỗi (Guilt Trip)]",
            "[Bẫy Cảm Xúc Độc Hại]",
            "[Thoát Khỏi Thao Túng]"
        ],
        "niche_tags": [
            ["#thaotungtamly", "#gaslighting", "#tamlyhocden", "#nhandienkethaotung"],
            ["#guilttrip", "#suthatcuocsong", "#ranhgioicanhan", "#bocchuan"],
            ["#baycamxuc", "#tamlyhanhvi", "#kynangsong", "#sauhai"],
            ["#thoatkhoithaotung", "#chualanhnoitam", "#truongthanh", "#baihoccanhan"],
            ["#toxicrelationships", "#trietlynhansinh", "#tuduy", "#tamsu"]
        ],
        "category_tags": ["#tamlyhoc", "#kynangsong", "#chualanh", "#tamlyhoc", "#phattrienbanthan"]
    },
    "FREEDOM (Tự do & Nỗi sợ tự chịu trách nhiệm)": {
        "prefix": [
            "[Nghịch Lý Tự Do]",
            "[Nỗi Sợ Trách Nhiệm]",
            "[Dũng Khí Trưởng Thành]",
            "[Tự Do Nội Tâm]",
            "[Triết Học Hiện Sinh]"
        ],
        "niche_tags": [
            ["#tudocanhan", "#trachnhiem", "#triethochienxinh", "#truongthanh"],
            ["#sohaisutudo", "#suthatcuocsong", "#tuduy", "#baihoccanhan"],
            ["#dungkhitruongthanh", "#thauhiệubảnthân", "#kynangsong", "#sauhai"],
            ["#tudonoitam", "#trietlynhansinh", "#tinhthuc", "#chualanh"],
            ["#hienxinh", "#gocnhincuocsong", "#phattrienbanthan", "#tamsu"]
        ],
        "category_tags": ["#triethoc", "#tamlyhoc", "#phattrienbanthan", "#kynangsong", "#triethoc"]
    },
    "TRUTH (Sự thật & Những lời tự bào chữa)": {
        "prefix": [
            "[Sự Thật Mất Lòng]",
            "[Lời Tự Bào Chữa]",
            "[Nỗi Sợ Sự Thật]",
            "[Bản Lĩnh Đối Diện]",
            "[Góc Nhìn Thực Tế]"
        ],
        "niche_tags": [
            ["#suthatphatlong", "#doidiensuthat", "#suthatcuocsong", "#sauhai"],
            ["#loitubaochua", "#tamlyhanhvi", "#thauhiệubảnthân", "#bocchuan"],
            ["#sohaisuthat", "#tuduyphanbien", "#kynangsong", "#baihoccanhan"],
            ["#banlinhdoidien", "#trietlynhansinh", "#truongthanh", "#tinhthuc"],
            ["#gocnhinthucte", "#triethoc", "#phattrienbanthan", "#tamsu"]
        ],
        "category_tags": ["#triethoc", "#tamlyhoc", "#phattrienbanthan", "#kynangsong", "#triethoc"]
    },
    "LOVE (Chiếm hữu đội lốt yêu thương)": {
        "prefix": [
            "[Yêu Hay Chiếm Hữu]",
            "[Tình Yêu Độc Hại]",
            "[Ranh Giới Trong Tình Yêu]",
            "[Tình Yêu Trưởng Thành]",
            "[Buông Bỏ Kiểm Soát]"
        ],
        "niche_tags": [
            ["#chiemhuu", "#tinhyeudochai", "#toxiclove", "#moiquanhe"],
            ["#yeuhaykiemsoat", "#suthatcuocsong", "#ranhgioicanhan", "#tamsu"],
            ["#ranhgioitinhyeu", "#tamlytinhyeu", "#chualanh", "#sauhai"],
            ["#tinhyeutruongthanh", "#erichfromm", "#baihoccanhan", "#trietlynhansinh"],
            ["#buongbokiemsoat", "#truongthanh", "#thauhiệubảnthân", "#tinhthuc"]
        ],
        "category_tags": ["#tamlyhoc", "#chualanh", "#kynangsong", "#triethoc", "#tamlyhoc"]
    },
    "LOYALTY (Lòng trung thành & Ranh giới trả giá)": {
        "prefix": [
            "[Cái Giá Của Lòng Trung Thành]",
            "[Trung Thành Mù Quáng]",
            "[Ranh Giới Tận Tụy]",
            "[Khi Nào Nên Rời Đi]",
            "[Lòng Tự Trọng Tối Thượng]"
        ],
        "niche_tags": [
            ["#trungthanh", "#trungthanhmuluang", "#suthatcuocsong", "#sauhai"],
            ["#ranhgioitantuy", "#ranhgioicanhan", "#kynangsong", "#baihoccanhan"],
            ["#khinaonenroidi", "#tamlyhanhvi", "#thauhiệubảnthân", "#tamsu"],
            ["#longtutrong", "#truongthanh", "#trietlynhansinh", "#chualanh"],
            ["#tuchoi", "#gocnhincuocsong", "#tuduyphanbien", "#phattrienbanthan"]
        ],
        "category_tags": ["#tamlyhoc", "#kynangsong", "#triethoc", "#phattrienbanthan", "#tamlyhoc"]
    },
    "ENVY (Đố kỵ ngầm & Sự so sánh)": {
        "prefix": [
            "[Nhận Diện Đố Kỵ Ngầm]",
            "[Chiếc Bẫy So Sánh]",
            "[Tâm Lý Ghen Tị]",
            "[Vượt Qua Tự Ti]",
            "[Hạnh Phúc Nội Tại]"
        ],
        "niche_tags": [
            ["#dokyngam", "#ghenty", "#tamlyhocden", "#nhandien"],
            ["#sosanhbanthan", "#suthatcuocsong", "#thauhiệubảnthân", "#sauhai"],
            ["#tamlyghenti", "#chualanhnoitam", "#kynangsong", "#baihoccanhan"],
            ["#vuotquatuoti", "#yeubanthan", "#truongthanh", "#tamsu"],
            ["#hanhphucnoitai", "#trietlynhansinh", "#tinhthuc", "#phattrienbanthan"]
        ],
        "category_tags": ["#tamlyhoc", "#chualanh", "#phattrienbanthan", "#kynangsong", "#tamlyhoc"]
    },
    "CROWD (Đám đông & Dũng khí bầy đàn)": {
        "prefix": [
            "[Tâm Lý Học Đám Đông]",
            "[Hiệu Ứng Bầy Đàn]",
            "[Dũng Khí Độc Lập]",
            "[Thoát Khỏi Định Kiến]",
            "[Tư Duy Độc Lập]"
        ],
        "niche_tags": [
            ["#tamlydamdong", "#hieuungbaydan", "#tuduydoctiep", "#lebon"],
            ["#dungkhibaydan", "#suthatcuocsong", "#tuduyphanbien", "#sauhai"],
            ["#dungkhiđộclập", "#kynangsong", "#thauhiệubảnthân", "#baihoccanhan"],
            ["#thoatkhoiđịnhkiến", "#truongthanh", "#trietlynhansinh", "#tamsu"],
            ["#tuduyđộclập", "#triethoc", "#phattrienbanthan", "#tinhthuc"]
        ],
        "category_tags": ["#tamlyhoc", "#triethoc", "#phattrienbanthan", "#kynangsong", "#tamlyhoc"]
    },
    "SUFFERING (Khổ đau & Thói quen đóng vai nạn nhân)": {
        "prefix": [
            "[Tâm Lý Nạn Nhân (Victim Mentality)]",
            "[Thói Quen Than Vãn]",
            "[Ngừng Đổ Lỗi]",
            "[Vượt Qua Tổn Thương]",
            "[Trưởng Thành Từ Nghịch Cảnh]"
        ],
        "niche_tags": [
            ["#tamlynanhan", "#victimmentality", "#ngungdoloi", "#thauhiệubảnthân"],
            ["#thoiwenthanvan", "#suthatcuocsong", "#kynangsong", "#sauhai"],
            ["#ngungbaibac", "#chualanhnoitam", "#truongthanh", "#baihoccanhan"],
            ["#vuotquatontheong", "#trietlynhansinh", "#yeubanthan", "#tamsu"],
            ["#truongthanhtunghichcanh", "#tinhthuc", "#phattrienbanthan", "#triethoc"]
        ],
        "category_tags": ["#tamlyhoc", "#chualanh", "#phattrienbanthan", "#kynangsong", "#tamlyhoc"]
    },
    "IDENTITY (Bản sắc khi ở một mình)": {
        "prefix": [
            "[Bạn Là Ai Khi Không Có Ai Nhìn]",
            "[Tìm Lại Chính Mình]",
            "[Lòng Tự Trọng Cốt Lõi]",
            "[Bản Sắc Cá Nhân]",
            "[Đặc Quyền Làm Chính Mình]"
        ],
        "niche_tags": [
            ["#bansaccanhan", "#timlaichinhminh", "#thauhiệubảnthân", "#chualanh"],
            ["#khiomoitminh", "#suthatcuocsong", "#tinhthuc", "#sauhai"],
            ["#longtutrong", "#yeubanthan", "#kynangsong", "#baihoccanhan"],
            ["#dacquyenlamchinhminh", "#truongthanh", "#trietlynhansinh", "#tamsu"],
            ["#banchatconnguoi", "#triethoc", "#phattrienbanthan", "#gocnhincuocsong"]
        ],
        "category_tags": ["#tamlyhoc", "#phattrienbanthan", "#triethoc", "#chualanh", "#tamlyhoc"]
    },
    "MEANING (Ý nghĩa hiện sinh & Sự vô nghĩa)": {
        "prefix": [
            "[Khủng Hoảng Hiện Sinh]",
            "[Tìm Ý Nghĩa Cuộc Sống]",
            "[Viktor Frankl & Ý Nghĩa Sống]",
            "[Vượt Qua Trống Rỗng]",
            "[Lý Do Để Tồn Tại]"
        ],
        "niche_tags": [
            ["#ynghiacuocsong", "#khunghoanghienxinh", "#viktorfrankl", "#triethoc"],
            ["#timynghiasong", "#suthatcuocsong", "#thauhiệubảnthân", "#sauhai"],
            ["#vuotquatrongrong", "#chualanhnoitam", "#kynangsong", "#baihoccanhan"],
            ["#lydodetontai", "#truongthanh", "#trietlynhansinh", "#tamsu"],
            ["#tutuonghienxinh", "#tinhthuc", "#phattrienbanthan", "#gocnhincuocsong"]
        ],
        "category_tags": ["#triethoc", "#tamlyhoc", "#chualanh", "#phattrienbanthan", "#triethoc"]
    },
    "SOLITUDE (Cô độc & Nỗi sợ tĩnh lặng)": {
        "prefix": [
            "[Nghệ Thuật Cô Độc]",
            "[Cô Độc Lành Mạnh]",
            "[Tại Sao Sợ Một Mình]",
            "[Sức Mạnh Của Tĩnh Lặng]",
            "[Làm Bạn Với Chính Mình]"
        ],
        "niche_tags": [
            ["#nghethuatcodon", "#codoclanhmanh", "#tinhlang", "#thauhiệubảnthân"],
            ["#taisaosomotminh", "#suthatcuocsong", "#chualanhnoitam", "#sauhai"],
            ["#sucmanhtinhlang", "#kynangsong", "#yeubanthan", "#baihoccanhan"],
            ["#lambanvoichinhminh", "#truongthanh", "#trietlynhansinh", "#tamsu"],
            ["#codocvatinhthuc", "#triethoc", "#phattrienbanthan", "#tinhthuc"]
        ],
        "category_tags": ["#tamlyhoc", "#chualanh", "#triethoc", "#phattrienbanthan", "#tamlyhoc"]
    },
    "STATUS (Danh vọng & Khiêm nhường trình diễn)": {
        "prefix": [
            "[Khiêm Nhường Giả Tạo (Humblebrag)]",
            "[Ảo Tưởng Danh Vọng]",
            "[Áp Lực Phải Thành Công]",
            "[Bản Chất Của Sự Thừa Nhận]",
            "[Tự Do Khỏi Định Kiến Xã Hội]"
        ],
        "niche_tags": [
            ["#khiemnhuonggiatao", "#humblebrag", "#danhvong", "#nhandien"],
            ["#aotuongthanhcong", "#suthatcuocsong", "#thauhiệubảnthân", "#sauhai"],
            ["#aplucthanhcong", "#kynangsong", "#bocchuan", "#baihoccanhan"],
            ["#suthuanhan", "#truongthanh", "#trietlynhansinh", "#tamsu"],
            ["#thoatkhoicoidinh", "#triethoc", "#phattrienbanthan", "#tuduyphanbien"]
        ],
        "category_tags": ["#tamlyhoc", "#phattrienbanthan", "#triethoc", "#kynangsong", "#tamlyhoc"]
    }
}

# Config cho 6 nhóm mới (101-150)
SUBTHEME_SEO_CONFIG = {
    "RANH GIỚI": {
        "prefix": "[Thiết Lập Ranh Giới Cá Nhân]",
        "tags": ["#ranhgioicanhan", "#tuchoi", "#kynangsong", "#truongthanh", "#hiyuabyss"],
        "category": "#kynangsong"
    },
    "THANH THẢN": {
        "prefix": "[Triết Học Khắc Kỷ & Bình Yên]",
        "tags": ["#triethockhacky", "#binhyentamhon", "#overthinking", "#chualanh", "#hiyuabyss"],
        "category": "#triethoc"
    },
    "KIÊN CƯỜNG": {
        "prefix": "[Sức Mạnh Vượt Qua Nghịch Cảnh]",
        "tags": ["#kiencuong", "#nghichcanh", "#phattrienbanthan", "#dongluc", "#hiyuabyss"],
        "category": "#phattrienbanthan"
    },
    "KẾT NỐI": {
        "prefix": "[Tình Yêu & Sự Gắn Kết Trưởng Thành]",
        "tags": ["#tinhyeutruongthanh", "#erichfromm", "#moiquanhe", "#tamlytinhyeu", "#hiyuabyss"],
        "category": "#tamlyhoc"
    },
    "BẢN SẮC": {
        "prefix": "[Đặc Quyền Làm Chính Mình]",
        "tags": ["#yeubanthan", "#bansaccanhan", "#longtutrong", "#thauhiệubảnthân", "#hiyuabyss"],
        "category": "#phattrienbanthan"
    },
    "VƯỢT PHÁN XÉT": {
        "prefix": "[Dũng Khí Thoát Khỏi Phán Xét]",
        "tags": ["#dungkhibidanghet", "#ngungquantam", "#suthatcuocsong", "#tuduyđộclập", "#hiyuabyss"],
        "category": "#triethoc"
    }
}

def optimize_posts():
    with open(INPUT_CSV, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    print(f"[*] Đang tối ưu SEO cho {len(rows)} bài đăng...")
    optimized_rows = []
    unique_hashtag_sets = set()

    for idx, row in enumerate(rows):
        stt = int(row[0])
        post_id = row[1]
        title = row[2]
        desc = row[3]
        author = row[4]
        # hashtags = row[5]
        slide_fmt = row[6]
        slide1 = row[7]
        slide2 = row[8]
        slide3 = row[9]
        full_text = row[10]
        theme = row[11]
        time_slot = row[12]
        schedule = row[13]
        image_theme = row[14]
        status = "SẴN SÀNG"

        # 1. OPTIMIZE TITLE (Dưới 90 từ, tích hợp SEO query brackets)
        new_title = title
        new_hashtags = []

        if idx < 100:
            # 20 CORE THEMES (5 posts each)
            cfg = THEME_SEO_CONFIG.get(theme)
            slot_in_theme = idx % 5
            prefix = cfg["prefix"][slot_in_theme]
            
            # Clean old brackets if any
            clean_t = title
            if clean_t.startswith("["):
                parts = clean_t.split("] ", 1)
                if len(parts) > 1:
                    clean_t = parts[1]

            new_title = f"{prefix} {clean_t}"
            
            # 5 Unique Hashtags
            t_niche = cfg["niche_tags"][slot_in_theme]
            t_cat = cfg["category_tags"][slot_in_theme]
            
            # Formulate 5 tags: [Niche1, Niche2, Category, Niche3/Author, #hiyuabyss]
            h_list = [t_niche[0], t_cat, t_niche[1], t_niche[2], "#hiyuabyss"]
            new_hashtags = " ".join(h_list)

        else:
            # 50 NEW CHARMING THEMES (101-150)
            theme_base = theme.split(" (")[0]
            sub_cfg = SUBTHEME_SEO_CONFIG.get(theme_base, {
                "prefix": "[Tâm Lý Học Chiêm Nghiệm]",
                "tags": ["#tamlyhoc", "#triethoc", "#chualanh", "#phattrienbanthan", "#hiyuabyss"],
                "category": "#tamlyhoc"
            })
            
            clean_t = title
            if clean_t.startswith("["):
                parts = clean_t.split("] ", 1)
                if len(parts) > 1:
                    clean_t = parts[1]
            
            new_title = f"{sub_cfg['prefix']} {clean_t}"
            
            # Author tag normalization
            author_clean = author.lower().replace(" ", "").replace("đ", "d").replace("ê", "e").replace("ô", "o").replace("ă", "a").replace("ư", "u").replace("ơ", "o").replace("í", "i").replace("á", "a").replace("à", "a").replace("ả", "a").replace("ã", "a").replace("ạ", "a").replace("'", "")
            author_tag = f"#{author_clean}" if len(author_clean) <= 15 else "#trietgia"
            
            tags_pool = sub_cfg["tags"]
            sub_intent = f"#{theme.split('(')[1].replace(')', '').replace(' ', '').lower()}" if "(" in theme else f"#baihoc{stt}"
            
            # Create a unique 5-tag combination for each post
            h_candidates = [
                tags_pool[0],
                tags_pool[1 if stt % 2 == 0 else 2],
                author_tag,
                sub_intent,
                "#hiyuabyss"
            ]
            # Ensure no duplicates inside the 5 tags
            seen_local = set()
            h_final = []
            for t in h_candidates:
                if t not in seen_local:
                    seen_local.add(t)
                    h_final.append(t)
            while len(h_final) < 5:
                fallback_tag = f"#tuduy{stt}" if f"#tuduy{stt}" not in seen_local else f"#chualanh{stt}"
                h_final.insert(3, fallback_tag)
                seen_local.add(fallback_tag)

            new_hashtags = " ".join(h_final)

        # 2. OPTIMIZE DESCRIPTION (SEO keyword first sentence + deep reflection + keyword CTA)
        clean_desc = desc.strip()
        # Ensure description starts with high-intent keyword if not present
        if not clean_desc.startswith("Trong tâm lý học") and not clean_desc.startswith("Theo triết học") and not clean_desc.startswith("Tâm lý học chỉ ra"):
            if "thao túng" in new_title.lower():
                kw_intro = "Trong tâm lý học hành vi, nhận diện kẻ thao túng và bẫy cảm xúc là kỹ năng sống sống còn. "
            elif "đạo đức giả" in new_title.lower() or "người tốt" in new_title.lower():
                kw_intro = "Tâm lý học chỉ ra rằng, ranh giới giữa lòng tốt chân thành và sự giả tạo có tính toán đôi khi chỉ cách nhau một sợi tóc. "
            elif "khắc kỷ" in new_title.lower() or "bình yên" in new_title.lower():
                kw_intro = "Triết học khắc kỷ dạy chúng ta phân định rõ ràng giữa điều ta kiểm soát được và miệng đời bên ngoài. "
            elif "ranh giới" in new_title.lower():
                kw_intro = "Thiết lập ranh giới cá nhân không phải là ích kỷ, mà là sự tôn trọng tối thiểu dành cho phẩm giá của chính mình. "
            elif "bản ngã" in new_title.lower() or "cái tôi" in new_title.lower():
                kw_intro = "Nhu cầu hơn người và chiếc bẫy bản ngã thường giam cầm chúng ta trong những cuộc chiến vô nghĩa. "
            else:
                kw_intro = "Mỗi trải nghiệm nội tâm đều là một chiếc gương phản chiếu bản chất sâu kín nhất của con người. "
            
            # Combine intro if clean_desc doesn't already contain it
            if kw_intro[:20] not in clean_desc:
                clean_desc = kw_intro + clean_desc

        # Ensure CTA question at the end for keyword comments
        if not clean_desc.endswith("?"):
            clean_desc += " Bạn đã từng trải qua cảm giác này chưa? Hãy để lại góc nhìn của bạn bên dưới phần bình luận nhé."

        unique_hashtag_sets.add(new_hashtags)

        optimized_rows.append([
            stt,
            post_id,
            new_title,
            clean_desc,
            author,
            new_hashtags,
            slide_fmt,
            slide1,
            slide2,
            slide3,
            full_text,
            theme,
            time_slot,
            schedule,
            image_theme,
            status
        ])

    print(f"[✓] Đã tạo {len(optimized_rows)} bài đăng tối ưu SEO.")
    print(f"[✓] Số bộ hashtag độc nhất: {len(unique_hashtag_sets)} / 150")

    # Lưu CSV
    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(optimized_rows)
    print(f"[✓] Đã ghi ra file: {OUTPUT_CSV}")

if __name__ == "__main__":
    optimize_posts()
