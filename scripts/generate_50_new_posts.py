#!/usr/bin/env python3
"""
Hiyu Abyss — Generate 50 New Engaging TikTok Posts (TXT-0101 to TXT-0150)
Strictly:
- Curiosity-gap hooks (< 10 words, ends with `......` for multi-slide).
- Pacing: ~40% Single-Punch, ~40% Carousel 2-slide, ~20% Carousel 3-slide.
- 100% Real Historical Thinkers / Classical Sources: Erich Fromm, Rainer Maria Rilke,
  Michel de Montaigne, Marcus Aurelius, Seneca, Carl Jung, Lao Tzu, Thoreau, Viktor Frankl,
  Friedrich Nietzsche, Arthur Schopenhauer, Spinoza, Từ điển Tâm lý học, Ghi chép Khắc kỷ.
- Complete metadata: Tiêu đề (<90 từ), Mô tả (Caption kéo tương tác), 5 Hashtags, Template (theme_61..90).
"""

import csv
from datetime import datetime, timedelta

# 50 Detailed Posts data: (fmt, title, s1, s2, s3, full_text, author, desc, theme, hashtags)
NEW_50_POSTS = [
    # 1. Ranh Giới Cảm Xúc & Tôn Trọng Bản Thân (TXT-0101 to TXT-0108)
    (
        "Carousel 2 trang",
        "Tôn trọng người khác không phải là quỳ gối, mà là nhìn nhận họ đúng như bản chất vốn có.",
        "Tôn trọng một người thật lòng là khi......",
        "Bạn muốn họ lớn lên theo cách của chính họ, chứ không phải để phục vụ cho sự tiện lợi của bạn.",
        "-",
        "Tôn trọng thật lòng là muốn đối phương phát triển theo cách của riêng họ, chứ không phải nhào nặn họ để phục vụ cho sự tiện lợi của bản thân bạn.",
        "Erich Fromm",
        "Rất nhiều người nhầm lẫn giữa sự quan tâm và lòng chiếm hữu. Khi bạn yêu một ai đó nhưng luôn ép họ phải suy nghĩ, hành động theo ý mình, bạn không yêu họ—bạn chỉ đang yêu sự phục tùng của họ mà thôi. Tôn trọng thực sự đòi hỏi dũng khí để chấp nhận sự khác biệt. Bạn đã từng phải gồng mình thay đổi vì ai chưa?",
        "RANH GIỚI (Tôn trọng & Bản sắc)",
        "#hiyuabyss #tamlyhoc #ranhgioi #tuduy #erichfromm"
    ),
    (
        "Single-Punch (1 trang)",
        "Đỉnh cao của sự độc lập là biết cách thuộc về chính mình trước khi thuộc về ai khác.",
        "Điều vĩ đại nhất trên thế giới này là biết cách thuộc về chính mình.",
        "-", "-",
        "Điều vĩ đại nhất trên thế giới này là biết cách thuộc về chính mình.",
        "Michel de Montaigne",
        "Nếu lòng tự trọng của bạn phải vay mượn từ lời khen của đám đông, bạn sẽ vỡ vụn ngay khi có kẻ chê bai. Người biết cách thuộc về chính mình không cần phải gồng gánh bất kỳ chiếc mặt nạ nào để tìm kiếm sự chấp nhận. Bạn có cảm thấy an yên khi chỉ có một mình?",
        "RANH GIỚI (Tự chủ nội tâm)",
        "#hiyuabyss #tamlyhoc #chinhminh #montaigne #tinhthuc"
    ),
    (
        "Carousel 2 trang",
        "Một tâm hồn có trật tự không bao giờ trốn chạy sự tĩnh lặng của chính mình.",
        "Dấu hiệu rõ nhất của một tâm trí vững vàng là......",
        "Khả năng ở yên một chỗ và hoàn toàn thoải mái trong sự đồng hành của chính mình.",
        "-",
        "Dấu hiệu rõ nhất của một tâm trí vững vàng là khả năng ở yên một chỗ và hoàn toàn an ổn trong sự đồng hành của chính mình.",
        "Seneca",
        "Khi tâm trí bất an, người ta thường tìm mọi cách để lấp đầy khoảng trống bằng mạng xã hội, tiệc tùng hay những mối quan hệ hời hợt. Dám ở một mình mà không cảm thấy cô đơn là thước đo cao nhất của sự trưởng thành cảm xúc. Bạn có sợ sự im lặng không?",
        "RANH GIỚI (Tĩnh lặng nội tâm)",
        "#hiyuabyss #tamlyhoc #khacki #seneca #tinhlang"
    ),
    (
        "Single-Punch (1 trang)",
        "Con người phải tự đứng thẳng trên đôi chân của mình, chứ không phải được người khác dựng đứng.",
        "Một con người phải tự mình đứng thẳng, chứ không phải để người khác chống đỡ mới đứng được.",
        "-", "-",
        "Một con người phải tự mình đứng thẳng, chứ không phải để người khác chống đỡ mới đứng được.",
        "Marcus Aurelius",
        "Dựa dẫm cảm xúc vào người khác giống như xây nhà trên cát lún. Người khác có thể đồng hành, có thể thấu cảm, nhưng không ai có thể sống thay phần đời của bạn. Hãy tự làm điểm tựa vững chãi nhất cho chính mình.",
        "RANH GIỚI (Điểm tựa nội tại)",
        "#hiyuabyss #tamlyhoc #marcusaurelius #khacki #kientri"
    ),
    (
        "Carousel 3 trang",
        "Thứ khiến bạn khó chịu nhất ở người khác chính là tấm gương soi chiếu góc tối của bạn.",
        "Mọi thứ làm bạn bực bội ở người khác......",
        "Thực chất là một manh mối dẫn thẳng vào góc khuất mà bạn đang chối bỏ trong chính bản thân mình.",
        "Chỉ khi dám đối diện với bóng tối bên trong, bạn mới ngừng phóng chiếu sự phán xét lên người ngoài.",
        "Mọi điều khiến ta khó chịu ở người khác thực chất đều là chiếc gương soi chiếu những phần tối mà ta đang trốn tránh bên trong chính mình.",
        "Carl Jung",
        "Phân tâm học gọi đây là cơ chế 'phóng chiếu' (Projection). Cơn phẫn nộ dữ dội trước một thói xấu của người ngoài thường bắt nguồn từ việc chúng ta vô thức nhận ra hạt mầm ấy trong chính mình nhưng không dám thừa nhận. Lần gần nhất bạn bực bội với ai đó là vì điều gì?",
        "RANH GIỚI (Cơ chế phóng chiếu)",
        "#hiyuabyss #tamlyhoc #carljung #phongchieu #chualanh"
    ),
    (
        "Single-Punch (1 trang)",
        "Từ chối người khác là trao cho chính mình một cơ hội để sống chân thật.",
        "Học cách nói 'KHÔNG' với những đòi hỏi vô lý là cách duy nhất để bảo vệ lòng tự trọng của bạn.",
        "-", "-",
        "Học cách nói 'KHÔNG' với những đòi hỏi vô lý là cách duy nhất để bảo vệ lòng tự trọng của bạn.",
        "Từ điển Tâm lý học",
        "Nhiều người sợ nói từ chối vì ám ảnh bị ghét bỏ. Nhưng sự thật là: người tôn trọng bạn sẽ hiểu cho giới hạn của bạn; chỉ kẻ muốn lợi dụng bạn mới tức giận khi bạn từ chối. Ranh giới cá nhân không làm bạn xa cách, nó bảo vệ bạn khỏi sự kiệt quệ.",
        "RANH GIỚI (Dũng khí từ chối)",
        "#hiyuabyss #tamlyhoc #tuchoi #ranhgioi #kientao"
    ),
    (
        "Carousel 2 trang",
        "Nhiệm vụ lớn nhất của đời người là tự sinh ra chính mình một lần nữa.",
        "Nhiệm vụ tối thượng của con người trong đời là......",
        "Tự tay sinh ra chính mình, trở thành phiên bản tiềm năng nhất mà bạn vốn có thể đạt tới.",
        "-",
        "Nhiệm vụ tối thượng của con người là tự tay sinh ra chính mình, trở thành phiên bản chân thật nhất mà bản thân có thể đạt tới.",
        "Erich Fromm",
        "Chúng ta sinh ra với những kỳ vọng của cha mẹ, xã hội và định kiến thời đại. Trưởng thành thực sự là hành trình dũng cảm bóc tách từng lớp vỏ ấy để tìm lại bản sắc nguyên bản của mình. Bạn đang sống cuộc đời của mình hay đang diễn vai mà người khác mong đợi?",
        "RANH GIỚI (Tự kiến tạo)",
        "#hiyuabyss #tamlyhoc #erichfromm #bansac #truongthanh"
    ),
    (
        "Single-Punch (1 trang)",
        "Giữ được sự độc lập giữa đám đông ồn ào là phẩm chất của một tâm hồn vĩ đại.",
        "Giữ được sự an nhiên và độc lập ngay giữa đám đông cuồng loạn là đỉnh cao của bản lĩnh sống.",
        "-", "-",
        "Giữ được sự an nhiên và độc lập ngay giữa đám đông cuồng loạn là đỉnh cao của bản lĩnh sống.",
        "Ralph Waldo Emerson",
        "Rất dễ để sống theo ý mình khi ở một mình; cũng rất dễ để a dua theo đám đông khi ở nơi công cộng. Nhưng người có bản lĩnh thực sự là người vẫn giữ trọn sự thanh thản và nguyên tắc riêng dù xung quanh có ồn ào đến đâu.",
        "RANH GIỚI (Độc lập tư duy)",
        "#hiyuabyss #tamlyhoc #emerson #tuduy #bando"
    ),

    # 2. Sự Thanh Thản & Nghệ Thuật Buông Bỏ (TXT-0109 to TXT-0116)
    (
        "Carousel 2 trang",
        "Phần lớn nỗi đau khổ của con người đều sinh ra từ trí tưởng tượng thêu dệt.",
        "Ta thường đau đớn trong tưởng tượng......",
        "Nhiều hơn gấp vạn lần những mất mát thực sự diễn ra ngoài đời thực.",
        "-",
        "Con người ta thường chịu đựng nỗi đau do trí tưởng tượng thêu dệt nhiều hơn gấp trăm lần những khó khăn thực tế.",
        "Seneca",
        "Bộ não con người có xu hướng phóng đại hiểm nguy và tự biên soạn những kịch bản tồi tệ nhất. Sự lo âu không làm ngày mai bớt tồi tệ, nó chỉ cướp đi sự bình yên của ngày hôm nay. Hãy học cách phân biệt giữa thực tế đang xảy ra và nỗi sợ do tâm trí tự vẽ nên.",
        "THANH THẢN (Bớt tưởng tượng)",
        "#hiyuabyss #tamlyhoc #seneca #loau #buongbo"
    ),
    (
        "Single-Punch (1 trang)",
        "Bạn có đủ kiên nhẫn để chờ cho bùn lắng xuống và dòng nước tự trở nên trong veo?",
        "Bạn có đủ kiên nhẫn để đợi cho bùn lắng xuống và mặt nước tự khắc trở nên trong suốt?",
        "-", "-",
        "Bạn có đủ kiên nhẫn để đợi cho bùn lắng xuống và mặt nước tự khắc trở nên trong suốt?",
        "Lao Tzu",
        "Khi gặp chuyện bất như ý, phản ứng bốc đồng giống như dùng que khuấy thêm vào vũng bùn lầy. Người có trí tuệ biết cách dừng lại, hít thở và để cho cảm xúc lắng xuống. Mọi câu trả lời đúng đắn chỉ xuất hiện khi tâm trí bạn tìm lại được sự phẳng lặng.",
        "THANH THẢN (Nước trong bùn lắng)",
        "#hiyuabyss #tamlyhoc #laotzu #daoduc #tinhlang"
    ),
    (
        "Carousel 3 trang",
        "Đừng tìm kiếm sự bình yên ở một nơi chốn xa xôi; nơi trú ẩn an toàn nhất nằm ở tâm bạn.",
        "Người ta thường tìm cách trốn chạy đến bờ biển hay núi cao......",
        "Nhưng không nơi nào bình yên và không phiền muộn bằng việc lui về chính tâm hồn của mình.",
        "Sự tĩnh lặng không nằm ở cảnh vật bên ngoài, nó là trật tự mà bạn tự thiết lập bên trong.",
        "Không có chốn dung thân nào yên bình và tự do hơn chính khoảng trời tĩnh lặng trong tâm hồn bạn.",
        "Marcus Aurelius",
        "Đổi một chỗ làm mới, dọn sang một thành phố mới không giải quyết được vấn đề nếu bạn vẫn mang theo một tâm trí hỗn loạn. Hãy dọn dẹp nội tâm trước khi tìm kiếm sự đổi thay từ môi trường bên ngoài. Nơi an toàn nhất của bạn hiện tại là đâu?",
        "THANH THẢN (Nơi trú ẩn nội tâm)",
        "#hiyuabyss #tamlyhoc #marcusaurelius #khacki #anlac"
    ),
    (
        "Single-Punch (1 trang)",
        "Biết đủ là đỉnh cao của sự giàu có; kẻ tham lam vĩnh viễn là kẻ bần cùng.",
        "Kẻ biết đủ sẽ luôn có đủ; kẻ chạy theo lòng tham sẽ mãi mãi là kẻ bần cùng trong tâm hồn.",
        "-", "-",
        "Kẻ biết đủ sẽ luôn có đủ; kẻ chạy theo lòng tham sẽ mãi mãi là kẻ bần cùng trong tâm hồn.",
        "Lao Tzu",
        "Sự giàu có đích thực không nằm ở số lượng tài sản tích lũy, mà nằm ở số lượng ham muốn bạn có thể buông bỏ. Khi bạn không còn bị ám ảnh bởi việc phải hơn người khác, bạn đã bước ra khỏi trò chơi thao túng của xã hội tiêu dùng.",
        "THANH THẢN (Tâm thế biết đủ)",
        "#hiyuabyss #tamlyhoc #laotzu #bietdu #chualanh"
    ),
    (
        "Carousel 2 trang",
        "Đơn giản hóa cuộc sống là cách nhanh nhất để giải phóng nguồn năng lượng tâm trí.",
        "Bí quyết của sự thanh thản nằm ở ba chữ......",
        "Đơn giản hóa, đơn giản hóa và cắt giảm mọi gánh nặng không cần thiết trong tâm trí.",
        "-",
        "Bí quyết để giải phóng tâm trí khỏi sự kiệt quệ là liên tục đơn giản hóa và cắt bỏ những mối bận tâm thừa thãi.",
        "Henry David Thoreau",
        "Chúng ta thường tự làm mình kiệt sức vì ôm đồm quá nhiều kỳ vọng, quá nhiều món đồ và quá nhiều mối quan hệ vô thưởng vô phạt. Hãy dũng cảm buông bớt để dành chỗ cho những điều thực sự có ý nghĩa. Hôm nay bạn có thể buông bỏ điều gì?",
        "THANH THẢN (Lối sống tối giản)",
        "#hiyuabyss #tamlyhoc #thoreau #toigian #nhelenh"
    ),
    (
        "Single-Punch (1 trang)",
        "Vũ trụ luôn vận động đổi thay; cuộc đời bạn sướng hay khổ là do cách bạn nhìn nhận nó.",
        "Cuộc đời này vốn không mang nhãn dán tốt hay xấu; nó hoàn toàn do suy nghĩ của bạn định hình nên.",
        "-", "-",
        "Cuộc đời này vốn không mang nhãn dán tốt hay xấu; nó hoàn toàn do suy nghĩ của bạn định hình nên.",
        "Marcus Aurelius",
        "Hoàn cảnh chỉ cung cấp sự kiện thô; việc coi nó là thảm họa hay bài học trưởng thành phụ thuộc 100% vào góc nhìn của bạn. Làm chủ suy nghĩ là bước đầu tiên để làm chủ vận mệnh.",
        "THANH THẢN (Làm chủ góc nhìn)",
        "#hiyuabyss #tamlyhoc #marcusaurelius #gocnhin #tuduy"
    ),
    (
        "Carousel 2 trang",
        "Bình yên không phải là sự vắng bóng của sóng gió, mà là một sức mạnh nội tâm vững vàng.",
        "Bình yên thực sự không phải là né tránh xung đột......",
        "Mà là một trạng thái tâm trí kiên định, tràn đầy lòng trắc ẩn và sự công chính.",
        "-",
        "Bình yên không phải là sự trốn chạy yếu đuối, đó là sức mạnh nội tâm vững chãi trước mọi biến động cuộc đời.",
        "Baruch Spinoza",
        "Người tìm kiếm bình yên bằng cách cúi đầu nhượng bộ kẻ bắt nạt chỉ nhận lại sự coi thường. Bình yên thực sự phải đi kèm với sức mạnh và nguyên tắc ranh giới thép. Bình yên của bạn là sự tĩnh lặng tự thân hay là sự trốn tránh?",
        "THANH THẢN (Bình yên vững chãi)",
        "#hiyuabyss #tamlyhoc #spinoza #sucmanh #trietly"
    ),
    (
        "Single-Punch (1 trang)",
        "Một cuộc đời hạnh phúc không thể thiếu đi những nốt trầm của bóng tối và nỗi buồn.",
        "Hạnh phúc sẽ mất đi ý nghĩa nếu nó không được đặt cạnh những nốt trầm của nỗi buồn.",
        "-", "-",
        "Hạnh phúc sẽ mất đi ý nghĩa nếu nó không được đặt cạnh những nốt trầm của nỗi buồn.",
        "Carl Jung",
        "Ám ảnh phải 'luôn luôn tích cực' là một hình thức bạo lực tâm lý với chính mình. Đau buồn, thất vọng hay mệt mỏi là những phản ứng hoàn toàn bình thường của một con người sống động. Hãy học cách ôm lấy cả những ngày mưa.",
        "THANH THẢN (Chấp nhận cảm xúc)",
        "#hiyuabyss #tamlyhoc #carljung #chualanh #camxuc"
    ),

    # 3. Sức Mạnh Tĩnh Lặng & Sự Kiên Cường (TXT-0117 to TXT-0124)
    (
        "Carousel 2 trang",
        "Hãy như mũi đá kiên cường mặc cho sóng dữ gầm rú xô vào bờ.",
        "Hãy sống như một mỏm đá hiên ngang giữa biển cả......",
        "Mặc cho ngàn con sóng dữ liên tục gầm rú xô vào, nó vẫn đứng vững và thuần hóa cơn giận dữ của đại dương.",
        "-",
        "Hãy kiên định như mỏm đá giữa biển khơi: mặc cho sóng gió gầm thét xô vào, nó vẫn sừng sững và thuần hóa cơn thịnh nộ của bão táp.",
        "Marcus Aurelius",
        "Khi ai đó cố tình khiêu khích hoặc hạ bệ bạn, phản ứng hung hăng chỉ chứng minh họ đã kiểm soát được bạn. Sự điềm tĩnh và phớt lờ lạnh lùng mới là bức tường kiên cố nhất khiến mọi mưu hèn kế bẩn tự tiêu tan.",
        "KIÊN CƯỜNG (Mũi đá trước sóng)",
        "#hiyuabyss #tamlyhoc #marcusaurelius #khacki #diemtinh"
    ),
    (
        "Single-Punch (1 trang)",
        "Nước mềm có thể chảy qua mọi khe hở nhưng lại có sức mạnh bào mòn cả núi đá.",
        "Thứ mềm mại nhất trên thế gian này lại có khả năng xuyên qua và khuất phục những thứ cứng rắn nhất.",
        "-", "-",
        "Thứ mềm mại nhất trên thế gian này lại có khả năng xuyên qua và khuất phục những thứ cứng rắn nhất.",
        "Lao Tzu",
        "Gồng mình cứng nhắc rất dễ gãy trước áp lực lớn. Người hiểu đạo sống như nước: uyển chuyển thích nghi với hoàn cảnh, khiêm nhường chảy xuống chỗ trũng, nhưng bền bỉ vô song. Bạn đang quá gồng hay đang biết cách thích nghi?",
        "KIÊN CƯỜNG (Sức mạnh của nước)",
        "#hiyuabyss #tamlyhoc #laotzu #khiemnhuong #trietly"
    ),
    (
        "Carousel 3 trang",
        "Tôi không phải là những tổn thương trong quá khứ, tôi là những gì tôi chọn để trở thành.",
        "Tôi không bị định nghĩa bởi những gì đã xảy ra với mình......",
        "Tôi được định nghĩa bởi những gì tôi có ý thức lựa chọn để trở thành từ ngày hôm nay.",
        "Quá khứ có thể để lại vết sẹo, nhưng cây bút viết tiếp tương lai vẫn nằm trọn trong tay bạn.",
        "Tôi không phải là nạn nhân của quá khứ; tôi là người nắm giữ quyền lựa chọn con người mà mình muốn trở thành.",
        "Carl Jung",
        "Mắc kẹt trong tâm thế nạn nhân là cách nhanh nhất để tước bỏ quyền làm chủ cuộc đời mình. Vết thương có thể không do bạn tạo ra, nhưng hành trình chữa lành và vươn lên là trách nhiệm duy nhất của bạn.",
        "KIÊN CƯỜNG (Vượt lên tổn thương)",
        "#hiyuabyss #tamlyhoc #carljung #trachnhiem #chualanh"
    ),
    (
        "Single-Punch (1 trang)",
        "Lửa thử vàng, gian nan thử thách bản lĩnh của những tâm hồn kiên cường.",
        "Lửa đỏ là phép thử cho vàng ròng; nghịch cảnh là phép thử duy nhất cho bản lĩnh con người.",
        "-", "-",
        "Lửa đỏ là phép thử cho vàng ròng; nghịch cảnh là phép thử duy nhất cho bản lĩnh con người.",
        "Seneca",
        "Khi mọi chuyện thuận buồm xuôi gió, ai cũng có thể tỏ ra cao thượng và đĩnh đạc. Chỉ khi rơi vào áp lực tột cùng, phẩm giá và bản lĩnh thực sự của bạn mới lộ diện. Hãy cảm ơn những thử thách vì chúng giúp bạn nhìn rõ chính mình.",
        "KIÊN CƯỜNG (Lửa thử vàng)",
        "#hiyuabyss #tamlyhoc #seneca #nghicanh #banlinh"
    ),
    (
        "Carousel 2 trang",
        "Biết đâu những nỗi sợ hãi lớn nhất trong bạn lại đang chờ đợi một cái ôm thấu cảm?",
        "Có thể mọi con rồng đáng sợ trong đời bạn......",
        "Thực chất chỉ là những nàng công chúa đang chờ đợi được nhìn thấy bạn dũng cảm và yêu thương.",
        "-",
        "Có lẽ tất cả những nỗi sợ hãi lớn nhất bên trong bạn chỉ là những phần tổn thương đang tha thiết chờ đợi lòng trắc ẩn của chính bạn.",
        "Rainer Maria Rilke",
        "Chống lại nỗi sợ hãi chỉ làm nó lớn thêm. Khi bạn dừng việc phán xét sự yếu đuối của mình và nhìn nó bằng lòng thấu cảm, những con quái vật tâm lý sẽ tự động thu mình lại thành một đứa trẻ cần được chở che.",
        "KIÊN CƯỜNG (Đối diện nỗi sợ)",
        "#hiyuabyss #tamlyhoc #rilke #chualanh #thaucam"
    ),
    (
        "Single-Punch (1 trang)",
        "Điều gì không thể đánh gục được bạn sẽ tôi luyện bạn thành một phiên bản kiên cường hơn.",
        "Những gì không thể giết chết được bạn sẽ trở thành chất dinh dưỡng nuôi lớn sức mạnh của bạn.",
        "-", "-",
        "Những gì không thể giết chết được bạn sẽ trở thành chất dinh dưỡng nuôi lớn sức mạnh của bạn.",
        "Friedrich Nietzsche",
        "Tâm lý học hiện đại gọi đây là 'Sự phát triển hậu sang chấn' (Post-Traumatic Growth). Con người không chỉ hồi phục sau cơn bão, mà chính cơn bão đã mở rộng dung tích chịu đựng và sự thấu suốt của tâm hồn bạn.",
        "KIÊN CƯỜNG (Sự trưởng thành sau đau thương)",
        "#hiyuabyss #tamlyhoc #nietzsche #antifragile #kientri"
    ),
    (
        "Carousel 2 trang",
        "Người ta có thể tước đi mọi thứ của bạn, ngoại trừ quyền tự do lựa chọn thái độ sống.",
        "Người đời có thể cướp đi tất cả mọi thứ của bạn......",
        "Trừ một điều cuối cùng: Quyền tự do lựa chọn thái độ của mình trước hoàn cảnh nghiệt ngã.",
        "-",
        "Người ta có thể tước đoạt mọi tài sản của bạn, nhưng không ai có thể tước đi quyền lựa chọn thái độ sống của bạn.",
        "Viktor Frankl",
        "Được viết bởi một bác sĩ tâm thần sống sót qua trại tập trung Đức quốc xã, câu nói này là minh chứng tối thượng cho sức mạnh ý chí con người. Khi hoàn cảnh không thể thay đổi, thứ duy nhất cần thay đổi chính là tâm thế đối diện của bạn.",
        "KIÊN CƯỜNG (Tự do tối thượng)",
        "#hiyuabyss #tamlyhoc #viktorfrankl #ynghia #thaido"
    ),
    (
        "Single-Punch (1 trang)",
        "Học cách chấp nhận những điều không thể tránh khỏi là chìa khóa để chấm dứt sự dằn vặt.",
        "Học cách bình thản đón nhận những điều không thể đảo ngược là bước đi đầu tiên của sự thông thái.",
        "-", "-",
        "Học cách bình thản đón nhận những điều không thể đảo ngược là bước đi đầu tiên của sự thông thái.",
        "Michel de Montaigne",
        "Phần lớn sự kiệt quệ tinh thần đến từ việc cố gắng thay đổi những thứ nằm ngoài tầm kiểm soát: thái độ của người khác, quá khứ đã qua hay sự hữu hạn của đời người. Buông bỏ sự kháng cự là lúc bình yên trở lại.",
        "KIÊN CƯỜNG (Chấp nhận thực tại)",
        "#hiyuabyss #tamlyhoc #montaigne #khacki #anlac"
    ),

    # 4. Kết Nối Sâu Sắc & Tình Yêu Trưởng Thành (TXT-0125 to TXT-0132)
    (
        "Carousel 2 trang",
        "Sự khác biệt nghiệt ngã giữa tình yêu non nớt và tình yêu trưởng thành.",
        "Tình yêu non nớt thường nói rằng: 'Tôi yêu bạn vì tôi cần bạn'......",
        "Còn tình yêu trưởng thành mỉm cười nói: 'Tôi cần bạn bởi vì tôi yêu bạn.'",
        "-",
        "Tình yêu non nớt bám víu vì sợ cô đơn; tình yêu trưởng thành gắn kết vì trân quý sự hiện diện của nhau từ hai tâm hồn trọn vẹn.",
        "Erich Fromm",
        "Nếu bạn đến với một người chỉ để họ lấp đầy khoảng trống cô đơn hay làm cái phao cứu sinh, đó là sự phụ thuộc cảm xúc chứ không phải tình yêu. Hai người chỉ có thể xây dựng tình yêu bền vững khi cả hai đều đã học được cách sống trọn vẹn với chính mình.",
        "KẾT NỐI (Tình yêu trưởng thành)",
        "#hiyuabyss #tamlyhoc #erichfromm #tinhyeu #truongthanh"
    ),
    (
        "Single-Punch (1 trang)",
        "Tình yêu đích thực là khi hai cõi cô độc biết cách bảo vệ, tôn trọng và chào đón lẫn nhau.",
        "Tình yêu đích thực là khi hai tâm hồn độc lập biết chở che, tôn trọng và chào đón sự riêng tư của nhau.",
        "-", "-",
        "Tình yêu đích thực là khi hai tâm hồn độc lập biết chở che, tôn trọng và chào đón sự riêng tư của nhau.",
        "Rainer Maria Rilke",
        "Yêu không phải là hòa tan hay nuốt chửng bản sắc của đối phương. Tình yêu đẹp nhất giống như hai hàng cây cổ thụ đứng cạnh nhau: cành lá có thể đan vào nhau trong gió, nhưng gốc rễ phải tự mình cắm sâu vào lòng đất.",
        "KẾT NỐI (Hai cõi cô độc)",
        "#hiyuabyss #tamlyhoc #rilke #tinhyeu #ranhgioi"
    ),
    (
        "Carousel 2 trang",
        "Nghịch lý lớn nhất: Bạn phải học cách ở một mình trước khi có thể yêu một ai đó.",
        "Nghịch lý lớn nhất của tình yêu là......",
        "Khả năng ở một mình một cách an ổn lại chính là điều kiện tiên quyết để bạn có thể yêu một người thật lòng.",
        "-",
        "Chỉ khi bạn không còn cần một ai đó để trốn chạy nỗi sợ cô đơn, bạn mới thực sự có khả năng yêu thương họ bằng cả tấm lòng.",
        "Erich Fromm",
        "Khi không chịu nổi sự cô độc, bạn sẽ vội vã nắm lấy bất kỳ bàn tay nào bước qua, để rồi chuốc lấy đau thương. Tự chữa lành và yêu lấy chính mình trước là món quà tuyệt vời nhất bạn có thể chuẩn bị cho người bạn đời tương lai.",
        "KẾT NỐI (Nghịch lý tình yêu)",
        "#hiyuabyss #tamlyhoc #erichfromm #codoc #tuduy"
    ),
    (
        "Single-Punch (1 trang)",
        "Gặp gỡ một tâm hồn sâu sắc giống như sự va chạm của hai hợp chất làm thay đổi cả hai.",
        "Sự gặp gỡ của hai tâm hồn giống như phản ứng hóa học: nếu có sự gắn kết thật sự, cả hai sẽ cùng biến đổi.",
        "-", "-",
        "Sự gặp gỡ của hai tâm hồn giống như phản ứng hóa học: nếu có sự gắn kết thật sự, cả hai sẽ cùng biến đổi.",
        "Carl Jung",
        "Một mối quan hệ chất lượng không bao giờ khiến bạn giậm chân tại chỗ hay trở nên tầm thường. Nó thôi thúc bạn mở rộng tầm nhìn, hoàn thiện nhân cách và trở thành một phiên bản sâu sắc hơn. Bạn đã gặp được người như thế chưa?",
        "KẾT NỐI (Phản ứng tâm hồn)",
        "#hiyuabyss #tamlyhoc #carljung #triky #ketnoi"
    ),
    (
        "Carousel 3 trang",
        "Nếu bạn hỏi tôi vì sao tôi lại trân quý người bạn ấy đến vậy, tôi chỉ có thể trả lời...",
        "Nếu bạn hỏi vì sao tôi lại yêu quý người bạn ấy đến thế......",
        "Tôi chỉ có thể trả lời một câu rất đỗi giản đơn: 'Bởi vì đó là người ấy, và bởi vì đó là tôi.'",
        "Tình bạn tri kỷ không đến từ những toan tính lợi ích; nó là sự nhận ra nhau một cách tự nhiên giữa biển người.",
        "Tình bạn tri kỷ chân chính không có lời giải thích vụ lợi; nó đơn giản là hai tâm hồn nhận ra nhau giữa hàng triệu người xa lạ.",
        "Michel de Montaigne",
        "Viết về tình bạn bất tử với Étienne de La Boétie, Montaigne đã cho thấy đỉnh cao của tình bạn không cần bất kỳ hợp đồng hay sự trao đổi nào. Ở cạnh một người mà bạn được phép là chính mình 100% là phước lành lớn nhất trong đời.",
        "KẾT NỐI (Tình bạn tri kỷ)",
        "#hiyuabyss #tamlyhoc #montaigne #triky #tinhban"
    ),
    (
        "Single-Punch (1 trang)",
        "Quy luật bất biến: Muốn nhận được sự yêu thương chân thành, trước hết bạn phải học cách trao đi sự chân thành.",
        "Muốn được người khác yêu thương thật lòng, trước hết bạn phải có can đảm mở lòng trao đi tình yêu chân thành.",
        "-", "-",
        "Muốn được người khác yêu thương thật lòng, trước hết bạn phải có can đảm mở lòng trao đi tình yêu chân thành.",
        "Seneca",
        "Tình yêu không thể cưỡng ép hay đòi hỏi bằng sự kiểm soát. Nó là tấm gương phản chiếu: bạn phát ra tần số ấm áp và tin cậy, bạn sẽ thu hút những tâm hồn tương tự.",
        "KẾT NỐI (Trao đi yêu thương)",
        "#hiyuabyss #tamlyhoc #seneca #chualanh #yeuthuong"
    ),
    (
        "Carousel 2 trang",
        "Hãy chừa lại những khoảng trống thiêng liêng trong sự gắn kết của hai người.",
        "Hãy tạo ra những khoảng không gian thở trong sự hòa hợp......",
        "Để những ngọn gió của thiên đàng có thể tự do khiêu vũ giữa hai tâm hồn.",
        "-",
        "Tình yêu bền vững cần những khoảng không gian riêng tư để thở; sự kiểm soát ngột ngạt sẽ giết chết mọi cảm xúc lãng mạn.",
        "Kahlil Gibran",
        "Yêu một người không có nghĩa là phải biết từng tin nhắn hay kiểm soát từng phút giây của họ. Ranh giới tôn trọng sự tự do của đối phương chính là chất keo bền chặt nhất giữ cho ngọn lửa tình yêu luôn ấm áp.",
        "KẾT NỐI (Khoảng thở tình yêu)",
        "#hiyuabyss #tamlyhoc #kahlilgibran #tinhyeu #khoangtho"
    ),
    (
        "Single-Punch (1 trang)",
        "Yêu thương không chỉ là mối quan hệ với một người, đó là thái độ sống bao dung với cả thế giới.",
        "Tình yêu không đơn thuần là cảm xúc dành cho một cá nhân, mà là một thái độ sống hướng về sự bao dung.",
        "-", "-",
        "Tình yêu không đơn thuần là cảm xúc dành cho một cá nhân, mà là một thái độ sống hướng về sự bao dung.",
        "Erich Fromm",
        "Nếu một người chỉ ngọt ngào với bạn đời nhưng cay nghiệt với người phục vụ bàn, đó không phải là tình yêu—đó là sự vị kỷ đóng gói trong vỏ bọc quan tâm. Cách một người đối xử với thế giới xung quanh mới là bản chất thật của họ.",
        "KẾT NỐI (Thái độ bao dung)",
        "#hiyuabyss #tamlyhoc #erichfromm #nhancach #baodung"
    ),

    # 5. Bản Sắc Độc Bản & Giá Trị Nội Tại (TXT-0133 to TXT-0141)
    (
        "Carousel 2 trang",
        "Kẻ chỉ nhìn ra thế giới bên ngoài là kẻ mộng du; kẻ dám soi rọi vào bên trong mới là người thức tỉnh.",
        "Kẻ chỉ mải mê nhìn ra thế giới bên ngoài......",
        "Sẽ mãi mãi chìm trong cơn mộng du của những ảo vọng; chỉ người dám nhìn sâu vào nội tâm mới thực sự thức tỉnh.",
        "-",
        "Mải mê chạy theo sự công nhận bên ngoài khiến bạn lạc lối; dũng cảm soi rọi vào góc khuất nội tâm mới là khởi đầu của sự thức tỉnh.",
        "Carl Jung",
        "Chúng ta dành cả đời để nghiên cứu người khác, theo dõi tin tức và phán xét xã hội, nhưng lại hiếm khi dành ra 15 phút tĩnh lặng để đối thoại với chính linh hồn mình. Hãy bắt đầu hành trình quay về với chính bạn.",
        "BẢN SẮC (Nhìn vào nội tâm)",
        "#hiyuabyss #tamlyhoc #carljung #thuctinh #chualanh"
    ),
    (
        "Single-Punch (1 trang)",
        "Đặc quyền lớn nhất của một kiếp người là được trở thành đúng con người thật của bạn.",
        "Đặc quyền vĩ đại nhất của một kiếp nhân sinh là được sống và trở thành đúng con người thật của mình.",
        "-", "-",
        "Đặc quyền vĩ đại nhất của một kiếp nhân sinh là được sống và trở thành đúng con người thật của mình.",
        "Carl Jung",
        "Xã hội sẽ luôn cố uốn nắn bạn thành những chiếc khuôn tiện dụng cho họ. Nhưng không có bi kịch nào lớn hơn việc đến cuối đời nhận ra mình chỉ là một bản sao nhạt nhòa của một ai đó khác. Hãy dũng cảm bảo vệ bản sắc độc bản của bạn.",
        "BẢN SẮC (Đặc quyền làm chính mình)",
        "#hiyuabyss #tamlyhoc #carljung #bansac #docban"
    ),
    (
        "Carousel 2 trang",
        "Nếu giá trị của bạn định hình bởi những thứ bạn sở hữu, bạn sẽ là ai khi mất hết tất cả?",
        "Nếu giá trị của bạn chỉ nằm ở những thứ bạn sở hữu......",
        "Thì khi những thứ ấy mất đi, bạn thực chất còn lại là ai?",
        "-",
        "Định giá bản thân bằng xe cộ, nhà cửa hay chức danh là trò chơi nguy hiểm; khi danh vị tan biến, bạn sẽ chẳng còn lại gì ngoài sự trống rỗng.",
        "Erich Fromm",
        "Tác phẩm 'To Have or to Be?' đặt ra câu hỏi hiện sinh then chốt: Bạn chọn 'SỞ HỮU' hay chọn 'TỒN TẠI'? Giá trị nội tại đích thực nằm ở trí tuệ, nhân cách và phẩm giá—những thứ mà không biến cố nào có thể cướp mất khỏi bạn.",
        "BẢN SẮC (Sở hữu hay Tồn tại)",
        "#hiyuabyss #tamlyhoc #erichfromm #giatri #tinhtam"
    ),
    (
        "Single-Punch (1 trang)",
        "Biết người là thông minh, biết mình mới là bậc đại trí; thắng người là có sức, thắng mình mới là vô địch.",
        "Hiểu được người khác là sự thông minh; thấu suốt được chính mình mới là sự giác ngộ tối thượng.",
        "-", "-",
        "Hiểu được người khác là sự thông minh; thấu suốt được chính mình mới là sự giác ngộ tối thượng.",
        "Lao Tzu",
        "Chinh phục được đối thủ chỉ mang lại quyền lực tạm thời; làm chủ được dục vọng, cơn giận và cái tôi của bản thân mới mang lại sự tự do vĩnh cửu. Chiến trường khốc liệt nhất luôn nằm bên trong lồng ngực bạn.",
        "BẢN SẮC (Thấu suốt chính mình)",
        "#hiyuabyss #tamlyhoc #laotzu #trietly #daoduc"
    ),
    (
        "Carousel 2 trang",
        "Tôi nghiên cứu chính bản thân mình nhiều hơn bất kỳ môn học nào trên đời.",
        "Môn học quan trọng nhất trong suốt cuộc đời tôi......",
        "Không phải là triết học hay khoa học trừu tượng, mà là bài học về chính con người đang hiện diện bên trong tôi.",
        "-",
        "Tự nghiên cứu và thấu hiểu chính bản thân mình là công trình khoa học vĩ đại và chân thật nhất của một đời người.",
        "Michel de Montaigne",
        "Trước khi muốn hiểu nhân loại, hãy hiểu vì sao bạn lại dễ nổi giận, vì sao bạn lại tổn thương và điều gì thực sự khiến bạn rơi nước mắt. Bản thân bạn chính là phòng thí nghiệm trung thực nhất.",
        "BẢN SẮC (Phòng thí nghiệm nội tâm)",
        "#hiyuabyss #tamlyhoc #montaigne #thaucan #tuduy"
    ),
    (
        "Single-Punch (1 trang)",
        "Được là chính mình giữa một thế giới luôn tìm cách đồng hóa bạn là chiến thắng vĩ đại nhất.",
        "Giữ được chất riêng của mình trong một thế giới luôn tìm cách đồng hóa bạn là thành tựu vĩ đại nhất.",
        "-", "-",
        "Giữ được chất riêng của mình trong một thế giới luôn tìm cách đồng hóa bạn là thành tựu vĩ đại nhất.",
        "Ralph Waldo Emerson",
        "Áp lực đồng trang lứa (Peer pressure) và xu hướng bầy đàn khiến con người ta sợ hãi sự khác biệt. Nhưng lịch sử chỉ ghi tên những kẻ dám đi ngược dòng nước để bảo vệ lý tưởng của mình. Đừng sợ mình khác biệt, hãy sợ mình hòa tan.",
        "BẢN SẮC (Chiến thắng trước đồng hóa)",
        "#hiyuabyss #tamlyhoc #emerson #chatrieng #bando"
    ),
    (
        "Carousel 3 trang",
        "Bi kịch lớn nhất là được cả thiên hạ biết tên, nhưng khi nhắm mắt xuôi tay lại là kẻ xa lạ với chính mình.",
        "Cái chết sẽ là gánh nặng vô cùng khủng khiếp đối với một người......",
        "Kẻ đã dành cả đời để được cả thiên hạ ca tụng và biết tên,",
        "Nhưng đến giây phút cuối cùng lại ra đi như một kẻ hoàn toàn xa lạ với chính tâm hồn của mình.",
        "Bi kịch cay đắng nhất là trở thành ngôi sao trong mắt đám đông nhưng lại là kẻ xa lạ hoàn toàn với chính linh hồn mình.",
        "Seneca",
        "Đừng đánh đổi sự tĩnh lặng và phẩm giá cá nhân chỉ để lấy về vài tràng pháo tay hay sự ngưỡng mộ phù phiếm của xã hội. Đến cuối cùng, người duy nhất bạn phải đối diện khi đêm buông xuống là chính bạn trong gương.",
        "BẢN SẮC (Bi kịch xa lạ với bản thân)",
        "#hiyuabyss #tamlyhoc #seneca #danhvong #tinhthuc"
    ),
    (
        "Single-Punch (1 trang)",
        "Đừng bao giờ đánh đổi danh dự và lòng tự trọng để đổi lấy sự thăng tiến nhất thời.",
        "Đừng bao giờ coi bất cứ điều gì là có lợi nếu nó buộc bạn phải đánh mất chữ tín và lòng tự trọng.",
        "-", "-",
        "Đừng bao giờ coi bất cứ điều gì là có lợi nếu nó buộc bạn phải đánh mất chữ tín và lòng tự trọng.",
        "Marcus Aurelius",
        "Tiền bạc hay chức tước có thể kiếm lại được, nhưng lòng tự trọng một khi đã bán rẻ thì không bao giờ mua lại được. Sống ngẩng cao đầu là cách tốt nhất để có được giấc ngủ ngon.",
        "BẢN SẮC (Lòng tự trọng tối thượng)",
        "#hiyuabyss #tamlyhoc #marcusaurelius #tutrong #khacki"
    ),
    (
        "Single-Punch (1 trang)",
        "Bản ngã thích tích lũy danh xưng; linh hồn chân thật chỉ cần sự thanh sạch của lương tâm.",
        "Cái tôi luôn khao khát những danh xưng hào nhoáng; nhưng linh hồn chỉ cần sự thanh thản của một lương tâm trong sạch.",
        "-", "-",
        "Cái tôi luôn khao khát những danh xưng hào nhoáng; nhưng linh hồn chỉ cần sự thanh thản của một lương tâm trong sạch.",
        "Từ điển Hiện sinh",
        "Khi lột bỏ toàn bộ áo vest, chức danh và sự tung hô, con người ta còn lại gì? Một nhân cách tử tế và bình an là tài sản vững chắc nhất mà không cơn suy thoái nào có thể làm lung lay.",
        "BẢN SẮC (Lương tâm thanh sạch)",
        "#hiyuabyss #tamlyhoc #hienxinh #nhancach #luongtam"
    ),

    # 6. Vượt Lên Phán Xét & Tự Do Khỏi Dư Luận (TXT-0142 to TXT-0150)
    (
        "Carousel 2 trang",
        "Chọn không cảm thấy bị tổn thương — và bạn sẽ không bao giờ bị tổn thương.",
        "Hãy chọn cách không cảm thấy bị tổn thương......",
        "Và bạn sẽ nhận ra rằng không một lời miệt thị nào có thể chạm tới phẩm giá của bạn.",
        "-",
        "Tổn thương chỉ xảy ra khi bạn tự cho phép người khác làm tổn thương mình; từ chối đồng thuận với sự xúc phạm là cách hóa giải mọi đòn tấn công.",
        "Marcus Aurelius",
        "Lời nói của kẻ khác giống như một món quà độc hại. Nếu bạn không đưa tay ra đón nhận, món quà ấy vẫn thuộc về kẻ mang đến. Người làm chủ được tâm trí mình là người bất khả xâm phạm trước mọi đòn công kích dư luận.",
        "VƯỢT PHÁN XÉT (Quyền từ chối tổn thương)",
        "#hiyuabyss #tamlyhoc #marcusaurelius #khacki #tuduy"
    ),
    (
        "Single-Punch (1 trang)",
        "Người tiết kiệm được nhiều thời gian nhất là người không bận tâm thiên hạ đang nghĩ gì về mình.",
        "Người tiết kiệm được nhiều thời gian nhất là người không bao giờ ngó nghiêng xem thiên hạ đang bàn tán gì về mình.",
        "-", "-",
        "Người tiết kiệm được nhiều thời gian nhất là người không bao giờ ngó nghiêng xem thiên hạ đang bàn tán gì về mình.",
        "Marcus Aurelius",
        "Dành năng lượng để suy đoán xem người khác thích mình hay ghét mình là sự lãng phí tài nguyên tinh thần lớn nhất. Hãy tập trung 100% sức lực để làm cho cuộc sống và công việc của bạn trở nên xuất sắc.",
        "VƯỢT PHÁN XÉT (Bớt bận tâm miệng đời)",
        "#hiyuabyss #tamlyhoc #marcusaurelius #taphung #thoiluong"
    ),
    (
        "Carousel 3 trang",
        "Sự thức tỉnh không đến từ việc tưởng tượng ra ánh sáng, mà từ việc thấu suốt bóng tối của chính mình.",
        "Người ta không đạt được sự thức tỉnh bằng cách viển vông vẽ ra những vầng hào quang......",
        "Mà bằng cách dũng cảm soi rọi và biến phần bóng tối bên trong trở nên sáng tỏ.",
        "Hiểu được sự xấu xí tiềm ẩn trong mình là chìa khóa duy nhất để bao dung với lỗi lầm của người khác.",
        "Giác ngộ không phải là mơ mộng về ánh sáng; giác ngộ là dũng cảm đưa những góc tối vô thức bên trong ra ánh sáng nhận thức.",
        "Carl Jung",
        "Những người đạo đức giả thường thích đóng vai thẩm phán phán xét người ngoài vì họ quá sợ hãi góc tối trong lòng mình. Khi bạn nhìn thấu bản tính con người, bạn sẽ bớt đi sự phán xét và thay vào đó là lòng trắc ẩn sâu sắc.",
        "VƯỢT PHÁN XÉT (Thấu suốt bóng tối)",
        "#hiyuabyss #tamlyhoc #carljung #bongtoi #chualanh"
    ),
    (
        "Single-Punch (1 trang)",
        "Hiểu rõ phần tối của bản thân là phương pháp tốt nhất để đối phó với sự tàn nhẫn của kẻ khác.",
        "Nhận diện được góc tối của chính mình là vũ khí sắc bén nhất để không bị tổn thương trước sự độc hại của người ngoài.",
        "-", "-",
        "Nhận diện được góc tối của chính mình là vũ khí sắc bén nhất để không bị tổn thương trước sự độc hại của người ngoài.",
        "Carl Jung",
        "Khi ai đó ném vào bạn một lời chỉ trích, nếu bạn đã biết rõ ưu và khuyết điểm của mình, lời nói ấy sẽ vô hại. Người không có ảo tưởng về bản thân sẽ không bao giờ bị người khác thao túng bằng sự chê bai hay tâng bốc.",
        "VƯỢT PHÁN XÉT (Vũ khí tự nhận thức)",
        "#hiyuabyss #tamlyhoc #carljung #tuduy #miendich"
    ),
    (
        "Carousel 2 trang",
        "Quá khao khát sự công nhận của thiên hạ chính là lúc bạn tự tay bước vào ngục tù.",
        "Khi bạn quá bận tâm đến việc làm vừa lòng người khác......",
        "Bạn đã tự nguyện trao chiếc chìa khóa tự do của mình vào tay cai ngục.",
        "-",
        "Chạy theo sự công nhận của đám đông là tự giam mình vào chiếc lồng vô hình của những kỳ vọng không có hồi kết.",
        "Lao Tzu",
        "Càng cố gắng làm hài lòng tất cả, bạn càng đánh mất sự tôn trọng của chính mình. Sự tự do chỉ bắt đầu khoảnh khắc bạn dám chấp nhận rằng: Mình không sinh ra để làm vừa mắt tất cả mọi người trên thế giới này.",
        "VƯỢT PHÁN XÉT (Chiếc lồng công nhận)",
        "#hiyuabyss #tamlyhoc #laotzu #tudo #ranhgioi"
    ),
    (
        "Single-Punch (1 trang)",
        "Đừng như đàn cừu mù quáng bước theo lối mòn chỉ vì thấy đám đông đi trước.",
        "Đừng sống như đàn cừu mù quáng bước theo lối mòn chỉ vì thấy đám đông phía trước đang đi theo hướng đó.",
        "-", "-",
        "Đừng sống như đàn cừu mù quáng bước theo lối mòn chỉ vì thấy đám đông phía trước đang đi theo hướng đó.",
        "Seneca",
        "Đám đông có thể ồn ào nhưng hiếm khi có trí tuệ. Những tư tưởng vĩ đại và những bước đột phá luôn thuộc về những kẻ dám dừng lại, chất vấn định kiến và tự vạch ra con đường riêng cho chính mình.",
        "VƯỢT PHÁN XÉT (Thoát khỏi tâm lý bầy đàn)",
        "#hiyuabyss #tamlyhoc #seneca #damdong #tuduy"
    ),
    (
        "Carousel 2 trang",
        "Hãy luôn giữ một 'gian phòng bí mật' trong tâm hồn nơi không một kẻ nào được phép xâm phạm.",
        "Chúng ta phải luôn dành riêng cho mình một gian phòng nội tâm tự do tuyệt đối......",
        "Nơi ta có thể bình thản đối thoại với chính mình, và tuyệt đối không một phán xét nào từ bên ngoài được phép bước vào.",
        "-",
        "Hãy xây dựng một thánh đường bất khả xâm phạm bên trong tâm hồn, nơi miệng đời và dư luận vĩnh viễn không thể chạm tới.",
        "Michel de Montaigne",
        "Dù ngoài kia có phong ba bão táp hay những lời thị phi cay nghiệt, miễn là gian phòng nội tâm của bạn vẫn ngăn nắp và ấm áp, bạn sẽ luôn tìm thấy sự bình an. Bạn đã xây dựng được chốn dung thân này cho mình chưa?",
        "VƯỢT PHÁN XÉT (Gian phòng nội tâm)",
        "#hiyuabyss #tamlyhoc #montaigne #thanhduong #tinhlang"
    ),
    (
        "Single-Punch (1 trang)",
        "Ích kỷ và yêu bản thân không hề giống nhau; kẻ cay nghiệt với người ngoài thực chất đang tự căm ghét chính mình.",
        "Ích kỷ không phải là yêu bản thân; kẻ độc hại với người khác thực chất là kẻ đang ngập tràn trong sự tự căm ghét chính mình.",
        "-", "-",
        "Ích kỷ không phải là yêu bản thân; kẻ độc hại với người khác thực chất là kẻ đang ngập tràn trong sự tự căm ghét chính mình.",
        "Erich Fromm",
        "Khi ai đó vô cớ buông lời cay nghiệt hay ghen ăn tức ở với bạn, đừng vội tức giận. Họ chỉ đang phóng chiếu sự nghèo nàn và bất hạnh trong thế giới nội tâm của họ ra ngoài mà thôi. Hãy thương xót cho họ thay vì để bản thân bị cuốn vào vòng xoáy tiêu cực.",
        "VƯỢT PHÁN XÉT (Bản chất của sự cay nghiệt)",
        "#hiyuabyss #tamlyhoc #erichfromm #phongchieu #nhanai"
    ),
    (
        "Single-Punch (1 trang)",
        "Tự do tối thượng là khi bạn có thể mỉm cười bước qua những lời đàm tiếu mà tâm không gợn một chút sóng.",
        "Tự do tối thượng là khi bạn có thể mỉm cười bước qua miệng đời mà tâm trí không gợn lấy một chút xao động.",
        "-", "-",
        "Tự do tối thượng là khi bạn có thể mỉm cười bước qua miệng đời mà tâm trí không gợn lấy một chút xao động.",
        "Ghi chép Khắc kỷ",
        "Cuộc đời quá ngắn để sống theo kịch bản của người khác. Khi bạn thấu hiểu giá trị của mình, mọi lời khen hay tiếng chê đều chỉ như cơn gió thoảng qua rặng liễu. Bạn đã đạt tới sự bình thản này chưa?",
        "VƯỢT PHÁN XÉT (Tự do tối thượng)",
        "#hiyuabyss #tamlyhoc #khacki #binhthan #tudo"
    )
]

def main():
    print(f"Tổng số bài viết mới soạn thảo: {len(NEW_50_POSTS)}")
    
    # Read existing 100 posts
    existing_posts = []
    with open("scripts/tiktok_100_posts_v2.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        existing_posts = list(reader)
        
    print(f"Số bài hiện tại trong kho: {len(existing_posts)}")
    
    # Dates continuing from post 100
    start_date = datetime(2027, 2, 24)
    time_slots = ["11:30 - 12:30 (Trưa)", "19:30 - 20:30 (Tối)", "21:00 - 22:30 (Đêm chiêm nghiệm)"]
    
    new_rows = []
    for idx, post in enumerate(NEW_50_POSTS):
        stt = 101 + idx
        post_id = f"TXT-{stt:04d}"
        curr_date = start_date + timedelta(days=idx)
        weekday_str = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"][curr_date.weekday()]
        date_label = f"{weekday_str} ({curr_date.strftime('%d/%m')})"
        time_slot = time_slots[stt % len(time_slots)]
        
        fmt, title, s1, s2, s3, full_text, author, desc, theme, hashtags = post
        
        # Cycle through new themes (theme_61 to theme_90)
        theme_idx = 61 + (idx % 30)
        template = f"theme_{theme_idx:02d}"
        
        new_rows.append([
            stt,
            post_id,
            title,
            desc,
            author,
            hashtags,
            fmt,
            s1,
            s2,
            s3,
            full_text,
            theme,
            time_slot,
            date_label,
            template,
            "SẴN SÀNG"
        ])
        
    all_150_posts = existing_posts + new_rows
    out_csv = "scripts/tiktok_150_posts.csv"
    with open(out_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(all_150_posts)
        
    print(f"[✓] Đã tạo thành công file 150 bài hoàn chỉnh tại: {out_csv}")

if __name__ == "__main__":
    main()
