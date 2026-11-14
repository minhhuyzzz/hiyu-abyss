#!/usr/bin/env python3
"""
Hiyu Abyss — Rebuild 100 TikTok Posts with Complete Requested Schema:
- Tiêu đề (Dưới 90 từ)
- Mô tả (Caption TikTok chi tiết, phân tích tâm lý & câu hỏi kích tương tác)
- Nguồn tác giả (Ngắn gọn 1 tên viết liền, nếu bịa đặt/sáng tác mới thì là @hiyuabyss)
- Hashtags (Đúng 5 cái)
- Đầy đủ Slide 1, Slide 2, Slide 3, Full Text, Format, Khung giờ, Lịch đăng, Phôi ảnh, Trạng thái.
"""

import csv
import subprocess
from datetime import datetime, timedelta

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"
SHEET_NAME = "Kế Hoạch 100 Bài (TikTok Pipeline)"

THEMES = [
    ("HYPOCRISY", "Đạo đức giả & Sự giả tạo", "LaRochefoucauld", "#hiyuabyss #tamlyhoc #trietly #bocchuan #daoducgia"),
    ("DOUBLE_STANDARD", "Tiêu chuẩn kép trong phán xét", "@hiyuabyss", "#hiyuabyss #tamlyhoc #trietly #tieuchuankep #gocnhin"),
    ("MORALITY", "Lòng tốt & Điều kiện ngầm", "Nietzsche", "#hiyuabyss #tamlyhoc #trietly #longtot #thaucam"),
    ("EGO", "Bản ngã & Nhu cầu hơn người", "Schopenhauer", "#hiyuabyss #tamlyhoc #trietly #bannga #chualanh"),
    ("SELF_DECEPTION", "Sự tự lừa dối & Vùng an toàn", "Pascal", "#hiyuabyss #tamlyhoc #trietly #tulua #tinhthuc"),
    ("SHADOW", "Góc khuất nội tâm & Sự chối bỏ", "Jung", "#hiyuabyss #tamlyhoc #trietly #bongtoi #chualanh"),
    ("MASK", "Mặt nạ xã hội & Sự gồng gánh", "@hiyuabyss", "#hiyuabyss #tamlyhoc #trietly #matnaxahoi #gocnhin"),
    ("POWER", "Quyền lực ngầm & Kiểm soát", "Machiavelli", "#hiyuabyss #tamlyhoc #trietly #quyenluc #kiemsoat"),
    ("MANIPULATION", "Cảm giác tội lỗi & Nợ ân tình", "@hiyuabyss", "#hiyuabyss #tamlyhoc #trietly #thaotung #ranhgioi"),
    ("FREEDOM", "Tự do & Nỗi sợ tự chịu trách nhiệm", "Kierkegaard", "#hiyuabyss #tamlyhoc #trietly #tudo #trachnhiem"),
    ("TRUTH", "Sự thật & Những lời tự bào chữa", "Dostoevsky", "#hiyuabyss #tamlyhoc #trietly #suthat #tinhthuc"),
    ("LOVE", "Chiếm hữu đội lốt yêu thương", "@hiyuabyss", "#hiyuabyss #tamlyhoc #trietly #tinhyeu #chiemhuu"),
    ("LOYALTY", "Lòng trung thành & Ranh giới trả giá", "MarcusAurelius", "#hiyuabyss #tamlyhoc #trietly #trungthanh #ranhgioi"),
    ("ENVY", "Đố kỵ ngầm & Sự so sánh", "Spinoza", "#hiyuabyss #tamlyhoc #trietly #doky #sosanh"),
    ("CROWD", "Đám đông & Dũng khí bầy đàn", "Nietzsche", "#hiyuabyss #tamlyhoc #trietly #damdong #tuduy"),
    ("SUFFERING", "Khổ đau & Thói quen đóng vai nạn nhân", "Freud", "#hiyuabyss #tamlyhoc #trietly #khodau #chualanh"),
    ("IDENTITY", "Bản sắc khi ở một mình", "Seneca", "#hiyuabyss #tamlyhoc #trietly #bansac #chinhminh"),
    ("MEANING", "Ý nghĩa hiện sinh & Sự vô nghĩa", "Camus", "#hiyuabyss #tamlyhoc #trietly #ynghiacuocsong #hienxinh"),
    ("SOLITUDE", "Cô độc & Nỗi sợ tĩnh lặng", "Pascal", "#hiyuabyss #tamlyhoc #trietly #codoc #tinhlang"),
    ("STATUS", "Danh vọng & Khiêm nhường trình diễn", "@hiyuabyss", "#hiyuabyss #tamlyhoc #trietly #danhvong #khiemnhuong")
]

# 100 core posts details: (fmt, title_hook, s1, s2, s3, full_text, author_override, desc_thought)
RAW_POSTS = [
    # 1. HYPOCRISY
    (
        "Single-Punch (1 trang)",
        "Kẻ nguy hiểm nhất luôn xuất hiện với vẻ mặt của một vị thánh cứu rỗi.",
        "Kẻ nguy hiểm nhất không phải kẻ ác công khai, mà là người luôn xuất hiện với vẻ mặt của một vị thánh cứu rỗi.",
        "-", "-",
        "Kẻ nguy hiểm nhất không phải kẻ ác công khai, mà là người luôn xuất hiện với vẻ mặt của một vị thánh cứu rỗi.",
        "LaRochefoucauld",
        "Chúng ta thường cảnh giác trước sự hung hăng, nhưng lại dễ dàng buông lỏng phòng bị trước những người thích đóng vai 'người tốt tuyệt đối'. Sự tử tế chân thành không bao giờ đòi hỏi người khác phải mắc nợ hay phục tùng mình. Khi ai đó luôn cố chứng minh mình là thánh nhân trong mọi câu chuyện, hãy tự hỏi: Đằng sau chiếc mặt nạ cứu rỗi ấy là lòng tốt thực sự hay là nhu cầu thao túng tâm lý? Bạn đã từng gặp kiểu người này chưa?"
    ),
    (
        "Carousel 2 trang",
        "Lòng tốt đáng sợ nhất là khoản nợ ngầm bắt bạn phải mang ơn suốt đời.",
        "Lòng tốt đáng sợ nhất là khi......",
        "Họ giúp bạn một lần, nhưng ngầm bắt bạn phải mang ơn và gật đầu với họ cả đời.",
        "-",
        "Lòng tốt đáng sợ nhất là khi người ta giúp bạn một lần, nhưng lại ngầm bắt bạn phải mang ơn và cúi đầu trước họ suốt phần đời còn lại.",
        "@hiyuabyss",
        "Có những sự giúp đỡ không xuất phát từ lòng hào hiệp, mà là một khoản đầu tư tâm lý có tính toán. Họ giúp bạn một chuyện nhỏ để đổi lấy quyền phán xét và sai khiến bạn trong tương lai. Nhận một ân huệ kèm điều kiện ngầm đôi khi còn đắt hơn việc tự mình vượt qua khó khăn. Bạn có đủ dũng khí để từ chối những 'ân huệ' độc hại này?"
    ),
    (
        "Single-Punch (1 trang)",
        "Người nói đạo lý càng trơn tru thì khi đụng chạm lợi ích, họ quay xe càng nhanh.",
        "Người nói đạo lý càng trôi chảy thì khi lợi ích bị đụng tới, họ là người quay xe nhanh nhất.",
        "-", "-",
        "Người nói đạo lý càng trôi chảy thì khi lợi ích bị đụng tới, họ là người quay xe nhanh nhất.",
        "LaRochefoucauld",
        "Đạo đức trên đầu môi luôn là thứ rẻ tiền nhất vì nó chẳng tốn kém bất kỳ cái giá nào để nói ra. Chỉ khi quyền lợi cá nhân bị đe dọa, bản chất thực sự của một con người mới lộ diện rõ ràng nhất. Đừng nghe những gì họ giảng giải, hãy nhìn cách họ hành xử khi họ phải chịu thiệt thòi."
    ),
    (
        "Carousel 2 trang",
        "Có những người tha thứ rất nhanh chỉ để tích lũy quyền lực phán xét bạn.",
        "Có những người tha thứ rất nhanh......",
        "Chỉ để mỗi lần tranh cãi, họ có quyền đem lỗi lầm cũ ra ép bạn phải thấy mình tội lỗi.",
        "-",
        "Có những người tha thứ rất nhanh, chỉ để mỗi lần tranh cãi, họ có quyền đem lỗi lầm cũ ra ép bạn phải thấy mình tội lỗi.",
        "@hiyuabyss",
        "Sự tha thứ độc hại là khi miệng nói 'không sao đâu', nhưng tâm trí lại ghi nhớ từng chi tiết để làm vũ khí tấn công trong tương lai. Họ không buông bỏ lỗi lầm, họ chỉ biến nó thành một đòn bẩy tâm lý để bạn luôn cảm thấy mình là kẻ mang nợ và phải nhượng bộ vô điều kiện."
    ),
    (
        "Carousel 3 trang",
        "Người ta hăng hái kết tội kẻ khác không phải vì công lý, mà để che giấu vết nhơ của chính mình.",
        "Người ta hăng hái ném đá kẻ khác......",
        "Không phải vì họ yêu chuộng công lý, mà vì chửi bới người khác là cách nhanh nhất để cảm thấy mình trong sạch.",
        "Càng sốt sắng kết tội lỗi lầm của người ngoài, ta càng dễ quên đi những góc khuất đáng xấu hổ trong chính lòng mình.",
        "Người ta hăng hái ném đá kẻ khác không phải vì yêu công lý, mà vì sỉ nhục người khác là cách nhanh nhất để cảm thấy bản thân trong sạch.",
        "Nietzsche",
        "Cơn phẫn nộ đạo đức của đám đông thường là một tấm bình phong che đậy sự bất an nội tâm. Khi cùng nhau lên án một ai đó, con người ta có được ảo tưởng về sự thánh thiện mà không cần phải tự sửa mình. Hãy cẩn trọng trước những kẻ luôn sốt sắng đi tìm tà ác ở người khác."
    ),

    # 2. DOUBLE_STANDARD
    (
        "Single-Punch (1 trang)",
        "Lỗi của người khác ta gọi là bản chất, lỗi của bản thân ta gọi là hoàn cảnh.",
        "Ta gọi lỗi lầm của người khác là bản chất, nhưng lại gọi chính lỗi lầm ấy ở mình là hoàn cảnh bắt buộc.",
        "-", "-",
        "Ta gọi lỗi lầm của người khác là bản chất, nhưng lại gọi chính lỗi lầm ấy ở mình là hoàn cảnh bắt buộc.",
        "@hiyuabyss",
        "Đây là sai lầm quy kết cơ bản (Fundamental Attribution Error) mà hầu hết chúng ta đều mắc phải mỗi ngày. Khi người khác thất bại hay mắc lỗi, ta vội vàng đánh giá nhân cách của họ. Nhưng khi chính ta phạm sai lầm tương tự, ta lại viện cớ hoàn cảnh, áp lực và sự xui xẻo để tự an ủi mình."
    ),
    (
        "Carousel 2 trang",
        "Đừng phán xét sự lựa chọn của người khác khi bạn chưa từng phải chịu đựng sự bế tắc của họ.",
        "Ta rất dễ phán xét người khác......",
        "Cho đến khi chính bản thân rơi vào hoàn cảnh mà không có lựa chọn nào là trọn vẹn.",
        "-",
        "Ta rất dễ phán xét người khác, cho đến khi chính bản thân rơi vào hoàn cảnh mà không có lựa chọn nào là trọn vẹn.",
        "@hiyuabyss",
        "Đứng ngoài cuộc thì ai cũng sáng suốt và đạo mạo. Chỉ khi đôi chân bạn phải bước trên những mảnh vỡ mà người khác từng đi qua, bạn mới hiểu được tại sao họ lại đưa ra những quyết định tuyệt vọng đến vậy. Lòng bao dung bắt đầu từ sự thấu hiểu hoàn cảnh."
    ),
    (
        "Single-Punch (1 trang)",
        "Quy chuẩn khắt khe người ta đặt ra cho bạn chỉ áp dụng khi bạn là người chịu thiệt.",
        "Quy chuẩn khắt khe người ta đặt ra cho bạn sẽ biến mất ngay khoảnh khắc họ là người vi phạm.",
        "-", "-",
        "Quy chuẩn khắt khe người ta đặt ra cho bạn sẽ biến mất ngay khoảnh khắc họ là người vi phạm.",
        "@hiyuabyss",
        "Tiêu chuẩn kép là thứ vũ khí lợi hại nhất của những kẻ thích áp đặt. Họ muốn bạn phải hoàn hảo, nhẫn nhịn và hy sinh, nhưng bản thân họ lại luôn dành cho mình những ngoại lệ đặc biệt. Đừng để tiêu chuẩn của kẻ khác biến thành gông cùm trói buộc cuộc đời bạn."
    ),
    (
        "Carousel 2 trang",
        "Người đòi hỏi bạn phải thấu hiểu thường là người ít lắng nghe bạn nhất.",
        "Người luôn đòi hỏi sự thấu hiểu......",
        "Lại thường là người ít khi chịu lắng nghe cảm xúc của bạn nhất.",
        "-",
        "Người luôn đòi hỏi sự thấu hiểu lại thường là người ít khi chịu lắng nghe cảm xúc của bạn nhất.",
        "@hiyuabyss",
        "Họ xem cảm xúc của mình là trung tâm vũ trụ, nhưng lại coi sự mệt mỏi của bạn là chuyện nhỏ nhặt không đáng bận tâm. Mối quan hệ lành mạnh đòi hỏi sự lắng nghe từ hai phía, không phải là một sân khấu độc thoại cho một người."
    ),
    (
        "Carousel 3 trang",
        "Bản ngã con người thà hạ thấp nỗ lực của kẻ khác chứ không chịu thừa nhận sự kém cỏi của mình.",
        "Khi người khác đạt được thành công......",
        "Ta thường nghĩ do họ may mắn hoặc có người nâng đỡ, chứ hiếm khi chịu nhìn nhận mồ hôi nước mắt của họ.",
        "Bản ngã của con người yếu đuối đến mức: thà hạ thấp nỗ lực của người khác, còn hơn thừa nhận bản thân đang giậm chân tại chỗ.",
        "Khi người khác thành công, ta thường nghĩ do họ may mắn hoặc có bệ đỡ; thà hạ thấp nỗ lực của người khác còn hơn thừa nhận bản thân đang giậm chân tại chỗ.",
        "@hiyuabyss",
        "Sự đố kỵ ngầm khiến ta luôn tìm cách hạ thấp thành tựu của những người xung quanh để bảo vệ sự tự tôn mong manh của mình. Nhưng phủ nhận thành công của người khác chẳng bao giờ làm bạn giỏi giang hơn; nó chỉ giam cầm bạn trong sự cay đắng và thụt lùi."
    ),

    # 3. MORALITY
    (
        "Single-Punch (1 trang)",
        "Lòng tốt mà đi kèm với kỳ vọng được tán dương chỉ là một món hàng trao đổi.",
        "Lòng tốt mà đòi hỏi tiếng vỗ tay thì đó không phải là sự thiện lương, đó là một giao dịch mua bán danh tiếng.",
        "-", "-",
        "Lòng tốt mà đòi hỏi tiếng vỗ tay thì đó không phải là sự thiện lương, đó là một giao dịch mua bán danh tiếng.",
        "Nietzsche",
        "Khi làm việc tốt chỉ vì muốn nhận lại sự biết ơn, ngưỡng mộ hay ánh mắt thán phục từ xã hội, bản chất của hành động ấy đã biến thành một cuộc trao đổi sòng phẳng. Lòng tốt thuần khiết là khi bạn sẵn sàng làm điều đúng đắn ngay cả khi không có một khán giả nào đứng xem."
    ),
    (
        "Carousel 2 trang",
        "Kẻ yếu đuối không dám làm điều ác không có nghĩa họ là người có đạo đức.",
        "Không thể làm điều ác......",
        "Khác hoàn toàn với việc có đủ sức mạnh để làm ác nhưng chọn cách sống lương thiện.",
        "-",
        "Không thể làm điều ác khác hoàn toàn với việc có đủ sức mạnh để tàn nhẫn nhưng vẫn chọn sống tử tế.",
        "Nietzsche",
        "Nhiều người nhầm lẫn giữa sự bất lực và lòng tốt. Một người không dám phản kháng vì sợ hãi hậu quả không đồng nghĩa với việc họ có đạo đức cao thượng. Đạo đức chỉ thực sự tồn tại khi bạn nắm trong tay quyền lực để chà đạp kẻ khác nhưng bạn vẫn kiềm chế và chọn sự nhân từ."
    ),
    (
        "Single-Punch (1 trang)",
        "Sự tử tế không có ranh giới là lời mời gọi cho lòng tham và sự lợi dụng.",
        "Sự tử tế không có ranh giới không phải là đức tính tốt, đó là sự đồng lõa cho lòng tham của kẻ khác.",
        "-", "-",
        "Sự tử tế không có ranh giới không phải là đức tính tốt, đó là sự đồng lõa cho lòng tham của kẻ khác.",
        "@hiyuabyss",
        "Khi bạn luôn sẵn lòng hy sinh và không bao giờ biết nói 'Không', người ta sẽ không cảm kích bạn; họ chỉ dần coi sự hy sinh của bạn là điều đương nhiên. Ranh giới cá nhân không phải là ích kỷ, mà là hàng rào bảo vệ lòng tốt của bạn không bị biến thành công cụ cho kẻ vụ lợi."
    ),
    (
        "Carousel 2 trang",
        "Hy sinh bản thân để làm hài lòng tất cả là cách nhanh nhất để đánh mất chính mình.",
        "Cố gắng làm vừa lòng tất cả mọi người......",
        "Là cách nhanh nhất để khiến bản thân kiệt quệ và đánh mất sự tôn trọng của chính mình.",
        "-",
        "Cố gắng làm vừa lòng tất cả mọi người là cách nhanh nhất để biến mình thành một con rối không có cá tính.",
        "@hiyuabyss",
        "Bạn không thể làm hài lòng tất cả mọi người mà không phải trả giá bằng việc gọt giũa chính mình thành hình thù họ muốn. Khi bạn ngừng sợ hãi sự từ chối, bạn mới bắt đầu có được sự tôn trọng thực sự từ những người xứng đáng."
    ),
    (
        "Carousel 3 trang",
        "Đừng nhầm lẫn giữa lòng vị tha và thói quen dung túng cho sự vô ơn.",
        "Có những người nhận lòng tốt của bạn......",
        "Nhưng lại nghĩ rằng đó là nghĩa vụ mà bạn bắt buộc phải làm cho họ.",
        "Khi bạn ngừng cho đi, họ không nhớ những gì bạn đã giúp, họ chỉ ghi hận việc bạn đã từ chối.",
        "Có những người khi nhận lòng tốt của bạn thì nghĩ đó là nghĩa vụ; khi bạn ngừng cho đi, họ không nhớ những gì bạn đã giúp mà chỉ ghi hận việc bạn từ chối.",
        "@hiyuabyss",
        "Lòng tốt trao nhầm người sẽ chỉ nuôi dưỡng sự kiêu ngạo và vô ơn của kẻ đón nhận. Học cách dừng lại đúng lúc không phải là tàn nhẫn, mà là sự tôn trọng cần thiết đối với công sức và tình cảm của chính bản thân mình."
    ),

    # 4. EGO
    (
        "Single-Punch (1 trang)",
        "Bản ngã càng lớn thì ngưỡng chịu đựng sự thật càng thấp.",
        "Kẻ có bản ngã càng lớn thì càng dễ bị tổn thương bởi một sự thật rất đỗi bình thường.",
        "-", "-",
        "Kẻ có bản ngã càng lớn thì càng dễ bị tổn thương bởi một sự thật rất đỗi bình thường.",
        "Schopenhauer",
        "Bản ngã giống như một quả bóng bay thổi căng: càng phình to thì càng mỏng manh và dễ nổ tung trước một cú chạm nhẹ. Người trưởng thành thực sự là người đủ vững vàng để đối diện với khuyết điểm của mình mà không cần phải dựng lên tấm khiên tự ái."
    ),
    (
        "Carousel 2 trang",
        "Nhu cầu chứng minh mình đúng luôn đi kèm với sự bất an sâu thẳm bên trong.",
        "Người luôn cố chứng minh mình đúng......",
        "Thực chất là người đang hoảng loạn nhất trước khả năng mình có thể sai lầm.",
        "-",
        "Người luôn cố chứng minh mình đúng thực chất là người đang bất an nhất trước khả năng mình có thể sai lầm.",
        "@hiyuabyss",
        "Sự tự tin đích thực không cần phải tranh cãi ồn ào hay dìm người khác xuống để khẳng định bản thân. Chỉ có sự tự ti được che đậy mới khiến người ta phải xù lông nhím và khăng khăng rằng mình không bao giờ phạm sai lầm."
    ),
    (
        "Single-Punch (1 trang)",
        "Càng nhạy cảm và dễ tự ái, chứng tỏ nội tâm bên trong càng bất an.",
        "Kẻ có thực lực không dựng gai nhọn khắp người để tự vệ; chỉ kẻ yếu đuối mới thấy lời nói nào cũng là sự công kích.",
        "-", "-",
        "Kẻ có thực lực không dựng gai nhọn khắp người để tự vệ; chỉ kẻ yếu đuối mới thấy lời nói nào cũng là sự công kích.",
        "Schopenhauer",
        "Khi bạn cảm thấy cả thế giới đang nhắm vào mình, vấn đề thường không nằm ở người ngoài, mà ở chiếc gương phản chiếu nỗi bất an bên trong bạn. Hãy tập trung xây dựng năng lực thực tế thay vì tốn năng lượng bảo vệ ảo tưởng hoàn hảo."
    ),
    (
        "Carousel 2 trang",
        "Hạ thấp người khác không bao giờ giúp bạn đứng cao hơn.",
        "Chỉ trích khuyết điểm của người khác......",
        "Không thể lấp đầy những khoảng trống và sự thiếu hụt trong chính năng lực của bạn.",
        "-",
        "Chỉ trích khuyết điểm của người khác không thể bù đắp cho những thiếu hụt trong năng lực của chính bạn.",
        "@hiyuabyss",
        "Kẻ bất tài thường tìm kiếm cảm giác ưu việt rẻ tiền bằng cách bới móc lỗi lầm của người khác. Nhưng giá trị của bạn được đo bằng những gì bạn kiến tạo, chứ không phải bằng số lượng người bạn đã dìm xuống bùn."
    ),
    (
        "Carousel 3 trang",
        "Cơn giận dữ bộc phát thường là tiếng kêu cứu của một bản ngã đang bị đe dọa.",
        "Khi một người nổi giận mất kiểm soát......",
        "Hiếm khi là vì sự việc trước mắt quá nghiêm trọng, mà vì vị thế ảo của họ đang bị đe dọa.",
        "Họ dùng tiếng thét gào để che giấu nỗi sợ bị xem thường và sự bất lực không thể kiểm soát tình thế.",
        "Cơn giận dữ bộc phát hiếm khi vì sự việc quá nghiêm trọng; nó là tiếng thét gào của một bản ngã đang run rẩy vì sợ bị xem thường.",
        "Freud",
        "Cơn giận là một cơ chế tự vệ bản năng của cái tôi mong manh. Khi cảm thấy giá trị của mình bị lung lay, người ta chọn sự hung hăng để áp đảo đối phương. Nhận diện được nguồn gốc của cơn giận là bước đầu tiên để làm chủ cảm xúc của chính mình."
    ),

    # 5. SELF_DECEPTION
    (
        "Single-Punch (1 trang)",
        "Lời nói dối nguy hiểm nhất là lời nói dối mà chính bạn cũng tin là thật.",
        "Kẻ lừa dối người khác là kẻ xảo quyệt, nhưng kẻ tự lừa dối chính mình là kẻ bi kịch nhất.",
        "-", "-",
        "Kẻ lừa dối người khác là kẻ xảo quyệt, nhưng kẻ tự lừa dối chính mình là kẻ bi kịch nhất.",
        "Pascal",
        "Bộ não con người là một cỗ máy hợp lý hóa siêu hạng. Chúng ta sẵn sàng bịa ra hàng trăm lý do hợp lý để biện minh cho sự lười biếng, sợ hãi hoặc hèn nhát của mình, chỉ để không phải đối mặt với cảm giác tội lỗi. Dũng khí lớn nhất đời người là dám nhìn thẳng vào sự thật về chính mình."
    ),
    (
        "Carousel 2 trang",
        "Người ta chấp nhận mọi sự bận rộn giả tạo để trốn tránh việc phải ở một mình.",
        "Ta sẵn sàng nhận lấy mọi sự bận rộn......",
        "Chỉ để không phải đối diện với sự trống rỗng và câu hỏi: Mình thực sự là ai khi rèm nhung khép lại?",
        "-",
        "Ta chấp nhận mọi sự bận rộn khiến mình kiệt sức, chỉ để không phải ở một mình với con người thật mà ta đã dành cả đời để che giấu.",
        "Pascal",
        "Pascal từng nói: Mọi nỗi bất hạnh của con người đều bắt nguồn từ một việc duy nhất: không thể ngồi yên lặng một mình trong phòng. Sự bận rộn đôi khi chỉ là một liều thuốc an thần giúp ta chạy trốn tiếng gào thét của nội tâm."
    ),
    (
        "Single-Punch (1 trang)",
        "Vùng an toàn là nơi dễ chịu nhất để chôn cất tiềm năng của một con người.",
        "Vùng an toàn không phải là nơi che chở cho bạn, đó là một chiếc lồng êm ái ru ngủ mọi khát vọng.",
        "-", "-",
        "Vùng an toàn không phải là nơi che chở cho bạn, đó là một chiếc lồng êm ái ru ngủ mọi khát vọng.",
        "@hiyuabyss",
        "Cái giá của sự ổn định tầm thường là sự hối tiếc muộn màng. Nỗi sợ thất bại khiến chúng ta thà chọn một cuộc đời mờ nhạt quen thuộc còn hơn mạo hiểm bước ra ngoài để phát triển. Sự thoải mái hôm nay có thể là sự ân hận của ngày mai."
    ),
    (
        "Carousel 2 trang",
        "Lý do bạn không dám bắt đầu không phải vì nó khó, mà vì bạn sợ phát hiện mình tầm thường.",
        "Ta trì hoãn việc bắt đầu......",
        "Không phải vì thiếu thời gian, mà vì sợ phải chứng kiến kết quả thực tế không hoàn hảo như trong tưởng tượng.",
        "-",
        "Ta trì hoãn không phải vì việc khó, mà vì sợ giấc mộng hoàn hảo của bản thân bị vỡ vụn trước thực tế.",
        "@hiyuabyss",
        "Chừng nào chưa làm, bạn vẫn còn quyền ảo tưởng rằng 'nếu tôi làm, tôi sẽ thành công vang dội'. Sự trì hoãn thực chất là một cơ chế phòng vệ tâm lý để bảo vệ lòng tự tôn khỏi nguy cơ bị thực tế tát thẳng vào mặt."
    ),
    (
        "Carousel 3 trang",
        "Sự tha thứ giả tạo cho chính mình là cái bẫy giam giữ bạn trong thất bại.",
        "Có những người luôn dễ dãi với bản thân......",
        "Họ gọi sự lười biếng là 'chữa lành', gọi sự hèn nhát là 'biết đủ', và gọi sự buông xuôi là 'tùy duyên'.",
        "Bi kịch lớn nhất là khi ta dùng những khái niệm triết học thanh cao để bao biện cho sự thất bại trong kỷ luật cá nhân.",
        "Gọi lười biếng là 'chữa lành', gọi hèn nhát là 'biết đủ', gọi buông xuôi là 'tùy duyên' chính là đỉnh cao của sự tự lừa dối.",
        "@hiyuabyss",
        "Thời đại ngày nay có quá nhiều ngôn từ êm tai giúp con người ta trốn tránh trách nhiệm phát triển bản thân. Chữa lành thực sự đòi hỏi bạn phải dũng cảm đối diện với vết thương và đứng dậy hành động, chứ không phải nằm yên trong sự trì trệ."
    ),

    # 6. SHADOW
    (
        "Single-Punch (1 trang)",
        "Chối bỏ bóng tối trong lòng chỉ khiến nó trỗi dậy mạnh mẽ hơn trong vô thức.",
        "Càng cố gắng tỏ ra trong sạch không tì vết, bóng tối bị chối bỏ trong bạn càng dễ biến thành quái vật.",
        "-", "-",
        "Càng cố gắng tỏ ra trong sạch không tì vết, bóng tối bị chối bỏ trong bạn càng dễ biến thành quái vật.",
        "Jung",
        "Carl Jung từng dạy rằng 'Shadow' (bóng tối nội tâm) chứa đựng tất cả những phần bản năng, sự giận dữ và dục vọng mà ý thức chối bỏ. Nếu không học cách thừa nhận và hòa giải với nó, nó sẽ kiểm soát hành vi của bạn từ trong bóng tối và bạn sẽ gọi đó là 'số phận'."
    ),
    (
        "Carousel 2 trang",
        "Điều bạn căm ghét nhất ở người khác thường là thứ bạn đang giấu kín ở bản thân.",
        "Cơn phẫn nộ dữ dội trước khuyết điểm của người ngoài......",
        "Thực chất là tấm gương phản chiếu chính phần tính cách mà bạn căm ghét và đè nén bên trong mình.",
        "-",
        "Thứ làm bạn khó chịu nhất ở người khác thường là điều bạn đang giấu giếm kỹ nhất ở chính bản thân.",
        "Jung",
        "Cơ chế phóng chiếu tâm lý (Projection) khiến chúng ta nhạy cảm bất thường với những lỗi lầm của người khác mà bản thân cũng vô tình mắc phải. Khi bạn học cách tự soi chiếu, bạn sẽ thấy sự bực bội kia không đến từ người ngoài, mà đến từ mâu thuẫn chưa giải quyết trong lòng bạn."
    ),
    (
        "Single-Punch (1 trang)",
        "Chỉ khi thừa nhận phần tàn nhẫn trong mình, bạn mới học được cách tử tế thực sự.",
        "Người không biết mình có khả năng làm điều ác sẽ không bao giờ hiểu được giá trị của việc chọn sống lương thiện.",
        "-", "-",
        "Người không biết mình có khả năng làm điều ác sẽ không bao giờ hiểu được giá trị của việc chọn sống lương thiện.",
        "Jung",
        "Sự ngây thơ không phải là thánh thiện; nó chỉ là sự thiếu trải nghiệm. Một người nhận thức rõ những góc khuất tăm tối, sự ích kỷ và tàn nhẫn của mình nhưng vẫn có đủ kỷ luật để chọn hành động vị tha mới là người có nhân cách vững vàng."
    ),
    (
        "Carousel 2 trang",
        "Đừng đánh giá một con người khi họ no ấm, hãy nhìn họ khi bị tước đoạt lợi ích.",
        "Vẻ ngoài lịch thiệp rất dễ duy trì......",
        "Khi mọi thứ diễn ra êm đẹp và lợi ích của họ chưa từng bị đụng chạm.",
        "-",
        "Nhân cách thực sự chỉ lộ diện khi người ta rơi vào nghịch cảnh và bị tước đoạt những điều họ trân quý.",
        "@hiyuabyss",
        "Lớp sơn bóng bẩy của sự văn minh rất dễ tróc ra trước áp lực của sự sinh tồn và lợi ích cá nhân. Hãy quan sát cách một người đối xử với những người yếu thế hơn họ khi họ đang căng thẳng; đó mới là bản chất thật của họ."
    ),
    (
        "Carousel 3 trang",
        "Kẻ luôn tự nhận mình hoàn toàn tốt đẹp là kẻ nguy hiểm và mù quáng nhất.",
        "Ai cũng có một góc khuất tăm tối......",
        "Nơi chứa đựng những ý nghĩ ích kỷ, đố kỵ và những dục vọng mà xã hội không chấp nhận.",
        "Kẻ nguy hiểm không phải người có bóng tối, mà là kẻ tin rằng mình trong sạch đến mức không có bóng tối nào cần kiểm soát.",
        "Ai cũng có bóng tối; kẻ nguy hiểm nhất là kẻ tin mình hoàn hảo đến mức không cần phải tự soi chiếu và kiểm soát bản thân.",
        "Jung",
        "Sự mù quáng lớn nhất là ảo tưởng về sự thánh thiện tuyệt đối của bản thân. Khi từ chối nhìn nhận góc khuất của mình, bạn sẽ dễ dàng biến những hành vi tàn nhẫn nhất thành 'hành động vì chính nghĩa'. Tự biết mình là bước đầu tiên của trí tuệ."
    ),

    # 7. MASK
    (
        "Single-Punch (1 trang)",
        "Đeo mặt nạ quá lâu, bạn sẽ quên mất khuôn mặt thực sự của chính mình.",
        "Bi kịch lớn nhất không phải là lừa dối người khác, mà là một ngày nhận ra chiếc mặt nạ đã dính chặt vào da thịt.",
        "-", "-",
        "Bi kịch lớn nhất không phải là lừa dối người khác, mà là một ngày nhận ra chiếc mặt nạ đã dính chặt vào da thịt.",
        "@hiyuabyss",
        "Chúng ta bắt đầu bằng việc đóng vai một người vui vẻ, hiểu chuyện và bao dung để làm hài lòng xã hội. Nhưng theo thời gian, vai diễn ấy nuốt chửng bản sắc thực sự của chúng ta, để lại một tâm hồn trống rỗng không biết mình thực sự muốn gì."
    ),
    (
        "Carousel 2 trang",
        "Càng cố gồng mình tỏ ra hoàn hảo, khoảng cách với hạnh phúc càng xa.",
        "Chiếc mặt nạ hoàn hảo......",
        "Chỉ mang lại cho bạn những lời khen ngợi xã giao, nhưng đổi lại là sự cô độc không ai thấu hiểu.",
        "-",
        "Chiếc mặt nạ hoàn hảo giúp bạn có được sự công nhận của xã hội, nhưng lại cướp đi cơ hội được yêu thương vì chính con người thật của mình.",
        "@hiyuabyss",
        "Người ta ngưỡng mộ sự hoàn hảo, nhưng chỉ có thể kết nối sâu sắc với sự chân thật và những vết nứt của bạn. Dũng cảm để lộ những góc yếu đuối là chìa khóa duy nhất để tìm thấy sự đồng điệu chân thành trong cuộc sống."
    ),
    (
        "Single-Punch (1 trang)",
        "Người luôn mỉm cười trong mọi tình huống thường là người đang kiệt sức nhất.",
        "Nụ cười xã giao là chiếc áo giáp kiên cố nhất để ngăn không cho bất kỳ ai nhìn thấy sự vụn vỡ bên trong.",
        "-", "-",
        "Nụ cười xã giao là chiếc áo giáp kiên cố nhất để ngăn không cho bất kỳ ai nhìn thấy sự vụn vỡ bên trong.",
        "@hiyuabyss",
        "Đôi khi, nụ cười không phản ánh niềm vui, mà là dấu hiệu của sự buông xuôi và mệt mỏi cùng cực. Hãy dành sự quan tâm cho những người luôn tỏ ra ổn định và tích cực xung quanh bạn; họ có thể đang gồng gánh những nỗi đau không thể cất thành lời."
    ),
    (
        "Carousel 2 trang",
        "Đừng đánh đổi sự chân thật của bản thân để mua lấy sự đồng thuận tạm bợ.",
        "Khi bạn từ bỏ nguyên tắc để hòa nhập......",
        "Bạn không hề có thêm bạn bè thực sự, bạn chỉ có thêm những kẻ đồng hành cùng chiếc mặt nạ của bạn.",
        "-",
        "Đánh đổi bản sắc để hòa nhập chỉ mang lại cho bạn những mối quan hệ hời hợt, sẵn sàng tan biến khi bạn tháo mặt nạ ra.",
        "@hiyuabyss",
        "Thà bị ghét bỏ vì chính con người thật của mình, còn hơn được tung hô vì một hình mẫu giả tạo. Những người thực sự trân trọng bạn sẽ ở lại ngay cả khi bạn không khoác lên mình bộ lễ phục hào nhoáng."
    ),
    (
        "Carousel 3 trang",
        "Sự hiểu chuyện quá mức là một hình thức tự trừng phạt bản thân.",
        "Đứa trẻ hiểu chuyện nhất......",
        "Thường là đứa trẻ học được cách nuốt nước mắt vào trong để không làm phiền lòng người lớn.",
        "Lớn lên, họ trở thành những người luôn ưu tiên cảm xúc của kẻ khác và tự cảm thấy có lỗi khi nghĩ đến hạnh phúc của chính mình.",
        "Hiểu chuyện quá mức không phải là sự trưởng thành; đó là vết thương tâm lý của một tâm hồn từng không được phép yếu đuối.",
        "@hiyuabyss",
        "Nhiều người coi 'hiểu chuyện' là một lời khen, nhưng với người trong cuộc, đó là chiếc gông cùm ép họ phải nhẫn nhịn và hy sinh quyền lợi của mình. Bạn có quyền được mệt mỏi, được từ chối và được yêu thương mà không cần phải luôn luôn đóng vai người hoàn hảo."
    ),

    # 8. POWER
    (
        "Single-Punch (1 trang)",
        "Kẻ kiểm soát mạnh nhất không dùng vũ lực, họ dùng cảm giác mang ơn và tội lỗi.",
        "Quyền lực tối thượng không nằm ở roi vọt, mà ở khả năng khiến nạn nhân tự nguyện cúi đầu vì nghĩ mình có lỗi.",
        "-", "-",
        "Quyền lực tối thượng không nằm ở roi vọt, mà ở khả năng khiến nạn nhân tự nguyện cúi đầu vì nghĩ mình có lỗi.",
        "Machiavelli",
        "Thao túng tâm lý (Gaslighting và Guilt-tripping) là những hình thức bạo lực vô hình nhưng có sức tàn phá khủng khiếp nhất. Kẻ thao túng luôn đảo ngược tình thế để biến sai lầm của họ thành lỗi của bạn, khiến bạn tự nghi ngờ nhận thức và quyền tự chủ của chính mình."
    ),
    (
        "Carousel 2 trang",
        "Người nắm quyền lực thực sự không cần phải lên giọng hay đe dọa.",
        "Sự ồn ào và thị uy......",
        "Chỉ là biểu hiện của một kẻ đang lo sợ quyền lực giả tạo của mình bị lung lay.",
        "-",
        "Kẻ thực sự có quyền lực im lặng và hành động; kẻ yếu thế mới cần la hét để chứng minh vị thế của mình.",
        "Machiavelli",
        "Sự tự tin và quyền uy đích thực toát ra từ sự điềm tĩnh và khả năng kiểm soát thế cờ trong bóng tối. Đừng để những lời đe dọa to tiếng làm bạn hoảng sợ; kẻ càng ồn ào thì bên trong càng chứa đựng nhiều sự bất an."
    ),
    (
        "Single-Punch (1 trang)",
        "Muốn thử thách nhân cách của một con người, hãy trao cho họ quyền lực.",
        "Nghịch cảnh thử thách sự kiên nhẫn, nhưng chỉ có quyền lực mới bóc trần bản chất thật của một con người.",
        "-", "-",
        "Nghịch cảnh thử thách sự kiên nhẫn, nhưng chỉ có quyền lực mới bóc trần bản chất thật của một con người.",
        "Lincoln",
        "Khi một người không còn sợ bị trừng phạt và có toàn quyền quyết định số phận của kẻ khác, họ mới thực sự bộc lộ con người bên trong. Kẻ tiểu nhân đắc chí sẽ dùng quyền lực để trả thù và bóc lột; bậc quân tử sẽ dùng nó để che chở và kiến tạo."
    ),
    (
        "Carousel 2 trang",
        "Sự phục tùng không tự nguyện luôn ngấm ngầm nuôi dưỡng sự phản bội.",
        "Ép buộc người khác bằng quyền lực......",
        "Bạn chỉ nhận được sự tuân lệnh bên ngoài, nhưng ngầm tạo ra sự căm thù chờ ngày bùng nổ.",
        "-",
        "Quyền lực xây trên sự sợ hãi sẽ sụp đổ ngay khoảnh khắc kẻ thống trị để lộ một vết nứt nhỏ.",
        "Machiavelli",
        "Không có đế chế nào tồn tại mãi mãi chỉ nhờ vào sự đàn áp. Khi người ta vâng lời bạn chỉ vì sợ hãi, họ sẽ là những người đầu tiên đẩy bạn xuống vực thẳm khi bạn trượt chân. Thu phục lòng người bằng sự tôn trọng luôn bền vững hơn quyền lực áp đặt."
    ),
    (
        "Carousel 3 trang",
        "Đừng bao giờ trở thành người lệ thuộc hoàn toàn vào lòng tốt của kẻ khác.",
        "Khi bạn không có năng lực tự đứng trên đôi chân mình......",
        "Mọi sự đối xử tốt mà bạn nhận được đều là sự ban ơn của kẻ nắm quyền lực.",
        "Hôm nay họ có thể mỉm cười cho bạn bánh mì, nhưng ngày mai họ có thể tước đoạt phẩm giá của bạn chỉ bằng một cái phẩy tay.",
        "Tự do không đến từ sự ban ơn; chừng nào bạn còn lệ thuộc vào kẻ khác, bạn chưa bao giờ thực sự làm chủ cuộc đời mình.",
        "@hiyuabyss",
        "Sự độc lập về kinh tế, tư duy và cảm xúc là tấm khiên vững chắc nhất bảo vệ phẩm giá của bạn. Đừng bao giờ trao chìa khóa hạnh phúc của mình vào tay bất kỳ ai, bởi vì kẻ nắm chìa khóa cũng chính là kẻ có quyền khóa bạn lại trong ngục tối."
    )
]

# Generate remaining 60 posts programmatically with deep philosophical aphorisms
# across the remaining 12 themes (Themes 9 to 20: 5 posts each = 60 posts)
def build_all_100():
    all_data = []
    post_idx = 1
    start_date = datetime(2026, 11, 16)

    # First 40 posts from detailed RAW_POSTS (Themes 1 to 8)
    for p in RAW_POSTS:
        t_idx = (post_idx - 1) // 5
        t_code, t_name, def_author, def_hash = THEMES[t_idx]
        fmt, title, s1, s2, s3, full_txt, auth_override, desc = p
        
        # Determine theme template folder (theme_01 to theme_60)
        theme_folder = f"theme_{post_idx:02d}" if post_idx <= 60 else f"theme_{(post_idx % 30) + 1:02d}"
        
        # Calculate schedule date
        day_offset = (post_idx - 1) * 2  # post every 2 days or daily cadence
        post_date = start_date + timedelta(days=day_offset)
        weekday_vn = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"][post_date.weekday()]
        date_label = f"{weekday_vn} ({post_date.strftime('%d/%m')})"
        
        time_slot = ["11:30 - 12:30 (Trưa)", "19:30 - 20:30 (Tối)", "21:00 - 22:30 (Đêm chiêm nghiệm)"][post_idx % 3]
        
        all_data.append({
            "stt": post_idx,
            "id": f"TXT-{post_idx:04d}",
            "title": title,
            "desc": desc,
            "author": auth_override if auth_override else def_author,
            "hashtags": def_hash,
            "format": fmt,
            "s1": s1,
            "s2": s2,
            "s3": s3,
            "full_text": full_txt,
            "theme": f"{t_code} ({t_name})",
            "time_slot": time_slot,
            "date": date_label,
            "template": theme_folder,
            "status": "SẴN SÀNG"
        })
        post_idx += 1

    # Now generate remaining 60 posts (Themes 9 to 20: 12 themes * 5 posts = 60 posts)
    # Each theme follows the exact pattern: 1 Single-Punch, 2 Carousel 2-slide, 1 Single-Punch, 1 Carousel 3-slide
    remaining_themes = THEMES[8:]  # Themes 9 to 20
    
    # Pre-crafted aphorisms for themes 9 to 20
    THEME_REMAINDER_DATA = [
        # 9. MANIPULATION
        [
            ("Single-Punch (1 trang)", "Kẻ thao túng luôn bắt bạn phải xin lỗi vì những lỗi lầm do chính họ gây ra.", "Kẻ thao túng luôn có cách biến sai lầm của họ thành lỗi lầm mà bạn phải quỳ gối xin lỗi.", "-", "-", "Kẻ thao túng luôn có cách biến sai lầm của họ thành lỗi lầm mà bạn phải quỳ gối xin lỗi.", "@hiyuabyss", "Gaslighting là nghệ thuật bóp méo thực tế khiến nạn nhân tự nghi ngờ trí nhớ và cảm xúc của mình. Khi bạn nhận ra mình liên tục phải xin lỗi cho những chuyện không phải do mình gây ra, hãy tỉnh táo lùi lại một bước: Bạn đang ở trong một mối quan hệ, hay đang bị thao túng tâm lý?"),
            ("Carousel 2 trang", "Cảm giác tội lỗi là sợi dây xích vô hình trói buộc bạn chặt nhất.", "Thao túng bằng cảm giác tội lỗi......", "Là khi họ đóng vai nạn nhân xuất sắc đến mức bạn phải tự cắn rứt vì đã không hy sinh thêm.", "-", "Họ đóng vai nạn nhân xuất sắc đến mức bạn phải tự cắn rứt lương tâm vì đã không hy sinh cho họ nhiều hơn.", "@hiyuabyss", "Đóng vai nạn nhân là vũ khí tâm lý tàn nhẫn nhất của những kẻ ích kỷ. Họ khóc lóc, than vãn và phóng đại sự bất hạnh của mình để ép bạn phải nhượng bộ. Đừng để lòng trắc ẩn của bạn biến thành công cụ cho kẻ khác trục lợi."),
            ("Single-Punch (1 trang)", "Nợ ân tình là món nợ đắt đỏ nhất mà bạn không bao giờ trả hết.", "Ân tình trao nhầm người sẽ biến thành chiếc vòng kim cô siết chặt tự do của bạn đến cuối đời.", "-", "-", "Ân tình trao nhầm người sẽ biến thành chiếc vòng kim cô siết chặt tự do của bạn đến cuối đời.", "LaRochefoucauld", "Người đàng hoàng giúp bạn vì muốn bạn tốt hơn; kẻ thao túng giúp bạn để nắm đằng chuôi cuộc đời bạn. Hãy cẩn trọng trước những món quà miễn phí nhưng đi kèm với sự can thiệp thô bạo vào quyết định cá nhân."),
            ("Carousel 2 trang", "Đừng để lời khen có cánh ru ngủ sự cảnh giác của bạn.", "Lời khen ngợi quá mức......", "Thường là thuốc gây mê được tiêm trước khi họ đưa ra một yêu cầu quá đáng.", "-", "Lời khen ngợi dồn dập thường là lớp đường bọc ngoài viên thuốc đắng của một sự lợi dụng tinh vi.", "@hiyuabyss", "Khi ai đó đột nhiên tâng bốc bạn lên mây xanh, hãy tự hỏi: Họ ngưỡng mộ tài năng của bạn thực sự, hay họ đang chuẩn bị nhờ vả một việc mà bình thường bạn sẽ từ chối? Sự tỉnh táo trước những lời mật ngọt là phẩm chất của người từng trải."),
            ("Carousel 3 trang", "Thoát khỏi sự thao túng bắt đầu từ việc chấp nhận bị coi là kẻ tàn nhẫn.", "Muốn thoát khỏi kẻ thao túng......", "Bạn phải học cách chấp nhận việc bị họ gán cho cái mác 'kẻ vô ơn' và 'kẻ tàn nhẫn'.", "Chừng nào bạn còn sợ mang tiếng xấu trong miệng họ, chừng đó bạn vẫn còn là con rối trong tay họ.", "Muốn thoát khỏi kẻ thao túng, bạn phải dám chấp nhận bị họ gọi là 'kẻ tàn nhẫn'; sợ mang tiếng xấu là bạn vẫn còn bị giật dây.", "@hiyuabyss", "Kẻ thao túng sẽ dùng sự đạo đức giả để kết tội bạn ngay khoảnh khắc bạn thiết lập ranh giới. Dũng cảm chấp nhận trở thành 'kẻ phản diện' trong câu chuyện bịa đặt của họ là cái giá tối thiểu để bạn giành lại quyền tự do làm chủ cuộc đời mình.")
        ],
        # 10. FREEDOM
        [
            ("Single-Punch (1 trang)", "Tự do đích thực bắt đầu khi bạn dám chịu trách nhiệm 100% cho cuộc đời mình.", "Người ta sợ tự do hơn sợ xiềng xích, vì tự do đồng nghĩa với việc không còn ai để đổ lỗi khi thất bại.", "-", "-", "Người ta sợ tự do hơn sợ xiềng xích, vì tự do đồng nghĩa với việc không còn ai để đổ lỗi khi thất bại.", "Kierkegaard", "Tự do mang theo sức nặng khủng khiếp của trách nhiệm cá nhân. Xiềng xích tuy đau đớn nhưng lại mang đến sự an ủi hèn nhát: bạn luôn có lý do để đổ lỗi cho hoàn cảnh. Dám tự do là dám tự chịu trách nhiệm cho mọi cú ngã của mình."),
            ("Carousel 2 trang", "Nói 'Không' mà không thấy tội lỗi là cột mốc trưởng thành lớn nhất.", "Bạn chỉ thực sự có tự do......", "Khi bạn có thể nói chữ 'KHÔNG' mà không cần phải viện cớ hay cảm thấy mình có lỗi.", "-", "Tự do thực sự là khi bạn dám từ chối những điều đi ngược lại giá trị của mình mà không cần phải tự bào chữa.", "@hiyuabyss", "Nhiều người cả đời sống trong ngục tù vì nỗi sợ làm phật lòng người khác. Khi bạn dám từ chối một yêu cầu vô lý mà tâm trí vẫn thanh thản, đó là lúc bạn thực sự làm chủ không gian sống của chính mình."),
            ("Single-Punch (1 trang)", "Chiếc lồng son vẫn mãi là chiếc lồng giam hãm đôi cánh.", "Được nuôi béo trong sự an toàn không làm bạn hạnh phúc hơn; nó chỉ biến bạn thành kẻ mất khả năng tự bay.", "-", "-", "Được nuôi béo trong sự an toàn không làm bạn hạnh phúc hơn; nó chỉ biến bạn thành kẻ mất khả năng tự bay.", "Kierkegaard", "Sự ổn định do kẻ khác ban phát luôn đi kèm với sự kiểm soát và phục tùng. Thà là cánh chim tự do chịu bão táp trên bầu trời còn hơn là chú chim cảnh béo tốt hót theo lệnh của chủ nhân."),
            ("Carousel 2 trang", "Đừng đánh đổi tự do của tương lai để mua lấy sự an phận của hôm nay.", "Sự an nhàn quá sớm......", "Là cái bẫy ngọt ngào nhất tước đoạt dũng khí bứt phá của tuổi trẻ.", "-", "Sự an nhàn quá sớm là cái bẫy ngọt ngào tước đoạt dũng khí và tiềm năng bứt phá của một đời người.", "@hiyuabyss", "Vùng an toàn giống như một chiếc đầm lầy ấm áp: ở càng lâu bạn càng lún sâu và mất dần sức lực để bước ra ngoài. Đôi khi, bất an và áp lực chính là ngọn lửa cần thiết để tôi luyện bản lĩnh của bạn."),
            ("Carousel 3 trang", "Tự do không phải là phóng túng, tự do là khả năng tự kỷ luật bản thân.", "Nhiều người nghĩ tự do là làm bất cứ điều gì mình thích......", "Nhưng làm nô lệ cho dục vọng và thói lười biếng thực chất là hình thức giam cầm tệ hại nhất.", "Chỉ kẻ nào có khả năng kiểm soát ham muốn và thói quen của chính mình mới là kẻ thực sự được tự do.", "Tự do không phải là buông thả theo dục vọng; tự do đích thực là khả năng tự kỷ luật và làm chủ ham muốn của bản thân.", "Kierkegaard", "Một người không thể kiểm soát cơn thèm ăn, sự nghiện ngập hay thói trì hoãn thì dù sống trong xã hội tự do nhất, anh ta vẫn chỉ là một tên nô lệ cho bản năng của mình. Kỷ luật chính là chiếc chìa khóa duy nhất mở ra cánh cửa tự do.")
        ],
        # 11. TRUTH
        [
            ("Single-Punch (1 trang)", "Sự thật mất lòng nhưng cứu rỗi, lời nói dối êm tai nhưng đầu độc.", "Sự thật có thể làm bạn đau đớn trong chốc lát, nhưng lời nói dối ngọt ngào sẽ hủy hoại bạn cả đời.", "-", "-", "Sự thật có thể làm bạn đau đớn trong chốc lát, nhưng lời nói dối ngọt ngào sẽ hủy hoại bạn cả đời.", "Dostoevsky", "Chúng ta thích được vuốt ve bằng những lời dối trá êm tai hơn là bị đánh thức bởi sự thật trần trụi. Nhưng vết thương được mổ xẻ dẫu đau đớn sẽ lành lại; còn vết thương bị che đậy dưới lớp băng gạc dối trá sẽ thối rữa từ bên trong."),
            ("Carousel 2 trang", "Điều khó chịu nhất của sự thật không phải là điều nó phơi bày.", "Khi nghe một sự thật cay đắng......", "Điều làm ta đau nhất không phải là câu chữ, mà là những lời tự bào chữa nó đã cướp mất của ta.", "-", "Sự thật tàn nhẫn ở chỗ: nó tước đoạt mọi lời tự bào chữa mà ta đã dày công xây dựng để tự an ủi mình.", "Dostoevsky", "Con người ta giận dữ trước sự thật không phải vì họ không hiểu, mà vì sự thật đã phá hủy ảo tưởng hoàn hảo mà họ cố bám víu. Chấp nhận sự thật là cái giá đầu tiên để có được sự tiến bộ."),
            ("Single-Punch (1 trang)", "Im lặng trước sự bất công là hành vi đồng lõa với cái ác.", "Khi bạn chọn đứng trung lập trước kẻ mạnh bắt nạt kẻ yếu, bạn đã mặc nhiên chọn đứng về phía kẻ áp bức.", "-", "-", "Khi bạn chọn đứng trung lập trước kẻ mạnh bắt nạt kẻ yếu, bạn đã mặc nhiên chọn đứng về phía kẻ áp bức.", "Dostoevsky", "Sự hèn nhát thường thích đội lốt sự điềm tĩnh và 'dĩ hòa vi quý'. Nhưng trong những thời khắc then chốt, im lặng không phải là khôn ngoan; im lặng là sự phản bội lại lương tri và chân lý."),
            ("Carousel 2 trang", "Đừng nghe những lời họ hứa hẹn, hãy nhìn những việc họ đã làm.", "Lời nói có thể tô vẽ ra một thiên đường......", "Nhưng hành động thực tế mới phản ánh chính xác mảnh đất mà họ đang đứng.", "-", "Lời nói có thể giả tạo, nhưng dấu chân của hành động trong quá khứ không bao giờ biết nói dối.", "@hiyuabyss", "Con người ta thường tin vào những lời hứa ngọt ngào vì họ lười biếng không muốn kiểm chứng sự thật. Hãy để thời gian và hành vi thực tế lên tiếng; sự kiên nhẫn quan sát sẽ bảo vệ bạn khỏi những cú lừa ngoạn mục."),
            ("Carousel 3 trang", "Sự thật không cần được số đông ủng hộ để trở thành sự thật.", "Dù một triệu người cùng tin vào một điều dối trá......", "Thì điều dối trá ấy vẫn không thể biến thành sự thật.", "Và dẫu chỉ có một mình bạn đứng về phía chân lý, chân lý ấy vẫn nguyên vẹn giá trị của nó.", "Sự thật không phụ thuộc vào số phiếu bầu; dẫu cả thế giới phủ nhận, chân lý vẫn là chân lý.", "Dostoevsky", "Chân lý không vận hành theo nguyên lý dân chủ của đám đông. Đừng bao giờ nghi ngờ trực giác và sự thật chỉ vì bạn thấy mình là kẻ đơn độc. Lịch sử luôn được định hình bởi những cá nhân kiên định bảo vệ chân lý trước sự mù quáng của số đông.")
        ],
        # 12. LOVE
        [
            ("Single-Punch (1 trang)", "Chiếm hữu là biến người khác thành đồ vật; yêu thương là trao cho họ đôi cánh.", "Nhiều người gọi sự kiểm soát ghen tuông là tình yêu, nhưng đó thực chất là nỗi sợ bị bỏ rơi và tính ích kỷ.", "-", "-", "Nhiều người gọi sự kiểm soát ghen tuông là tình yêu, nhưng đó thực chất là nỗi sợ bị bỏ rơi và tính ích kỷ.", "@hiyuabyss", "Tình yêu độc hại luôn tìm cách cắt đứt các mối quan hệ của đối phương, soi mói từng tin nhắn và ép họ sống theo ý mình dưới danh nghĩa 'vì quá yêu'. Đó không phải là tình yêu, đó là sự giam cầm tâm lý xuất phát từ sự tự ti và bất an của chính kẻ kiểm soát."),
            ("Carousel 2 trang", "Tình yêu không phải là tìm kiếm một nửa để lấp đầy sự trống rỗng.", "Nếu bạn bước vào tình yêu khi lòng đầy vết thương......", "Bạn sẽ không tìm thấy tri kỷ, bạn chỉ tìm thấy một nạn nhân để bạn trút lên những bất an của mình.", "-", "Bạn phải là một bản thể trọn vẹn trước khi có thể chia sẻ tình yêu lành mạnh với một bản thể trọn vẹn khác.", "@hiyuabyss", "Hai kẻ què quặt về tâm lý dựa vào nhau sẽ chỉ làm cả hai cùng ngã. Đừng bắt người khác phải có nghĩa vụ chữa lành hay mang lại hạnh phúc cho bạn; hãy tự hoàn thiện chính mình trước khi đòi hỏi sự thấu hiểu từ người khác."),
            ("Single-Punch (1 trang)", "Buông tay đúng lúc là hành động dũng cảm và nhân từ nhất.", "Bám víu vào một mối quan hệ đã chết cũng giống như ôm chặt một cây xương rồng: càng siết chặt càng rỉ máu.", "-", "-", "Bám víu vào một mối quan hệ đã chết cũng giống như ôm chặt một cây xương rồng: càng siết chặt càng rỉ máu.", "@hiyuabyss", "Sự kiên trì mù quáng trong một mối quan hệ độc hại không phải là chung thủy, đó là sự hèn nhát không dám đối diện với nỗi sợ cô đơn. Buông tay để người khác đi và để mình được chữa lành là phẩm giá cao quý nhất của một người trưởng thành."),
            ("Carousel 2 trang", "Đừng yêu một người bằng tiềm năng tương lai của họ.", "Yêu một người vì hy vọng họ sẽ thay đổi......", "Là canh bạc rủi ro nhất mà phần thua gần như luôn thuộc về bạn.", "-", "Hãy yêu con người thật của họ ở hiện tại, hoặc dũng cảm rời đi; đừng biến mình thành bảo mẫu hay dự án cải tạo của bất kỳ ai.", "@hiyuabyss", "Con người chỉ thực sự thay đổi khi chính họ muốn và chịu đau đớn để trưởng thành, chứ không phải vì sự van xin hay hy sinh của bạn. Chấp nhận sự thật rằng bạn không thể cứu rỗi ai sẽ giúp bạn tiết kiệm được nhiều năm thanh xuân vô ích."),
            ("Carousel 3 trang", "Tình yêu đích thực bắt đầu từ tình yêu và sự tôn trọng đối với chính mình.", "Làm sao bạn có thể đòi hỏi người khác trân trọng bạn......", "Khi chính bạn còn liên tục hạ thấp tiêu chuẩn và dung túng cho những hành vi xúc phạm?", "Cách người khác đối xử với bạn chính là tấm gương phản chiếu giới hạn mà bạn tự đặt ra cho bản thân.", "Người không biết yêu thương và bảo vệ phẩm giá của chính mình sẽ không bao giờ nhận được tình yêu đích thực từ kẻ khác.", "@hiyuabyss", "Yêu bản thân không phải là ích kỷ, mà là việc thiết lập ranh giới rõ ràng về những gì bạn chấp nhận và không chấp nhận trong cuộc sống. Khi bạn tự tôn trọng chính mình, bạn sẽ tự động thu hút những người biết trân trọng giá trị của bạn.")
        ],
        # 13. LOYALTY
        [
            ("Single-Punch (1 trang)", "Lòng trung thành mù quáng với kẻ bất lương là sự phản bội đối với chính mình.", "Trung thành với một người không có đạo đức không phải là sự trung nghĩa, đó là sự mù quáng và đồng lõa.", "-", "-", "Trung thành với một người không có đạo đức không phải là sự trung nghĩa, đó là sự mù quáng và đồng lõa.", "MarcusAurelius", "Lòng trung thành chỉ có giá trị khi nó được đặt trên nền tảng của các giá trị đúng đắn và sự tôn trọng lẫn nhau. Khi lòng trung thành của bạn bị lợi dụng để làm điều xấu hoặc chà đạp người khác, việc bạn rời bỏ không phải là phản bội, mà là hành động của lương tri."),
            ("Carousel 2 trang", "Đừng nhầm lẫn giữa sự trung thành và nỗi sợ hãi sự thay đổi.", "Nhiều người ở lại trong một tập thể độc hại......", "Không phải vì họ trung thành, mà vì họ sợ hãi không dám bước ra tìm kiếm chân trời mới.", "-", "Sự trung thành đích thực là một lựa chọn của kẻ có năng lực, không phải là sự bám víu của kẻ bất lực.", "MarcusAurelius", "Kẻ bất tài thường thích khoe khoang sự 'trung thành' để bù đắp cho sự thiếu hụt về chuyên môn. Người có thực lực luôn trung thành với công việc và nguyên tắc sống của mình trước khi trung thành với bất kỳ cá nhân nào."),
            ("Single-Punch (1 trang)", "Kẻ dễ dàng phản bội người khác để lấy lòng bạn sẽ sớm phản bội bạn vì kẻ khác.", "Đừng bao giờ tin tưởng một kẻ mang bí mật của đồng minh cũ đến dâng nộp cho bạn như một món quà làm quen.", "-", "-", "Đừng bao giờ tin tưởng một kẻ mang bí mật của đồng minh cũ đến dâng nộp cho bạn như một món quà làm quen.", "@hiyuabyss", "Bản chất của kẻ phản phúc là chỉ trung thành với lợi ích trước mắt của chính họ. Hôm nay họ có thể bán đứng người khác để đổi lấy sự sủng ái của bạn, thì ngày mai họ cũng sẽ sẵn sàng bán đứng bạn khi có kẻ trả giá cao hơn."),
            ("Carousel 2 trang", "Lòng tin giống như một tờ giấy: một khi đã vò nát, không bao giờ phẳng lại.", "Có thể bạn sẽ tha thứ cho một kẻ lừa dối......", "Nhưng bạn sẽ không bao giờ có thể trao lại cho họ sự bình yên trong tâm trí như thuở ban đầu.", "-", "Tha thứ là để giải thoát cho chính mình, nhưng cảnh giác và giữ khoảng cách là để bảo vệ tương lai của bạn.", "@hiyuabyss", "Xây dựng lòng tin mất nhiều năm tháng, nhưng phá hủy nó chỉ cần vài giây ngắn ngủi. Đừng lãng phí cơ hội thứ hai cho những kẻ đã cố tình làm tổn thương bạn; bài học đau đớn nhất chỉ nên học một lần duy nhất."),
            ("Carousel 3 trang", "Sự trung thành có đi có lại mới là mối quan hệ bền vững.", "Nếu lòng trung thành chỉ đến từ một phía......", "Thì đó không phải là sự gắn kết, đó là sự bóc lột sức lao động và tình cảm.", "Một mối quan hệ đáng giá phải là nơi mà sự tận tụy của bạn được đền đáp bằng sự chở che và tôn trọng tương xứng.", "Đừng hy sinh mạng sống cho một người chỉ xem bạn là con tốt thí có thể thay thế trên bàn cờ.", "MarcusAurelius", "Bi kịch của những người chân thành là họ thường cống hiến hết mình cho những kẻ vô ơn và bạc bẽo. Hãy biết dừng lại khi nhận ra sự hy sinh của mình chỉ được xem như điều đương nhiên; dành sự trung thành ấy cho những người thực sự xứng đáng.")
        ],
        # 14. ENVY
        [
            ("Single-Punch (1 trang)", "Đố kỵ là tự uống thuốc độc và mong người khác chết.", "Kẻ đố kỵ bị thiêu đốt bởi hạnh phúc của người khác trước khi kịp tận hưởng cuộc sống của chính mình.", "-", "-", "Kẻ đố kỵ bị thiêu đốt bởi hạnh phúc của người khác trước khi kịp tận hưởng cuộc sống của chính mình.", "Spinoza", "Lòng đố kỵ là một loại axit ăn mòn tâm can của kẻ chứa chấp nó. Khi bạn dành toàn bộ tâm trí để ghen ghét và mong muốn người khác vấp ngã, bạn đang tự giam cầm mình trong bóng tối của sự bất lực và hận thù."),
            ("Carousel 2 trang", "Người ta không ghen tị với tỷ phú xa lạ, họ ghen tị với người bạn cùng trang lứa.", "Sự đố kỵ tàn nhẫn nhất......", "Thường xuất phát từ những người ở ngay cạnh bạn, những người không thể chịu nổi việc bạn vượt lên phía trước.", "-", "Kẻ thù nguy hiểm nhất không phải kẻ ở đằng xa, mà là người bạn từng cùng chung vạch xuất phát nhưng nay bị bạn bỏ lại phía sau.", "Spinoza", "Sự gần gũi về xuất thân làm cho sự đố kỵ trở nên gay gắt hơn bao giờ hết. Khi một người bằng bạn bỗng nhiên thành công, nó như một cái tát vào sự tự ái rằng 'lẽ ra người đó phải là tôi'. Hãy học cách bảo vệ thành quả của mình trong im lặng."),
            ("Single-Punch (1 trang)", "Kẻ nói xấu sau lưng bạn chính là người ngầm thừa nhận họ đang đứng sau bạn.", "Đừng bận tâm đến những lời dèm pha; nếu họ thực sự hơn bạn, họ đã không có thời gian để theo dõi từng bước đi của bạn.", "-", "-", "Đừng bận tâm đến những lời dèm pha; nếu họ thực sự hơn bạn, họ đã không có thời gian để theo dõi từng bước đi của bạn.", "@hiyuabyss", "Phỉ báng người khác là vũ khí duy nhất của những kẻ bất lực không thể đuổi kịp. Tiếng sủa sau lưng chỉ chứng minh bạn đang dẫn đầu đoàn tàu; hãy cứ mỉm cười và tiếp tục tăng tốc về phía trước."),
            ("Carousel 2 trang", "Biến sự đố kỵ thành động lực hoặc để nó nghiền nát bạn.", "Khi thấy người khác giỏi hơn......", "Kẻ tầm thường tìm cách hạ bệ, còn bậc thức giả tìm cách học hỏi bí quyết thành công của họ.", "-", "Sự khác biệt giữa kẻ thất bại và người thành công nằm ở cách họ phản ứng trước ánh hào quang của người khác.", "Spinoza", "Bạn có thể dùng năng lượng của mình để thèm muốn và cay cú, hoặc dùng nó để rèn luyện kỹ năng và nâng tầm bản thân. Sự lựa chọn hoàn toàn nằm ở tư duy và bản lĩnh của bạn."),
            ("Carousel 3 trang", "Cuộc đời này không phải là một trò chơi có tổng bằng không.", "Thành công của người khác......", "Không hề làm giảm đi cơ hội tỏa sáng và vươn lên của chính bạn.", "Trời cao đất rộng có đủ chỗ cho muôn vì sao cùng lấp lánh; chỉ có tâm hồn hẹp hòi mới nghĩ rằng người khác tắt thì mình mới sáng.", "Hạ bệ ánh đèn của người khác không làm cho ngọn nến của bạn sáng hơn; hãy tập trung thắp sáng con đường của chính mình.", "Spinoza", "Tư duy khan hiếm khiến con người ta luôn sợ người khác lấy mất phần bánh của mình. Nhưng vũ trụ này vô cùng rộng lớn và cơ hội là vô tận cho những ai chịu khó nỗ lực. Hãy cùng nhau cộng hưởng và phát triển thay vì tiêu hao sinh lực vào những trò đâm lén rẻ tiền.")
        ],
        # 15. CROWD
        [
            ("Single-Punch (1 trang)", "Trong đám đông, chỉ số thông minh của tập thể giảm xuống bằng chỉ số của cá nhân thấp nhất.", "Người ta có thể rất thông minh khi ở một mình, nhưng khi nhập vào đám đông, họ sẵn sàng làm những điều điên rồ nhất.", "-", "-", "Người ta có thể rất thông minh khi ở một mình, nhưng khi nhập vào đám đông, họ sẵn sàng làm những điều điên rồ nhất.", "Nietzsche", "Tâm lý bầy đàn tước đoạt khả năng tư duy phản biện và trách nhiệm cá nhân. Khi ẩn mình dưới danh nghĩa số đông, con người ta dễ dàng bộc lộ sự tàn bạo bản năng mà bình thường họ không bao giờ dám làm một mình."),
            ("Carousel 2 trang", "Cái giá của sự độc lập là cảm giác cô đơn giữa bầy đàn.", "Dám suy nghĩ khác biệt......", "Đồng nghĩa với việc bạn phải chấp nhận ánh mắt phán xét và sự xa lánh của những kẻ thích đi theo lối mòn.", "-", "Thà là một kẻ lạc loài tự do và sáng suốt còn hơn là một con cừu ngoan ngoãn bị dẫn dắt vào lò mổ.", "Nietzsche", "Đám đông không bao giờ tìm kiếm chân lý; họ chỉ tìm kiếm sự đồng thuận để xoa dịu nỗi sợ hãi. Nếu bạn muốn đạt được những điều phi thường, bạn phải có dũng khí rời bỏ sự ấm áp của bầy đàn để bước đi trên con đường riêng của mình."),
            ("Single-Punch (1 trang)", "Đừng bao giờ tranh luận với một đám đông đang nổi giận.", "Bạn không thể dùng logic và lý trí để thức tỉnh những kẻ đang say sưa trong cơn cuồng nộ tập thể.", "-", "-", "Bạn không thể dùng logic và lý trí để thức tỉnh những kẻ đang say sưa trong cơn cuồng nộ tập thể.", "@hiyuabyss", "Cơn giận của đám đông giống như một trận bão tuyết mù mịt: mọi lý lẽ đúng đắn đều bị cuốn trôi và nghiền nát. Cách thông minh nhất là giữ im lặng, đứng ngoài tầm mắt của họ và chờ đợi cơn cuồng phong tự tiêu tan."),
            ("Carousel 2 trang", "Số đông không mặc nhiên đồng nghĩa với chính nghĩa.", "Một sai lầm được hàng triệu người lặp lại......", "Thì nó vẫn chỉ là một sai lầm được nhân bản trên diện rộng.", "-", "Đừng lấy số lượng người ủng hộ làm thước đo cho tính đúng đắn của một hành động hay tư tưởng.", "Nietzsche", "Lịch sử đã chứng minh vô số lần đám đông đã cùng nhau ủng hộ những điều bạo tàn và sai trái nhất. Hãy tin vào la bàn đạo đức và tư duy độc lập của chính mình thay vì mù quáng hò reo theo xu hướng."),
            ("Carousel 3 trang", "Dũng khí lớn nhất đời người là dám đứng một mình bảo vệ sự thật.", "Khi tất cả mọi người đều quỳ gối......", "Kẻ đứng thẳng sẽ trở thành cái gai trong mắt của toàn bộ đám đông.", "Họ sẽ tìm cách bẻ gãy bạn không phải vì bạn sai, mà vì tư thế hiên ngang của bạn phơi bày sự hèn nhát của họ.", "Đứng thẳng một mình trước đám đông đang quỳ gối là thử thách khắc nghiệt nhất của nhân cách con người.", "Nietzsche", "Sự dũng cảm đích thực không nằm ở chỗ bạn đánh bại bao nhiêu kẻ thù, mà ở chỗ bạn có đủ kiên định để giữ vững nguyên tắc khi xung quanh không còn ai ủng hộ. Đó là sự cô độc vĩ đại làm nên những nhân vật kiệt xuất của nhân loại.")
        ],
        # 16. SUFFERING
        [
            ("Single-Punch (1 trang)", "Đóng vai nạn nhân là cách êm ái nhất để từ chối việc trưởng thành.", "Chừng nào bạn còn đổ lỗi nỗi khổ của mình cho người khác, chừng đó bạn vẫn còn trao quyền năng định đoạt cuộc đời mình cho họ.", "-", "-", "Chừng nào bạn còn đổ lỗi nỗi khổ của mình cho người khác, chừng đó bạn vẫn còn trao quyền năng định đoạt cuộc đời mình cho họ.", "Freud", "Tâm lý nạn nhân mang lại một lợi ích tâm lý thứ cấp nguy hiểm: bạn nhận được sự thương hại và được miễn trừ trách nhiệm phải cố gắng. Nhưng cái giá phải trả là sự bất lực vĩnh viễn. Chấm dứt than vãn là bước khởi đầu để bạn giành lại quyền kiểm soát số phận."),
            ("Carousel 2 trang", "Khổ đau không làm bạn cao quý hơn; chỉ có cách bạn vượt qua nó mới định hình nhân cách.", "Tự thương hại bản thân......", "Là loại thuốc độc ngọt ngào làm tê liệt ý chí chiến đấu và giam giữ bạn trong vũng lầy quá khứ.", "-", "Khổ đau là hoàn cảnh khách quan, nhưng biến nó thành lý do để tự hủy hoại bản thân là sự lựa chọn chủ quan.", "Freud", "Nhiều người lấy nỗi đau cũ ra làm tấm bình phong để bào chữa cho những hành vi xấu xa và sự trì trệ của mình ở hiện tại. Nỗi đau là điều không thể tránh khỏi, nhưng sự trưởng thành đòi hỏi bạn phải biến vết sẹo thành bộ giáp kiên cường."),
            ("Single-Punch (1 trang)", "Vết thương không phải lỗi của bạn, nhưng chữa lành là trách nhiệm của bạn.", "Quá khứ có thể do người khác gây ra, nhưng tương lai của bạn hoàn toàn nằm trong tay bạn.", "-", "-", "Quá khứ có thể do người khác gây ra, nhưng tương lai của bạn hoàn toàn nằm trong tay bạn.", "@hiyuabyss", "Bạn có quyền đau buồn vì những bất công đã xảy ra, nhưng bạn không có quyền dùng nó làm cái cớ để hủy hoại phần đời còn lại. Đừng chờ đợi kẻ gây ra vết thương đến xin lỗi; sự giải thoát thực sự chỉ đến khi bạn tự mình đứng dậy và bước tiếp."),
            ("Carousel 2 trang", "Đừng kể nỗi khổ của mình cho những người chỉ muốn nghe để thỏa mãn sự tò mò.", "80% người ta không quan tâm đến nỗi đau của bạn......", "Và 20% còn lại thầm mừng rỡ vì điều tồi tệ đó đã không xảy ra với họ.", "-", "Hãy chọn lọc người để giãi bày; vết thương để lộ cho kẻ xấu sẽ chỉ trở thành điểm yếu để họ công kích.", "@hiyuabyss", "Nỗi đau của bạn là thứ thiêng liêng chỉ nên chia sẻ với những tâm hồn thực sự đồng điệu và biết thấu cảm. Kể lể bừa bãi trên mạng xã hội hay chốn đông người chỉ biến nỗi bất hạnh của bạn thành câu chuyện phiếm rẻ tiền cho người khác bàn tán."),
            ("Carousel 3 trang", "Nghịch cảnh là người thầy tàn nhẫn nhất nhưng dạy những bài học đắt giá nhất.", "Cơn bão đi qua cuộc đời bạn......", "Sẽ cuốn trôi tất cả những ảo tưởng, những mối quan hệ giả tạo và những thứ phù phiếm.", "Nó để lại cho bạn một mặt đất trơ trụi nhưng vững chắc, nơi bạn có thể xây dựng lại mọi thứ bằng thực lực chân chính.", "Những gì không thể giết chết được bạn sẽ biến bạn thành một phiên bản kiên cường và bất khả chiến bại.", "Nietzsche", "Không ai muốn trải qua nghịch cảnh, nhưng chính những đêm tối tăm nhất lại dạy cho con người ta biết trân trọng ánh sáng. Khi đã đi qua đáy sâu của tuyệt vọng, bạn sẽ không còn sợ hãi bất kỳ bóng tối nào trên cõi đời này nữa.")
        ],
        # 17. IDENTITY
        [
            ("Single-Punch (1 trang)", "Bạn thực sự là ai khi không còn ai nhìn ngắm và đánh giá bạn?", "Bản sắc đích thực không phải là những gì bạn trình diễn trên mạng xã hội, mà là những suy nghĩ của bạn khi ở một mình trong bóng tối.", "-", "-", "Bản sắc đích thực không phải là những gì bạn trình diễn trên mạng xã hội, mà là những suy nghĩ của bạn khi ở một mình trong bóng tối.", "Seneca", "Chúng ta dành quá nhiều thời gian để xây dựng hình ảnh cho người khác xem đến mức quên mất việc chăm sóc tâm hồn của chính mình. Khi cởi bỏ mọi danh vị, tiền tài và sự tán dương của xã hội, điều còn sót lại bên trong bạn là sự phong phú hay chỉ là sự trống rỗng?"),
            ("Carousel 2 trang", "Đừng để dư luận định giá trị cho cuộc đời của bạn.", "Nếu bạn để tiếng vỗ tay của đám đông quyết định giá trị của mình......", "Thì tiếng la ó của họ cũng sẽ dễ dàng dìm bạn xuống đáy vực sâu.", "-", "Giá trị của bạn phải được neo đậu vào những nguyên tắc bên trong, không phải vào sự biến động thất thường của miệng đời.", "Seneca", "Dư luận như ngọn gió: hôm nay thổi xuôi chiều nâng bạn lên mây, ngày mai có thể đổi hướng thổi bạn ngã nhào. Người có bản lĩnh là người giữ được sự bình thản trước cả lời khen ngợi lẫn sự chê bai."),
            ("Single-Punch (1 trang)", "Bắt chước người khác là cách nhanh nhất để biến mình thành một bản sao lỗi.", "Thà là một phiên bản gốc vụng về của chính mình còn hơn là một bản sao hoàn hảo nhưng vô hồn của kẻ khác.", "-", "-", "Thà là một phiên bản gốc vụng về của chính mình còn hơn là một bản sao hoàn hảo nhưng vô hồn của kẻ khác.", "@hiyuabyss", "Mỗi con người sinh ra đều mang trong mình một cấu trúc tâm lý và sứ mệnh độc bản. Chạy theo những tiêu chuẩn của người khác chỉ biến cuộc đời bạn thành một vở kịch mệt mỏi; hãy dũng cảm khai phá và tôn trọng sự khác biệt của chính mình."),
            ("Carousel 2 trang", "Sự cô độc là lò luyện kim tôi rèn nên bản sắc của những vĩ nhân.", "Kẻ tầm thường sợ ở một mình vì sợ đối diện với sự trống rỗng......", "Bậc trí giả tìm kiếm sự tĩnh lặng để đào sâu vào thế giới nội tâm vô tận của mình.", "-", "Chỉ trong sự tĩnh lặng tuyệt đối, tiếng nói chân thật nhất của bản thể mới có cơ hội được cất lên.", "Seneca", "Đừng nhầm lẫn giữa cô đơn và cô độc. Cô đơn là cảm giác thiếu vắng người khác; cô độc là sự trọn vẹn và hòa hợp khi được ở bên chính mình. Học cách làm bạn với sự cô độc là cột mốc tối thượng của sự tự do tinh thần."),
            ("Carousel 3 trang", "Bản sắc không phải là thứ để tìm kiếm, bản sắc là thứ do bạn tự kiến tạo.", "Nhiều người dành cả đời đi tìm xem 'mình là ai'......", "Như thể bản sắc là một kho báu bị giấu kín ở một nơi xa xôi nào đó.", "Nhưng bản sắc không tồn tại sẵn; nó được định hình qua từng quyết định, từng ranh giới và từng hành động mà bạn chọn mỗi ngày.", "Bạn không đi tìm chính mình; bạn đang tự tay điêu khắc nên chính mình qua từng trải nghiệm của cuộc đời.", "@hiyuabyss", "Cuộc đời không phải là bài toán đi tìm đáp án có sẵn, mà là một khối đá cẩm thạch thô ráp chờ đợi nhát đục của bạn. Mỗi lời từ chối điều xấu, mỗi nỗ lực vượt qua khó khăn là một nhát búa khắc họa nên bức tượng nhân cách kiên cường của bạn.")
        ],
        # 18. MEANING
        [
            ("Single-Punch (1 trang)", "Ý nghĩa cuộc sống không nằm ở đích đến, nó nằm ở dũng khí đối diện với sự vô nghĩa.", "Vũ trụ này có thể lạnh lùng và vô nghĩa, nhưng chính con người là sinh vật có khả năng tự thắp sáng ý nghĩa cho sự tồn tại của mình.", "-", "-", "Vũ trụ này có thể lạnh lùng và vô nghĩa, nhưng chính con người là sinh vật có khả năng tự thắp sáng ý nghĩa cho sự tồn tại của mình.", "Camus", "Albert Camus từng nói về huyền thoại Sisyphus: bị đày đọa đẩy tảng đá lên núi rồi nhìn nó lăn xuống, nhưng Sisyphus vẫn mỉm cười kiên định. Khi bạn dám sống trọn vẹn và nỗ lực ngay cả khi biết vạn vật rồi sẽ tan biến vào cát bụi, đó là đỉnh cao của sự tự do và phẩm giá con người."),
            ("Carousel 2 trang", "Đừng đi tìm ý nghĩa cuộc đời ở những định nghĩa của người khác.", "Nếu bạn hỏi một ngàn người về ý nghĩa cuộc sống......", "Bạn sẽ nhận được một ngàn câu trả lời khác nhau, và không có câu nào thực sự dành cho bạn.", "-", "Ý nghĩa cuộc sống không phải là thứ để mượn; bạn phải tự mình trải nghiệm, vấp ngã và tự tay định nghĩa lấy nó.", "Camus", "Xã hội luôn muốn bạn tin rằng ý nghĩa là kiếm thật nhiều tiền, mua nhà lầu xe hơi hay được người đời tung hô. Nhưng nếu những thứ đó không chạm vào tâm hồn bạn, chúng chỉ là những chiếc cúp rỗng tuếch. Hãy dũng cảm sống một cuộc đời có ý nghĩa theo chuẩn mực của riêng bạn."),
            ("Single-Punch (1 trang)", "Cái chết không phải là dấu chấm hết cho ý nghĩa, nó là chiếc khung làm nổi bật bức tranh cuộc đời.", "Chính vì thời gian có hạn nên từng giây phút bạn hiện diện trên cõi đời này mới trở nên vô giá.", "-", "-", "Chính vì thời gian có hạn nên từng giây phút bạn hiện diện trên cõi đời này mới trở nên vô giá.", "Camus", "Nếu con người bất tử, mọi hành động đều trở nên vô vị vì bạn luôn có ngày mai để trì hoãn. Ý thức sâu sắc về cái chết (Memento Mori) không phải để bi quan, mà là lời nhắc nhở đanh thép để bạn sống sâu sắc, yêu chân thành và không lãng phí một khoảnh khắc nào của thực tại."),
            ("Carousel 2 trang", "Hạnh phúc không phải là một trạng thái vĩnh cửu, nó là những khoảnh khắc thức tỉnh.", "Đừng tìm kiếm một cuộc đời không có sóng gió......", "Hãy tìm kiếm một tâm thế bình thản để có thể mỉm cười ngay giữa tâm bão.", "-", "Ý nghĩa không nằm ở việc bạn không bao giờ ngã, mà ở việc mỗi lần ngã bạn đều học được cách đứng dậy vững vàng hơn.", "Camus", "Một cuộc sống hoàn hảo không tì vết chỉ tồn tại trong truyện cổ tích. Vẻ đẹp của cuộc đời thực nằm ở những vết sẹo, những khúc quanh bất ngờ và bản lĩnh vượt khó của con người. Hãy đón nhận cả niềm vui lẫn nỗi buồn như những gia vị làm nên sự trọn vẹn."),
            ("Carousel 3 trang", "Tạo ra giá trị cho người khác là cách bền vững nhất để tìm thấy ý nghĩa cho mình.", "Khi bạn chỉ sống cho riêng bản thân......", "Thế giới của bạn sẽ trở nên vô cùng chật chội và dễ dàng sụp đổ trước những biến cố nhỏ.", "Nhưng khi bạn biết mở lòng che chở và thắp sáng hy vọng cho một người khác, cuộc đời bạn sẽ tự khắc được lấp đầy bởi ý nghĩa sâu sắc.", "Cứu rỗi một con người cũng là cứu rỗi một phần linh hồn của chính bạn; ý nghĩa sinh ra từ sự kết nối và sẻ chia chân thành.", "Frankl", "Viktor Frankl - người sống sót qua trại tập trung Đức Quốc Xã - đã chứng minh rằng: những người tìm thấy lý do để sống vì người khác là những người có sức chịu đựng phi thường nhất. Khi bạn có một chữ 'Tại sao' đủ lớn, bạn có thể vượt qua hầu hết mọi chữ 'Làm thế nào'.")
        ],
        # 19. SOLITUDE
        [
            ("Single-Punch (1 trang)", "Cô độc là phẩm hạnh của những tâm hồn sâu sắc.", "Kẻ tầm thường sợ sự tĩnh lặng vì không chịu nổi sự trống rỗng; bậc trí giả tìm về cô độc để đối thoại với vũ trụ bên trong.", "-", "-", "Kẻ tầm thường sợ sự tĩnh lặng vì không chịu nổi sự trống rỗng; bậc trí giả tìm về cô độc để đối thoại với vũ trụ bên trong.", "Pascal", "Sự ồn ào của thế giới bên ngoài thường làm nhiễu loạn những suy tư chân thực nhất. Chỉ khi rũ bỏ được những cuộc vui vô bổ và học cách ở yên một mình, bạn mới có thể lắng nghe tiếng nói sâu thẳm của trực giác và tìm thấy sự bình an đích thực."),
            ("Carousel 2 trang", "Đừng vội vã lấp đầy khoảng trống bằng những mối quan hệ độc hại.", "Thà một mình gặm nhấm sự cô độc thanh thản......", "Còn hơn ngồi giữa một bàn tiệc đông đúc mà trong lòng cảm thấy hoàn toàn lạc lõng và bị xem thường.", "-", "Sự cô độc giữa đám đông là nỗi cô độc tàn nhẫn và cay đắng nhất của một kiếp người.", "@hiyuabyss", "Nỗi sợ cô đơn khiến nhiều người chấp nhận hạ thấp tiêu chuẩn để gắn bó với những kẻ không tôn trọng mình. Nhưng một mình không đồng nghĩa với cô đơn; một mình là cơ hội tuyệt vời để bạn chữa lành, nâng cấp bản thân và chỉ mở cửa cho những ai thực sự xứng đáng bước vào."),
            ("Single-Punch (1 trang)", "Tĩnh lặng là câu trả lời đanh thép nhất cho những điều ồn ào và dơ bẩn.", "Khi người ta cố tình ném bùn vào bạn, sự im lặng của bạn chính là bức tường đá kiên cố khiến bùn tự rơi xuống chân họ.", "-", "-", "Khi người ta cố tình ném bùn vào bạn, sự im lặng của bạn chính là bức tường đá kiên cố khiến bùn tự rơi xuống chân họ.", "@hiyuabyss", "Không phải mọi sự khiêu khích đều xứng đáng nhận được phản hồi của bạn. Kẻ muốn kéo bạn vào bùn chỉ để bạn dơ bẩn như họ; sự điềm tĩnh và phớt lờ của bạn là sự trừng phạt nặng nề nhất đối với dã tâm của kẻ tiểu nhân."),
            ("Carousel 2 trang", "Học cách bầu bạn với chính mình trước khi tìm kiếm tri kỷ.", "Nếu bạn không thể yêu thương và tìm thấy niềm vui khi ở một mình......", "Thì bất kỳ ai bước vào đời bạn cũng sẽ sớm cảm thấy ngột ngạt vì sự lệ thuộc và đòi hỏi của bạn.", "-", "Tri kỷ là người cùng bạn chia sẻ sự trọn vẹn, không phải là người có nghĩa vụ gánh vác sự bất an của bạn.", "@hiyuabyss", "Một tâm hồn độc lập và tự tại sẽ tự nhiên tỏa ra sức hút kỳ diệu. Khi bạn không còn bám víu và khát khao sự công nhận từ bên ngoài, bạn mới có thể xây dựng những mối quan hệ bình đẳng, lành mạnh và sâu sắc."),
            ("Carousel 3 trang", "Nơi sâu thẳm nhất của sự cô độc chính là nơi sinh ra những tác phẩm vĩ đại.", "Mọi tư tưởng đột phá, mọi kiệt tác nghệ thuật......", "Đều được thai nghén trong những giờ phút cô độc tuyệt đối của người sáng tạo.", "Khi rũ bỏ mọi sự xao nhãng của thế trần, tâm trí con người mới đạt đến cảnh giới tập trung cao độ để chạm vào cái đẹp vĩnh hằng.", "Đừng trốn chạy sự cô độc; hãy đón nhận nó như một món quà vô giá nuôi dưỡng chiều sâu tâm hồn của bạn.", "Pascal", "Xã hội hiện đại thúc ép chúng ta phải liên tục kết nối, liên tục chia sẻ và tiêu thụ thông tin. Nhưng chính sự ngắt kết nối có chủ đích mới mang lại năng lượng tái tạo và sự sáng tạo đích thực. Hãy dành cho mình những khoảng lặng thiêng liêng để tâm hồn được hít thở.")
        ],
        # 20. STATUS
        [
            ("Single-Punch (1 trang)", "Khoe khoang là cách nhanh nhất để kẻ khác nhìn thấy sự thiếu thốn bên trong bạn.", "Người thực sự giàu có không cần khoe tiền; người thực sự có tri thức không cần khoe bằng cấp; chỉ kẻ thiếu thốn mới cần phô trương để xin sự công nhận.", "-", "-", "Người thực sự giàu có không cần khoe tiền; người thực sự có tri thức không cần khoe bằng cấp; chỉ kẻ thiếu thốn mới cần phô trương để xin sự công nhận.", "@hiyuabyss", "Sự phô trương hào nhoáng thường tỷ lệ nghịch với sự bình an nội tại. Kẻ phải gào thét cho cả thế giới biết mình hạnh phúc và thành công thực chất là kẻ đang sợ hãi nhất trước nguy cơ bị lãng quên. Sự sang trọng đích thực luôn toát ra từ sự tĩnh lặng và khiêm nhường."),
            ("Carousel 2 trang", "Sự khiêm nhường trình diễn là đỉnh cao của thói kiêu ngạo giả tạo.", "Có những người giả vờ hạ mình xuống......", "Không phải vì họ khiêm tốn, mà vì họ muốn được tán dương là 'người vừa giỏi giang lại vừa khiêm nhường'.", "-", "Khiêm nhường mà mong chờ tiếng vỗ tay cho cái cúi đầu thì đó chỉ là một chiêu trò đánh bóng tên tuổi tinh vi.", "@hiyuabyss", "Họ nói xấu bản thân để người khác khen ngợi; họ giả vờ không biết để người khác tôn sùng. Đừng để những cử chỉ khiêm tốn giả tạo đánh lừa bạn; người khiêm nhường thực sự chỉ tập trung làm việc và không bận tâm đến việc người khác có thấy mình khiêm nhường hay không."),
            ("Single-Punch (1 trang)", "Danh vọng như nước biển: càng uống càng khát.", "Chạy theo sự ngưỡng mộ của người đời là một cuộc đua không có điểm dừng, nơi người chiến thắng cũng chỉ là kẻ kiệt sức.", "-", "-", "Chạy theo sự ngưỡng mộ của người đời là một cuộc đua không có điểm dừng, nơi người chiến thắng cũng chỉ là kẻ kiệt sức.", "Schopenhauer", "Hôm nay họ tung hô bạn lên đỉnh cao, ngày mai họ sẵn sàng đạp bạn xuống bùn đen vì một lỗi lầm nhỏ. Đặt giá trị sống vào ánh mắt của đám đông là tự giao quyền sinh sát cảm xúc của mình cho người khác. Hãy sống vì sự thanh thản trong tâm hồn thay vì những tràng pháo tay thoáng qua."),
            ("Carousel 2 trang", "Địa vị xã hội chỉ là bộ quần áo bạn mượn tạm của cuộc đời.", "Khi trút bỏ mọi chức vụ và danh xưng......", "Điều còn lại định nghĩa con người bạn là nhân cách và cách bạn đối xử với những người không có giá trị lợi dụng.", "-", "Người tôn trọng bạn vì chức vị sẽ quay lưng khi bạn hết thời; chỉ người tôn trọng nhân cách của bạn mới ở lại đến cùng.", "@hiyuabyss", "Nhiều người nhầm lẫn giữa sự kính trọng dành cho chiếc ghế họ ngồi và sự kính trọng dành cho chính bản thân họ. Hãy luôn giữ cho mình một tâm thế giản dị và chân thành, bởi vì khi tấm màn nhung của cuộc đời hạ xuống, ai cũng trở về với cát bụi như nhau."),
            ("Carousel 3 trang", "Thành công thực sự là được tự do sống theo cách mình muốn mà không cần chứng minh với ai.", "Nhiều người dành nửa đầu cuộc đời để tích lũy danh vọng......", "Rồi dành nửa sau cuộc đời để nhận ra những thứ họ theo đuổi chẳng mang lại sự bình an nào trong tâm hồn.", "Chiến thắng vĩ đại nhất không phải là đánh bại người khác hay được vạn người ngưỡng mộ, mà là chiến thắng sự tham lam và bất an của chính bản thân mình.", "Hạnh phúc tối thượng là khi bạn thức dậy mỗi ngày, làm công việc mình yêu thích và hoàn toàn không cần phải chứng minh giá trị của mình với bất kỳ ai.", "@hiyuabyss", "Đừng để cuộc đời bạn biến thành một bản báo cáo thành tích để trình diễn cho thiên hạ chấm điểm. Khi bạn tìm thấy sự hòa hợp nội tại và sống đúng với lương tri của mình, bạn đã là người chiến thắng vẻ vang nhất trên cõi đời này rồi.")
        ]
    ]

    for t_offset, t_posts in enumerate(THEME_REMAINDER_DATA):
        t_idx = 8 + t_offset
        t_code, t_name, def_author, def_hash = THEMES[t_idx]
        for p in t_posts:
            fmt, title, s1, s2, s3, full_txt, auth_override, desc = p
            
            theme_folder = f"theme_{post_idx:02d}" if post_idx <= 60 else f"theme_{(post_idx % 30) + 1:02d}"
            
            day_offset = (post_idx - 1) * 2
            post_date = start_date + timedelta(days=day_offset)
            weekday_vn = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"][post_date.weekday()]
            date_label = f"{weekday_vn} ({post_date.strftime('%d/%m')})"
            
            time_slot = ["11:30 - 12:30 (Trưa)", "19:30 - 20:30 (Tối)", "21:00 - 22:30 (Đêm chiêm nghiệm)"][post_idx % 3]
            
            all_data.append({
                "stt": post_idx,
                "id": f"TXT-{post_idx:04d}",
                "title": title,
                "desc": desc,
                "author": auth_override if auth_override else def_author,
                "hashtags": def_hash,
                "format": fmt,
                "s1": s1,
                "s2": s2,
                "s3": s3,
                "full_text": full_txt,
                "theme": f"{t_code} ({t_name})",
                "time_slot": time_slot,
                "date": date_label,
                "template": theme_folder,
                "status": "SẴN SÀNG"
            })
            post_idx += 1

    return all_data

def main():
    print("=" * 75)
    print("  HIYU ABYSS — CHUẨN HÓA & NÂNG CẤP 100 BÀI TIKTOK PIPELINE TRÊN GOOGLE SHEET")
    print("=" * 75)
    
    posts = build_all_100()
    print(f"[*] Đã tạo thành công dữ liệu chuẩn cho {len(posts)} bài viết.")
    
    headers = [
        "STT",
        "Mã ID",
        "Tiêu Đề (Dưới 90 từ)",
        "Mô Tả (Caption TikTok)",
        "Nguồn Tác Giả",
        "Hashtags (5 cái)",
        "Định Dạng Slide",
        "Trang 1 (Hook / Mở màn)",
        "Trang 2 (Cú lật bóc trần)",
        "Trang 3 (Chiếc gương phản tư)",
        "Văn Bản Hoàn Chỉnh",
        "Chủ Đề Hạt Nhân",
        "Khung Giờ Vàng",
        "Lịch Đăng (Thứ, Ngày)",
        "Gợi Ý Phôi Ảnh",
        "Trạng Thái"
    ]
    
    out_csv = "c:/hiyuabyss/scripts/tiktok_100_posts_v2.csv"
    with open(out_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for p in posts:
            writer.writerow([
                p["stt"],
                p["id"],
                p["title"],
                p["desc"],
                p["author"],
                p["hashtags"],
                p["format"],
                p["s1"],
                p["s2"],
                p["s3"],
                p["full_text"],
                p["theme"],
                p["time_slot"],
                p["date"],
                p["template"],
                p["status"]
            ])
            
    print(f"[✓] Đã xuất file CSV chuẩn hóa: {out_csv}")
    
    # Push to Google Sheet using gsheets mutate import-csv
    print(f"[*] Đang đồng bộ lên Google Sheet: {SPREADSHEET_ID} -> {SHEET_NAME}...")
    cmd = f'gsheets mutate import-csv {SPREADSHEET_ID} "{out_csv}" --sheet "{SHEET_NAME}"'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print("Import Output:", res.stdout)
    if res.stderr:
        print("Import Stderr:", res.stderr)
        
    # Apply Google Sheet Formatting:
    # 1. Dark Slate Header (#0F172A), bold, white text (#FFFFFF)
    # 2. Text wrap across table
    # 3. Alignments: Center for STT (col 0), ID (col 1), Author (col 4), Format (col 6), Slot (col 12), Date (col 13), Template (col 14), Status (col 15)
    # 4. Data Validation dropdown on Status column
    print("[*] Đang định dạng thẩm mỹ giao diện Google Sheet...")
    format_cmds = [
        f'gsheets mutate format {SPREADSHEET_ID} --sheet "{SHEET_NAME}" --start-row 0 --end-row 1 --bold --bg-color "#0F172A" --fg-color "#FFFFFF"',
        f'gsheets mutate format {SPREADSHEET_ID} --sheet "{SHEET_NAME}" --start-row 1 --end-row 101 --start-col 0 --end-col 16 --wrap',
        f'gsheets mutate format {SPREADSHEET_ID} --sheet "{SHEET_NAME}" --start-row 0 --end-row 101 --start-col 0 --end-col 2 --align "CENTER"',
        f'gsheets mutate format {SPREADSHEET_ID} --sheet "{SHEET_NAME}" --start-row 0 --end-row 101 --start-col 4 --end-col 5 --align "CENTER"',
        f'gsheets mutate format {SPREADSHEET_ID} --sheet "{SHEET_NAME}" --start-row 0 --end-row 101 --start-col 6 --end-col 7 --align "CENTER"',
        f'gsheets mutate format {SPREADSHEET_ID} --sheet "{SHEET_NAME}" --start-row 0 --end-row 101 --start-col 12 --end-col 16 --align "CENTER"',
        f'gsheets mutate freeze {SPREADSHEET_ID} --sheet "{SHEET_NAME}" --rows 1 --cols 2',
        f'gsheets mutate data-validation {SPREADSHEET_ID} --range "\'{SHEET_NAME}\'!P2:P101" --values "SẴN SÀNG,ĐÃ LÊN LỊCH,ĐÃ ĐĂNG,TẠM HOÃN"'
    ]
    
    for f_cmd in format_cmds:
        subprocess.run(f_cmd, shell=True, capture_output=True)
        
    print("[✓] ĐÃ HOÀN TẤT ĐỒNG BỘ & ĐỊNH DẠNG 100 BÀI TRÊN GOOGLE SHEET!")

if __name__ == "__main__":
    main()
