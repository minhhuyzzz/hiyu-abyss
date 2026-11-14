#!/usr/bin/env python3
"""
Hiyu Abyss — 100 Posts Generator conforming strictly to INTENT-TIKTOK-01:
- Format Diversity: ~40% Single-Punch (1 trang), ~40% Carousel 2 trang, ~20% Carousel 3 trang.
- Hook Standards: Under 10 words, ends with `......` (curiosity gap) for multi-slide posts.
- Vietnamese Nuances: Natural, visceral, authentic psychological insights without academic/translation stiffness.
"""

import csv
from datetime import datetime, timedelta

THEMES = [
    ("HYPOCRISY", "Đạo đức giả & Sự giả tạo"),
    ("DOUBLE_STANDARD", "Tiêu chuẩn kép trong phán xét"),
    ("MORALITY", "Lòng tốt & Điều kiện ngầm"),
    ("EGO", "Bản ngã & Nhu cầu hơn người"),
    ("SELF_DECEPTION", "Sự tự lừa dối & Vùng an toàn"),
    ("SHADOW", "Góc khuất nội tâm & Sự chối bỏ"),
    ("MASK", "Mặt nạ xã hội & Sự gồng gánh"),
    ("POWER", "Quyền lực ngầm & Kiểm soát"),
    ("MANIPULATION", "Cảm giác tội lỗi & Nợ ân tình"),
    ("FREEDOM", "Tự do & Nỗi sợ tự chịu trách nhiệm"),
    ("TRUTH", "Sự thật & Những lời tự bào chữa"),
    ("LOVE", "Chiếm hữu đội lốt yêu thương"),
    ("LOYALTY", "Lòng trung thành & Ranh giới trả giá"),
    ("ENVY", "Đố kỵ ngầm & Sự so sánh"),
    ("CROWD", "Đám đông & Dũng khí bầy đàn"),
    ("SUFFERING", "Khổ đau & Thói quen đóng vai nạn nhân"),
    ("IDENTITY", "Bản sắc khi ở một mình"),
    ("MEANING", "Ý nghĩa hiện sinh & Sự vô nghĩa"),
    ("SOLITUDE", "Cô độc & Nỗi sợ tĩnh lặng"),
    ("STATUS", "Danh vọng & Khiêm nhường trình diễn")
]

# Danh sách 100 bài chi tiết: mỗi theme 5 bài
# Định dạng bài trong theme:
# Bài 1: Single-Punch (1 trang)
# Bài 2: Carousel 2 trang (Hook < 10 từ `......` -> Twist)
# Bài 3: Single-Punch (1 trang)
# Bài 4: Carousel 2 trang (Hook < 10 từ `......` -> Twist)
# Bài 5: Carousel 3 trang (Hook < 10 từ `......` -> Twist -> Mirror)

ALL_100_POSTS = [
    # 1. HYPOCRISY
    [
        "Single-Punch (1 trang độc bản)",
        "Tấm áo tử tế",
        "Kẻ nguy hiểm nhất không phải kẻ ác công khai, mà là người luôn xuất hiện với vẻ mặt của một vị thánh cứu rỗi.",
        "-",
        "-",
        "Kẻ nguy hiểm nhất không phải kẻ ác công khai, mà là người luôn xuất hiện với vẻ mặt của một vị thánh cứu rỗi."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Khoản nợ vô hình",
        "Lòng tốt đáng sợ nhất là khi......",
        "Họ giúp bạn một lần, nhưng ngầm bắt bạn phải mang ơn và gật đầu với họ cả đời.",
        "-",
        "Lòng tốt đáng sợ nhất là khi người ta giúp bạn một lần, nhưng lại ngầm bắt bạn phải mang ơn và cúi đầu trước họ suốt phần đời còn lại."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Đạo lý và ngoại lệ",
        "Người nói đạo lý càng trôi chảy thì khi lợi ích bị đụng tới, họ là người quay xe nhanh nhất.",
        "-",
        "-",
        "Người nói đạo lý càng trôi chảy thì khi lợi ích bị đụng tới, họ là người quay xe nhanh nhất."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Sự tha thứ có độc",
        "Có những người tha thứ rất nhanh......",
        "Chỉ để mỗi lần tranh cãi, họ có quyền đem lỗi lầm cũ ra ép bạn phải thấy mình tội lỗi.",
        "-",
        "Có những người tha thứ rất nhanh, chỉ để mỗi lần tranh cãi, họ có quyền đem lỗi lầm cũ ra ép bạn phải thấy mình tội lỗi."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Phẫn nộ vay mượn",
        "Người ta hăng hái ném đá kẻ khác......",
        "Không phải vì họ yêu chuộng công lý, mà vì chửi bới người khác là cách dễ nhất để cảm thấy mình tử tế.",
        "Càng sốt sắng kết tội lỗi lầm của người ngoài, ta càng dễ quên đi những góc tối hèn kém của chính mình.",
        "Người ta hăng hái ném đá kẻ khác không phải vì yêu công lý, mà vì chửi bới người khác là cách dễ nhất để cảm thấy mình tử tế; càng sốt sắng kết tội người ngoài, ta càng dễ lờ đi những góc tối hèn kém của chính mình."
    ],

    # 2. DOUBLE_STANDARD
    [
        "Single-Punch (1 trang độc bản)",
        "Cán cân lệch",
        "Ta gọi sai lầm của người khác là bản tính xấu xa, nhưng lại gọi cùng sai lầm ấy ở mình là hoàn cảnh bắt buộc.",
        "-",
        "-",
        "Ta gọi sai lầm của người khác là bản tính xấu xa, nhưng lại gọi cùng sai lầm ấy ở mình là hoàn cảnh bắt buộc."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Thẳng thắn hay tàn nhẫn",
        "Ranh giới giữa thẳng thắn và độc ác......",
        "Là ta gọi sự cay nghiệt của mình là thật thà, nhưng lại coi sự thật thà của người khác là thiếu dạy dỗ.",
        "-",
        "Ranh giới giữa thẳng thắn và độc ác rất mong manh: ta gọi sự cay nghiệt của mình là thật thà, nhưng lại coi sự thật thà của người khác là thiếu dạy dỗ."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Ranh giới tự vệ",
        "Khi người khác từ chối thì ta bảo họ vô tình; khi chính ta quay lưng thì ta bảo mình đang học cách yêu bản thân.",
        "-",
        "-",
        "Khi người khác từ chối thì ta bảo họ vô tình; khi chính ta quay lưng thì ta bảo mình đang học cách yêu bản thân."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Góc khuất và bí mật",
        "Tại sao ta dễ kết tội người khác dối trá......",
        "Trong khi những chuyện ta giấu giếm lại luôn được dán nhãn là 'quyền riêng tư chính đáng'?",
        "-",
        "Tại sao ta dễ kết tội người khác dối trá, trong khi những chuyện ta giấu giếm lại luôn được dán nhãn là quyền riêng tư chính đáng?"
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Thành bại và sự tự tôn",
        "Khi người khác đạt được thành công......",
        "Ta thường nghĩ do họ may mắn hoặc có người nâng đỡ, chứ hiếm khi chịu tin họ cũng cày cuốc như ta.",
        "Bản ngã của con người yếu đuối đến mức: thà hạ thấp nỗ lực của người khác còn hơn thừa nhận mình kém cỏi.",
        "Khi người khác thành công, ta thường nghĩ do họ may mắn hoặc có quan hệ; bản ngã thà hạ thấp nỗ lực của người khác còn hơn dũng cảm thừa nhận sự thua kém của chính mình."
    ],

    # 3. MORALITY
    [
        "Single-Punch (1 trang độc bản)",
        "Nhân cách trong bóng tối",
        "Đạo đức của một người thể hiện rõ nhất qua cách họ đối xử với những kẻ không thể mang lại cho họ bất kỳ lợi ích nào.",
        "-",
        "-",
        "Đạo đức của một người thể hiện rõ nhất qua cách họ đối xử với những kẻ không thể mang lại cho họ bất kỳ lợi ích nào."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Cái bẫy của sự hy sinh",
        "Hy sinh quá nhiều đôi khi là......",
        "Một cách tích lũy quyền lực, để sau này dùng cảm giác tội lỗi điều khiển cuộc đời của người nhận.",
        "-",
        "Hy sinh quá nhiều đôi khi là một cách tích lũy quyền lực, để sau này dùng cảm giác tội lỗi điều khiển cuộc đời của người nhận."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Lòng tốt không ranh giới",
        "Lòng tốt mà không có ranh giới sẽ không nhận được lòng biết ơn, mà chỉ nuôi lớn sự lấn lướt của kẻ trơ trẽn.",
        "-",
        "-",
        "Lòng tốt mà không có ranh giới sẽ không nhận được lòng biết ơn, mà chỉ nuôi lớn sự lấn lướt của kẻ trơ trẽn."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Bất lực hay lương thiện",
        "Nhiều người nghĩ mình lương thiện......",
        "Chỉ vì họ chưa bao giờ có cơ hội hoặc chưa đủ quyền lực để làm điều ác.",
        "-",
        "Nhiều người nghĩ mình lương thiện chỉ vì họ chưa bao giờ có cơ hội hoặc chưa đủ sức mạnh để làm điều ác; kiềm chế được sức mạnh phá hủy mới thực sự là tử tế."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Sự tha thứ vô tội vạ",
        "Dễ dàng bỏ qua cho kẻ làm tổn thương bạn......",
        "Không làm họ thay đổi, mà chỉ gửi đi một tín hiệu rằng họ có thể làm tổn thương bạn thêm một lần nữa.",
        "Khoan dung với kẻ không biết hối hận thực chất là bạn đang tự tàn nhẫn với chính bản thân mình.",
        "Dễ dàng tha thứ cho kẻ làm tổn thương mình không làm họ hối hận, mà chỉ gửi đi tín hiệu rằng họ có thể tái phạm; khoan dung vô tội vạ thực chất là tự tàn nhẫn với chính mình."
    ],

    # 4. EGO
    [
        "Single-Punch (1 trang độc bản)",
        "Hơn thua trong im lặng",
        "Người thực sự giỏi không mất thời gian tranh cãi; chỉ những kẻ mang nội tâm rỗng tuếch mới cần âm thanh gầm rú để lấn át người khác.",
        "-",
        "-",
        "Người thực sự giỏi không mất thời gian tranh cãi; chỉ những kẻ mang nội tâm rỗng tuếch mới cần âm thanh gầm rú để lấn át người khác."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Khát khao được công nhận",
        "Tại sao một lời chê lại đau lâu hơn mười lời khen......?",
        "Vì bản ngã luôn tin mình hoàn hảo, và nó không thể chịu nổi vết xước từ sự thật.",
        "-",
        "Một lời chê đau lâu hơn mười lời khen vì bản ngã luôn tự ru ngủ rằng mình hoàn hảo, và nó không thể chịu đựng nổi một vết xước từ sự thật."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Hạ bệ để nâng mình",
        "Chỉ có kẻ thiếu tự tin vào giá trị của mình mới phải dìm người khác xuống để cảm thấy mình đang đứng cao hơn.",
        "-",
        "-",
        "Chỉ có kẻ thiếu tự tin vào giá trị của mình mới phải dìm người khác xuống để cảm thấy mình đang đứng cao hơn."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Lời xin lỗi khó khăn",
        "Nhiều người thà mất đi mối quan hệ quý giá......",
        "Còn hơn là phải nói ra một câu xin lỗi và thừa nhận mình đã sai.",
        "-",
        "Nhiều người thà đánh mất một mối quan hệ quý giá còn hơn là nói ra một câu xin lỗi và thừa nhận mình đã sai; cái tôi đắt đỏ chỉ mua được sự cô độc."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Vòng lặp tự ái",
        "Càng nhạy cảm và dễ nổi nóng......",
        "Chứng tỏ nội tâm bên trong của bạn càng mong manh và bất an.",
        "Kẻ có thực lực không dựng gai nhọn khắp người để tự vệ; chỉ kẻ sợ bị nhìn thấu mới luôn xù lông trước mọi ánh nhìn.",
        "Càng dễ nổi nóng và tự ái chứng tỏ nội tâm bên trong càng bất an; kẻ thực sự vững vàng không cần dựng gai nhọn khắp người chỉ để che giấu sự sợ hãi bị nhìn thấu."
    ],

    # 5. SELF_DECEPTION
    [
        "Single-Punch (1 trang độc bản)",
        "Vùng an toàn độc hại",
        "Lời nói dối tàn nhẫn nhất không đến từ người ngoài, mà là lời ta tự thì thầm vào tai mình mỗi sáng để khỏi phải thay đổi.",
        "-",
        "-",
        "Lời nói dối tàn nhẫn nhất không đến từ người ngoài, mà là lời ta tự thì thầm vào tai mình mỗi sáng để khỏi phải thay đổi."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Ảo tưởng về sự bận rộn",
        "Ta vùi đầu vào làm việc thâu đêm suốt sáng......",
        "Không phải vì đam mê, mà vì sợ cảm giác phải đối diện với sự trống rỗng khi ở một mình.",
        "-",
        "Ta vùi đầu vào bận rộn không phải vì đam mê, mà vì quá sợ hãi cảm giác phải đối diện với sự trống rỗng khi ở một mình."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Bao biện cho sự yếu hèn",
        "Đừng gọi sự chần chừ và hèn nhát của mình là thận trọng; thận trọng có hành động, còn hèn nhát chỉ biết chờ đợi.",
        "-",
        "-",
        "Đừng gọi sự chần chừ và hèn nhát của mình là thận trọng; thận trọng có hành động, còn hèn nhát chỉ biết chờ đợi."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Hy vọng mù quáng",
        "Thứ giam cầm bạn trong đau khổ lâu nhất......",
        "Không phải là sự tuyệt vọng, mà là tia hy vọng hão huyền rằng đối phương sẽ tự thay đổi vì bạn.",
        "-",
        "Thứ giam cầm bạn trong đau khổ lâu nhất không phải là sự tuyệt vọng, mà là tia hy vọng hão huyền rằng đối phương sẽ tự thay đổi vì bạn."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Tự xoa dịu vết thương",
        "Ta thường tìm đến những người sẵn sàng nói dối ta......",
        "Hơn là lắng nghe những người tát sự thật vào mặt ta để ta tỉnh giấc.",
        "Bởi vì thuốc đắng thì khó nuốt, còn mật ngọt độc dược lại khiến ta ngủ say trong vùng an toàn chết người.",
        "Ta có xu hướng tìm đến người vuốt ve sự yếu đuối hơn là người chỉ ra sự thật; bởi vì thuốc đắng thì khó nuốt, còn mật ngọt bao biện lại khiến ta ngủ say trong vũng lầy của chính mình."
    ],

    # 6. SHADOW
    [
        "Single-Punch (1 trang độc bản)",
        "Con thú bị xích",
        "Càng cố tỏ ra lương thiện và thuần khiết, phần u tối bên trong bạn càng đói khát và chờ chực bùng phát.",
        "-",
        "-",
        "Càng cố tỏ ra lương thiện và thuần khiết, phần u tối bên trong bạn càng đói khát và chờ chực bùng phát."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Điểm ghét ở người khác",
        "Điều bạn căm ghét tột cùng ở một ai đó......",
        "Thường là phần xấu xí mà chính bạn đang cố giấu giếm và chối bỏ ở bản thân mình.",
        "-",
        "Điều bạn căm ghét tột cùng ở người khác thường chính là phần xấu xí mà bạn đang cố che giấu và chối bỏ ở chính mình."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Chấp nhận góc khuất",
        "Trưởng thành không phải là tiêu diệt mọi suy nghĩ xấu xa, mà là học cách sống chung và không để chúng sai khiến bạn.",
        "-",
        "-",
        "Trưởng thành không phải là tiêu diệt mọi suy nghĩ xấu xa, mà là học cách sống chung và không để chúng sai khiến bạn."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Sự bộc phát bất ngờ",
        "Khi một người hiền lành bỗng trở nên tàn nhẫn......",
        "Đó không phải là họ thay đổi, mà là chiếc mặt nạ chịu đựng của họ vừa bị vỡ vụn.",
        "-",
        "Khi một người hiền lành bỗng trở nên tàn nhẫn, đó không phải là họ thay đổi, mà là chiếc mặt nạ chịu đựng của họ vừa bị vỡ vụn."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Bóng tối được thuần hóa",
        "Kẻ không biết giận dữ không phải là thánh nhân......",
        "Mà là kẻ quá hèn nhát để bảo vệ những giá trị cốt lõi của đời mình.",
        "Biết cách sử dụng sự tàn nhẫn một cách có kiểm soát mới là thứ bảo vệ sự tử tế của bạn khỏi bị chà đạp.",
        "Kẻ không dám giận dữ không phải là thánh nhân mà là kẻ bất lực; chỉ khi biết sử dụng sự tàn nhẫn một cách có kiểm soát, bạn mới đủ sức bảo vệ lòng tử tế của mình khỏi bị chà đạp."
    ],

    # 7. MASK
    [
        "Single-Punch (1 trang độc bản)",
        "Kiệt sức vì hoàn hảo",
        "Mặt nạ bạn đeo càng đẹp, bạn càng sợ tháo nó ra; cho đến một ngày bạn quên mất gương mặt thật của mình trông như thế nào.",
        "-",
        "-",
        "Mặt nạ bạn đeo càng đẹp, bạn càng sợ tháo nó ra; cho đến một ngày bạn quên mất gương mặt thật của mình trông như thế nào."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Nụ cười nơi đông người",
        "Cười nhiều nơi công cộng chưa chắc đã hạnh phúc......",
        "Đó đôi khi chỉ là phản xạ phòng vệ để không ai hỏi bạn đang gặp chuyện gì.",
        "-",
        "Cười nhiều nơi công cộng chưa chắc đã hạnh phúc, đó đôi khi chỉ là phản xạ phòng vệ để không ai hỏi bạn đang gặp chuyện gì."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Sự vừa lòng của thiên hạ",
        "Cố gắng làm vừa lòng tất cả mọi người là cách nhanh nhất để biến mình thành một kẻ không có chút cá tính nào.",
        "-",
        "-",
        "Cố gắng làm vừa lòng tất cả mọi người là cách nhanh nhất để biến mình thành một kẻ không có chút cá tính nào."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Về nhà sau một ngày",
        "Cảm giác nhẹ nhõm nhất sau một ngày dài......",
        "Không phải là được nghỉ ngơi, mà là được phép ngừng đóng vai một người vui vẻ và tích cực.",
        "-",
        "Cảm giác nhẹ nhõm nhất sau một ngày dài không phải là nghỉ ngơi, mà là được phép ngừng đóng vai một người vui vẻ và tích cực."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Chiếc lồng của sự chuẩn mực",
        "Ta sống cả đời theo kỳ vọng của cha mẹ, bạn bè và xã hội......",
        "Nhưng đến khi nhắm mắt xuôi tay, không một ai trong số họ có thể sống thay phần đời dang dở của ta.",
        "Dũng cảm lớn nhất đời người là dám từ bỏ chiếc áo khoác của kẻ khác để sống trọn vẹn với sự bất toàn của chính mình.",
        "Ta dành cả đời sống theo kỳ vọng của thiên hạ nhưng không ai sống thay phần đời dang dở của ta; dũng cảm lớn nhất là dám cởi bỏ chiếc mặt nạ chuẩn mực để sống trọn vẹn với sự bất toàn của chính mình."
    ],

    # 8. POWER
    [
        "Single-Punch (1 trang độc bản)",
        "Bản chất lộ diện",
        "Muốn biết bản chất thực sự của một người, đừng nhìn cách họ đối xử với sếp; hãy nhìn cách họ quát tháo người phục vụ.",
        "-",
        "-",
        "Muốn biết bản chất thực sự của một người, đừng nhìn cách họ đối xử với sếp; hãy nhìn cách họ quát tháo người phục vụ."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Quyền lực của sự im lặng",
        "Kẻ thích kiểm soát thường không dùng nắm đấm......",
        "Họ dùng sự im lặng và thái độ lạnh nhạt để khiến bạn tự dằn vặt và nhận lỗi trước.",
        "-",
        "Kẻ thích kiểm soát thường không dùng bạo lực; họ dùng sự im lặng và thái độ lạnh nhạt để khiến bạn tự dằn vặt và nhận lỗi trước."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Kẻ phục tùng hôm nay",
        "Kẻ khúm núm cúi đầu trước kẻ mạnh hôm nay sẽ là kẻ dẫm đạp tàn bạo nhất lên kẻ yếu khi họ có cơ hội nắm quyền.",
        "-",
        "-",
        "Kẻ khúm núm cúi đầu trước kẻ mạnh hôm nay sẽ là kẻ dẫm đạp tàn bạo nhất lên kẻ yếu khi họ có cơ hội nắm quyền."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Ràng buộc tài chính",
        "Tiền trao đi kèm với sự can thiệp thô bạo......",
        "Không phải là sự giúp đỡ của tình thân, mà là một hợp đồng mua quyền định đoạt cuộc đời bạn.",
        "-",
        "Tiền trao đi kèm với sự can thiệp thô bạo không phải là sự giúp đỡ của tình thân, mà là một hợp đồng mua quyền định đoạt cuộc đời bạn."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Ảo tưởng kiểm soát",
        "Bạn càng cố gắng kiểm soát suy nghĩ của người khác......",
        "Bạn càng biến mình thành tù nhân cho những hành động thất thường của họ.",
        "Quyền lực tối thượng không nằm ở việc sai khiến được ai, mà ở việc không một ai có thể làm lung lay sự bình an nội tại của bạn.",
        "Càng cố gắng kiểm soát người khác, bạn càng biến mình thành tù nhân cho hành vi của họ; quyền lực tối thượng là khi không một ai có thể làm lung lay sự bình an nội tại của bạn."
    ],

    # 9. MANIPULATION
    [
        "Single-Punch (1 trang độc bản)",
        "Vũ khí nước mắt",
        "Nước mắt của kẻ đóng vai nạn nhân đôi khi là thứ vũ khí tàn độc nhất để ép bạn phải trở thành kẻ thủ ác.",
        "-",
        "-",
        "Nước mắt của kẻ đóng vai nạn nhân đôi khi là thứ vũ khí tàn độc nhất để ép bạn phải trở thành kẻ thủ ác."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Thao túng bằng tình thương",
        "Câu nói 'Tao làm thế chỉ vì lo cho mày'......",
        "Thực chất là lời biện minh quen thuộc để bắt bạn sống theo ý muốn và nỗi sợ của họ.",
        "-",
        "Câu nói 'Tao làm thế chỉ vì lo cho mày' thực chất là lời biện minh quen thuộc để bắt bạn sống theo ý muốn và nỗi sợ của người khác."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Ranh giới bị xóa nhòa",
        "Khi một người liên tục vi phạm ranh giới của bạn và trách bạn hẹp hòi, họ không tôn trọng bạn; họ chỉ đang thử xem bạn chịu đựng được đến đâu.",
        "-",
        "-",
        "Khi một người liên tục vi phạm ranh giới của bạn và trách bạn hẹp hòi, họ không tôn trọng bạn; họ chỉ đang thử xem bạn chịu đựng được đến đâu."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Bẫy tội lỗi trong gia đình",
        "Đứa trẻ hiểu chuyện và ngoan ngoãn nhất......",
        "Thường là đứa trẻ học được cách nuốt nước mắt vào trong để đổi lấy một ngày yên ấm trong nhà.",
        "-",
        "Đứa trẻ hiểu chuyện nhất thường là đứa trẻ học được cách nuốt nước mắt vào trong để đổi lấy một ngày yên ấm trong gia đình."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Đảo ngược trắng đen",
        "Kẻ thao túng đỉnh cao không bao giờ đôi co......",
        "Họ khéo léo biến sai lầm rành rành của họ thành lỗi lầm do sự nhạy cảm thái quá của chính bạn.",
        "Đến mức bạn bắt đầu nghi ngờ trí nhớ của mình và tự xin lỗi vì đã cảm thấy bị tổn thương.",
        "Kẻ thao túng không đôi co, họ khéo léo biến lỗi của mình thành do sự nhạy cảm thái quá của bạn; đến mức bạn bắt đầu nghi ngờ chính cảm xúc của mình và đi xin lỗi kẻ đã làm tổn thương bạn."
    ],

    # 10. FREEDOM
    [
        "Single-Punch (1 trang độc bản)",
        "Tự do và cái giá",
        "Người ta đòi hỏi tự do rất hăng hái, nhưng khi nhận được tự do rồi, họ lại hoảng loạn tìm một kẻ khác để đổ lỗi cho sai lầm của mình.",
        "-",
        "-",
        "Người ta đòi hỏi tự do rất hăng hái, nhưng khi nhận được tự do rồi, họ lại hoảng loạn tìm một kẻ khác để đổ lỗi cho sai lầm của mình."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Xiềng xích tự nguyện",
        "Chúng ta dễ dàng chui vào những chiếc lồng......",
        "Chỉ vì trong chiếc lồng đó, người ta cho ta thức ăn đều đặn và không bắt ta phải suy nghĩ.",
        "-",
        "Chúng ta dễ dàng chui vào những chiếc lồng chỉ vì nơi đó có thức ăn đều đặn và không bắt ta phải tự chịu trách nhiệm cho cuộc đời mình."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Chấp nhận cô đơn",
        "Muốn bay một mình trên bầu trời tự do, bạn phải chấp nhận cái lạnh buốt giá mà không một kẻ sống theo đàn nào hiểu được.",
        "-",
        "-",
        "Muốn bay một mình trên bầu trời tự do, bạn phải chấp nhận cái lạnh buốt giá mà không một kẻ sống theo đàn nào hiểu được."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Áp lực của sự lựa chọn",
        "Khi bạn có quyền tự quyết định mọi thứ......",
        "Bạn sẽ nhận ra rằng không có gì đáng sợ hơn việc phải hoàn toàn chịu trách nhiệm cho những thất bại của mình.",
        "-",
        "Khi có quyền tự quyết định mọi thứ, bạn sẽ nhận ra không có gì đáng sợ hơn việc phải hoàn toàn chịu trách nhiệm cho những thất bại của chính mình."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Tự do đích thực",
        "Tự do không phải là làm bất cứ điều gì bạn muốn......",
        "Mà là bạn có đủ dũng khí để từ chối làm những điều đi ngược lại phẩm giá của mình.",
        "Kẻ có thể nói chữ 'Không' mà không thấy tội lỗi mới là kẻ thực sự được tự do giữa cuộc đời này.",
        "Tự do không phải là muốn làm gì thì làm, mà là có dũng khí từ chối những điều đi ngược lại phẩm giá; kẻ có thể nói 'Không' mà không cắn rứt mới là kẻ tự do đích thực."
    ],

    # 11. TRUTH
    [
        "Single-Punch (1 trang độc bản)",
        "Sự thật đắng cay",
        "Người ta không ghét sự thật; người ta chỉ ghét cảm giác bẽ bàng khi sự thật đó lột trần chiếc áo tự hào bấy lâu của họ.",
        "-",
        "-",
        "Người ta không ghét sự thật; người ta chỉ ghét cảm giác bẽ bàng khi sự thật đó lột trần chiếc áo tự hào bấy lâu của họ."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Sự im lặng của kẻ thức thời",
        "Khi nhìn thấu một sự dối trá......",
        "Người khôn ngoan không vạch mặt ngay, mà họ lùi lại một bước để xem màn kịch diễn được đến đâu.",
        "-",
        "Khi nhìn thấu một sự dối trá, người khôn ngoan không vạch mặt ngay, mà họ lùi lại một bước để xem màn kịch diễn được đến đâu."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Bức tranh tự vẽ",
        "Ta thường tin vào những điều khiến ta thấy an tâm, chứ không phải những điều phản ánh đúng thực tế.",
        "-",
        "-",
        "Ta thường tin vào những điều khiến ta thấy an tâm, chứ không phải những điều phản ánh đúng thực tế."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Cái giá của sự chân thật",
        "Nói thật với một người đang say trong ảo tưởng......",
        "Chẳng khác nào bạn đang châm lửa đốt cháy ngôi nhà hạnh phúc duy nhất mà họ có.",
        "-",
        "Nói thật với một người đang say trong ảo tưởng chẳng khác nào bạn châm lửa đốt cháy ngôi nhà hạnh phúc duy nhất mà họ có; họ sẽ hận bạn thay vì biết ơn."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Tấm gương không nịnh bợ",
        "Sự thật luôn giống như một tấm gương lạnh lùng......",
        "Nó không bao giờ sửa đổi hình ảnh để làm vui lòng người soi chiếu.",
        "Kẻ đập vỡ tấm gương không làm cho mình đẹp hơn; họ chỉ đang tự biến mình thành kẻ mù quáng giữa bóng tối.",
        "Sự thật giống như tấm gương lạnh lùng không nịnh bợ ai; kẻ tức tối đập vỡ gương không làm mình đẹp hơn, mà chỉ tự giam mình trong sự mù quáng."
    ],

    # 12. LOVE
    [
        "Single-Punch (1 trang độc bản)",
        "Chiếm hữu và tình yêu",
        "Nhiều người nói yêu bạn, nhưng thực chất họ chỉ yêu cảm giác được sở hữu và điều khiển cuộc đời của bạn mà thôi.",
        "-",
        "-",
        "Nhiều người nói yêu bạn, nhưng thực chất họ chỉ yêu cảm giác được sở hữu và điều khiển cuộc đời của bạn mà thôi."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Nỗi sợ bị bỏ rơi",
        "Ta bám víu lấy một người không còn yêu ta......",
        "Không phải vì tình cảm còn sâu đậm, mà vì sợ cảm giác phải đối diện với sự thất bại và cô độc một mình.",
        "-",
        "Ta bám víu người không còn yêu ta không phải vì tình sâu đậm, mà vì quá sợ hãi cảm giác phải đối diện với sự thất bại và cô độc một mình."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Ranh giới trong tình cảm",
        "Tình yêu không cần bạn phải xóa bỏ cái tôi của mình; một tình yêu lành mạnh là hai cá thể độc lập bước đi cạnh nhau.",
        "-",
        "-",
        "Tình yêu không cần bạn phải xóa bỏ cái tôi của mình; một tình yêu lành mạnh là hai cá thể độc lập bước đi cạnh nhau."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Đánh đổi bản thân",
        "Càng thay đổi bản thân để làm hài lòng người khác......",
        "Họ lại càng xem thường bạn, vì ngay cả bản thân bạn còn không biết cách trân trọng chính mình.",
        "-",
        "Càng thay đổi bản thân để làm hài lòng đối phương, họ lại càng xem thường bạn; vì ngay cả bạn còn không tôn trọng con người thật của mình."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Tình yêu trưởng thành",
        "Yêu một người là cho họ toàn quyền làm tổn thương bạn......",
        "Nhưng bạn vẫn tin rằng họ sẽ không bao giờ làm điều đó.",
        "Và nếu họ làm tổn thương bạn, bạn đủ tự trọng và dũng khí để bước đi mà không cần một lời van xin.",
        "Yêu là trao cho người khác quyền làm tổn thương mình nhưng tin họ không làm vậy; và nếu họ phản bội niềm tin ấy, bạn đủ dũng khí bước đi mà không cần van xin."
    ],

    # 13. LOYALTY
    [
        "Single-Punch (1 trang độc bản)",
        "Lòng trung thành mù quáng",
        "Trung thành với một kẻ không có đạo đức không phải là nghĩa khí, mà là đồng lõa với sự bất công.",
        "-",
        "-",
        "Trung thành với một kẻ không có đạo đức không phải là nghĩa khí, mà là đồng lõa với sự bất công."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Khi quyền lợi cạn kiệt",
        "Muốn biết ai trung thành với bạn......",
        "Hãy quan sát thái độ của họ khi bạn không còn giá trị lợi dụng hoặc khi bạn gặp hoạn nạn.",
        "-",
        "Muốn biết ai trung thành, hãy nhìn thái độ của họ khi bạn không còn giá trị lợi dụng; lúc sa cơ lỡ vận là lúc bộ mặt thật lộ diện rõ ràng nhất."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Cái giá của sự phản bội",
        "Kẻ phản bội bạn một lần sẽ phản bội bạn lần thứ hai, chỉ cần cái giá người ta trả cho lần sau đủ hấp dẫn.",
        "-",
        "-",
        "Kẻ phản bội bạn một lần sẽ phản bội bạn lần thứ hai, chỉ cần cái giá người ta trả cho lần sau đủ hấp dẫn."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Lòng tốt bị lợi dụng",
        "Người hay chịu thiệt thòi trong các mối quan hệ......",
        "Thường là người coi trọng nghĩa khí hơn lợi ích, và xui xẻo thay, thế giới này lại vận hành bằng lợi ích.",
        "-",
        "Người hay chịu thiệt thòi thường là người coi trọng nghĩa khí hơn lợi ích; và cay đắng thay, đa phần các mối quan hệ ngoài đời lại vận hành bằng lợi ích."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Trung thành với chính mình",
        "Trước khi thề thốt trung thành với bất kỳ ai......",
        "Hãy tự hỏi bạn đã từng trung thực và trung thành với những ước mơ của chính mình hay chưa.",
        "Bỏ rơi bản thân để cung phụng sự nghiệp của người khác là sự phản bội cay đắng nhất của đời người.",
        "Trước khi thề thốt trung thành với ai, hãy tự hỏi bạn đã trung thực với ước mơ của mình chưa; bỏ rơi bản thân để phục tùng kẻ khác là sự phản bội cay đắng nhất."
    ],

    # 14. ENVY
    [
        "Single-Punch (1 trang độc bản)",
        "Chất độc đố kỵ",
        "Đố kỵ là tự mình uống thuốc độc nhưng lại mong cho người khác chết.",
        "-",
        "-",
        "Đố kỵ là tự mình uống thuốc độc nhưng lại mong cho người khác chết."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Kẻ ghen ghét gần gũi",
        "Người ghen tị với bạn nhiều nhất......",
        "Hiếm khi là người xa lạ, mà thường là những người bạn cùng trang lứa, cùng xuất phát điểm nhưng bị bạn bỏ lại phía sau.",
        "-",
        "Người ghen tị với bạn nhiều nhất hiếm khi là người xa lạ, mà thường là bạn bè cùng xuất phát điểm nhưng nay bị bạn bỏ lại phía sau."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Khen ngợi có gai",
        "Lời khen kèm theo chữ 'nhưng' thực chất không phải là khen; đó là cách kẻ đố kỵ giảm bớt nỗi đau thua kém của chính họ.",
        "-",
        "-",
        "Lời khen kèm theo chữ 'nhưng' thực chất không phải là khen; đó là cách kẻ đố kỵ giảm bớt nỗi đau thua kém của chính họ."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Nỗi đau của kẻ so sánh",
        "Bạn sẽ không bao giờ cảm thấy đủ đầy......",
        "Nếu thước đo hạnh phúc của bạn luôn dựa trên những thứ mà người bên cạnh đang sở hữu.",
        "-",
        "Bạn sẽ không bao giờ cảm thấy đủ đầy nếu thước đo hạnh phúc của bạn luôn dựa trên những thứ mà người bên cạnh đang sở hữu."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Chuyển hóa đố kỵ",
        "Khi thấy người khác hơn mình, phản xạ đầu tiên của bản ngã là tìm vết nhơ để hạ bệ họ......",
        "Nhưng hành động đó không làm bạn tiến lên một centimet nào, nó chỉ biến bạn thành kẻ cay độc bên lề cuộc đời.",
        "Học cách thừa nhận điểm giỏi của đối phương là bước đầu tiên để bạn thoát khỏi cái bóng hèn hạ của chính mình.",
        "Hạ bệ người giỏi hơn không giúp bạn tiến lên, mà chỉ biến bạn thành kẻ cay độc; thừa nhận thực lực của đối phương là bước đầu tiên để thoát khỏi sự hèn hạ."
    ],

    # 15. CROWD
    [
        "Single-Punch (1 trang độc bản)",
        "Can đảm bầy đàn",
        "Đám đông rất dũng cảm khi ném đá tập thể, nhưng khi đứng riêng từng người một, họ lại hèn nhát không dám chịu trách nhiệm cho bất kỳ điều gì.",
        "-",
        "-",
        "Đám đông rất dũng cảm khi ném đá tập thể, nhưng khi đứng riêng từng người một, họ lại hèn nhát không dám chịu trách nhiệm cho bất kỳ điều gì."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Tiếng nói thiểu số",
        "Chân lý không bao giờ thuộc về số đông......",
        "Chân lý thuộc về những người dám nói lên sự thật ngay cả khi cả thế giới đang gật đầu theo một lời nói dối.",
        "-",
        "Chân lý không mặc nhiên thuộc về số đông; chân lý thuộc về những người dám nói thật ngay cả khi cả đám đông đang say sưa gật đầu theo một lời nói dối."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Lạc lối giữa tập thể",
        "Đi theo đám đông rất dễ dàng, nhưng nó sẽ dẫn bạn đến đúng nơi mà tất cả những người bình thường đều phải đến: sự tầm thường.",
        "-",
        "-",
        "Đi theo đám đông rất dễ dàng, nhưng nó sẽ dẫn bạn đến đúng nơi mà tất cả những người bình thường đều phải đến: sự tầm thường."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Ảo tưởng của sự đồng thuận",
        "Khi hàng ngàn người cùng làm một điều ngu ngốc......",
        "Điều ngu ngốc đó vẫn không thể biến thành một hành động khôn ngoan.",
        "-",
        "Khi hàng ngàn người cùng đồng thanh làm một điều ngu ngốc, điều đó vẫn không thể biến thành sự thông thái."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Tách khỏi dòng người",
        "Để không bị đám đông cuốn trôi......",
        "Bạn phải chấp nhận việc bị hiểu lầm, bị tẩy chay và bị gán cho những cái mác lập dị.",
        "Nhưng cái giá của sự cô độc đó vẫn rẻ hơn rất nhiều so với cái giá của việc đánh mất chính mình giữa dòng đời xô bồ.",
        "Để không bị đám đông cuốn trôi, bạn phải chấp nhận bị hiểu lầm và tẩy chay; nhưng cái giá của cô độc vẫn rẻ hơn nhiều so với việc đánh mất chính mình."
    ],

    # 16. SUFFERING
    [
        "Single-Punch (1 trang độc bản)",
        "Nghiện đóng vai nạn nhân",
        "Có những người bám chặt lấy nỗi đau của quá khứ, vì nếu buông nỗi đau đó ra, họ sẽ không còn lý do gì để bao biện cho sự thất bại hiện tại.",
        "-",
        "-",
        "Có những người bám chặt lấy nỗi đau của quá khứ, vì nếu buông nỗi đau đó ra, họ sẽ không còn lý do gì để bao biện cho sự thất bại hiện tại."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Vết thương và sự trưởng thành",
        "Nỗi đau tự nó không dạy cho bạn điều gì......",
        "Chỉ có cách bạn đối diện, nghiền ngẫm và vượt qua nó mới tạo nên sức mạnh thực sự của bạn.",
        "-",
        "Nỗi đau tự nó không tạo nên bài học; chỉ có cách bạn đối diện, nghiền ngẫm và vượt qua vết thương mới tạo nên bản lĩnh thực sự."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Khoe mẽ nỗi đau",
        "Đem vết thương của mình ra kể lể cho cả thiên hạ nghe không phải là cách chữa lành; đó chỉ là hành vi cầu xin sự thương hại rẻ tiền.",
        "-",
        "-",
        "Đem vết thương của mình ra kể lể cho cả thiên hạ nghe không phải là cách chữa lành; đó chỉ là hành vi cầu xin sự thương hại rẻ tiền."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Vòng lặp tự thương hại",
        "Càng ngâm mình trong cảm giác tủi thân......",
        "Bạn càng trao quyền năng cho những kẻ đã từng làm tổn thương bạn tiếp tục điều khiển cuộc đời mình.",
        "-",
        "Càng ngâm mình trong sự tủi thân, bạn càng trao quyền cho những kẻ làm tổn thương bạn tiếp tục điều khiển tâm trạng và tương lai của mình."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Sự chuyển hóa của nỗi đau",
        "Khổ đau là người thầy nghiêm khắc nhất......",
        "Nó đập vỡ mọi ảo tưởng ngọt ngào mà bạn từng tự vẽ ra về cuộc sống và con người.",
        "Nhưng chính từ đống tro tàn của những đổ vỡ đó, một nhân cách kiên cường và bất khả xâm phạm mới thực sự được sinh ra.",
        "Khổ đau đập vỡ mọi ảo tưởng ngọt ngào bạn từng tự vẽ ra; nhưng chính từ đống tro tàn của sự đổ vỡ đó, một nhân cách kiên cường mới thực sự được tái sinh."
    ],

    # 17. IDENTITY
    [
        "Single-Punch (1 trang độc bản)",
        "Khi ánh đèn sân khấu tắt",
        "Bạn thực sự là ai khi chỉ có một mình trong căn phòng tối, không điện thoại, không mạng xã hội và không có bất kỳ ai để trình diễn?",
        "-",
        "-",
        "Bạn thực sự là ai khi chỉ có một mình trong căn phòng tối, không điện thoại, không mạng xã hội và không có bất kỳ ai để trình diễn?"
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Định nghĩa bản thân",
        "Nếu tước đi công việc, tiền bạc và danh tiếng......",
        "Thứ còn lại bên trong bạn là một tâm hồn phong phú, hay chỉ là một đống tro tàn trống rỗng?",
        "-",
        "Nếu tước đi chức danh, tiền bạc và danh tiếng, thứ còn lại bên trong bạn là một nội tâm vững vàng, hay chỉ là một khoảng trống hoang tàn?"
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Bắt chước người khác",
        "Ta dành nửa đời đầu để cố giống người khác, và dành nửa đời sau để vật lộn tìm lại chính con người ban đầu của mình.",
        "-",
        "-",
        "Ta dành nửa đời đầu để cố giống người khác, và dành nửa đời sau để vật lộn tìm lại chính con người ban đầu của mình."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Sợ bị lãng quên",
        "Nhiều người phát cuồng vì sự chú ý trên mạng......",
        "Bởi vì họ sợ rằng nếu không có người nhìn ngó, họ sẽ không thể tự cảm nhận được sự tồn tại của chính mình.",
        "-",
        "Nhiều người phát cuồng vì lượt tương tác ảo chỉ vì sợ rằng nếu không ai nhìn ngó, họ không thể tự chứng minh được sự tồn tại của chính mình."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Gốc rễ bên trong",
        "Một cái cây có rễ cắm sâu vào lòng đất......",
        "Sẽ không bao giờ sợ hãi những cơn bão điên cuồng gào thét trên mặt đất.",
        "Cũng vậy, người có nội lực vững vàng sẽ không bị lay chuyển bởi bất kỳ lời khen tiếng chê nào của người đời.",
        "Cái cây có rễ sâu không sợ bão táp; cũng vậy, người có bản sắc và nội lực vững vàng sẽ không bao giờ bị lay chuyển bởi lời phán xét của thiên hạ."
    ],

    # 18. MEANING
    [
        "Single-Punch (1 trang độc bản)",
        "Đi tìm ý nghĩa",
        "Cuộc đời này vốn dĩ không có sẵn ý nghĩa; ý nghĩa là thứ do chính bạn tự tay nhào nặn và chịu trách nhiệm đến cùng.",
        "-",
        "-",
        "Cuộc đời này vốn dĩ không có sẵn ý nghĩa; ý nghĩa là thứ do chính bạn tự tay nhào nặn và chịu trách nhiệm đến cùng."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Ảo tưởng về đích đến",
        "Người ta thường nghĩ khi đạt được mục tiêu thì sẽ hạnh phúc......",
        "Nhưng khi đứng trên đỉnh cao rồi, thứ ập đến đầu tiên lại là cảm giác hụt hẫng và trống trải vô tận.",
        "-",
        "Người ta tưởng chạm đến đích là hạnh phúc, nhưng khi đứng trên đỉnh cao, thứ ập đến đầu tiên lại là sự hụt hẫng và trống trải vô tận."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Sự phi lý của cuộc sống",
        "Bi kịch lớn nhất không phải là chết đi, mà là sống cả đời nhưng chưa từng thực sự thức tỉnh một ngày nào.",
        "-",
        "-",
        "Bi kịch lớn nhất không phải là chết đi, mà là sống cả đời nhưng chưa từng thực sự thức tỉnh một ngày nào."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Hành động nhỏ bé",
        "Đừng chờ đợi một sứ mệnh vĩ đại mới bắt đầu sống......",
        "Ý nghĩa nằm ngay trong cách bạn nấu một bữa ăn, đọc một trang sách và tử tế với người bên cạnh hôm nay.",
        "-",
        "Đừng đợi sứ mệnh to tát mới bắt đầu sống; ý nghĩa nằm ngay trong cách bạn trân trọng từng khoảnh khắc bình dị của thực tại hôm nay."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Thức tỉnh giữa hư vô",
        "Vũ trụ này không quan tâm bạn đau khổ hay hạnh phúc......",
        "Mọi quy luật đều vận hành một cách lạnh lùng và vô cảm.",
        "Nhưng chính vì sự vô nghĩa đó, sự lựa chọn sống tử tế và can đảm của bạn mới trở nên thiêng liêng và quý giá nhất.",
        "Vũ trụ vận hành lạnh lùng và không bận tâm đến cảm xúc của bạn; nhưng chính giữa hư vô đó, sự can đảm sống tử tế của bạn mới trở nên thiêng liêng nhất."
    ],

    # 19. SOLITUDE
    [
        "Single-Punch (1 trang độc bản)",
        "Sợ sự im lặng",
        "Người không thể chịu nổi một giờ im lặng một mình là người đang sợ hãi phải nghe thấy tiếng gào thét từ chính tâm hồn đổ nát của họ.",
        "-",
        "-",
        "Người không thể chịu nổi một giờ im lặng một mình là người đang sợ hãi phải nghe thấy tiếng gào thét từ chính tâm hồn đổ nát của họ."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Cô độc hay cô đơn",
        "Cô đơn là khi bạn thèm khát có ai đó ở cạnh......",
        "Còn cô độc là khi bạn tìm thấy sự an nhiên tuyệt đối trong sự tĩnh lặng của chính mình.",
        "-",
        "Cô đơn là khi bạn thèm khát sự hiện diện của người khác; còn cô độc là trạng thái an nhiên tuyệt đối khi tự làm bạn với chính mình."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Thanh lọc các mối quan hệ",
        "Thà một mình ngẩng cao đầu đi trong đêm tối, còn hơn ngồi chung bàn tiệc với những kẻ nói cười nhưng trong lòng toan tính đâm sau lưng.",
        "-",
        "-",
        "Thà một mình ngẩng cao đầu đi trong đêm tối, còn hơn ngồi chung bàn tiệc với những kẻ nói cười nhưng trong lòng toan tính đâm sau lưng."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Nơi tái tạo năng lượng",
        "Sự tĩnh lặng không bao giờ làm hại bạn......",
        "Nó chỉ gạt bỏ những tiếng ồn giả tạo để bạn nghe rõ điều gì thực sự quan trọng trong cuộc đời mình.",
        "-",
        "Sự tĩnh lặng không làm hại bạn; nó chỉ gạt bỏ những ồn ào giả tạo để bạn nhận ra điều gì thực sự xứng đáng để bận tâm."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Tự do nơi hoang vắng",
        "Khi bạn không còn sợ hãi sự cô độc......",
        "Sẽ không một ai có thể dùng sự bỏ rơi để đe dọa hoặc thao túng cuộc đời bạn được nữa.",
        "Đó là lúc bạn đạt đến đỉnh cao của sự tự do tinh thần: tự tại, bất biến và hoàn toàn làm chủ số phận mình.",
        "Khi không còn sợ cô độc, không ai có thể dùng sự bỏ rơi để thao túng bạn; đó là lúc bạn chạm đến sự tự do tinh thần cao nhất."
    ],

    # 20. STATUS
    [
        "Single-Punch (1 trang độc bản)",
        "Khiêm nhường giả tạo",
        "Kẻ cố tình hạ mình nơi đông người thường là kẻ khao khát được thiên hạ nâng lên vị trí cao nhất.",
        "-",
        "-",
        "Kẻ cố tình hạ mình nơi đông người thường là kẻ khao khát được thiên hạ nâng lên vị trí cao nhất."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Hào quang dư luận",
        "Đám đông có thể tung hô bạn lên mây xanh hôm nay......",
        "Và cũng chính họ sẽ dẫm đạp bạn xuống đất bùn tàn nhẫn nhất vào ngày mai chỉ sau một tin đồn.",
        "-",
        "Đám đông có thể tung hô bạn hôm nay và dẫm đạp bạn xuống bùn vào ngày mai; kẻ gửi gắm tự trọng vào dư luận đang xây nhà trên cát lún."
    ],
    [
        "Single-Punch (1 trang độc bản)",
        "Giá trị thực sự",
        "Đẳng cấp của một người không nằm ở chức danh trên danh thiếp hay số dư tài khoản; nó nằm ở sự đĩnh đạc khi bị tước bỏ toàn bộ hào nhoáng bên ngoài.",
        "-",
        "-",
        "Đẳng cấp của một người không nằm ở chức danh trên danh thiếp hay số dư tài khoản; nó nằm ở sự đĩnh đạc khi bị tước bỏ toàn bộ hào nhoáng bên ngoài."
    ],
    [
        "Carousel 2 trang (Đọc lướt 5-6s)",
        "Khoe khoang sự tử tế",
        "Khi bạn làm việc thiện mà nóng lòng muốn cả thế giới biết......",
        "Đó không còn là lòng trắc ẩn nữa, mà là một chiến dịch truyền thông quảng bá cho bản ngã của bạn.",
        "-",
        "Làm việc thiện mà sốt sắng chụp ảnh đăng lên mạng không còn là lòng trắc ẩn, mà là một chiến dịch truyền thông đánh bóng bản ngã."
    ],
    [
        "Carousel 3 trang (Đọc sâu 7-9s)",
        "Vượt lên danh vị",
        "Người tự tin vào năng lực thực sự của mình......",
        "Không bao giờ cần phải phô trương tài sản hay dùng chức tước để ép người khác phải nể phục.",
        "Họ bước đi đĩnh đạc, nói năng từ tốn, bởi vì phẩm giá của vàng thật thì không bao giờ sợ bị thời gian làm phai mờ.",
        "Người vững vàng thực sự không cần phô trương chức tước để ép người khác nể; phẩm giá vàng thật thì không bao giờ sợ bị thời gian làm phai mờ."
    ]
]

def build_100_posts():
    posts = []
    post_idx = 1
    start_date = datetime(2026, 11, 16)
    time_slots = ["11:30 - 12:30 (Trưa)", "19:30 - 20:30 (Tối)", "21:00 - 22:30 (Đêm chiêm nghiệm)"]

    for t_idx, (t_code, t_name) in enumerate(THEMES):
        for item_idx in range(5):
            flat_idx = t_idx * 5 + item_idx
            fmt_type, p_title, p_s1, p_s2, p_s3, p_full = ALL_100_POSTS[flat_idx]
            
            post_id = f"TXT-{post_idx:04d}"
            curr_date = start_date + timedelta(days=post_idx - 1)
            date_str = curr_date.strftime("%Y-%m-%d")
            weekday_str = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"][curr_date.weekday()]
            full_date_label = f"{weekday_str} ({curr_date.strftime('%d/%m')})"
            time_slot = time_slots[post_idx % len(time_slots)]

            hashtags = f"#hiyuabyss #{t_code.lower()} #tamlyhoc #trietngon #darkpsychology #bocchuan #gocnhin #phanthu"
            visual = "Tone tối giản Dark Mode, nhạc piano/ambient trầm, chữ sans-serif trắng trên nền xám than, hiệu ứng fade chậm"

            posts.append([
                post_idx,
                full_date_label,
                date_str,
                time_slot,
                post_id,
                p_title,
                f"{t_code} ({t_name})",
                fmt_type,
                p_s1,
                p_s2,
                p_s3,
                p_full,
                hashtags,
                visual,
                "SẴN SÀNG"
            ])
            post_idx += 1

    return posts

def main():
    posts = build_100_posts()
    headers = [
        "STT",
        "Lịch Đăng (Thứ, Ngày)",
        "Ngày chuẩn (YYYY-MM-DD)",
        "Khung Giờ Vàng",
        "Mã ID",
        "Tiêu Đề Bài Viết",
        "Chủ Đề Hạt Nhân",
        "Định Dạng Slide",
        "Trang 1 (Hook / Nội dung chính)",
        "Trang 2 (Cú lật bóc trần)",
        "Trang 3 (Chiếc gương phản tư)",
        "Văn Bản Hoàn Chỉnh (Full Text)",
        "Hashtags Đề Xuất",
        "Gợi Ý Visual & Âm Thanh",
        "Trạng Thái"
    ]

    out_csv = "scripts/tiktok_100_posts.csv"
    with open(out_csv, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(posts)

    print(f"Đã tạo thành công {len(posts)} bài triết ngôn độc bản đa dạng định dạng tại {out_csv}")

if __name__ == "__main__":
    main()
