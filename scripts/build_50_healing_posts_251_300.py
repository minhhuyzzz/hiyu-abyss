#!/usr/bin/env python3
# scripts/build_50_healing_posts_251_300.py
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Build 50 Healing, Light & Psychological Resilience Posts (STT 251 - 300)
Tạo 50 bài nội dung mới theo trường phái Tâm lý học Chữa lành, Ánh sáng & Sức bật Tinh thần.
Xuất ra:
- scripts/posts_251_300.json
- scripts/tiktok_300_posts.csv (và cập nhật scripts/tiktok_200_posts.csv thành 300 dòng)
- 50 file markdown tại editorial/content/TXT-0251.md đến TXT-0300.md
"""

import json
import csv
import os

OUTPUT_JSON = "scripts/posts_251_300.json"
CSV_200_PATH = "scripts/tiktok_200_posts.csv"
CSV_300_PATH = "scripts/tiktok_300_posts.csv"
CONTENT_DIR = "editorial/content"

POSTS_DATA = [
    # =========================================================================
    # CỤM 1: TỰ TRẮC ẨN & HÒA GIẢI BẢN THÂN (STT 251 - 263 · 13 BÀI)
    # =========================================================================
    {
        "stt": 251,
        "id": "TXT-0251",
        "title": "[Tự Trắc Ẩn] Đừng dùng sự hiểu biết của hôm nay để dằn vặt sự dại khờ của ngày hôm qua.",
        "author": "Kristin Neff",
        "topic": "TỰ TRẮC ẨN (Chữa lành & Hòa giải)",
        "topic_code": "SELF_COMPASSION",
        "format": "Carousel 3 trang",
        "hook": "Bạn đang trừng phạt chính mình......",
        "twist": "Vì những quyết định sai lầm trong quá khứ, nhưng bạn quên mất rằng: Phiên bản của bạn ngày ấy đã phải vật lộn với những tổn thương, sự thiếu hiểu biết và nỗi sợ hãi tột cùng mà họ có lúc đó.",
        "mirror": "Nếu ngày xưa bạn biết những điều bạn biết hôm nay, bạn đã không lựa chọn như thế. Tha thứ cho chính mình không phải là bao biện; đó là cái ôm thấu cảm dành cho một đứa trẻ đã kiệt sức để bạn có thể đứng đây ngày hôm nay.",
        "deep": "-",
        "caption": "Tiến sĩ Kristin Neff, người tiên phong nghiên cứu về Tự Trắc Ẩn (Self-Compassion), chỉ ra rằng: Sự tự trách móc tàn nhẫn không bao giờ giúp con người tiến bộ; nó chỉ giam cầm bạn trong mặc cảm tội lỗi. Hãy nhìn lại phiên bản cũ bằng đôi mắt của một người quan sát bao dung. Bạn đã bao giờ tự nói lời xin lỗi với chính mình chưa?",
        "hashtags": "#tutracan #kristinneff #chualanh #thaothuchinhminh #hiyuabyss",
        "full_text": "Bạn đang trừng phạt chính mình vì quyết định sai lầm trong quá khứ... Nhưng ngày ấy bạn đã cố hết sức với nhận thức lúc đó. Tha thứ cho chính mình là cái ôm thấu cảm cho phiên bản đã kiệt sức.",
        "hours": "20:00 - 21:30",
        "schedule": "Thứ Hai",
        "concept": "Một người quỳ bên dòng suối trong vắt dưới ánh trăng, nhẹ nhàng rửa sạch bùn đất trên đôi bàn tay trầy xước."
    },
    {
        "stt": 252,
        "id": "TXT-0252",
        "title": "[Tự Trắc Ẩn] Sự mong manh không phải là yếu đuối; đó là thước đo chính xác nhất của lòng dũng cảm.",
        "author": "Brené Brown",
        "topic": "TỰ TRẮC ẨN (Chữa lành & Hòa giải)",
        "topic_code": "SELF_COMPASSION",
        "format": "Carousel 2 trang",
        "hook": "Dám để người khác nhìn thấy sự bất toàn của mình......",
        "twist": "Không phải là hành động đầu hàng; đó là khoảnh khắc bạn vứt bỏ chiếc áo giáp sắt nặng nề đang bóp nghẹt hơi thở của bạn để bước ra giữa đấu trường cuộc đời với phẩm giá chân thật nhất.",
        "mirror": "-",
        "deep": "-",
        "caption": "Tiến sĩ Brené Brown khẳng định: Sự mong manh (Vulnerability) là cái nôi sinh ra tình yêu, sự gắn kết và niềm hân hoan đích thực. Cố tỏ ra bất khả xâm phạm chỉ khiến bạn cô độc trong pháo đài do chính mình dựng nên. Dũng cảm để lộ vết thương là bước đầu tiên để chữa lành. Bạn có dám gỡ bỏ lớp mặt nạ gượng gạo hôm nay?",
        "hashtags": "#brenebrown #sumongmanh #dungcam #chualanh #hiyuabyss",
        "full_text": "Dám để người khác thấy sự bất toàn không phải yếu đuối... Đó là dũng khí vứt bỏ chiếc áo giáp sắt bóp nghẹt hơi thở để sống chân thật với phẩm giá của mình.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Ba",
        "concept": "Một hiệp sĩ cởi bỏ chiếc mũ giáp sắt đặt lên tảng đá, hít thở làn gió sớm trong lành trên thảo nguyên xanh."
    },
    {
        "stt": 253,
        "id": "TXT-0253",
        "title": "[Tự Trắc Ẩn] Nghịch lý kỳ diệu: Chỉ khi chấp nhận trọn vẹn bản thân, bạn mới có thể thực sự thay đổi.",
        "author": "Carl Rogers",
        "topic": "TỰ TRẮC ẨN (Chữa lành & Hòa giải)",
        "topic_code": "SELF_COMPASSION",
        "format": "Single-Punch (1 trang)",
        "hook": "Nghịch lý kỳ diệu của tâm hồn: Chỉ khi bạn học cách chấp nhận chính mình như bạn đang là, bạn mới có thể bắt đầu thay đổi một cách tự nhiên và bền vững.",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Nhà tâm lý học nhân văn Carl Rogers đúc kết: Cuộc chiến chống lại chính mình luôn là cuộc chiến duy nhất mà bạn cầm chắc phần thất bại. Khi bạn ngừng đay nghiến những khuyết điểm, nguồn năng lượng đó sẽ chuyển hóa thành sức mạnh tái tạo. Bạn đang ghét bỏ hay đang kiên nhẫn nuôi dưỡng chính mình?",
        "hashtags": "#carlrogers #chapnhanbanthan #tamlynhanvan #chualanh #hiyuabyss",
        "full_text": "Nghịch lý kỳ diệu của tâm hồn: Chỉ khi bạn học cách chấp nhận chính mình như bạn đang là, bạn mới có thể bắt đầu thay đổi một cách tự nhiên và bền vững.",
        "hours": "19:30 - 20:30",
        "schedule": "Thứ Tư",
        "concept": "Một mầm cây nhỏ bé tự tin tách vỏ hạt vươn mình đón những giọt nắng ban mai ấm áp."
    },
    {
        "stt": 254,
        "id": "TXT-0254",
        "title": "[Tự Trắc Ẩn] Khoảng dừng RAIN: Đừng tin tất cả những gì bộ não đang tự thêu dệt để trừng phạt bạn.",
        "author": "Tara Brach",
        "topic": "TỰ TRẮC ẨN (Chữa lành & Hòa giải)",
        "topic_code": "SELF_COMPASSION",
        "format": "Carousel 3 trang",
        "hook": "Cảm xúc tiêu cực chỉ là một đám mây ghé qua......",
        "twist": "Nó không phải là bản chất con người bạn. Sai lầm lớn nhất là khi bạn đồng nhất sự lo âu, thất vọng hay tự ti thành danh tính vĩnh viễn của chính mình.",
        "mirror": "Hãy thực hành 4 bước RAIN: Nhận diện (Recognize) - Cho phép hiện diện (Allow) - Thấu hiểu với lòng trắc ẩn (Investigate) - Nuôi dưỡng bằng tình yêu (Nurture). Cơn bão nào rồi cũng phải nhường chỗ cho bầu trời quang đãng.",
        "deep": "-",
        "caption": "Tiến sĩ tâm lý học Tara Brach hướng dẫn phương pháp RAIN giúp giải phóng tâm trí khỏi vòng xoáy tự chỉ trích. Hãy học cách ngồi lại bên nỗi buồn như một người bạn tri kỷ thay vì xua đuổi nó. Khi bạn đối xử dịu dàng với vết thương, nó sẽ tự khắc khép miệng. Hôm nay bạn có đang dành cho mình một khoảng lặng dịu êm?",
        "hashtags": "#tarabrach #rainpractice #chualanhnoitam #tinhthuc #hiyuabyss",
        "full_text": "Cảm xúc tiêu cực chỉ là đám mây ghé qua... Đừng đồng nhất nỗi buồn thành danh tính của bạn. Hãy nhận diện, cho phép và ôm ấp nó bằng lòng trắc ẩn.",
        "hours": "20:00 - 21:00",
        "schedule": "Thứ Năm",
        "concept": "Một ngọn nến sáng dịu dàng đặt bên khung cửa sổ nhìn ra khu vườn êm ả sau cơn mưa rào."
    },
    {
        "stt": 255,
        "id": "TXT-0255",
        "title": "[Tự Trắc Ẩn] Mỉm cười với đứa trẻ bên trong: Bạn không cần phải luôn mạnh mẽ để xứng đáng được yêu.",
        "author": "Thích Nhất Hạnh",
        "topic": "TỰ TRẮC ẨN (Chữa lành & Hòa giải)",
        "topic_code": "SELF_COMPASSION",
        "format": "Carousel 2 trang",
        "hook": "Đằng sau sự gắt gỏng hay khép kín của bạn hôm nay......",
        "twist": "Là một đứa trẻ năm xưa từng bị bỏ rơi, từng phải tự gồng mình lên để sinh tồn trong một môi trường không an toàn; và đứa trẻ đó chỉ đang khao khát được bạn ôm lấy và nói rằng: 'Mọi chuyện đã qua rồi, em an toàn rồi.'",
        "mirror": "-",
        "deep": "-",
        "caption": "Thiền sư Thích Nhất Hạnh răn dạy: Trong mỗi chúng ta đều có một đứa trẻ năm tuổi mang theo những vết thương chưa lành. Sự trưởng thành đích thực không phải là xua đuổi đứa trẻ ấy, mà là quay về lắng nghe và vỗ về nó bằng năng lượng tỉnh thức. Bạn đã bao giờ lắng nghe tiếng khóc thầm của chính mình?",
        "hashtags": "#thichnhathanh #duatrebentrong #chualanh #hieuvathuong #hiyuabyss",
        "full_text": "Đằng sau sự gắt gỏng hôm nay là đứa trẻ năm xưa từng bị tổn thương... Hãy quay về ôm lấy nó và nói: 'Mọi chuyện đã qua rồi, em an toàn rồi.'",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Sáu",
        "concept": "Một bàn tay người lớn ấm áp nhẹ nhàng nắm lấy bàn tay nhỏ bé của một đứa trẻ dưới bóng cây cổ thụ thanh bình."
    },
    {
        "stt": 256,
        "id": "TXT-0256",
        "title": "[Tự Trắc Ẩn] Học cách trở thành bến đỗ an toàn cho chính mình trước khi tìm kiếm sự che chở nơi người khác.",
        "author": "Kristin Neff",
        "topic": "TỰ TRẮC ẨN (Chữa lành & Hòa giải)",
        "topic_code": "SELF_COMPASSION",
        "format": "Single-Punch (1 trang)",
        "hook": "Thế giới ngoài kia có thể phán xét bạn, nhưng tâm hồn bạn phải là nơi trú ẩn an toàn nhất mà bạn có thể tìm về mà không sợ bị kết án.",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Khi bạn đối xử với bản thân bằng sự khắt khe của một quan tòa, bạn sẽ luôn sống trong sợ hãi. Nhưng khi bạn trở thành người bạn đồng hành trung thành nhất của chính mình, không có lời chỉ trích nào từ thế gian có thể đánh sụp được bạn. Bạn có đang là đồng minh hay là kẻ thù lớn nhất của mình?",
        "hashtags": "#tutracan #bendoantoan #yeuthuongchinhminh #kristinneff #hiyuabyss",
        "full_text": "Thế giới ngoài kia có thể phán xét bạn, nhưng tâm hồn bạn phải là nơi trú ẩn an toàn nhất mà bạn có thể tìm về mà không sợ bị kết án.",
        "hours": "19:30 - 20:30",
        "schedule": "Thứ Bảy",
        "concept": "Một ngôi nhà gỗ ấm cúng tỏa ánh sáng vàng êm đềm giữa rừng thông phủ tuyết trắng xóa."
    },
    {
        "stt": 257,
        "id": "TXT-0257",
        "title": "[Tự Trắc Ẩn] Cho phép bản thân nghỉ ngơi: Nghỉ ngơi không phải là phần thưởng của năng suất, đó là điều kiện sinh tồn.",
        "author": "Gabor Maté",
        "topic": "TỰ TRẮC ẨN (Chữa lành & Hòa giải)",
        "topic_code": "SELF_COMPASSION",
        "format": "Carousel 2 trang",
        "hook": "Nếu bạn không chủ động dành thời gian để nghỉ ngơi......",
        "twist": "Thì cơ thể và tâm trí của bạn sẽ tự động chọn một ngày đẹp trời để ngã quỵ và ép bạn phải dừng lại bằng một cơn kiệt sức hoặc bệnh tật trầm trọng.",
        "mirror": "-",
        "deep": "-",
        "caption": "Bác sĩ Gabor Maté nhấn mạnh trong 'When the Body Says No': Cơ thể luôn ghi nhớ những căng thẳng mà bộ não cố tình phớt lờ. Lắng nghe tiếng mệt mỏi của thân thể và dám đặt công việc xuống là hành động tự trắc ẩn can đảm nhất. Hôm nay bạn đã cho phép mình được thở một cách trọn vẹn chưa?",
        "hashtags": "#gabormate #nghingoi #langnghecothe #suckhoetinhthan #hiyuabyss",
        "full_text": "Nếu bạn không chủ động dành thời gian nghỉ ngơi... Cơ thể sẽ chọn một ngày để ép bạn phải dừng lại bằng sự kiệt sức. Nghỉ ngơi là điều kiện để tái sinh.",
        "hours": "20:00 - 21:00",
        "schedule": "Chủ Nhật",
        "concept": "Một cánh võng đung đưa dưới rặng liễu xanh rì rào bên mặt hồ gợn sóng lăn tăn trong buổi chiều nắng nhẹ."
    },
    {
        "stt": 258,
        "id": "TXT-0258",
        "title": "[Tự Trắc Ẩn] Buông bỏ chiếc mặt nạ cầu toàn: Hoàn hảo là ảo ảnh, trưởng thành mới là hiện thực.",
        "author": "Brené Brown",
        "topic": "TỰ TRẮC ẨN (Chữa lành & Hòa giải)",
        "topic_code": "SELF_COMPASSION",
        "format": "Carousel 3 trang",
        "hook": "Chủ nghĩa cầu toàn không phải là nỗ lực vươn lên xuất sắc......",
        "twist": "Đó là chiếc khiên phòng thủ nặng nề của nỗi sợ: 'Nếu tôi hoàn hảo, tôi sẽ không bị tổn thương, không bị phán xét và không bị chê cười.'",
        "mirror": "Nhưng cuộc đời vốn không bao giờ hoàn hảo. Dám chấp nhận một phiên bản chưa trọn vẹn nhưng chân thật và tiến bộ từng ngày chính là chìa khóa mở ra sự tự do đích thực của tâm hồn.",
        "deep": "-",
        "caption": "Brené Brown chỉ ra sự khác biệt sống còn: Hướng đến sự xuất sắc là vì sự phát triển bản thân; còn cầu toàn là vì nỗi sợ miệng đời. Hãy buông chiếc khiên ấy xuống để đôi tay bạn được tự do đón nhận cuộc sống. Bạn có đang kiệt sức vì cố gồng mình làm hài lòng tất cả?",
        "hashtags": "#brenebrown #chuniacautoan #tudonoitam #phattrienbanthan #hiyuabyss",
        "full_text": "Cầu toàn không phải nỗ lực xuất sắc, mà là chiếc khiên sợ hãi miệng đời. Dám chấp nhận phiên bản chưa hoàn hảo mới là chìa khóa của tự do đích thực.",
        "hours": "20:00 - 21:30",
        "schedule": "Thứ Hai",
        "concept": "Một chiếc bình gốm mộc mạc mang vết nứt tự nhiên nhưng cắm một cành hoa dại khoe sắc rực rỡ."
    },
    {
        "stt": 259,
        "id": "TXT-0259",
        "title": "[Tự Trắc Ẩn] Bạn không cần phải có ích mới có quyền được tồn tại trên cõi đời này.",
        "author": "Carl Rogers",
        "topic": "TỰ TRẮC ẨN (Chữa lành & Hòa giải)",
        "topic_code": "SELF_COMPASSION",
        "format": "Single-Punch (1 trang)",
        "hook": "Giá trị của bạn nằm ở chính sự hiện hữu của bạn, không phải ở số lượng công việc bạn hoàn thành hay sự hài lòng bạn mang lại cho người khác.",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Nhiều người trong chúng ta lớn lên với niềm tin sai lầm rằng: 'Mình chỉ xứng đáng được yêu khi mình làm hài lòng ai đó hoặc đạt được thành tích gì đó.' Hãy thức tỉnh: Bạn sinh ra đã là một kỳ tích trọn vẹn của vũ trụ. Bạn có đang gắn giá trị bản thân vào chiếc thước đo của xã hội?",
        "hashtags": "#carlrogers #giatribanthan #tutuoi #chualanhnoitam #hiyuabyss",
        "full_text": "Giá trị của bạn nằm ở chính sự hiện hữu của bạn, không phải ở số lượng công việc bạn hoàn thành hay sự hài lòng bạn mang lại cho người khác.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Ba",
        "concept": "Một cánh đồng hoa cỏ dại bạt ngàn nở rộ tự do dưới bầu trời bao la mà không cần bất kỳ sự công nhận nào."
    },
    {
        "stt": 260,
        "id": "TXT-0260",
        "title": "[Tự Trắc Ẩn] Đừng so sánh hậu trường hỗn độn của mình với sân khấu lộng lẫy của người khác.",
        "author": "Kristin Neff",
        "topic": "TỰ TRẮC ẨN (Chữa lành & Hòa giải)",
        "topic_code": "SELF_COMPASSION",
        "format": "Carousel 2 trang",
        "hook": "Khi bạn nhìn vào hào quang thành công của người khác......",
        "twist": "Bạn chỉ đang nhìn thấy phần nổi của tảng băng chìm; bạn không thấy được những đêm mất ngủ, sự hoang mang và những vết thương rỉ máu mà họ cũng đang phải âm thầm chịu đựng như chính bạn.",
        "mirror": "-",
        "deep": "-",
        "caption": "Cảm giác cô độc và thất bại thường xuất hiện khi ta đem nỗi đau sâu kín nhất của mình đi so sánh với nụ cười lung linh trên mạng xã hội của kẻ khác. Con người chung một nỗi khổ đau và bất toàn (Common Humanity). Hãy dịu dàng với hành trình của riêng bạn. Bạn có đang tự làm khổ mình bằng sự so sánh khập khiễng?",
        "hashtags": "#tutracan #sosanh #kristinneff #binhan #hiyuabyss",
        "full_text": "Khi nhìn vào hào quang người khác, bạn chỉ thấy sân khấu lộng lẫy chứ không thấy hậu trường đẫm nước mắt. Hãy kiên nhẫn với hành trình của riêng mình.",
        "hours": "19:30 - 20:30",
        "schedule": "Thứ Tư",
        "concept": "Một ngọn hải đăng sừng sững trong đêm tối chiếu rọi luồng sáng ấm áp hướng dẫn con thuyền nhỏ giữa biển."
    },
    {
        "stt": 261,
        "id": "TXT-0261",
        "title": "[Tự Trắc Ẩn] Ranh giới giữa kiên nhẫn và chịu đựng: Chữa lành cần thời gian, không thể đốt cháy giai đoạn.",
        "author": "Tara Brach",
        "topic": "TỰ TRẮC ẨN (Chữa lành & Hòa giải)",
        "topic_code": "SELF_COMPASSION",
        "format": "Carousel 3 trang",
        "hook": "Vết thương sâu cần thời gian để mọc da non......",
        "twist": "Bạn không thể bắt một cái cây lớn lên chỉ sau một đêm bằng cách kéo ngọn nó lên, cũng như bạn không thể ép trái tim mình phải lành lặn ngay lập tức sau một đổ vỡ tan nát.",
        "mirror": "Kiên nhẫn với chính mình là hình thức yêu thương tối cao. Hôm nay dù bạn chỉ tiến thêm được một bước nhỏ, hoặc đơn giản là giữ cho mình không gục ngã, điều đó đã là một chiến thắng phi thường.",
        "deep": "-",
        "caption": "Tara Brach nhắc nhở: Hãy tôn trọng nhịp điệu tự nhiên của tâm hồn. Chữa lành không phải là một đường thẳng đi lên, nó có những khúc quanh và những ngày mệt mỏi thụt lùi. Đừng mất kiên nhẫn với chính mình. Bạn đã tự ghi nhận sự nỗ lực âm thầm của bản thân ngày hôm nay chưa?",
        "hashtags": "#tarabrach #kiennhan #chualanh #suckhoetinhthan #hiyuabyss",
        "full_text": "Vết thương sâu cần thời gian mọc da non... Đừng ép mình phải lành lặn ngay sau đổ vỡ. Kiên nhẫn với chính mình là hình thức yêu thương tối cao.",
        "hours": "20:00 - 21:00",
        "schedule": "Thứ Năm",
        "concept": "Một mầm sồi non mọc lên kiên cường từ kẽ nứt của một tảng đá hoa cương cổ thụ phủ rêu xanh."
    },
    {
        "stt": 262,
        "id": "TXT-0262",
        "title": "[Tự Trắc Ẩn] Thừa nhận nỗi đau không làm bạn yếu đi, nó chứng minh bạn còn đang sống trọn vẹn.",
        "author": "Carl Rogers",
        "topic": "TỰ TRẮC ẨN (Chữa lành & Hòa giải)",
        "topic_code": "SELF_COMPASSION",
        "format": "Single-Punch (1 trang)",
        "hook": "Trái tim biết đau là trái tim còn biết yêu thương; đừng đóng băng cảm xúc của mình chỉ vì sợ hãi những vết xước của cuộc đời.",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Trốn chạy nỗi đau bằng sự lạnh lùng vô cảm chỉ tạo ra sự tê liệt cảm xúc. Khi bạn can đảm mở lòng đón nhận cả niềm vui lẫn nỗi buồn, cuộc đời bạn mới thực sự nở hoa rực rỡ và chân thực. Bạn có đang cho phép mình được cảm nhận trọn vẹn từng nhịp đập của sự sống?",
        "hashtags": "#carlrogers #camxuc #songtronven #chualanh #hiyuabyss",
        "full_text": "Trái tim biết đau là trái tim còn biết yêu thương; đừng đóng băng cảm xúc của mình chỉ vì sợ hãi những vết xước của cuộc đời.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Sáu",
        "concept": "Một bông hoa sen thanh khiết vươn mình nở rộ ngát hương từ bùn lầy dưới ánh bình minh rạng rỡ."
    },
    {
        "stt": 263,
        "id": "TXT-0263",
        "title": "[Tự Trắc Ẩn] Hãy là người đầu tiên tin tưởng vào tiềm năng vô hạn đang ngủ yên trong bạn.",
        "author": "Abraham Maslow",
        "topic": "TỰ TRẮC ẨN (Chữa lành & Hòa giải)",
        "topic_code": "SELF_COMPASSION",
        "format": "Carousel 2 trang",
        "hook": "Nếu chính bạn còn nghi ngờ năng lực của mình......",
        "twist": "Thì cả thế giới dù có vỗ tay tán thưởng cũng không thể làm cho bạn cảm thấy tự tin; sự công nhận từ bên ngoài chỉ là bọt xà phòng mong manh, chỉ có niềm tin tự thân sâu thẳm mới là mỏ neo vững chắc.",
        "mirror": "-",
        "deep": "-",
        "caption": "Nhà tâm lý học Abraham Maslow nhấn mạnh: Nhu cầu tự hiện thực hóa bản thân (Self-Actualization) bắt nguồn từ việc tin tưởng vào phẩm giá và tài năng nội tại của chính mình. Đừng đợi ai đó phong tước mới dám cất cánh bay. Hôm nay, bạn có dám tin vào đôi cánh của chính mình?",
        "hashtags": "#maslow #tuhienthuchoa #tintoibanthan #sucmanhnoitam #hiyuabyss",
        "full_text": "Nếu bạn còn nghi ngờ chính mình, lời tán dương của thế gian chỉ là bọt nước. Hãy là người đầu tiên đặt trọn niềm tin vào đôi cánh của bản thân.",
        "hours": "20:00 - 21:30",
        "schedule": "Thứ Bảy",
        "concept": "Một chú chim đại bàng sải rộng đôi cánh bay vút lên bầu trời bao la trên đỉnh núi tuyết ngập tràn ánh nắng."
    },

    # =========================================================================
    # CỤM 2: BÌNH THẢN KHẮC KỶ & LÀM CHỦ TÂM TRÍ (STT 264 - 275 · 12 BÀI)
    # =========================================================================
    {
        "stt": 264,
        "id": "TXT-0264",
        "title": "[Khắc Kỷ Bình Thản] Thước đo tự do: Phân định rạch ròi điều trong tầm kiểm soát và ngoài tầm kiểm soát.",
        "author": "Epictetus",
        "topic": "KHẮC KỶ (Bình thản & Tự chủ)",
        "topic_code": "STOIC_SERENITY",
        "format": "Carousel 3 trang",
        "hook": "Hầu hết những nỗi đau khổ của bạn......",
        "twist": "Đều bắt nguồn từ việc bạn cố gắng kiểm soát những thứ vốn dĩ không bao giờ thuộc quyền kiểm soát của bạn: Ý nghĩ của người khác, thời tiết, quá khứ và kết quả của ngày mai.",
        "mirror": "Thứ duy nhất thuộc về bạn là nhận thức, thái độ và hành động của bạn ngay giây phút này. Khi bạn trả lại những thứ ngoài tầm tay cho vũ trụ, bạn sẽ tìm thấy sự bình an tuyệt đối trong tâm hồn.",
        "deep": "-",
        "caption": "Bậc thầy Epictetus mở đầu cuốn Cẩm Nang Khắc Kỷ bằng nguyên lý tối thượng (Dichotomy of Control): Hạnh phúc và tự do chỉ bắt đầu từ khoảnh khắc ta biết buông tay những gì không thể kiểm soát. Bạn đang hao tổn năng lượng vào việc kiểm soát ai hay điều gì ngoài bản thân?",
        "hashtags": "#epictetus #khackyluatsong #dichotomyofcontrol #binhan #hiyuabyss",
        "full_text": "Hầu hết đau khổ đến từ việc cố kiểm soát điều ngoài tầm tay: Miệng đời, quá khứ và ngày mai. Trả lại chúng cho vũ trụ, bạn sẽ chạm vào tự do tuyệt đối.",
        "hours": "20:00 - 21:30",
        "schedule": "Chủ Nhật",
        "concept": "Một người lữ hành điềm tĩnh bước đi trên con đường đá ven biển trong buổi bình minh tĩnh lặng, mặc sóng biển vỗ rì rào."
    },
    {
        "stt": 265,
        "id": "TXT-0265",
        "title": "[Khắc Kỷ Bình Thản] Pháo đài nội tâm: Bạn có quyền lực trên tâm trí mình, không phải các sự kiện bên ngoài.",
        "author": "Marcus Aurelius",
        "topic": "KHẮC KỶ (Bình thản & Tự chủ)",
        "topic_code": "STOIC_SERENITY",
        "format": "Carousel 2 trang",
        "hook": "Nếu một điều gì đó bên ngoài làm bạn tổn thương......",
        "twist": "Thì nỗi đau đó không thực sự đến từ sự kiện ấy; nó đến từ chính sự phán xét và cách bạn diễn giải về nó. Và bạn hoàn toàn có quyền xóa bỏ sự phán xét đó ngay lúc này.",
        "mirror": "-",
        "deep": "-",
        "caption": "Hoàng đế La Mã Marcus Aurelius đúc kết trong Trầm Tưởng: Thế giới bên ngoài chỉ là những sự kiện khách quan vô cảm; chính tâm trí bạn mới là kẻ trao quyền cho nó làm tổn thương mình. Hãy thu mình về pháo đài nội tâm kiên cố. Bạn có muốn tước bỏ quyền làm bạn đau khổ của hoàn cảnh hôm nay?",
        "hashtags": "#marcusaurelius #tramtuong #phaodainoitam #khacky #hiyuabyss",
        "full_text": "Nếu điều bên ngoài làm bạn đau, nỗi đau ấy không đến từ sự kiện mà đến từ cách bạn phán xét nó. Bạn có toàn quyền tước bỏ sự phán xét đó ngay lúc này.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Hai",
        "concept": "Một pháo đài bằng đá cổ kính đứng sừng sững trên mỏm núi cao giữa bầu trời xanh trong vắt không một gợn mây."
    },
    {
        "stt": 266,
        "id": "TXT-0266",
        "title": "[Khắc Kỷ Bình Thản] Chúng ta đau khổ vì trí tưởng tượng nhiều hơn là vì thực tế cuộc đời.",
        "author": "Seneca",
        "topic": "KHẮC KỶ (Bình thản & Tự chủ)",
        "topic_code": "STOIC_SERENITY",
        "format": "Single-Punch (1 trang)",
        "hook": "Đừng tự đày đọa mình bằng những viễn cảnh tồi tệ chưa từng xảy ra; phần lớn những con quái vật bạn sợ hãi chỉ tồn tại trong suy nghĩ của chính bạn.",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Triết gia Seneca viết trong những bức thư gửi Lucilius: Nỗi sợ hãi tương lai làm cạn kiệt niềm vui hiện tại. Hãy kéo tâm trí mình về với thực tại trần trụi. Ngay giây phút này, bạn có đang an toàn và thở được không? Đừng để nỗi sợ bóng ma tương lai cướp đi sự bình yên của ngày hôm nay.",
        "hashtags": "#seneca #khacky #loau #songhientai #hiyuabyss",
        "full_text": "Đừng tự đày đọa mình bằng những viễn cảnh tồi tệ chưa từng xảy ra; phần lớn những con quái vật bạn sợ hãi chỉ tồn tại trong suy nghĩ của chính bạn.",
        "hours": "19:30 - 20:30",
        "schedule": "Thứ Ba",
        "concept": "Một người ngồi đọc sách thư thái bên ngọn đèn dầu ấm áp trong căn phòng gỗ nhìn ra đêm trăng thanh bình."
    },
    {
        "stt": 267,
        "id": "TXT-0267",
        "title": "[Khắc Kỷ Bình Thản] Amor Fati: Đừng chỉ chịu đựng nghịch cảnh, hãy yêu lấy nó như nguyên liệu tôi rèn bản lĩnh.",
        "author": "Friedrich Nietzsche",
        "topic": "KHẮC KỶ (Bình thản & Tự chủ)",
        "topic_code": "STOIC_SERENITY",
        "format": "Carousel 3 trang",
        "hook": "Công thức cho sự vĩ đại của con người......",
        "twist": "Không phải là mong muốn quá khứ khác đi, cũng không phải ước ao một cuộc đời trải đầy hoa hồng êm ả; mà là nhìn thẳng vào từng vết thương, từng mất mát và mỉm cười nói: 'Tôi yêu tất cả những điều này.'",
        "mirror": "Ngọn lửa lớn không bao giờ sợ gió; ngọn gió làm tắt ngọn nến nhưng lại thổi bùng ngọn lửa rừng. Mọi chông gai đều là củi khô nuôi dưỡng ngọn lửa ý chí trong bạn.",
        "deep": "-",
        "caption": "Triết lý Amor Fati (Yêu số phận) là đỉnh cao của sự trưởng thành nhận thức. Thay vì oán trách tại sao bão tố lại rơi vào đầu mình, hãy tự hỏi: 'Cơn bão này đang dạy mình trở nên kiên cường ra sao?' Bạn đã sẵn sàng đón nhận thử thách với nụ cười kiêu hãnh của một chiến binh?",
        "hashtags": "#amorfati #nietzsche #yeusophan #suckienkiong #hiyuabyss",
        "full_text": "Công thức của sự vĩ đại là Amor Fati: Yêu lấy từng vết thương như nguyên liệu tôi luyện. Ngọn gió làm tắt ngọn nến nhưng thổi bùng ngọn lửa rừng kiêu hãnh.",
        "hours": "20:00 - 21:00",
        "schedule": "Thứ Tư",
        "concept": "Một ngọn đuốc rực sáng bùng cháy mạnh mẽ trên đỉnh đèo cao trong một đêm ngàn sao lấp lánh."
    },
    {
        "stt": 268,
        "id": "TXT-0268",
        "title": "[Khắc Kỷ Bình Thản] Trở ngại chính là con đường: Thứ cản đường ta sẽ trở thành lối đi cho ta.",
        "author": "Marcus Aurelius",
        "topic": "KHẮC KỶ (Bình thản & Tự chủ)",
        "topic_code": "STOIC_SERENITY",
        "format": "Carousel 2 trang",
        "hook": "Khi bạn gặp một bức tường đá chặn lối......",
        "twist": "Đừng tuyệt vọng quay đầu; bức tường đó xuất hiện không phải để ngăn cản bạn, mà để thử thách xem bạn có đủ sáng tạo và kiên trì để biến nó thành bậc thang bước lên tầm cao mới hay không.",
        "mirror": "-",
        "deep": "-",
        "caption": "Marcus Aurelius viết câu cách ngôn bất hủ: 'The impediment to action advances action. What stands in the way becomes the way.' (Trở ngại hành động sẽ thúc đẩy hành động. Thứ cản đường trở thành con đường). Khó khăn chính là người thầy nghiêm khắc nhưng công bằng nhất. Bạn đang nhìn thử thách như tảng đá chặn đường hay bậc thang nâng tầm?",
        "hashtags": "#marcusaurelius #theobstacleistheway #khacky #vuotquakhokhan #hiyuabyss",
        "full_text": "Thứ cản đường ta sẽ trở thành con đường cho ta. Bức tường xuất hiện không để ngăn cản bạn, mà để thử thách xem bạn có biến nó thành bậc thang vươn cao.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Năm",
        "concept": "Một con đường mòn uốn lượn vượt qua những tảng đá gồ ghề vươn thẳng lên đỉnh núi cao đón ánh mặt trời."
    },
    {
        "stt": 269,
        "id": "TXT-0269",
        "title": "[Khắc Kỷ Bình Thản] Sự tĩnh lặng giữa giông bão: Hãy giống như vách đá làm dịu cơn cuồng nộ của sóng ngầm.",
        "author": "Marcus Aurelius",
        "topic": "KHẮC KỶ (Bình thản & Tự chủ)",
        "topic_code": "STOIC_SERENITY",
        "format": "Single-Punch (1 trang)",
        "hook": "Bất kể người đời có buông lời cay nghiệt hay hành xử thấp hèn, nhiệm vụ duy nhất của bạn là giữ vững sự chính trực và ánh sáng điềm tĩnh trong tâm hồn mình.",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Mỗi ngày chúng ta đều có thể gặp những kẻ vô ơn, xảo quyệt và thô lỗ. Nếu bạn đáp trả họ bằng chính sự cay độc của họ, bạn đã tự kéo mình xuống ngang hàng với họ. Điềm tĩnh và bao dung là sức mạnh tối thượng của một tâm hồn thượng đẳng. Hôm nay bạn có giữ được pháo đài bình thản ấy trước những va đập?",
        "hashtags": "#marcusaurelius #diemtinh #chinhsat #khackyluatsong #hiyuabyss",
        "full_text": "Bất kể người đời hành xử thấp hèn, nhiệm vụ duy nhất của bạn là giữ vững sự chính trực và ánh sáng điềm tĩnh trong tâm hồn mình.",
        "hours": "20:00 - 21:30",
        "schedule": "Thứ Sáu",
        "concept": "Một vách đá hoa cương sừng sững bên bờ đại dương bao la, từng đợt sóng bạc đầu xô vào rồi tan biến thành bọt trắng êm đềm."
    },
    {
        "stt": 270,
        "id": "TXT-0270",
        "title": "[Khắc Kỷ Bình Thản] Memento Mori: Nhớ rằng bạn sẽ chết không phải để bi quan, mà để trân quý từng hơi thở hôm nay.",
        "author": "Seneca",
        "topic": "KHẮC KỶ (Bình thản & Tự chủ)",
        "topic_code": "STOIC_SERENITY",
        "format": "Carousel 3 trang",
        "hook": "Bạn sống như thể bạn sẽ bất tử trên cõi đời này......",
        "twist": "Bạn lãng phí hàng giờ để bực tức vì một câu nói của người dưng, tiếc nuối những chuyện vụn vặt và hoãn lại những ước mơ chân thật nhất của mình sang ngày mai.",
        "mirror": "Hãy nhớ rằng: Hơi thở này là duy nhất, ngày hôm nay là vô giá. Khi bạn nhận thức được sự hữu hạn của đời người, mọi giận hờn nhỏ nhen lập tức biến thành tro bụi, nhường chỗ cho tình yêu thương và sự tỉnh thức.",
        "deep": "-",
        "caption": "Triết gia Seneca nhắc nhở: 'Cuộc đời không ngắn ngủi, chỉ là chúng ta đã lãng phí quá nhiều.' Memento Mori là liều thuốc giải độc cho sự trì hoãn và những âu lo vô bổ. Bạn có đang sống trọn vẹn cho những điều thực sự quan trọng trong ngày hôm nay?",
        "hashtags": "#seneca #mementomori #tranquycuocsong #khacky #hiyuabyss",
        "full_text": "Ý thức về sự hữu hạn của đời người (Memento Mori) là liều thuốc làm tan biến mọi giận hờn vụn vặt, nhường chỗ cho tình yêu thương và sự sống trọn vẹn hôm nay.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Bảy",
        "concept": "Một chiếc đồng hồ cát bằng đồng cổ kính đặt bên một đóa hoa hồng đỏ thắm nở rộ dưới ánh nắng ban trưa ấm áp."
    },
    {
        "stt": 271,
        "id": "TXT-0271",
        "title": "[Khắc Kỷ Bình Thản] Làm chủ phản ứng: Giữa kích thích và phản ứng luôn có một khoảng trống của tự do.",
        "author": "Viktor Frankl",
        "topic": "KHẮC KỶ (Bình thản & Tự chủ)",
        "topic_code": "STOIC_SERENITY",
        "format": "Carousel 2 trang",
        "hook": "Khi ai đó xúc phạm hoặc làm bạn nổi giận......",
        "twist": "Bạn không bắt buộc phải phản xạ ngay như một cỗ máy; giữa sự kiện xảy ra và phản ứng của bạn luôn có một khoảng dừng tĩnh lặng — và chính trong khoảng dừng đó chứa đựng tự do và sự trưởng thành của bạn.",
        "mirror": "-",
        "deep": "-",
        "caption": "Bác sĩ Viktor Frankl đúc kết từ địa ngục trại tập trung: Thứ duy nhất người ta không thể cướp đi từ bạn là quyền tự do lựa chọn thái độ trước hoàn cảnh. Đừng để người khác cầm remote điều khiển cảm xúc của bạn. Bạn có dám hít một hơi thật sâu để làm chủ khoảng dừng quý giá đó?",
        "hashtags": "#viktorfrankl #khoangdungtutri #lamchucamxuc #tudonoitam #hiyuabyss",
        "full_text": "Giữa kích thích và phản ứng có một khoảng dừng; trong khoảng dừng đó chứa đựng tự do và sự trưởng thành của bạn. Hãy làm chủ phản ứng của chính mình.",
        "hours": "19:30 - 20:30",
        "schedule": "Chủ Nhật",
        "concept": "Một chiếc chuông đồng tĩnh lặng treo dưới mái hiên chùa cổ giữa buổi sáng sớm sương mờ thanh tịnh."
    },
    {
        "stt": 272,
        "id": "TXT-0272",
        "title": "[Khắc Kỷ Bình Thản] Không có kẻ thù nào bên ngoài nguy hiểm bằng sự mất kiểm soát bên trong chính bạn.",
        "author": "Epictetus",
        "topic": "KHẮC KỶ (Bình thản & Tự chủ)",
        "topic_code": "STOIC_SERENITY",
        "format": "Single-Punch (1 trang)",
        "hook": "Kẻ làm bạn tổn thương không phải là người lăng mạ bạn, mà là chính nhận thức của bạn khi bạn tin rằng mình đang bị tổn thương.",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Epictetus dạy rằng: Một tảng đá không thể bị tổn thương bởi những lời nguyền rủa; bạn cũng có thể trở nên bất khả chiến bại như tảng đá ấy nếu bạn không để sự phán xét của kẻ khác thâm nhập vào pháo đài tâm trí mình. Sự tĩnh lặng là tấm khiên bất khả xuyên thủng. Bạn đã trang bị tấm khiên ấy cho mình chưa?",
        "hashtags": "#epictetus #khackyluatsong #tamkhiendiemptinh #tuchu #hiyuabyss",
        "full_text": "Kẻ làm bạn tổn thương không phải người lăng mạ bạn, mà là chính nhận thức của bạn khi bạn tin rằng mình đang bị tổn thương. Sự tĩnh lặng là tấm khiên bất khả chiến bại.",
        "hours": "20:00 - 21:30",
        "schedule": "Thứ Hai",
        "concept": "Một chiếc gương đồng phẳng lặng sáng bóng phản chiếu ánh sáng mặt trời xua tan bóng tối u ám."
    },
    {
        "stt": 273,
        "id": "TXT-0273",
        "title": "[Khắc Kỷ Bình Thản] Đừng đòi hỏi hoàn cảnh phải theo ý bạn; hãy muốn chúng xảy ra như bản chất của chúng.",
        "author": "Epictetus",
        "topic": "KHẮC KỶ (Bình thản & Tự chủ)",
        "topic_code": "STOIC_SERENITY",
        "format": "Carousel 2 trang",
        "hook": "Cơn giận dữ xuất hiện khi bạn bắt thực tế......",
        "twist": "Phải phục tùng theo những kỳ vọng cứng nhắc trong đầu bạn; nhưng khi bạn học được cách đón nhận dòng chảy cuộc đời như dòng nước êm đềm lượn qua các ghềnh đá, tâm hồn bạn sẽ luôn tìm thấy sự an lạc.",
        "mirror": "-",
        "deep": "-",
        "caption": "Sự mềm mại và linh hoạt của dòng nước là bài học vĩ đại nhất của sự sống. Càng cố chấp gồng mình chống lại quy luật tự nhiên, bạn càng đau đớn. Hãy hòa mình vào dòng chảy của vũ trụ với sự khiêm nhường và tỉnh táo. Bạn đang gồng mình chống cự hay đang thuận theo dòng chảy với sự tự chủ?",
        "hashtags": "#epictetus #thuantunhien #binhthancuocsong #khacky #hiyuabyss",
        "full_text": "Cơn giận xuất hiện khi bắt thực tế phải phục tùng kỳ vọng trong đầu. Học cách đón nhận dòng chảy cuộc đời như dòng nước qua ghềnh đá để tìm an lạc.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Ba",
        "concept": "Một dòng suối mát lành trong vắt uốn lượn êm ả qua những phiến đá tròn nhẵn dưới bóng rừng xanh mát."
    },
    {
        "stt": 274,
        "id": "TXT-0274",
        "title": "[Khắc Kỷ Bình Thản] Đơn giản hóa cuộc sống: Sự giàu có đích thực là có ít ham muốn, không phải có nhiều của cải.",
        "author": "Seneca",
        "topic": "KHẮC KỶ (Bình thản & Tự chủ)",
        "topic_code": "STOIC_SERENITY",
        "format": "Carousel 3 trang",
        "hook": "Kẻ nghèo nhất không phải là người có ít tiền......",
        "twist": "Mà là người luôn thèm khát những thứ mình chưa có và lo sợ đánh mất những thứ mình đang sở hữu; lòng tham vô đáy biến bạn thành nô lệ vĩnh viễn cho những vật ngoài thân.",
        "mirror": "Biết đủ là đỉnh cao của sự tự do. Khi tâm hồn bạn không còn bị trói buộc bởi những nhu cầu phù phiếm, một chén trà thơm, một cuốn sách hay và một buổi hoàng hôn tĩnh lặng cũng đủ làm bạn thấy đủ đầy hơn cả một bậc đế vương.",
        "deep": "-",
        "caption": "Seneca nhắc nhở: Hãy phân biệt giữa nhu cầu tự nhiên của cơ thể và những ham muốn vô tận do xã hội cấy vào đầu bạn. Cắt giảm những gánh nặng không cần thiết là cách nhanh nhất để tâm trí bạn được thảnh thơi bay bổng. Hôm nay bạn có thể buông bớt một ham muốn nào để lòng mình nhẹ nhõm hơn?",
        "hashtags": "#seneca #bietdu #sogngtoigian #khacky #hiyuabyss",
        "full_text": "Biết đủ là đỉnh cao của tự do. Kẻ nghèo nhất là người luôn thèm khát không đáy. Khi không bị trói buộc bởi hư danh, một chén trà thơm cũng đủ làm nên hạnh phúc.",
        "hours": "19:30 - 20:30",
        "schedule": "Thứ Tư",
        "concept": "Một tách trà gốm mộc tỏa khói nghi ngút bên cuốn sách mở trên chiếc bàn gỗ mộc ngoài ban công tràn ngập nắng mai."
    },
    {
        "stt": 275,
        "id": "TXT-0275",
        "title": "[Khắc Kỷ Bình Thản] Bình minh mỗi ngày là một lời mời gọi sống trọn vẹn và cống hiến cho đời.",
        "author": "Marcus Aurelius",
        "topic": "KHẮC KỶ (Bình thản & Tự chủ)",
        "topic_code": "STOIC_SERENITY",
        "format": "Single-Punch (1 trang)",
        "hook": "Khi bạn thức dậy vào buổi sáng, hãy nhớ rằng bạn đang được ban tặng một đặc ân vô giá: Được sống, được thở, được suy nghĩ, được yêu thương và được cống hiến.",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Hoàng đế Marcus Aurelius từng tự nhắc nhở bản thân mỗi khi muốn lười biếng trên giường: 'Ta thức dậy để làm công việc của một con người.' Mỗi buổi sáng là một cơ hội tái sinh để bạn sống đẹp hơn ngày hôm qua. Bạn sẽ đón chào ngày mới hôm nay với lòng biết ơn hay với tiếng thở dài?",
        "hashtags": "#marcusaurelius #binhminh #songynghia #khacky #hiyuabyss",
        "full_text": "Khi thức dậy vào buổi sáng, hãy nhớ bạn được trao đặc ân vô giá: Được sống, được thở, được suy nghĩ, được yêu thương và được cống hiến trọn vẹn.",
        "hours": "20:00 - 21:00",
        "schedule": "Thứ Năm",
        "concept": "Ánh mặt trời vàng rực rỡ ló dạng trên biển mây đỉnh núi, chiếu rọi luồng sáng ấm áp xuống nhân gian bừng tỉnh giấc."
    },

    # =========================================================================
    # CỤM 3: KẾT NỐI LÀNH MẠNH & GIAO TIẾP THẤU CẢM (STT 276 - 288 · 13 BÀI)
    # =========================================================================
    {
        "stt": 276,
        "id": "TXT-0276",
        "title": "[Giao Tiếp Thấu Cảm] Giao tiếp trắc ẩn NVC: Kết nối vượt qua rào cản của sự phán xét và chỉ trích.",
        "author": "Marshall Rosenberg",
        "topic": "KẾT NỐI LÀNH MẠNH (Giao tiếp & Thấu cảm)",
        "topic_code": "AUTHENTIC_CONNECTION",
        "format": "Carousel 3 trang",
        "hook": "Phía sau mọi lời chỉ trích gay gắt......",
        "twist": "Là một nhu cầu chính đáng chưa được đáp ứng và một nỗi đau chưa được thấu hiểu. Kẻ dùng bạo lực ngôn từ thực chất là người đang bất lực trong việc cất lên tiếng nói chân thật của mình.",
        "mirror": "Giao tiếp trắc ẩn (Nonviolent Communication) dạy ta 4 bước: Quan sát không phán xét - Bày tỏ cảm xúc thật - Gọi tên nhu cầu cốt lõi - Đưa ra đề nghị cụ thể. Khi ta thôi chỉ trích, cánh cửa đồng cảm sẽ tự động mở ra.",
        "deep": "-",
        "caption": "Tiến sĩ Marshall Rosenberg khẳng định: Ngôn từ có thể là những bức tường ngăn cách, nhưng cũng có thể là những ô cửa sổ kết nối tâm hồn. Thay vì tấn công đối phương, hãy dũng cảm nói rõ nhu cầu của chính mình. Lần gần nhất bạn lắng nghe người khác mà không ngắt lời hay phán xét là khi nào?",
        "hashtags": "#marshallrosenberg #nvc #giaotieptracan #thaucam #hiyuabyss",
        "full_text": "Phía sau mọi lời chỉ trích là một nhu cầu chưa được lắng nghe. Hãy thực hành NVC: Quan sát không phán xét, bày tỏ cảm xúc thật và gọi tên nhu cầu để mở ra sự thấu cảm.",
        "hours": "20:00 - 21:30",
        "schedule": "Thứ Sáu",
        "concept": "Hai người ngồi đối diện nhau trong khu vườn hoa nở rộ, ánh mắt thấu cảm chan hòa dưới bóng cây râm mát."
    },
    {
        "stt": 277,
        "id": "TXT-0277",
        "title": "[Giao Tiếp Thấu Cảm] Lắng nghe sâu: Món quà quý giá nhất bạn có thể trao tặng một người là sự hiện diện trọn vẹn.",
        "author": "Thích Nhất Hạnh",
        "topic": "KẾT NỐI LÀNH MẠNH (Giao tiếp & Thấu cảm)",
        "topic_code": "AUTHENTIC_CONNECTION",
        "format": "Carousel 2 trang",
        "hook": "Hầu hết chúng ta không lắng nghe để thấu hiểu......",
        "twist": "Chúng ta chỉ đang lắng nghe để chuẩn bị phản bác, đưa ra lời khuyên hoặc chứng minh rằng mình đúng; và trong sự ồn ào của cái tôi đó, chúng ta đánh mất cơ hội thực sự chạm vào tâm hồn người khác.",
        "mirror": "-",
        "deep": "-",
        "caption": "Thiền sư Thích Nhất Hạnh răn dạy về Lắng Nghe Sâu (Deep Listening): Chỉ cần ngồi yên và lắng nghe với lòng từ bi, không phán xét, không sửa lưng, bạn đã có thể giúp người đối diện trút bỏ được một nửa gánh nặng đau khổ trong lòng họ. Bạn có thể dành cho người thân yêu 10 phút hiện diện trọn vẹn hôm nay?",
        "hashtags": "#thichnhathanh #langnghesau #hienhuatronven #yeuthuong #hiyuabyss",
        "full_text": "Lắng nghe sâu không phải để phản bác hay cho lời khuyên, mà là trao tặng sự hiện diện trọn vẹn giúp đối phương trút bỏ gánh nặng trong lòng.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Bảy",
        "concept": "Một người ngồi im lặng lắng nghe bên cạnh người bạn tri kỷ dưới ánh trăng êm dịu bên hiên nhà gỗ."
    },
    {
        "stt": 278,
        "id": "TXT-0278",
        "title": "[Giao Tiếp Thấu Cảm] Yêu là nghệ thuật cần học hỏi và rèn luyện, không phải một cảm xúc ngẫu nhiên rơi xuống.",
        "author": "Erich Fromm",
        "topic": "KẾT NỐI LÀNH MẠNH (Giao tiếp & Thấu cảm)",
        "topic_code": "AUTHENTIC_CONNECTION",
        "format": "Single-Punch (1 trang)",
        "hook": "Tình yêu trưởng thành nói: 'Tôi cần bạn vì tôi yêu bạn.' Còn tình yêu non nớt nói: 'Tôi yêu bạn vì tôi cần bạn để lấp đầy sự trống rỗng trong tôi.'",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Triết gia Erich Fromm phân tích trong kiệt tác 'The Art of Loving': Tình yêu đích thực không phải là sự phụ thuộc cảm xúc (Codependency) hay sự chiếm đoạt; nó là sự quan tâm chủ động, tôn trọng và nâng đỡ sự tự do của đối phương. Bạn đang yêu người khác để lấp đầy nỗi sợ hay để cùng nhau thăng hoa?",
        "hashtags": "#erichfromm #theartofloving #nghethuatyeu #tinhyeutruongthanh #hiyuabyss",
        "full_text": "Tình yêu trưởng thành nói: 'Tôi cần bạn vì tôi yêu bạn.' Còn tình yêu non nớt nói: 'Tôi yêu bạn vì tôi cần bạn lấp đầy sự trống rỗng trong tôi.'",
        "hours": "19:30 - 20:30",
        "schedule": "Chủ Nhật",
        "concept": "Hai cây đại thụ xanh tốt mọc cạnh nhau trong một thung lũng, cành lá đan xen nhưng gốc rễ đứng độc lập vững chãi."
    },
    {
        "stt": 279,
        "id": "TXT-0279",
        "title": "[Giao Tiếp Thấu Cảm] 5 Chiếc chìa khóa hàn gắn: Xây dựng tài khoản tình cảm bằng những hành động nhỏ nhặt hàng ngày.",
        "author": "John Gottman",
        "topic": "KẾT NỐI LÀNH MẠNH (Giao tiếp & Thấu cảm)",
        "topic_code": "AUTHENTIC_CONNECTION",
        "format": "Carousel 3 trang",
        "hook": "Hôn nhân hay tình bạn bền vững......",
        "twist": "Không được xây dựng bằng những kỳ nghỉ xa hoa hay những lời thề non hẹn biển; nó được dệt nên từ những cử chỉ nhỏ bé lặp đi lặp lại: Một cái ôm ấm áp buổi sáng, một lời cảm ơn chân thành, một ánh mắt thấu hiểu sau ngày dài mệt mỏi.",
        "mirror": "Quy tắc vàng 5:1 của Gottman chỉ ra: Cần ít nhất 5 tương tác tích cực để bù đắp cho 1 tương tác tiêu cực. Hãy chủ động tích lũy sự tin cậy và lòng biết ơn vào tài khoản tình cảm mỗi ngày.",
        "deep": "-",
        "caption": "Tiến sĩ John Gottman đã dành hơn 40 năm nghiên cứu hàng ngàn cặp đôi tại Love Lab. Bí quyết để một mối quan hệ không bao giờ tàn phai chính là sự quan tâm có ý thức trong những khoảnh khắc đời thường nhất. Hôm nay bạn đã gửi một lời yêu thương chân thật nào đến người bên cạnh chưa?",
        "hashtags": "#johngottman #honnhanbenvung #tuvandantam #yeuthuonghangngay #hiyuabyss",
        "full_text": "Mối quan hệ bền vững dệt nên từ những cử chỉ nhỏ bé đời thường: Một lời cảm ơn, một cái ôm ấm áp. Hãy duy trì tỷ lệ vàng 5 tích cực cho 1 tiêu cực.",
        "hours": "20:00 - 21:30",
        "schedule": "Thứ Hai",
        "concept": "Một bàn ăn nhỏ ấm cúng trong ánh nến vàng, một bình hoa tươi và hai tách trà thơm bốc khói nhẹ."
    },
    {
        "stt": 280,
        "id": "TXT-0280",
        "title": "[Giao Tiếp Thấu Cảm] Dũng cảm nói lời xin lỗi chân thành: Nhận lỗi không làm giảm giá trị của bạn, nó nâng tầm nhân cách.",
        "author": "Harriet Lerner",
        "topic": "KẾT NỐI LÀNH MẠNH (Giao tiếp & Thấu cảm)",
        "topic_code": "AUTHENTIC_CONNECTION",
        "format": "Carousel 2 trang",
        "hook": "Một lời xin lỗi kèm theo chữ 'nhưng'......",
        "twist": "Không phải là sự hối lỗi; đó là sự bao biện và trút ngược lỗi lầm sang nạn nhân. Lời xin lỗi đích thực phải dũng cảm chịu trách nhiệm trọn vẹn về hành vi của mình mà không cần đòi hỏi đối phương phải lập tức tha thứ.",
        "mirror": "-",
        "deep": "-",
        "caption": "Bác sĩ tâm lý Harriet Lerner trong 'Why Won't You Apologize?' chỉ ra: Một lời xin lỗi vụng về hay phòng thủ chỉ đào sâu thêm vết thương. Ngược lại, dám nhận lỗi chân thành là cầu nối mạnh mẽ nhất để tái thiết lòng tin đã rạn nứt. Bạn có đủ dũng khí nói lời xin lỗi không điều kiện?",
        "hashtags": "#harrietlerner #xinloichanthanh #taitietlongtin #giaotiep #hiyuabyss",
        "full_text": "Lời xin lỗi kèm chữ 'nhưng' là lời bao biện. Lời xin lỗi chân thành là dũng cảm nhận trách nhiệm trọn vẹn để hàn gắn niềm tin mà không đòi hỏi đối phương phải tha thứ ngay.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Ba",
        "concept": "Hai bàn tay nắm chặt lấy nhau làm chiếc cầu nối qua một khe nứt đất đá đang dần liền lại."
    },
    {
        "stt": 281,
        "id": "TXT-0281",
        "title": "[Giao Tiếp Thấu Cảm] Cho đi từ sự đủ đầy: Chiếc ly của bạn phải tràn thì người khác mới có nước để uống.",
        "author": "Carl Rogers",
        "topic": "KẾT NỐI LÀNH MẠNH (Giao tiếp & Thấu cảm)",
        "topic_code": "AUTHENTIC_CONNECTION",
        "format": "Single-Punch (1 trang)",
        "hook": "Yêu thương bản thân không phải là ích kỷ; bạn không thể trao cho người khác thứ mà chính tâm hồn bạn đang thiếu đói và cạn kiệt.",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Nhiều người lầm tưởng sự hy sinh mù quáng là đức hạnh, để rồi tích lũy oán hận khi người khác không đền đáp tương xứng. Khi bạn tự chăm sóc tâm hồn mình tràn trề sinh lực, tình yêu thương và sự rộng lượng sẽ tự nhiên tuôn chảy mà không kèm theo bất kỳ chiếc hóa đơn nợ nần nào. Chiếc ly của bạn hôm nay đang vơi hay đang đầy?",
        "hashtags": "#carlrogers #yeuchinhminh #choidutroin #longtracan #hiyuabyss",
        "full_text": "Yêu thương bản thân không phải là ích kỷ; bạn không thể trao cho người khác thứ mà chính tâm hồn bạn đang thiếu đói và cạn kiệt.",
        "hours": "19:30 - 20:30",
        "schedule": "Thứ Tư",
        "concept": "Một đài phun nước bằng đá cẩm thạch ngập tràn dòng nước trong vắt tuôn trào hào phóng ra thảm cỏ xanh mướt xung quanh."
    },
    {
        "stt": 282,
        "id": "TXT-0282",
        "title": "[Giao Tiếp Thấu Cảm] Tôn trọng sự khác biệt: Yêu một người là tôn trọng khoảng không gian tự do của họ.",
        "author": "Kahlil Gibran",
        "topic": "KẾT NỐI LÀNH MẠNH (Giao tiếp & Thấu cảm)",
        "topic_code": "AUTHENTIC_CONNECTION",
        "format": "Carousel 3 trang",
        "hook": "Hãy yêu nhau tha thiết nhưng đừng biến tình yêu thành gông cùm......",
        "twist": "Hãy để tình yêu như một đại dương mênh mông dập dềnh giữa hai bờ bến linh hồn. Đừng đứng quá sát nhau dưới bóng râm của nhau, vì cây sồi và cây trắc bá không thể lớn lên dưới bóng của cây kia.",
        "mirror": "Hai cột trụ cùng nâng đỡ một mái đền, nhưng chúng phải đứng cách xa nhau. Tình yêu đích thực là hai cá nhân độc lập cùng chung một hướng đi, chứ không phải hòa tan để đánh mất chính mình.",
        "deep": "-",
        "caption": "Thi hào Kahlil Gibran trong 'Kẻ Tiên Tri' (The Prophet) để lại bài học vượt thời gian về ranh giới trong tình yêu. Sự gắn kết bền vững nhất là khi cả hai tôn trọng sự tự do và bản sắc riêng của nhau. Bạn có đang vô tình biến tình yêu thành chiếc lồng giam cầm đối phương?",
        "hashtags": "#kahlilgibran #theprophet #tinhyeutudo #ranhgioilanhmanh #hiyuabyss",
        "full_text": "Hãy yêu nhau như hai cột trụ cùng nâng đỡ mái đền: Đứng cạnh nhau nhưng giữ khoảng cách thiêng liêng để cây này không che khuất bóng râm của cây kia.",
        "hours": "20:00 - 21:00",
        "schedule": "Thứ Năm",
        "concept": "Những hàng cột đá cẩm thạch La Mã sừng sững nâng đỡ một mái vòm cổ kính mở rộng ra bầu trời xanh ngập nắng."
    },
    {
        "stt": 283,
        "id": "TXT-0283",
        "title": "[Giao Tiếp Thấu Cảm] Lời nói dịu dàng có thể bẻ gãy sự cứng nhắc của cơn thịnh nộ.",
        "author": "Thích Nhất Hạnh",
        "topic": "KẾT NỐI LÀNH MẠNH (Giao tiếp & Thấu cảm)",
        "topic_code": "AUTHENTIC_CONNECTION",
        "format": "Carousel 2 trang",
        "hook": "Dùng lửa để dập tắt ngọn lửa chỉ làm đám cháy bùng to hơn......",
        "twist": "Khi đối phương đang bị cơn giận dữ thiêu đốt, vũ khí duy nhất có thể dập tắt nó là dòng nước mát lành của sự kiên nhẫn và lời ái ngữ dịu êm xuất phát từ một trái tim không toan tính.",
        "mirror": "-",
        "deep": "-",
        "caption": "Thực hành Ái Ngữ (Loving Speech) là nghệ thuật nói những lời xây dựng, chữa lành và đem lại niềm tin. Nó không đồng nghĩa với sự nhu nhược hay thỏa hiệp giả tạo; đó là sức mạnh của một tâm hồn đã làm chủ được cảm xúc của chính mình. Bạn có thể chọn cách hạ giọng để đối thoại thay vì gào thét?",
        "hashtags": "#thichnhathanh #aingu #tinhyeuthuong #kiemsoatcongiandi #hiyuabyss",
        "full_text": "Dùng lửa để dập lửa chỉ làm cháy to hơn. Dòng nước mát lành của sự kiên nhẫn và lời ái ngữ dịu êm là cách duy nhất làm tan biến cơn thịnh nộ.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Sáu",
        "concept": "Một giọt sương mai trong vắt đọng trên cánh hoa sen hồng dịu dàng phản chiếu ánh nắng bình minh."
    },
    {
        "stt": 284,
        "id": "TXT-0284",
        "title": "[Giao Tiếp Thấu Cảm] Tìm thấy niềm vui trong thành công của người khác: Thuốc giải độc cho lòng đố kỵ.",
        "author": "Martin Seligman",
        "topic": "KẾT NỐI LÀNH MẠNH (Giao tiếp & Thấu cảm)",
        "topic_code": "AUTHENTIC_CONNECTION",
        "format": "Single-Punch (1 trang)",
        "hook": "Thước đo độ cao thượng của một tâm hồn là khả năng vỗ tay chúc mừng chiến thắng của người khác với một nụ cười chân thành không một chút gợn lòng đố kỵ.",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Trong tâm lý học tích cực, 'Active-Constructive Responding' (Phản hồi tích cực chủ động) khi đón nhận tin vui của người thân là chỉ số dự báo chính xác nhất về độ bền của mối quan hệ. Khi bạn thực lòng mừng cho niềm vui của người khác, bạn đang mở rộng thế giới của chính mình. Bạn đã chúc mừng ai bằng cả tấm lòng hôm nay?",
        "hashtags": "#martinseligman #tamlyhoctichcuc #khongdooky #tinhban #hiyuabyss",
        "full_text": "Thước đo độ cao thượng là khả năng vỗ tay chúc mừng chiến thắng của người khác với nụ cười chân thành không một chút gợn lòng đố kỵ.",
        "hours": "19:30 - 20:30",
        "schedule": "Thứ Bảy",
        "concept": "Hai người bạn cùng nâng ly chúc mừng dưới ánh hoàng hôn vàng rực rỡ trên đồi cỏ xanh ngát."
    },
    {
        "stt": 285,
        "id": "TXT-0285",
        "title": "[Giao Tiếp Thấu Cảm] Gắn kết an toàn: Tự do là điều kiện tiên quyết để tình cảm nở hoa.",
        "author": "John Bowlby",
        "topic": "KẾT NỐI LÀNH MẠNH (Giao tiếp & Thấu cảm)",
        "topic_code": "AUTHENTIC_CONNECTION",
        "format": "Carousel 3 trang",
        "hook": "Tình cảm không phải là một chiếc lồng vàng giam giữ......",
        "twist": "Nó giống như bến cảng bình yên: Một con thuyền neo đậu ở đó để nạp năng lượng và sửa chữa những hư tổn, chứ không phải để bị xích chặt vĩnh viễn không bao giờ dám ra khơi.",
        "mirror": "Gắn kết an toàn (Secure Attachment) là khi cả hai trao cho nhau sự tin cậy tuyệt đối: Bạn có thể tự do sải cánh khám phá thế giới, và bạn luôn biết rằng phía sau luôn có một vòng tay ấm áp sẵn sàng đón bạn trở về.",
        "deep": "-",
        "caption": "Nhà phân tâm học John Bowlby, cha đẻ của Thuyết Gắn Kết (Attachment Theory), chứng minh: Những đứa trẻ được bao bọc an toàn sẽ là những người dũng cảm khám phá thế giới nhất. Trong tình yêu cũng vậy: Sự an toàn tạo nên đôi cánh tự do. Mối quan hệ của bạn là bến đỗ bình yên hay là chiếc xiềng xích nặng nề?",
        "hashtags": "#johnbowlby #thuyetganket #ganketan toan #tinhyeulanhmanh #hiyuabyss",
        "full_text": "Gắn kết an toàn là bến cảng bình yên nuôi dưỡng đôi cánh tự do: Cho phép nhau sải cánh khám phá thế giới nhưng luôn biết có một nơi ấm áp đón trở về.",
        "hours": "20:00 - 21:30",
        "schedule": "Chủ Nhật",
        "concept": "Một ngọn hải đăng trắng cổ kính bên bờ biển êm đềm chiếu ánh sáng ấm áp hướng dẫn con thuyền về bến."
    },
    {
        "stt": 286,
        "id": "TXT-0286",
        "title": "[Giao Tiếp Thấu Cảm] Buông bỏ sự phán xét: Mọi người đều đang chiến đấu trong một cuộc chiến vô hình của riêng họ.",
        "author": "Plato",
        "topic": "KẾT NỐI LÀNH MẠNH (Giao tiếp & Thấu cảm)",
        "topic_code": "AUTHENTIC_CONNECTION",
        "format": "Carousel 2 trang",
        "hook": "Hãy tử tế với tất cả những ai bạn gặp trên đường......",
        "twist": "Bởi vì mỗi con người bước qua cuộc đời bạn đều đang phải mang vác một gánh nặng tâm lý hay chiến đấu trong một cuộc chiến cam go mà mắt thường bạn không bao giờ nhìn thấy được.",
        "mirror": "-",
        "deep": "-",
        "caption": "Câu danh ngôn nổi tiếng của Plato nhắc nhở chúng ta về lòng trắc ẩn phổ quát. Trước khi nổi giận hay phán xét một ai đó hành xử không như ý, hãy tự nhắc mình: Họ cũng đang vật lộn với những nỗi bất an của riêng họ. Sự dịu dàng là món quà quý giá nhất bạn có thể trao tặng cho nhân gian.",
        "hashtags": "#plato #tutetrongcuocsong #thaucam #longnhanai #hiyuabyss",
        "full_text": "Hãy tử tế với tất cả mọi người, vì ai cũng đang phải chiến đấu trong một cuộc chiến vô hình cam go mà bạn không hề nhìn thấy được.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Hai",
        "concept": "Một người khách qua đường mỉm cười trao tặng chiếc bánh mì ấm nóng cho một người vô gia cư dưới ánh nắng sớm mùa đông."
    },
    {
        "stt": 287,
        "id": "TXT-0287",
        "title": "[Giao Tiếp Thấu Cảm] Sự hiện diện chất lượng: Tắt màn hình điện thoại để bật lại kết nối giữa người với người.",
        "author": "Sherry Turkle",
        "topic": "KẾT NỐI LÀNH MẠNH (Giao tiếp & Thấu cảm)",
        "topic_code": "AUTHENTIC_CONNECTION",
        "format": "Single-Punch (1 trang)",
        "hook": "Chúng ta có hàng ngàn bạn bè trên mạng nhưng không có một ai để tâm sự khi ngã lòng; hãy học cách đặt chiếc điện thoại xuống để nhìn thẳng vào mắt người đang ngồi đối diện bạn.",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Giáo sư Sherry Turkle cảnh báo trong 'Alone Together': Công nghệ kết nối chúng ta với thế giới ảo nhưng làm xói mòn khả năng đồng cảm sâu sắc ngoài đời thực. Ánh mắt chân thành và giọng nói ấm áp không bao giờ có thể bị thay thế bởi những dòng tin nhắn vô cảm. Bạn có thể dành trọn vẹn sự chú ý cho người bên cạnh tối nay?",
        "hashtags": "#sherryturkle #ketnoithucte #cungketoithoi #songcham #hiyuabyss",
        "full_text": "Đặt chiếc điện thoại xuống để nhìn thẳng vào mắt người ngồi đối diện bạn. Sự hiện diện chất lượng là món quà quý giá nhất trong thời đại số xô bồ.",
        "hours": "19:30 - 20:30",
        "schedule": "Thứ Ba",
        "concept": "Hai người bạn cùng ngồi bên bếp lửa ấm áp trong đêm lạnh, cùng trò chuyện và ngắm sao trời."
    },
    {
        "stt": 288,
        "id": "TXT-0288",
        "title": "[Giao Tiếp Thấu Cảm] Lòng biết ơn là chiếc chìa khóa mở ra sự thịnh vượng cảm xúc trong mọi mối quan hệ.",
        "author": "Brené Brown",
        "topic": "KẾT NỐI LÀNH MẠNH (Giao tiếp & Thấu cảm)",
        "topic_code": "AUTHENTIC_CONNECTION",
        "format": "Carousel 3 trang",
        "hook": "Người hạnh phúc không phải là người có tất cả những gì tốt nhất......",
        "twist": "Mà là người biết trân trọng và biết ơn những điều bình dị nhất mà họ đang có: Một bữa cơm ấm, một mái nhà che mưa nắng, một người sẵn sàng lắng nghe khi họ mệt mỏi.",
        "mirror": "Lòng biết ơn chủ động biến những điều bình thường thành kỳ diệu, biến sự thiếu thốn thành đủ đầy và biến sự xa cách thành một tình tri kỷ thâm sâu.",
        "deep": "-",
        "caption": "Brené Brown qua nhiều thập kỷ nghiên cứu chỉ ra rằng: Bạn không thể tìm thấy niềm hân hoan đích thực nếu thiếu vắng sự thực hành lòng biết ơn. Khi ta biết ơn sự có mặt của người khác trong đời mình, tình yêu tự khắc đâm chồi nảy lộc. Bạn biết ơn điều gì nhất ở người đồng hành của mình hôm nay?",
        "hashtags": "#brenebrown #longbieton #hanhphucdongian #yeuthuong #hiyuabyss",
        "full_text": "Lòng biết ơn chủ động biến những điều bình dị thành kỳ diệu, biến sự thiếu thốn thành đủ đầy và biến người xa lạ thành tình tri kỷ thâm sâu.",
        "hours": "20:00 - 21:00",
        "schedule": "Thứ Tư",
        "concept": "Một mâm quả ngọt chín mọng đặt trên chiếc khăn trải bàn trắng tinh khôi bên cửa sổ tràn ngập ánh nắng vàng của mùa thu hoạch."
    },

    # =========================================================================
    # CỤM 4: Ý NGHĨA SỐNG & SỨC BẬT TỔN THƯƠNG (STT 289 - 300 · 12 BÀI)
    # =========================================================================
    {
        "stt": 289,
        "id": "TXT-0289",
        "title": "[Sức Bật Tinh Thần] Người có lý do để sống có thể chịu đựng được hầu hết mọi nghịch cảnh cuộc đời.",
        "author": "Viktor Frankl",
        "topic": "Ý NGHĨA SỐNG (Sức bật sau nghịch cảnh)",
        "topic_code": "MEANING_RESILIENCE",
        "format": "Carousel 3 trang",
        "hook": "Khi bạn đối diện với một mất mát to lớn......",
        "twist": "Đừng hỏi: 'Tại sao điều này lại xảy ra với tôi?'; câu hỏi đó chỉ dẫn bạn vào ngõ cụt của sự oán hận. Hãy hỏi: 'Nghịch cảnh này đang đòi hỏi điều gì ở tôi, và tôi có thể tạo ra ý nghĩa gì từ nỗi đau này?'",
        "mirror": "Con người không được định hình bởi những gì xảy ra với họ, mà bởi cách họ lựa chọn phản ứng và đứng dậy sau đống tro tàn. Ý nghĩa cuộc sống không phải thứ để đi tìm, đó là thứ do chính bạn kiến tạo qua từng hành động kiên cường.",
        "deep": "-",
        "caption": "Bác sĩ Viktor Frankl trong kiệt tác 'Đi Tìm Lẽ Sống' (Man's Search for Meaning) chứng minh rằng: Ngay cả trong hoàn cảnh khắc nghiệt nhất, con người vẫn có thể tìm thấy ý nghĩa sống qua việc yêu thương, cống hiến và lòng quả cảm. Bạn đang lựa chọn kiến tạo ý nghĩa nào cho hành trình của mình?",
        "hashtags": "#viktorfrankl #ditimlesong #sucbatinhthan #kienquyet #hiyuabyss",
        "full_text": "Người có lý do để sống có thể vượt qua mọi nghịch cảnh. Thay vì oán trách số phận, hãy hỏi: 'Tôi có thể tạo ra ý nghĩa gì từ nỗi đau này để đứng dậy kiêu hãnh?'",
        "hours": "20:00 - 21:30",
        "schedule": "Thứ Năm",
        "concept": "Một ngọn nến sáng rực kiên cường giữa bóng tối đêm đông, chiếu rọi những trang nhật ký mở ra tương lai hy vọng."
    },
    {
        "stt": 290,
        "id": "TXT-0290",
        "title": "[Sức Bật Tinh Thần] Nghệ thuật Kintsugi: Vết nứt hàn gắn bằng vàng ròng biến sự đổ vỡ thành kiệt tác vô giá.",
        "author": "Nghệ thuật Nhật Bản (Triết lý Wabi-Sabi)",
        "topic": "Ý NGHĨA SỐNG (Sức bật sau nghịch cảnh)",
        "topic_code": "MEANING_RESILIENCE",
        "format": "Carousel 2 trang",
        "hook": "Đừng xấu hổ về những vết sẹo tâm hồn......",
        "twist": "Những chiếc bát gốm vỡ trong nghệ thuật Kintsugi của Nhật Bản không bị vứt bỏ; nghệ nhân dùng sơn mài trộn vàng ròng để hàn gắn từng mảnh vỡ, biến vết nứt thành điểm nhấn lộng lẫy và đắt giá nhất của tác phẩm.",
        "mirror": "-",
        "deep": "-",
        "caption": "Tâm hồn bạn sau những lần vấp ngã và tổn thương cũng giống như chiếc bát Kintsugi: Những vết sẹo không chứng minh bạn bị khiếm khuyết; chúng chứng minh bạn đã sống, đã chiến đấu kiên cường và hồi sinh rực rỡ hơn bao giờ hết. Bạn có dám tự hào về những vết sẹo kiêu hãnh của mình?",
        "hashtags": "#kintsugi #wabisabi #vetseotuhao #chualanh #hiyuabyss",
        "full_text": "Vết nứt hàn gắn bằng vàng ròng (Kintsugi) biến sự đổ vỡ thành kiệt tác. Vết sẹo tâm hồn không phải khiếm khuyết; đó là minh chứng bạn đã hồi sinh kiên cường.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Sáu",
        "concept": "Một chiếc bát gốm tráng men màu lam cổ kính với những đường nứt được hàn gắn lấp lánh bằng vàng ròng tỏa sáng dưới nắng."
    },
    {
        "stt": 291,
        "id": "TXT-0291",
        "title": "[Sức Bật Tinh Thần] Niềm lạc quan có cơ sở: Hy vọng không phải ảo tưởng, đó là chiến lược hành động can đảm.",
        "author": "Martin Seligman",
        "topic": "Ý NGHĨA SỐNG (Sức bật sau nghịch cảnh)",
        "topic_code": "MEANING_RESILIENCE",
        "format": "Single-Punch (1 trang)",
        "hook": "Lạc quan đích thực không phải là nhắm mắt làm ngơ trước khó khăn, mà là niềm tin sắt đá rằng dù hoàn cảnh có tồi tệ đến đâu, bạn vẫn luôn có khả năng hành động để làm cho mọi thứ tốt đẹp hơn.",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Giáo sư Martin Seligman chứng minh trong 'Learned Optimism': Lạc quan là một kỹ năng tư duy có thể học tập và rèn luyện được. Kẻ bi quan xem thất bại là vĩnh viễn và do lỗi bản thân; người lạc quan xem thử thách là tạm thời và là cơ hội học hỏi. Bạn đang chọn lăng kính nào để nhìn về tương lai?",
        "hashtags": "#martinseligman #learnedoptimism #lacquanbenthuc #sucmanhynghia #hiyuabyss",
        "full_text": "Lạc quan có cơ sở không phải ảo tưởng nhắm mắt làm ngơ, mà là niềm tin sắt đá rằng bạn luôn có khả năng hành động để làm cho cuộc sống tốt đẹp hơn.",
        "hours": "19:30 - 20:30",
        "schedule": "Thứ Bảy",
        "concept": "Một ngọn mầm xanh non kiên cường đâm chồi vươn lên giữa lớp đất cằn cỗi đón những giọt mưa đầu mùa."
    },
    {
        "stt": 292,
        "id": "TXT-0292",
        "title": "[Sức Bật Tinh Thần] Trạng thái Dòng Chảy (Flow): Đỉnh cao của hạnh phúc là đắm chìm trọn vẹn trong điều mình yêu.",
        "author": "Mihaly Csikszentmihalyi",
        "topic": "Ý NGHĨA SỐNG (Sức bật sau nghịch cảnh)",
        "topic_code": "MEANING_RESILIENCE",
        "format": "Carousel 3 trang",
        "hook": "Hạnh phúc đích thực không nằm ở sự nhàn rỗi hưởng thụ......",
        "twist": "Nó xuất hiện khi bạn dồn toàn bộ tâm trí, kỹ năng và đam mê vào một nhiệm vụ đầy thách thức; nơi mà quá khứ tan biến, tương lai không còn tồn tại, chỉ còn lại sự tập trung tuyệt đối và niềm vui sáng tạo vô bờ bến.",
        "mirror": "Đó chính là trạng thái Dòng Chảy (Flow). Khi bạn quên đi sự hiện diện của cái tôi nhỏ bé để hòa làm một với công việc bạn đang làm, bạn chạm vào nguồn năng lượng vô tận của vũ trụ.",
        "deep": "-",
        "caption": "Nhà tâm lý học Mihaly Csikszentmihalyi dành cả đời nghiên cứu về 'Flow': Khoảnh khắc con người cảm thấy sống động nhất là khi họ vượt qua giới hạn của mình trong sự say mê thuần khiết. Điều gì khiến bạn say mê đến mức quên hết thời gian và không gian xung quanh?",
        "hashtags": "#flow #mihalycsikszentmihalyi #dongchaydamme #hanhphucdichthuc #hiyuabyss",
        "full_text": "Trạng thái Dòng Chảy (Flow) là khi bạn đắm chìm trọn vẹn trong công việc đầy thách thức với niềm say mê thuần khiết, quên đi cái tôi để hòa làm một với sáng tạo.",
        "hours": "20:00 - 21:00",
        "schedule": "Chủ Nhật",
        "concept": "Một người nghệ nhân say mê chạm khắc từng đường nét tỉ mỉ trên khối đá cẩm thạch trong ánh nắng chiều rọi qua khung cửa sổ."
    },
    {
        "stt": 293,
        "id": "TXT-0293",
        "title": "[Sức Bật Tinh Thần] Sự phát triển sau sang chấn: Những vết nứt là nơi ánh sáng rọi vào tâm hồn bạn.",
        "author": "Leonard Cohen / Richard Tedeschi",
        "topic": "Ý NGHĨA SỐNG (Sức bật sau nghịch cảnh)",
        "topic_code": "MEANING_RESILIENCE",
        "format": "Carousel 2 trang",
        "hook": "Có một vết nứt trong mọi thứ trên thế gian......",
        "twist": "Nhưng đừng vội vàng che đậy nó; chính qua vết nứt đó mà ánh sáng của sự tỉnh thức, lòng trắc ẩn sâu sắc và sức mạnh tiềm ẩn mới có cơ hội rọi thẳng vào tâm hồn bạn.",
        "mirror": "-",
        "deep": "-",
        "caption": "Hiện tượng 'Post-Traumatic Growth' (Trưởng thành sau sang chấn) chứng minh rằng: Những biến cố đau đớn nhất thường trở thành chất xúc tác mạnh mẽ nhất để con người tái định nghĩa giá trị sống, trân quý các mối quan hệ và khám phá sức mạnh nội tâm phi thường. Cơn giông bão vừa qua đã để lại trong bạn hạt mầm ánh sáng nào?",
        "hashtags": "#posttraumaticgrowth #anhsangnoitam #leonardcohen #chualanh #hiyuabyss",
        "full_text": "Có vết nứt trong mọi sự vật, nhưng chính qua vết nứt đó mà ánh sáng rọi vào. Sang chấn đau đớn nhất có thể trở thành chất xúc tác cho sự trưởng thành vĩ đại.",
        "hours": "20:00 - 21:30",
        "schedule": "Thứ Hai",
        "concept": "Một hang đá tối tăm bỗng bừng sáng rực rỡ bởi luồng ánh sáng mặt trời vàng óng chiếu xuyên qua một kẽ nứt trên vòm đá."
    },
    {
        "stt": 294,
        "id": "TXT-0294",
        "title": "[Sức Bật Tinh Thần] Tự do nội tâm: Không hoàn cảnh nào có thể giam cầm một tâm hồn kiên định.",
        "author": "Nelson Mandela",
        "topic": "Ý NGHĨA SỐNG (Sức bật sau nghịch cảnh)",
        "topic_code": "MEANING_RESILIENCE",
        "format": "Single-Punch (1 trang)",
        "hook": "Tôi là thuyền trưởng của số phận tôi, tôi là người chỉ huy của linh hồn tôi; xiềng xích có thể trói buộc thân xác, nhưng không bao giờ có thể giam cầm được một ý chí tự do.",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Nelson Mandela trải qua 27 năm ngục tù nhưng bước ra với nụ cười bao dung và tinh thần hòa giải vĩ đại. Bài thơ 'Invictus' khắc sâu chân lý hiện sinh: Khi tâm hồn bạn tự do và kiên định, không bức tường giam hay hoàn cảnh nghiệt ngã nào có thể biến bạn thành nạn nhân. Bạn có đang nắm chắc tay chèo của con thuyền đời mình?",
        "hashtags": "#nelsonmandela #invictus #tudonoitam #kientrigiaotrieu #hiyuabyss",
        "full_text": "Tôi là thuyền trưởng của số phận tôi, là người chỉ huy của linh hồn tôi. Xiềng xích có thể trói thân xác nhưng không bao giờ giam cầm được ý chí tự do kiêu hãnh.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Ba",
        "concept": "Một cánh buồm trắng căng gió kiêu hãnh vượt qua ngọn sóng biển khơi hùng vĩ hướng thẳng về chân trời rực rỡ nắng mai."
    },
    {
        "stt": 295,
        "id": "TXT-0295",
        "title": "[Sức Bật Tinh Thần] Sức mạnh của lòng trắc ẩn xã hội: Khi bạn thắp sáng con đường cho người khác, chính bạn cũng được soi tỏ.",
        "author": "Albert Schweitzer",
        "topic": "Ý NGHĨA SỐNG (Sức bật sau nghịch cảnh)",
        "topic_code": "MEANING_RESILIENCE",
        "format": "Carousel 2 trang",
        "hook": "Mục đích tối hậu của đời người......",
        "twist": "Không phải chỉ là mưu cầu hạnh phúc vị kỷ cho riêng mình; mục đích cao cả nhất là phục vụ, cống hiến và thể hiện lòng nhân ái để xoa dịu những nỗi đau của tha nhân.",
        "mirror": "-",
        "deep": "-",
        "caption": "Bác sĩ đoạt giải Nobel Hòa bình Albert Schweitzer khẳng định: Những người thực sự hạnh phúc nhất là những người đã tìm ra cách phục vụ đồng loại. Lòng nhân ái không bao giờ làm bạn nghèo đi; nó làm tâm hồn bạn trở nên giàu có và rạng rỡ lạ kỳ. Hôm nay bạn đã gieo một hạt mầm tử tế nào cho cuộc đời?",
        "hashtags": "#albertschweitzer #longnhanai #conghendoimoi #songynghia #hiyuabyss",
        "full_text": "Mục đích cao cả của đời người là phục vụ và xoa dịu nỗi đau của đồng loại. Khi bạn thắp sáng con đường cho người khác, chính bạn cũng được soi tỏ ấm áp.",
        "hours": "19:30 - 20:30",
        "schedule": "Thứ Tư",
        "concept": "Một người cầm ngọn đèn lồng ấm áp giơ cao dẫn lối cho đoàn người vượt qua con đường rừng đêm tối mịt mùng."
    },
    {
        "stt": 296,
        "id": "TXT-0296",
        "title": "[Sức Bật Tinh Thần] Mọi mùa đông khắc nghiệt rồi cũng phải nhường chỗ cho mùa xuân đâm chồi nảy lộc.",
        "author": "Albert Camus",
        "topic": "Ý NGHĨA SỐNG (Sức bật sau nghịch cảnh)",
        "topic_code": "MEANING_RESILIENCE",
        "format": "Carousel 3 trang",
        "hook": "Giữa mùa đông băng giá lạnh buốt nhất......",
        "twist": "Tôi bất chợt phát hiện ra rằng: Bên trong sâu thẳm tâm hồn mình luôn ẩn chứa một mùa hè bất khả chiến bại; một nguồn sinh lực mãnh liệt không thể bị vùi dập bởi bất kỳ cơn bão tuyết nào của số phận.",
        "mirror": "Dù hoàn cảnh hiện tại của bạn có tăm tối đến đâu, hãy nhớ rằng hạt mầm sự sống vẫn đang âm thầm chờ đợi dưới lớp đất băng giá. Chỉ cần bạn kiên nhẫn giữ lấy ngọn lửa hy vọng, mùa xuân chắc chắn sẽ quay trở lại.",
        "deep": "-",
        "caption": "Albert Camus để lại câu văn bất hủ: 'In the depth of winter, I finally learned that within me there lay an invincible summer.' Sức bật tinh thần không phải là thứ có sẵn từ bên ngoài, nó là ngọn lửa nội tại mà không ai có thể dập tắt nếu bạn không cho phép. Bạn có đang giữ vững ngọn lửa mùa hè bất khả chiến bại trong lòng mình?",
        "hashtags": "#albertcamus #muahebatkhachienbai #hyvongsosong #kienquyet #hiyuabyss",
        "full_text": "Giữa mùa đông băng giá, tôi nhận ra trong mình có một mùa hè bất khả chiến bại. Hạt mầm sự sống vẫn âm thầm chờ đợi để bừng nở khi mùa xuân trở lại.",
        "hours": "20:00 - 21:00",
        "schedule": "Thứ Năm",
        "concept": "Một cành cây khẳng khiu giữa tuyết trắng bỗng đâm chồi nảy ra những nụ hoa anh đào hồng thắm rực rỡ dưới nắng ấm."
    },
    {
        "stt": 297,
        "id": "TXT-0297",
        "title": "[Sức Bật Tinh Thần] Dũng cảm sống cuộc đời của chính mình: Tiếng gọi thức tỉnh lương tri.",
        "author": "Mary Oliver",
        "topic": "Ý NGHĨA SỐNG (Sức bật sau nghịch cảnh)",
        "topic_code": "MEANING_RESILIENCE",
        "format": "Single-Punch (1 trang)",
        "hook": "Hãy nói cho tôi biết: Bạn dự định làm gì với cuộc đời hoang dã và quý giá duy nhất này của bạn?",
        "twist": "-",
        "mirror": "-",
        "deep": "-",
        "caption": "Nữ thi sĩ Mary Oliver kết thúc bài thơ 'The Summer Day' bằng câu hỏi làm thức tỉnh hàng triệu linh hồn: Cuộc đời này quá ngắn ngủi để sống theo kỳ vọng của người khác hay chôn vùi trong những nỗi âu lo vô bổ. Bạn có đang sống cuộc đời thực sự thuộc về bạn? Hôm nay, bạn sẽ chọn làm điều gì để cuộc đời bạn không bị lãng phí?",
        "hashtags": "#maryoliver #cuocdoisangquy #songchinhminh #thuctinh #hiyuabyss",
        "full_text": "Hãy nói cho tôi biết: Bạn dự định làm gì với cuộc đời hoang dã và quý giá duy nhất này của bạn? Đừng lãng phí cuộc đời vào những nỗi sợ hãi hư vô.",
        "hours": "11:30 - 12:30",
        "schedule": "Thứ Sáu",
        "concept": "Một người đứng giang rộng hai tay trên đỉnh đồi lộng gió, hít thở bầu không khí tự do dưới bầu trời hoàng hôn tím rực rỡ."
    },
    {
        "stt": 298,
        "id": "TXT-0298",
        "title": "[Sức Bật Tinh Thần] Nuôi dưỡng cảm xúc biết ơn và hân hoan: Chìa khóa cho một tâm hồn bất hoại.",
        "author": "Martin Seligman",
        "topic": "Ý NGHĨA SỐNG (Sức bật sau nghịch cảnh)",
        "topic_code": "MEANING_RESILIENCE",
        "format": "Carousel 2 trang",
        "hook": "Hạnh phúc không phải là không có vấn đề......",
        "twist": "Hạnh phúc là khả năng giữ vững sự bình an và tìm thấy vẻ đẹp kỳ diệu của cuộc sống ngay giữa lòng những vấn đề đang tồn tại; đó là sự lựa chọn tập trung vào ánh sáng thay vì đắm chìm trong bóng tối.",
        "mirror": "-",
        "deep": "-",
        "caption": "Mô hình PERMA của Martin Seligman chỉ ra 5 trụ cột của sự hưng thịnh tâm lý: Cảm xúc tích cực, Sự gắn kết, Mối quan hệ lành mạnh, Ý nghĩa sống và Thành tựu. Bạn không cần phải đợi mọi khó khăn chấm dứt mới cho phép mình mỉm cười. Hôm nay bạn chọn nhìn vào đám mây đen hay luồng ánh sáng sau đám mây?",
        "hashtags": "#martinseligman #perma #hungthinhtamly #binhannoitam #hiyuabyss",
        "full_text": "Hạnh phúc không phải là không có vấn đề, mà là khả năng giữ bình an và tìm thấy vẻ đẹp cuộc sống ngay giữa khó khăn. Hãy chọn tập trung vào ánh sáng.",
        "hours": "19:30 - 20:30",
        "schedule": "Thứ Bảy",
        "concept": "Cầu vồng bảy sắc rực rỡ vắt ngang qua bầu trời xanh ngắt ngay sau cơn mưa rào mùa hạ."
    },
    {
        "stt": 299,
        "id": "TXT-0299",
        "title": "[Sức Bật Tinh Thần] Sự tha thứ tối hậu: Cởi trói cho kẻ thù và nhận ra kẻ tù nhân được giải thoát chính là bạn.",
        "author": "Lewis B. Smedes",
        "topic": "Ý NGHĨA SỐNG (Sức bật sau nghịch cảnh)",
        "topic_code": "MEANING_RESILIENCE",
        "format": "Carousel 3 trang",
        "hook": "Ôm giữ thù hận cũng giống như uống thuốc độc......",
        "twist": "Rồi hy vọng kẻ làm tổn thương mình sẽ chết; sự thù hận không làm đau kẻ thù của bạn, nó chỉ gặm nhấm và thiêu rụi từng tế bào bình an trong tâm hồn của chính bạn.",
        "mirror": "Tha thứ không phải là biện minh cho hành vi sai trái của kẻ khác; tha thứ là hành động dũng cảm cắt đứt chiếc dây xích trói buộc bạn vào quá khứ để trả lại tự do cho tâm hồn bạn. Kẻ tù nhân được giải thoát chính là bạn.",
        "deep": "-",
        "caption": "Học giả Lewis B. Smedes đúc kết câu châm ngôn kinh điển: 'To forgive is to set a prisoner free and discover that the prisoner was you.' (Tha thứ là giải thoát cho một tù nhân, để rồi nhận ra tù nhân đó chính là bạn). Đừng để người làm tổn thương bạn tiếp tục sống miễn phí trong tâm trí bạn. Bạn đã sẵn sàng mở khóa buồng giam ấy để bước ra tự do?",
        "hashtags": "#thathuchinhminh #buongbothuhan #tudonoitam #smedes #hiyuabyss",
        "full_text": "Tha thứ không phải bao biện cho kẻ sai, mà là cắt đứt sợi xích trói buộc bạn vào quá khứ. Giải thoát cho kẻ thù để nhận ra kẻ tù nhân được cứu chính là bạn.",
        "hours": "20:00 - 21:00",
        "schedule": "Chủ Nhật",
        "concept": "Một chiếc lồng chim bằng sắt mở toang cửa, chú chim bồ câu trắng vỗ cánh bay vút lên bầu trời bao la tự do."
    },
    {
        "stt": 300,
        "id": "TXT-0300",
        "title": "[Cột Mốc 300 Bài] Trí tuệ tối thượng: Từ vực thẳm bóng tối bước ra ánh sáng của sự điềm tĩnh và bao dung.",
        "author": "Marcus Aurelius & Carl Rogers",
        "topic": "Ý NGHĨA SỐNG (Sức bật sau nghịch cảnh)",
        "topic_code": "MEANING_RESILIENCE",
        "format": "Carousel 3 trang",
        "hook": "Hành trình đi qua 300 triết ngôn của Hiyu Abyss......",
        "twist": "Không phải để biến bạn thành một kẻ phán xét hay cay nghiệt trước thói đời; mà là để bạn nhìn thấu mọi ngóc ngách của sự bất toàn con người, để rồi từ đó bao dung hơn với người khác và nhân từ hơn với chính bản thân mình.",
        "mirror": "Đi qua tận cùng bóng tối để tìm thấy ánh sáng bất diệt. Bạn đứng đây ngày hôm nay: Không ngạo mạn, không sợ hãi, tự chủ, điềm tĩnh và tràn ngập tình yêu thương cuộc sống. Đó chính là đỉnh cao của bản lĩnh làm người.",
        "deep": "-",
        "caption": "Đạt đến cột mốc lịch sử 300 bài viết của Hiyu Abyss: Mục đích tối hậu của tri thức tâm lý và triết học không phải để chiến thắng người khác, mà là để làm chủ chính mình và thắp sáng lên tình người. Đi qua vực thẳm để chạm vào bình yên bất hoại. Cảm ơn bạn đã cùng Hiyu Abyss bước đi trên hành trình thức tỉnh tâm hồn này!",
        "hashtags": "#hiyuabyss #cotmoc300 #thuctinhtamhon #anhsangchualanh #trietngontamly",
        "full_text": "Đi qua 300 triết ngôn không phải để cay nghiệt với thế gian, mà để bao dung hơn với tha nhân và nhân từ hơn với chính mình. Đỉnh cao của bản lĩnh là ánh sáng của lòng từ bi.",
        "hours": "20:00 - 21:30",
        "schedule": "Thứ Hai",
        "concept": "Một ngọn núi hùng vĩ đón ánh bình minh rạng rỡ dát vàng, một con suối mát lành tuôn chảy tưới mát cả thung lũng hoa nở rộ bên dưới."
    }
]

def main():
    print("=== TẠO DỮ LIỆU 50 BÀI CHỮA LÀNH (STT 251 - 300) ===")
    assert len(POSTS_DATA) == 50, f"Expected 50 posts, got {len(POSTS_DATA)}"
    
    # 1. Lưu JSON
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(POSTS_DATA, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã lưu {OUTPUT_JSON} (50 bài).")

    # 2. Tạo scripts/tiktok_300_posts.csv và cập nhật scripts/tiktok_200_posts.csv
    header = [
        'STT', 'Mã ID', 'Tiêu Đề (Dưới 90 từ)', 'Mô Tả (Caption TikTok)',
        'Nguồn Tác Giả', 'Hashtags (5 cái)', 'Định Dạng Slide',
        'Trang 1 (Hook / Mở màn)', 'Trang 2 (Cú lật bóc trần)',
        'Trang 3 (Chiếc gương phản tư)', 'Trang 4 (Đúc kết / Phản tư sâu)',
        'Văn Bản Hoàn Chỉnh', 'Chủ Đề Hạt Nhân', 'Khung Giờ Vàng',
        'Lịch Đăng (Thứ, Ngày)', 'Gợi Ý Phôi Ảnh', 'Trạng Thái'
    ]

    existing_rows = []
    if os.path.exists(CSV_200_PATH):
        with open(CSV_200_PATH, "r", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            existing_header = next(reader)
            existing_rows = list(reader)

    print(f"Số hàng hiện tại trong CSV: {len(existing_rows)}")
    
    # Giữ đúng 250 hàng cũ nếu đã có
    clean_existing = existing_rows[:250]

    new_csv_rows = []
    for p in POSTS_DATA:
        row = [
            str(p["stt"]),
            p["id"],
            p["title"],
            p["caption"],
            p["author"],
            p["hashtags"],
            p["format"],
            p["hook"],
            p["twist"],
            p["mirror"],
            p["deep"],
            p["full_text"],
            p["topic"],
            p["hours"],
            p["schedule"],
            p["concept"],
            "SẴN SÀNG"
        ]
        new_csv_rows.append(row)

    total_300_rows = clean_existing + new_csv_rows
    print(f"Tổng số hàng sau khi ghép: {len(total_300_rows)}")

    # Ghi vào CSV 300 và cập nhật CSV 200
    with open(CSV_300_PATH, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(total_300_rows)
    print(f"✅ Đã tạo {CSV_300_PATH} với {len(total_300_rows)} hàng.")

    with open(CSV_200_PATH, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(total_300_rows)
    print(f"✅ Đã cập nhật {CSV_200_PATH} với {len(total_300_rows)} hàng.")

    # 3. Tạo 50 file Markdown trong editorial/content/
    os.makedirs(CONTENT_DIR, exist_ok=True)
    md_created = 0
    for p in POSTS_DATA:
        md_filename = f"{p['id']}.md"
        md_filepath = os.path.join(CONTENT_DIR, md_filename)
        
        theme_id = f"theme_{p['stt']}"
        md_content = f"""---
id: {p['id']}
title: "{p['title']}"
content_type: INSPIRED_ORIGINAL
author_attribution: "{p['author']}"
topic_codes:
  - {p['topic_code']}
image_ref: "{theme_id}"
slide_format: "{p['format']}"
status: APPROVED
created_at: "2026-11-19"
updated_at: "2026-11-19"
---

# {p['title']}

> {p['hook']} {p['twist']}

## Diễn Giải & Chiêm Nghiệm Biên Tập
{p['caption']}

## Cấu Trúc Trình Diễn Đa Nhịp (Slides)
- **Trang 1 (Hook):** {p['hook']}
- **Trang 2 (Cú lật):** {p['twist']}
- **Trang 3 (Phản tư):** {p['mirror']}
- **Trang 4 (Đúc kết):** {p['deep']}

## Từ Khóa & Phân Loại
{p['hashtags']}
"""
        with open(md_filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
        md_created += 1

    print(f"✅ Đã tạo thành công {md_created} file markdown trong {CONTENT_DIR} ({POSTS_DATA[0]['id']}.md -> {POSTS_DATA[-1]['id']}.md).")

if __name__ == '__main__':
    main()
