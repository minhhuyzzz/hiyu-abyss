#!/usr/bin/env python3
"""
Hiyu Abyss — Full 100 Posts Generator & Google Sheets Importer
Tất cả 100 bài đều được viết độc lập, chi tiết:
- Slide 1: Hook mở màn HOÀN CHỈNH (không bị cắt đứt câu).
- Slide 2: Cú lật bóc trần HOÀN CHỈNH.
- Slide 3: Chiếc gương phản tư HOÀN CHỈNH.
- Độ dài tăng 5-10 từ, sâu lắng, đậm chất Hiyu Abyss, không sáo ngữ.
- Tiêu đề, Hashtags, Khung giờ vàng chuẩn xác.
"""

import csv
import subprocess
from datetime import datetime, timedelta

SPREADSHEET_ID = "1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY"

THEMES = [
    ("HYPOCRISY", "Đạo đức giả & Vẻ thánh thiện"),
    ("DOUBLE_STANDARD", "Tiêu chuẩn kép trong phán xét"),
    ("MORALITY", "Lòng tốt & Điều kiện ngầm"),
    ("EGO", "Bản ngã & Nhu cầu hơn người"),
    ("SELF_DECEPTION", "Sự tự lừa dối & Vùng an toàn"),
    ("SHADOW", "Bóng tối nội tâm & Sự chối bỏ"),
    ("MASK", "Mặt nạ xã hội & Sự trình diễn"),
    ("POWER", "Quyền lực & Kiểm soát ngầm"),
    ("MANIPULATION", "Thao túng tâm lý & Cảm giác tội lỗi"),
    ("FREEDOM", "Tự do & Nỗi sợ trách nhiệm"),
    ("TRUTH", "Sự thật & Những lời tự bào chữa"),
    ("LOVE", "Tình yêu, Gắn bó & Chiếm hữu"),
    ("LOYALTY", "Lòng trung thành & Ranh giới trả giá"),
    ("ENVY", "Đố kỵ & Sự so sánh ngầm"),
    ("CROWD", "Đám đông & Sự can đảm bầy đàn"),
    ("SUFFERING", "Khổ đau & Sự bám chấp vết thương"),
    ("IDENTITY", "Bản sắc khi không còn khán giả"),
    ("MEANING", "Ý nghĩa hiện sinh & Sự phi lý"),
    ("SOLITUDE", "Cô đơn & Nỗi sợ tĩnh lặng"),
    ("STATUS", "Danh vọng & Khiêm nhường trình diễn")
]

# Danh mục 100 bài chi tiết (20 chủ đề x 5 bài)
# Mỗi bài: [Title, Slide1_Hook, Slide2_Twist, Slide3_Reflect, FullText]
ALL_100_POSTS = [
    # 1. HYPOCRISY
    [
        "Tấm bình phong của sự thánh thiện",
        "Kẻ xấu luôn tìm cách khoác lên mình vẻ ngoài tử tế và đạo mạo nhất.",
        "Không phải vì họ muốn hướng thiện, mà vì sự tử tế là tấm bình phong an toàn nhất để che đậy dã tâm.",
        "Khi một người quá vội vã chứng minh mình thanh cao, hãy tự hỏi họ đang cần che giấu điều gì.",
        "Kẻ xấu luôn tìm cách khoác lên mình vẻ thánh thiện, không phải vì họ muốn hướng thiện, mà vì sự tử tế là tấm bình phong an toàn nhất để che đậy dã tâm."
    ],
    [
        "Khi lòng tốt đòi hỏi sự phục tùng",
        "Có bao giờ bạn nhận được sự giúp đỡ nhiệt tình, nhưng sau đó cảm thấy ngột ngạt?",
        "Có những ân huệ chỉ thực sự trở thành món nợ khi người nhận bắt đầu nói không. Sự giúp đỡ lúc ấy không phải là tình cảm, mà là khoản đầu tư mua sự phục tùng.",
        "Người ban ơn chân chính tôn trọng ranh giới của bạn; kẻ toan tính sẽ nhắc lại ơn nghĩa ngay khi bạn không chịu nghe lời.",
        "Có những ân huệ chỉ thực sự trở thành món nợ khi người nhận bắt đầu nói không; sự giúp đỡ trao đi lúc ấy không phải là tình cảm, mà là khoản đầu tư mua quyền kiểm soát."
    ],
    [
        "Nguyên tắc chỉ dành cho người khác",
        "Người thích rao giảng đạo đức thường là người sở hữu nhiều ngoại lệ nhất.",
        "Họ đặt ra những chuẩn mực khắt khe cho cả thế giới tuân theo, nhưng lại ngầm chuẩn bị sẵn cho mình một lối thoát an toàn khi phải trả giá.",
        "Đạo đức thực sự không nằm ở những điều ta bắt người khác làm, mà ở những điều ta sẵn sàng chịu thiệt thòi để giữ gìn.",
        "Người thích rao giảng đạo lý thường là người sở hữu nhiều ngoại lệ nhất; họ đặt ra chuẩn mực cho cả thiên hạ, nhưng lại ngầm chuẩn bị lối thoát riêng khi bản thân phải trả giá."
    ],
    [
        "Sự bao dung có tính toán",
        "Có những người tha thứ cho bạn rất nhanh, nhưng không bao giờ để bạn quên lỗi lầm.",
        "Họ giữ lại sự bao dung như một bằng chứng về lòng cao thượng, để mỗi khi tranh luận, bạn luôn là kẻ phải cúi đầu nhận tội.",
        "Sự tha thứ biến thành độc hại khi nó không nhằm hàn gắn vết thương, mà nhằm duy trì vị thế kẻ cả trên người khác.",
        "Có những người tha thứ cho bạn rất nhanh, nhưng không bao giờ để bạn quên lỗi lầm; họ giữ lại sự bao dung như một đặc quyền để bắt bạn cả đời phải mang cảm giác mắc nợ."
    ],
    [
        "Sự phẫn nộ đạo đức vay mượn",
        "Tại sao người ta lại hăng hái lên án kẻ khác trên mạng xã hội đến thế?",
        "Sự phẫn nộ đạo đức công khai thường là cách rẻ tiền nhất để cảm thấy mình lương thiện mà không cần phải thực hiện bất kỳ hành động tử tế nào ngoài đời thực.",
        "Khi ném đá một người, người ta không tìm kiếm công lý; họ tìm kiếm một tấm vé miễn trừ để quên đi những góc khuất xấu xí của chính mình.",
        "Sự phẫn nộ đạo đức công khai là cách rẻ tiền nhất để cảm thấy mình cao thượng mà không phải trả giá; ném đá kẻ khác trở thành tấm vé miễn trừ để người ta quên đi sự bất toàn của chính mình."
    ],

    # 2. DOUBLE_STANDARD
    [
        "Bản chất của người và hoàn cảnh của ta",
        "Tại sao cùng một sai lầm, ta lại dễ dàng tha thứ cho mình hơn người khác?",
        "Ta thường gọi lỗi lầm của người khác là bản chất suy đồi, nhưng lại gọi chính lỗi lầm ấy ở bản thân là do hoàn cảnh đưa đẩy.",
        "Chiếc cán cân công lý của con người luôn có xu hướng nới tay với chính kẻ đang cầm nó.",
        "Ta gọi lỗi lầm của người khác là bản chất, nhưng lại gọi chính lỗi lầm ấy ở bản thân là hoàn cảnh bắt buộc; chiếc cán cân phán xét luôn tự động nghiêng về phía có lợi cho kẻ cầm cân."
    ],
    [
        "Thẳng thắn hay tàn nhẫn",
        "Nhiều người tự hào mình là kẻ sống thẳng thắn và không biết thảo mai.",
        "Nhưng ranh giới giữa thẳng thắn và tàn nhẫn nằm ở chỗ: ta gọi sự cay độc của mình là chân thật, nhưng lại coi sự chân thật của người khác là xúc phạm.",
        "Sự thật không cần những lưỡi dao tẩm độc để chứng minh giá trị của nó.",
        "Ranh giới giữa thẳng thắn và tàn nhẫn rất mong manh: ta gọi sự cay độc của mình là tính cách chân thật, nhưng lại lập tức kết tội sự thẳng thắn của người khác là thiếu giáo dục."
    ],
    [
        "Bảo vệ bản thân hay ích kỷ",
        "Khi người khác từ chối giúp đỡ, ta phán xét họ lạnh lùng và vô cảm.",
        "Nhưng khi chính ta từ chối một ai đó, ta lại tự hào rằng mình đã biết thiết lập ranh giới cá nhân và học cách yêu thương bản thân.",
        "Tiêu chuẩn kép tinh vi nhất là khi ta đem tâm lý học ra để hợp thức hóa sự vô tâm của chính mình.",
        "Khi người khác từ chối ta, ta phán xét họ vô cảm; nhưng khi chính ta quay lưng, ta lại gọi đó là thiết lập ranh giới; tiêu chuẩn kép tinh vi nhất là dùng thuật ngữ tâm lý để bao biện cho sự ích kỷ."
    ],
    [
        "Bí mật và sự lừa dối",
        "Ta kết án sự dối trá của người khác như một tội ác không thể tha thứ.",
        "Nhưng những điều ta giấu giếm lại luôn được dán nhãn là sự riêng tư chính đáng cần được tôn trọng.",
        "Sự thật chỉ dễ chịu khi nó đứng về phía bảo vệ hình ảnh của ta.",
        "Ta kết án sự giấu giếm của người khác như một tội đồ phản bội, nhưng lại gọi những góc khuất của mình là quyền riêng tư thiêng liêng; sự thật chỉ được tôn vinh khi nó không đe dọa chiếc mặt nạ của ta."
    ],
    [
        "Thành công và may mắn",
        "Khi người khác đạt được thành tựu, ta thường nghĩ họ gặp thời hoặc có bệ đỡ.",
        "Nhưng khi bản thân gặt hái kết quả, ta tin tuyệt đối rằng đó là nhờ tài năng, mồ hôi và sự nỗ lực phi thường của chính mình.",
        "Nỗi đau của bản ngã là không thể chấp nhận rằng kẻ khác cũng đã từng nỗ lực nhiều như ta.",
        "Ta thường xem thành công của người khác là nhờ may mắn và quan hệ, nhưng lại tin thành tựu của mình hoàn toàn do thực lực; bản ngã thà hạ thấp người đời còn hơn thừa nhận sự thua kém của bản thân."
    ],

    # 3. MORALITY
    [
        "Lòng tốt khi không có khán giả",
        "Bạn có bao giờ tự hỏi giá trị của một hành động tốt nằm ở đâu?",
        "Phẩm chất đạo đức của một con người không được đo bằng những gì họ làm trước ống kính, mà bằng cách họ đối xử với những kẻ không thể mang lại cho họ bất kỳ lợi ích nào.",
        "Lòng tốt có điều kiện là một cuộc đổi chác; chỉ có sự tử tế trong bóng tối mới là nhân cách.",
        "Đạo đức của một con người không đo bằng những việc tốt làm trước ánh đèn sân khấu, mà bằng cách họ cư xử trong bóng tối với những kẻ không thể mang lại cho họ bất kỳ giá trị trao đổi nào."
    ],
    [
        "Khi sự hy sinh trở thành vũ khí",
        "Sự hy sinh quá mức đôi khi không xuất phát từ tình yêu thương thuần khiết.",
        "Nó là một cách tích lũy quyền lực ngầm, để sau này người hy sinh có thể dùng cảm giác tội lỗi bóp nghẹt mọi quyền tự do của người nhận.",
        "Một ân huệ đè nặng sự hy sinh sẽ biến mối quan hệ thành một nhà tù vô hình.",
        "Sự hy sinh quá mức đôi khi là cách tích lũy quyền lực tàn nhẫn nhất; người ta cho đi tất cả chỉ để biến người nhận thành kẻ cả đời không bao giờ được phép làm điều mình muốn."
    ],
    [
        "Cái giá của sự tử tế vô điều kiện",
        "Nếu bạn luôn tử tế với tất cả mọi người, bạn sẽ sớm nhận ra một sự thật cay đắng.",
        "Sự tha thứ vô giới hạn sẽ không tạo ra sự biết ơn, mà chỉ nuôi dưỡng sự lấn lướt của những kẻ quen sống dựa trên sự nhẫn nhịn của người khác.",
        "Lòng tốt thiếu đi ranh giới chỉ là sự yếu đuối đội lốt bao dung.",
        "Lòng tốt không có ranh giới sẽ không tạo ra sự biết ơn, mà chỉ nuôi dưỡng sự trơ trẽn; tha thứ cho kẻ không biết hối hận thực chất là đồng lõa với sự bất công."
    ],
    [
        "Đạo đức và sự an toàn",
        "Rất nhiều người tự nhận mình là người lương thiện chỉ vì họ chưa có cơ hội để làm điều ác.",
        "Sự lương thiện không phải là thiếu năng lực làm hại người khác; lương thiện là khi bạn nắm trong tay sức mạnh để phá hủy nhưng vẫn lựa chọn kiềm chế.",
        "Đừng nhầm lẫn giữa sự bất lực và phẩm hạnh.",
        "Rất nhiều người tự nhận mình lương thiện chỉ vì chưa từng có cơ hội làm điều xấu; đừng nhầm lẫn giữa sự bất lực và phẩm hạnh, bởi chỉ kẻ có khả năng làm hại mà chọn dừng lại mới thực sự có đạo đức."
    ],
    [
        "Sự thánh thiện tàn nhẫn",
        "Có những kẻ dùng chính sự thánh thiện của mình để bức tử người khác.",
        "Họ không bao giờ vi phạm bất kỳ điều luật nào, nhưng cách họ nhìn người khác với ánh mắt thương hại và phán xét lại sắc hơn mọi lưỡi dao.",
        "Tội lỗi lớn nhất của sự hoàn hảo là nó tước đi quyền được làm người bất toàn của những người xung quanh.",
        "Có những kẻ dùng chính sự chuẩn mực của mình để bức tử người khác; họ không làm sai điều gì, nhưng ánh mắt khinh miệt ẩn sau sự bao dung của họ lại tàn nhẫn hơn bất kỳ sự sỉ nhục nào."
    ],

    # 4. EGO
    [
        "Nhu cầu chứng minh sự quan trọng",
        "Tại sao con người lại sợ cảm giác bị lãng quên hơn cả cái chết?",
        "Bản ngã thà bị căm ghét còn hơn phải chấp nhận sự thật rằng sự tồn tại của nó hoàn toàn vô nghĩa đối với vũ trụ này.",
        "Mọi sự ồn ào ta tạo ra chỉ là tiếng hét trong vô vọng để khẳng định: Ta đang ở đây.",
        "Bản ngã thà bị người đời căm ghét còn hơn chịu đựng cảm giác vô hình; mọi sự ồn ào và tranh cãi ta tạo ra thực chất chỉ là tiếng kêu cứu tuyệt vọng để khẳng định sự quan trọng của chính mình."
    ],
    [
        "Nỗi sợ bị nhìn thấu",
        "Ta khao khát được một người thấu hiểu tận cùng tâm can.",
        "Nhưng ngay khi có ai đó chạm đúng vào điểm yếu hoặc nỗi sợ mà ta che giấu, phản xạ đầu tiên của bản ngã là tấn công hoặc bỏ chạy.",
        "Ta không muốn được thấu hiểu; ta chỉ muốn được ngưỡng mộ một cách mù quáng.",
        "Ta luôn than thở rằng không ai hiểu mình, nhưng ngay khi có kẻ nhìn thấu nỗi bất an bên dưới chiếc mặt nạ, bản ngã lập tức dựng lên bức tường phòng vệ; ta khao khát sự tán thưởng chứ không phải sự thật."
    ],
    [
        "Cái bẫy của việc luôn luôn đúng",
        "Trong mọi cuộc tranh cãi, mục tiêu thực sự của bạn là tìm ra chân lý hay bảo vệ cái tôi?",
        "Người cố chấp bảo vệ ý kiến của mình không quan tâm đến sự thật; họ chỉ đang liều chết bảo vệ cảm giác thượng đẳng trước đối phương.",
        "Chiến thắng một cuộc tranh luận thường phải trả giá bằng một mối quan hệ đổ vỡ.",
        "Người cố chấp tranh cãi không quan tâm đến chân lý; họ chỉ liều chết bảo vệ cảm giác thượng đẳng của cái tôi; chiến thắng bằng lý lẽ thường là thất bại cay đắng nhất trong việc kết nối con người."
    ],
    [
        "Khiêm nhường trình diễn",
        "Sự khiêm nhường đôi khi chỉ là một cách kín đáo để đứng cao hơn người khác.",
        "Người ta cúi đầu xuống không phải vì họ thấy mình nhỏ bé, mà vì họ đang chờ đợi tiếng vỗ tay tán thưởng cho cái cúi đầu ấy.",
        "Lời tự chê trách khéo léo nhất chính là lời xin được khen ngợi gián tiếp.",
        "Sự khiêm nhường trình diễn là hình thức kiêu ngạo tinh vi nhất; người ta cúi đầu không phải vì thấy mình nhỏ bé, mà vì muốn gom nhặt những lời khen ngợi cho sự khiêm tốn của chính mình."
    ],
    [
        "Đồng nhất mình với thành tựu",
        "Nếu tước bỏ danh thiếp, tài sản và sự công nhận, bạn còn lại là ai?",
        "Khi một người đánh đồng bản sắc của mình với những thứ bên ngoài, mỗi một thất bại nhỏ đều sẽ biến thành một cuộc khủng hoảng sinh tử của tâm hồn.",
        "Vật sở hữu cuối cùng sẽ quay lại sở hữu chính kẻ tạo ra nó.",
        "Khi đánh đồng giá trị bản thân với danh vị và tài sản, mỗi thất bại bên ngoài sẽ trở thành một đòn hủy diệt nội tâm; ta đau đớn không phải vì mất đi đồ vật, mà vì mất đi chỗ bấu víu của bản ngã."
    ],

    # 5. SELF_DECEPTION
    [
        "Căn phòng của sự im lặng",
        "Tại sao con người không thể ngồi yên lặng một mình trong phòng?",
        "Người ta chấp nhận mọi sự bận rộn khiến mình kiệt sức, chỉ để không phải ở một mình với người mà họ đã dành cả đời để che giấu.",
        "Tiếng ồn bên ngoài là liều thuốc giảm đau cho sự trống rỗng bên trong.",
        "Người ta sẵn sàng nhận lấy mọi sự bận rộn khiến mình kiệt sức, chỉ để không phải đối diện với sự trống rỗng trong một căn phòng im lặng; công việc đôi khi chỉ là liều thuốc giảm đau để trốn chạy chính mình."
    ],
    [
        "Những lời bào chữa hoàn hảo",
        "Bộ não con người là một cỗ máy ngụy biện vĩ đại nhất từng tồn tại.",
        "Nó có thể tìm ra lý do đạo đức cho hành vi đê tiện nhất, và tìm ra sự cao thượng cho sự hèn nhát tồi tệ nhất của chính chủ nhân.",
        "Điều khó chịu nhất của sự thật không phải là nó trần trụi, mà là nó cướp mất những lời an ủi giả tạo ta đã mất công thêu dệt.",
        "Bộ não là cỗ máy ngụy biện tài ba nhất: nó luôn biết cách dán nhãn cao thượng cho sự hèn nhát của ta; điều khó chịu nhất của sự thật là nó tước đoạt những lời bào chữa mà ta đã bấu víu bấy lâu."
    ],
    [
        "Khu vườn an toàn của sự ảo tưởng",
        "Nhiều người thà sống trong một lời nói dối êm đềm còn hơn chấp nhận một sự thật giải thoát.",
        "Bởi vì lời nói dối chỉ đòi hỏi sự mù quáng thụ động, còn sự thật đòi hỏi một cuộc phẫu thuật đau đớn để tái thiết lại toàn bộ cuộc đời.",
        "Con người không yêu chân lý; con người chỉ yêu những gì làm họ thấy an tâm.",
        "Người ta thà sống trong lời nói dối quen thuộc còn hơn đón nhận sự thật giải thoát; bởi vì dối trá chỉ cần sự thỏa hiệp mù quáng, còn sự thật đòi hỏi cái giá của việc đập vỡ toàn bộ thế giới quan cũ."
    ],
    [
        "Lời hứa cho tương lai",
        "Ngày mai tôi sẽ bắt đầu thay đổi; ngày mai tôi sẽ sống khác.",
        "Lời hứa hẹn về tương lai thường là cách tinh vi nhất để lương tâm được phép tiếp tục buông thả trong hiện tại.",
        "Sự trì hoãn không phải là lười biếng; đó là một thỏa thuận ngầm giữa nỗi sợ và sự tự huyễn hoặc.",
        "Lời hứa hẹn thay đổi vào ngày mai là cách tinh tế nhất để bản ngã tiếp tục sa đọa trong hôm nay; sự trì hoãn thực chất là một thỏa thuận ngầm giữa nỗi sợ thất bại và ảo tưởng về quyền năng vô hạn."
    ],
    [
        "Đồng lõa với kẻ làm tổn thương",
        "Có những người bám chặt lấy kẻ làm tổn thương mình và gọi đó là sự chung thủy.",
        "Họ không chịu thừa nhận rằng việc ở lại không phải vì tình yêu vĩ đại, mà vì nỗi sợ hãi tột cùng trước sự cô độc và việc phải tự chịu trách nhiệm cho số phận mình.",
        "Sự cam chịu đôi khi chỉ là sự hèn nhát được ngụy trang dưới danh nghĩa đức hy sinh.",
        "Nhiều người bám lấy mối quan hệ độc hại và gọi đó là sự thủy chung; họ không dám thừa nhận rằng mình ở lại không phải vì tình yêu, mà vì nỗi sợ cô độc lớn hơn lòng tự trọng của chính mình."
    ],

    # 6. SHADOW
    [
        "Phần bị chối bỏ lên tiếng",
        "Điều bạn căm ghét nhất ở người khác thường là điều gì?",
        "Đó chính là phần bóng tối mà bạn đã tốn rất nhiều công sức để đè nén trong chính tâm hồn mình, nay đột ngột xuất hiện tự do trước mắt bạn.",
        "Người ta ném đá kẻ khác để trừng phạt phần đen tối của chính bản thân mình.",
        "Điều ta căm ghét tột cùng ở người khác thường là phần bóng tối ta đã kỳ công chôn giấu trong chính mình; phán xét kẻ khác thực chất là cách gián tiếp để trừng phạt phần bản năng mà ta không dám thừa nhận."
    ],
    [
        "Mặt trái của người luôn hiền lành",
        "Những người cả đời không bao giờ dám nổi giận thường nguy hiểm nhất.",
        "Cơn giận bị kìm nén không biến mất; nó biến thành sự mỉa mai, sự thụ động phá hoại (*passive-aggressive*) và nọc độc ngấm ngầm hủy hoại các mối quan hệ.",
        "Một nhân cách lành mạnh cần biết cách nói không và bộc lộ sự giận dữ một cách có kiểm soát.",
        "Kẻ không bao giờ dám nổi giận không phải là thánh nhân; sự tức giận bị đè nén sẽ biến chất thành độc dược ngầm, hủy hoại các mối quan hệ bằng sự mỉa mai cay nghiệt và thái độ bất hợp tác thụ động."
    ],
    [
        "Chiếc gương của sự đố kỵ",
        "Khi thấy một người tỏa sáng, phản ứng đầu tiên trong lòng bạn là gì?",
        "Bóng tối nội tâm luôn tìm cách bới móc khiếm khuyết của người khác, chỉ để xoa dịu cảm giác cay đắng về sự bất tài của chính mình.",
        "Khen ngợi chân thành một người vượt trội hơn ta đòi hỏi một lòng dũng cảm phi thường.",
        "Bóng tối nội tâm luôn thôi thúc ta bới móc vết nhơ của người thành công, chỉ để xoa dịu nỗi nhục nhã về sự bất tài của chính mình; thừa nhận người khác giỏi hơn đòi hỏi một lòng can đảm hiếm có."
    ],
    [
        "Quái vật bên trong kẻ tử tế",
        "Ai trong chúng ta cũng nuôi dưỡng một con thú hoang trong góc tối.",
        "Nếu bạn không thừa nhận sự tồn tại của nó, một ngày nào đó khi bạn kiệt sức hoặc mất kiểm soát, nó sẽ nuốt chửng toàn bộ phần người của bạn.",
        "Ánh sáng không đến từ việc chối bỏ bóng tối, mà từ việc can đảm bước vào và thuần hóa nó.",
        "Ai cũng giấu một con thú hoang trong góc khuất tâm hồn; nếu cứ cố chấp phủ nhận sự tồn tại của nó, nó sẽ đợi khoảnh khắc ta suy sụp nhất để bùng lên và cắn xé toàn bộ phẩm giá mà ta dày công gây dựng."
    ],
    [
        "Sự tự căm ghét chính mình",
        "Kẻ độc hại nhất với cuộc đời bạn không phải là kẻ thù bên ngoài.",
        "Đó là giọng nói thì thầm trong đầu bạn mỗi đêm, liên tục nhắc lại những sai lầm cũ và thuyết phục bạn rằng bạn không xứng đáng được hạnh phúc.",
        "Hòa giải với phần bóng tối của bản thân là trận chiến gian nan nhất đời người.",
        "Kẻ thù tàn độc nhất không nằm ở thế giới ngoài kia, mà là giọng nói độc hại trong đầu luôn nhắc lại những vết thương cũ; hòa giải với sự bất toàn của chính mình là trận chiến sinh tử của một kiếp người."
    ],

    # 7. MASK
    [
        "Trình diễn trên sân khấu xã hội",
        "Ta sống phần lớn cuộc đời như một diễn viên quên mất kịch bản.",
        "Ta khoác lên chiếc mặt nạ cười vui để làm vừa lòng khán giả, cho đến khi trở về nhà và nhận ra khuôn mặt thật bên dưới đã teo tóp từ lâu.",
        "Cái giá của sự hòa nhập đôi khi là đánh mất bản năng chân thật của chính mình.",
        "Ta mải miết diễn tròn vai trên sân khấu xã hội để đổi lấy những tràng pháo tay hời hợt, cho đến khi tấm màn nhung khép lại và ta nhận ra mình đã quên mất gương mặt thật của chính bản thân."
    ],
    [
        "Sự thân thiện công nghiệp",
        "Những nụ cười xã giao có thể mua được sự thuận tiện tạm thời.",
        "Nhưng nó cũng tạo ra một thế giới nơi không ai dám bộc lộ nỗi đau, và tất cả mọi người đều cô độc sau lớp vỏ bọc hoàn hảo.",
        "Một lời từ chối chân thành vẫn ấm áp hơn một nụ cười giả tạo được tính toán trước.",
        "Nụ cười xã giao tạo ra một xã hội tiện lợi nhưng băng giá, nơi mọi người đều giấu kín vết thương sau vẻ ngoài hoàn hảo; sự thân thiện giả tạo là hình thức cô lập con người tàn nhẫn nhất."
    ],
    [
        "Chiếc mặt nạ của sự mạnh mẽ",
        "Người luôn tỏ ra không cần ai giúp đỡ thường là người tuyệt vọng nhất.",
        "Họ dùng sự gai góc và độc lập như một tấm khiên phòng thủ, chỉ vì sợ rằng nếu bộc lộ sự yếu đuối, họ sẽ bị ruồng bỏ một lần nữa.",
        "Can đảm không phải là không bao giờ khóc; can đảm là dám thừa nhận mình đang tổn thương.",
        "Kẻ luôn cố tỏ ra mạnh mẽ và không cần ai che chở thường là người mang nhiều vết thương nhất; sự bất cần chỉ là chiếc áo giáp tuyệt vọng để bảo vệ một tâm hồn đã quá sợ hãi sự từ chối."
    ],
    [
        "Khi chiếc mặt nạ dính chặt vào da thịt",
        "Nếu bạn đeo một chiếc mặt nạ đủ lâu, bạn sẽ bắt đầu tin nó là khuôn mặt của mình.",
        "Đến một ngày bạn muốn lột bỏ nó để sống thật, bạn sẽ nhận ra nó đã ăn sâu vào da thịt, và việc gỡ bỏ nó sẽ khiến bạn chảy máu.",
        "Tự do bắt đầu từ khoảnh khắc ta dám chấp nhận sự vụng về chân thật của mình.",
        "Đeo một chiếc mặt nạ quá lâu sẽ khiến nó bám chặt vào da thịt; ngày ta muốn sống thật cũng là ngày ta phải chấp nhận nỗi đau đớn xé toạc lớp vỏ bọc đã gắn liền với danh tiếng cả đời."
    ],
    [
        "Nhu cầu được người khác định nghĩa",
        "Ta thường hỏi người khác: Tôi trông thế nào? Tôi sống có ổn không?",
        "Bởi vì ta không có can đảm tự định nghĩa giá trị của mình, nên đành trao quyền chấm điểm cuộc đời mình cho ánh mắt của những kẻ qua đường.",
        "Khi bạn cần sự công nhận của đám đông để thấy mình có giá trị, bạn đã tự nguyện biến mình thành nô lệ.",
        "Khi trao quyền định giá cuộc đời mình cho ánh mắt của người đời, bạn đã tự nguyện ký vào bản hợp đồng nô dịch; kẻ chỉ thở được nhờ lời khen sẽ chết ngạt ngay khi đám đông quay lưng đi."
    ],

    # 8. POWER
    [
        "Bản chất của sự kiểm soát ngầm",
        "Quyền lực thâm độc nhất không xuất hiện dưới dạng gậy gộc hay đe dọa.",
        "Nó xuất hiện dưới hình thức của sự chăm sóc chu đáo đến mức tước đi toàn bộ khả năng tự sinh tồn và tư duy độc lập của nạn nhân.",
        "Kẻ giam cầm bạn tinh vi nhất là kẻ cho bạn một chiếc lồng bằng vàng và gọi đó là sự che chở.",
        "Quyền lực đáng sợ nhất không nằm ở sự bạo tàn, mà nằm ở sự bảo bọc quá mức; chiếc lồng được mạ vàng và dán nhãn tình thương là nơi tước đi đôi cánh tự do của con người một cách êm ái nhất."
    ],
    [
        "Cơn nghiện sự phục tùng",
        "Người thích ra lệnh cho người khác thường che giấu một nỗi sợ hãi tột cùng.",
        "Họ sợ cảm giác bất lực trước số phận của chính mình, nên buộc phải tìm cách thao túng những người yếu thế xung quanh để tạo ra ảo tưởng về quyền năng.",
        "Kẻ bạo chúa bên ngoài thường là một đứa trẻ hoảng loạn bên trong.",
        "Cơn nghiện kiểm soát người khác luôn bắt nguồn từ nỗi bất lực trước chính số phận mình; kẻ thích thị uy quyền lực thực chất chỉ là một tâm hồn đang hoảng loạn cố bấu víu vào sự phục tùng của kẻ yếu."
    ],
    [
        "Trách nhiệm giả tạo",
        "Tôi làm điều này hoàn toàn là vì trách nhiệm với tập thể.",
        "Những kẻ thích nhân danh tập thể và đại cuộc thường là những kẻ khao khát quyền lực cá nhân mãnh liệt nhất nhưng lại không dám đứng tên trách nhiệm.",
        "Hãy cảnh giác với những kẻ luôn đòi hỏi người khác phải hy sinh vì mục đích chung.",
        "Những kẻ luôn miệng nhân danh đại cuộc để đòi hỏi sự hy sinh thường là kẻ hưởng lợi nhiều nhất; quyền lực ẩn sau danh nghĩa tập thể là thứ quyền lực tàn nhẫn và vô trách nhiệm nhất."
    ],
    [
        "Sự im lặng như một vũ khí",
        "Trong các mối quan hệ, sự im lặng trừng phạt (*silent treatment*) là một hình thức bạo lực tâm lý tàn bạo.",
        "Nó không nhằm giải quyết mâu thuẫn, mà nhằm tra tấn đối phương bằng sự mơ hồ và cảm giác bất an, cho đến khi họ phải van xin sự tha thứ.",
        "Giao tiếp là nhịp cầu; sự im lặng có chủ đích là một sự cắt đứt tàn nhẫn.",
        "Sự im lặng trừng phạt không phải là điềm tĩnh, mà là thứ vũ khí bạo lực lạnh lùng nhất; nó dùng sự cô lập để bẻ gãy lòng tự trọng của đối phương cho đến khi họ phải quỳ gối xin lỗi vì một lỗi lầm mơ hồ."
    ],
    [
        "Khi kẻ bị áp bức nắm quyền",
        "Bi kịch lớn nhất của lịch sử không phải là sự tàn bạo của kẻ áp bức.",
        "Đó là khi những kẻ từng bị áp bức vươn lên nắm quyền lực, họ không xóa bỏ sự áp bức, mà chỉ đổi chỗ ngồi để trở thành những kẻ bạo chúa tàn bạo hơn.",
        "Người ta không ghét sự bất công; người ta chỉ ghét việc mình không phải là kẻ được hưởng lợi từ sự bất công đó.",
        "Bi kịch lớn nhất là khi kẻ bị áp bức nắm được quyền bính, họ hiếm khi tìm cách xóa bỏ ngục tù mà chỉ vội vã chiếm lấy vị trí của cai ngục; người ta không ghét bạo quyền, người ta chỉ thèm muốn đặc quyền."
    ],

    # 9. MANIPULATION
    [
        "Đóng vai nạn nhân để thao túng",
        "Kẻ thao túng nguy hiểm nhất không bao giờ lớn tiếng quát nạt bạn.",
        "Họ khéo léo đóng vai kẻ đáng thương bị cả thế giới ruồng bỏ, để biến lòng trắc ẩn của bạn thành sợi dây tự trói tay chân mình.",
        "Nước mắt của một kẻ ích kỷ đôi khi có sức hủy diệt lớn hơn sự hung bạo của kẻ độc tài.",
        "Kẻ thao túng xuất sắc nhất luôn đóng vai nạn nhân vô tội; họ dùng nước mắt và sự bất hạnh để biến lòng trắc ẩn của bạn thành sợi dây xích, ép bạn phải hy sinh quyền lợi của mình để chuộc lấy cảm giác an tâm giả tạo."
    ],
    [
        "Tống tiền cảm xúc",
        "Khi ai đó liên tục nhắc lại những gì họ đã hy sinh vì bạn, hãy cẩn thận.",
        "Đó không còn là tình cảm thuần khiết; đó là một bản hóa đơn nợ nần được đem ra đòi nợ mỗi khi bạn có ý định sống theo ý mình.",
        "Tình thương biến thành độc dược khi nó được dùng làm cái cớ để tước đoạt tự do của người khác.",
        "Khi một người liên tục nhắc lại những hy sinh trong quá khứ, đó không còn là ân tình mà là một hợp đồng tống tiền cảm xúc; họ bắt bạn phải trả nợ cả đời bằng sự ngoan ngoãn và phục tùng tuyệt đối."
    ],
    [
        "Nghệ thuật làm bạn nghi ngờ chính mình (Gaslighting)",
        "Đỉnh cao của sự thao túng là khiến bạn nghi ngờ chính đôi mắt và cảm xúc của mình.",
        "Họ bóp méo sự thật khéo léo đến mức khiến bạn tin rằng mình là kẻ điên rồ, kẻ suy diễn và là nguồn gốc của mọi bất hạnh trong mối quan hệ.",
        "Khi bạn bắt đầu xin lỗi vì những điều mình không làm sai, bạn đã hoàn toàn rơi vào bẫy của họ.",
        "Đỉnh cao của sự thao túng tâm lý là khiến bạn phải nghi ngờ chính ký ức và sự tỉnh táo của mình; khoảnh khắc bạn cúi đầu nhận lỗi cho sự tàn nhẫn của kẻ khác cũng là lúc bạn trao trọn quyền kiểm soát linh hồn mình."
    ],
    [
        "Khen ngợi có điều kiện",
        "Có những người chỉ khen ngợi bạn khi bạn làm đúng theo ý muốn của họ.",
        "Sự công nhận bị biến thành mồi câu để gây nghiện tâm lý, và họ sẽ tước bỏ nó ngay khi bạn thể hiện quan điểm độc lập.",
        "Đừng bán rẻ chính kiến của mình chỉ để đổi lấy vài lời vuốt ve hời hợt.",
        "Sự tán thưởng có điều kiện là liều thuốc gây nghiện nguy hiểm nhất; kẻ thao túng dùng lời khen như mồi nhử để thuần hóa bạn, và sẽ lập tức rút lại sự ấm áp ngay khi bạn dám cất lên tiếng nói riêng."
    ],
    [
        "Chiếc bẫy của sự cứu rỗi",
        "Nhiều người bước vào một mối quan hệ độc hại vì mang trong mình ảo tưởng làm đấng cứu thế.",
        "Họ tin rằng tình yêu và sự nhẫn nhịn của mình có thể chữa lành một kẻ tàn nhẫn, để rồi nhận ra mình chỉ là bia đỡ đạn cho những cơn cuồng nộ của đối phương.",
        "Bạn không thể cứu vớt một người đang tận hưởng vũng lầy của chính họ.",
        "Ảo tưởng nguy hiểm nhất là tin rằng tình yêu của mình có thể cứu rỗi một tâm hồn tàn nhẫn; người ta thường nhầm lẫn giữa sự vị tha cao cả và việc tình nguyện trở thành bao cát để kẻ khác trút bỏ sự độc hại."
    ],

    # 10. FREEDOM
    [
        "Nỗi sợ trách nhiệm của tự do",
        "Ai cũng lớn tiếng đòi hỏi quyền tự do lựa chọn cho cuộc đời mình.",
        "Nhưng điều họ thực sự khiếp sợ là khi lựa chọn ấy sụp đổ, họ không còn một ai khác trên đời để đổ lỗi.",
        "Tự do không phải là một món quà êm đềm; tự do là một gánh nặng khổng lồ của trách nhiệm.",
        "Con người luôn khao khát tự do nhưng lại khiếp sợ cái giá của nó; bởi vì tự do đồng nghĩa với việc khi thất bại hay đau khổ, ta không còn bất kỳ tấm bình phong hay kẻ thù nào để đổ lỗi cho số phận."
    ],
    [
        "Chiếc lồng quen thuộc",
        "Nhiều người thà sống cả đời trong một ngục tù quen thuộc còn hơn bước ra khoảng trời tự do xa lạ.",
        "Bởi vì trong ngục tù họ được cho ăn và chỉ lối, còn ngoài tự do họ phải tự tìm đường và chịu đựng sự đói khát.",
        "Nô lệ đôi khi yêu chiếc xiềng xích của mình hơn là lòng dũng cảm để phá bỏ nó.",
        "Người ta thà cam chịu sống trong một ngục tù quen thuộc còn hơn bước ra khoảng trời tự do xa lạ; sự lệ thuộc mang lại cảm giác an toàn giả tạo, còn tự do đòi hỏi sự cô độc và can đảm tự sinh tồn."
    ],
    [
        "Bán tự do đổi lấy sự an toàn",
        "Sự an toàn là miếng mồi ngon nhất để bẫy những kẻ sợ hãi số phận.",
        "Kẻ sẵn sàng từ bỏ tự do cá nhân để đổi lấy sự bảo bọc tạm thời sẽ sớm nhận ra mình mất cả tự do lẫn sự an toàn.",
        "Bình yên mua bằng sự phục tùng chỉ là sự hoãn lại của ngày hành quyết.",
        "Kẻ sẵn sàng đánh đổi tự do để mua lấy sự an toàn tạm thời sẽ sớm nhận ra mình mất cả hai; bình yên đạt được bằng sự quỳ gối thực chất chỉ là chiếc án treo đợi ngày người khác đổi ý."
    ],
    [
        "Tự do và sự cô độc",
        "Cái giá đắt nhất của việc sống tự do là sự cô độc.",
        "Khi bạn từ chối đi theo con đường mòn của đám đông, bạn sẽ phải quen với việc đi một mình trong màn đêm và không có tiếng vỗ tay khích lệ.",
        "Nhưng thà cô độc trong tự do còn hơn ấm áp trong sự giam cầm tư tưởng.",
        "Cái giá đắt đỏ nhất của tự do là sự cô độc; khi từ chối bước đi theo bầy đàn, bạn phải chấp nhận màn đêm thinh lặng và việc không còn bất kỳ bờ vai nào để bấu víu mỗi khi chùn chân."
    ],
    [
        "Tự do nội tâm đích thực",
        "Tự do không phải là muốn làm gì thì làm theo bản năng hỗn loạn.",
        "Tự do thực sự là khi bạn có đủ dũng khí để từ chối những điều trái với lương tâm, ngay cả khi cả thế giới đang đe dọa hoặc cám dỗ bạn.",
        "Kẻ không làm chủ được dục vọng của mình vĩnh viễn là một tù nhân.",
        "Tự do đích thực không phải là buông thả theo mọi ham muốn bản năng; tự do là năng lực kiên quyết nói không với những cám dỗ làm tha hóa nhân cách, ngay cả khi việc từ chối đòi hỏi một sự trả giá đắt."
    ],

    # 11. TRUTH
    [
        "Sự thật và những lời tự bào chữa",
        "Điều khó chịu nhất của sự thật không nằm ở sự tàn nhẫn của nó.",
        "Nó nằm ở chỗ nó cướp mất toàn bộ những câu chuyện ngụy biện êm ái mà ta đã mất bao năm tháng để thêu dệt nhằm ru ngủ bản thân.",
        "Sự thật giải thoát bạn, nhưng trước hết nó sẽ làm bạn tổn thương sâu sắc.",
        "Điều khó chịu nhất của sự thật không phải là sự cay đắng, mà là nó cướp mất những lời an ủi giả tạo ta đã bấu víu bấy lâu; sự thật giải thoát con người, nhưng trước hết nó sẽ đập vỡ chiếc mặt nạ an toàn của họ."
    ],
    [
        "Ảo tưởng được ưa chuộng hơn chân lý",
        "Người ta hiếm khi săn lùng sự thật trần trụi về cuộc sống.",
        "Họ chỉ săn lùng những bằng chứng để xác nhận lại định kiến và củng cố thêm niềm tin sẵn có của mình.",
        "Con người không yêu chân lý; con người chỉ yêu cảm giác thấy mình luôn đúng.",
        "Người đời không đi tìm chân lý; họ chỉ mải miết thu nhặt những mảnh ghép để củng cố thêm định kiến sẵn có; con người không khao khát sự thật, con người chỉ khao khát cảm giác được xác nhận rằng mình không sai."
    ],
    [
        "Sự thật nửa vời nguy hiểm hơn dối trá",
        "Một lời nói dối trắng trợn rất dễ bị phát hiện và tiêu diệt.",
        "Nhưng một sự thật nửa vời được pha trộn khéo léo với sự im lặng có chủ đích mới là thứ độc dược giết chết niềm tin của con người một cách êm ái nhất.",
        "Kẻ nói dối nguy hiểm nhất là kẻ chỉ kể đúng một nửa câu chuyện.",
        "Một sự thật nửa vời nguy hiểm hơn ngàn lời dối trá trắng trợn; kẻ dùng 90% sự thật để bao bọc cho 10% sự bóp méo có chủ đích là kẻ có năng lực đầu độc nhận thức của người khác tàn bạo nhất."
    ],
    [
        "Phẫu thuật tâm hồn bằng sự thật",
        "Nhìn thẳng vào sự thật về chính mình giống như một cuộc phẫu thuật không dùng thuốc tê.",
        "Nó bóc tách từng lớp da thịt của sự tự ái, phơi bày những thói hư tật xấu mà ta đã giấu kín dưới danh xưng tính cách.",
        "Nhưng đó là nỗi đau duy nhất có thể chữa lành sự mục ruỗng bên trong.",
        "Đối diện với sự thật về bản thân là cuộc đại phẫu đau đớn nhất không thuốc tê; nhưng thà chịu đựng nỗi đau xé lòng để cắt bỏ khối u tự dối, còn hơn sống cả đời trong sự hoại tử êm ái của ảo tưởng."
    ],
    [
        "Khi sự thật trở thành vũ khí",
        "Có những người nói sự thật không phải vì họ yêu chuộng công lý.",
        "Họ dùng sự thật như một lưỡi dao sắc bén để hạ nhục và tước đoạt phẩm giá của người khác dưới chiêu bài 'tôi chỉ nói thẳng'.",
        "Chân lý thiếu đi lòng trắc ẩn sẽ biến thành một hành vi bạo lực tinh thần.",
        "Sự thật khi thiếu vắng lòng trắc ẩn sẽ trở thành thứ bạo lực tàn nhẫn nhất; kẻ dùng sự thật trần trụi để đâm thấu vết thương của người khác không phải là người thẳng thắn, mà là một kẻ độc ác có lý lẽ."
    ],

    # 12. LOVE
    [
        "Yêu hay sợ hãi sự trống rỗng",
        "Nhiều người lầm tưởng sự cuồng nhiệt là biểu hiện của tình yêu vĩ đại.",
        "Thực chất, họ bám chặt lấy đối phương chỉ vì không thể chịu đựng nổi cảm giác đối diện với sự trống rỗng và cô độc của chính tâm hồn mình.",
        "Khi bạn cần một người để lấp đầy khoảng trống, bạn đang lợi dụng họ chứ không phải yêu họ.",
        "Nhiều mối tình nồng nhiệt thực chất chỉ là sự bấu víu tuyệt vọng vào chiếc phao cứu sinh; người ta không yêu đối phương vì con người họ, mà chỉ đang dùng họ như một liều thuốc để khỏa lấp sự trống rỗng bên trong."
    ],
    [
        "Chiếm hữu nhân danh sự chở che",
        "Sự kiểm soát tinh vi nhất luôn mang chiếc áo khoác của tình thương.",
        "Người ta đòi hỏi biết mọi tin nhắn, mọi cuộc gặp gỡ và kiểm soát từng suy nghĩ của bạn, rồi dán nhãn đó là sự quan tâm và lo lắng cho tương lai.",
        "Tình yêu trao cho người ta sự tự do; sự sở hữu chỉ tạo ra một nhà tù có hai người.",
        "Kiểm soát tinh vi nhất là thứ kiểm soát được dán nhãn lo lắng cho người mình yêu; tình yêu chân chính chắp thêm đôi cánh tự do, còn thói chiếm hữu ích kỷ chỉ biến mối quan hệ thành một nhà giam ngột ngạt."
    ],
    [
        "Yêu một hình bóng tưởng tượng",
        "Ta thường không yêu con người bằng xương bằng thịt đang đứng trước mặt ta.",
        "Ta chỉ đang yêu một phiên bản hoàn hảo mà trí tưởng tượng của ta đã vẽ nên và áp đặt lên họ, để rồi thất vọng cay đắng khi họ bộc lộ những khiếm khuyết rất đỗi con người.",
        "Thừa nhận người mình yêu có góc tối là bài học đầu tiên của tình yêu trưởng thành.",
        "Ta thường không yêu con người thật của đối phương mà chỉ yêu bức tượng hoàn hảo do trí tưởng tượng ta tạc nên; bi kịch bắt đầu khi bức tượng ấy cử động và bộc lộ những vết xước bất toàn của kiếp người."
    ],
    [
        "Sự cân đo trong tình cảm",
        "Khoảnh khắc một người bắt đầu tính toán xem ai cho đi nhiều hơn, tình yêu đã chết.",
        "Mối quan hệ lúc ấy bị biến thành một bàn cân kinh doanh, nơi mỗi cử chỉ quan tâm đều ngầm gắn kèm một chiếc hóa đơn đòi lại quyền lợi.",
        "Tình yêu không phải là một cuộc đổi chác sòng phẳng; đó là sự dâng hiến tự nguyện không toan tính.",
        "Khoảnh khắc một mối quan hệ xuất hiện sự so đo ai hy sinh nhiều hơn cũng là lúc tình yêu biến chất thành một cuộc buôn bán; khi sự ân cần gắn liền với hóa đơn đòi nợ, sự ấm áp đã biến thành giá lạnh."
    ],
    [
        "Biết buông tay là đỉnh cao của yêu thương",
        "Không phải tình yêu nào cũng có kết thúc trọn vẹn, và điều đó hoàn toàn bình thường.",
        "Đỉnh cao của sự gắn kết không phải là ghì chặt lấy một người đang đau khổ, mà là đủ dũng cảm để buông tay khi nhận ra sự có mặt của mình chỉ mang lại ngột ngạt cho cả hai.",
        "Có những sự rời đi là cách đẹp nhất để bảo toàn phẩm giá của tình yêu.",
        "Đỉnh cao của tình yêu trưởng thành không phải là ghì chặt lấy nhau trong tuyệt vọng; dũng cảm buông tay khi nhận ra sự hiện diện của mình chỉ đem lại tổn thương là sự tôn trọng thiêng liêng nhất dành cho đối phương."
    ],

    # 13. LOYALTY
    [
        "Lòng trung thành và cái giá phải trả",
        "Người ta có thể thề thốt trung thành rất dễ dàng khi sóng yên biển lặng.",
        "Nhưng lòng trung thành chỉ thực sự được thử thách khi nó bắt đầu đòi hỏi người ta phải trả giá bằng danh dự, tiền bạc hoặc sự an toàn của chính mình.",
        "Chỉ khi chiếc thuyền bắt đầu chìm, ta mới biết ai là người ở lại chèo chống.",
        "Lòng trung thành là thứ dễ tuyên bố nhất khi hoàn cảnh thuận lợi; chỉ khi nghịch cảnh ập đến và đòi hỏi người ta phải đánh đổi quyền lợi cá nhân, bộ mặt thật của những lời thề thốt mới lộ diện."
    ],
    [
        "Trung thành mù quáng là sự đồng lõa",
        "Có một sự khác biệt rất lớn giữa lòng trung thành và sự mù quáng.",
        "Khi bạn trung thành với một kẻ tàn nhẫn và bao che cho những việc làm phi nghĩa của họ, bạn không phải là một người nghĩa khí; bạn là một kẻ đồng phạm hèn nhát.",
        "Trung thành với cái xấu là sự phản bội lại chính phẩm giá của bản thân.",
        "Trung thành mù quáng với kẻ xấu không phải là nghĩa khí mà là sự hèn nhát đồng lõa; khi lòng trung thành đi ngược lại công lý và lương tri, nó đã biến chất thành một tội ác núp bóng phẩm hạnh."
    ],
    [
        "Nhát dao từ kẻ thân cận",
        "Kẻ thù trước mắt hiếm khi có thể làm bạn tổn thương tận cùng.",
        "Vết thương chí mạng nhất luôn đến từ người mà bạn từng mở toang cánh cửa phòng thủ, người biết rõ nhất bạn yếu đuối ở đâu và sẵn sàng đâm vào đúng vết sẹo ấy khi có cơ hội.",
        "Sự phản bội chỉ đau đớn khi nó đến từ kẻ ta từng coi là người nhà.",
        "Nhát dao chí mạng nhất không bao giờ đến từ kẻ thù ngoài chiến tuyến; nó luôn đến từ kẻ được ta trao trọn niềm tin và quay lưng lại để bảo vệ, bởi chỉ có họ mới biết chính xác điểm yếu nơi tim ta."
    ],
    [
        "Sự phản bội bắt đầu từ những điều nhỏ nhặt",
        "Không có sự phản bội nào xuất hiện đột ngột như một tiếng sét.",
        "Nó bắt đầu từ những lần thỏa hiệp vụn vặt, những lời nói dối vô hại và những khoảnh khắc im lặng khi thấy điều bất công đối với người bạn của mình.",
        "Hãy cảnh giác với những vết nứt nhỏ trước khi cây cầu sụp đổ.",
        "Sự phản bội lớn lao luôn khởi đầu từ những lần thỏa hiệp nhỏ nhặt; kẻ hôm nay im lặng khi bạn bị vu oan sẽ là kẻ ngày mai sẵn sàng ném viên đá đầu tiên khi thấy bạn thất thế."
    ],
    [
        "Trung thành với chính mình trước hết",
        "Trước khi thề thốt sống chết vì bất kỳ ai, hãy tự soi lại lòng mình.",
        "Nếu để giữ sự trung thành với người khác mà bạn phải bán rẻ giá trị sống và phản bội lại tiếng nói của lương tâm, thì sự trung thành ấy là một sự tha hóa.",
        "Người không trung thực được với chính mình sẽ không bao giờ trung thành được với ai.",
        "Trước khi tuyên thệ trung thành với một ai đó, hãy tự hỏi ta có đang phản bội lại chính mình; kẻ sẵn sàng chà đạp lên lương tâm để làm vừa lòng người khác sẽ phản bội bạn ngay khi có một cái giá hời hơn."
    ],

    # 14. ENVY
    [
        "Ngưỡng mộ biến chất thành đố kỵ",
        "Ranh giới giữa sự ngưỡng mộ và lòng đố kỵ chỉ cách nhau một sợi tóc.",
        "Khi ta ngưỡng mộ một người nhưng nhận ra mình không bao giờ có thể đạt được như họ, cảm giác bất lực sẽ nhanh chóng biến thành mong muốn nhìn thấy họ sụp đổ.",
        "Kẻ đố kỵ không muốn vươn lên bằng bạn; họ chỉ muốn kéo bạn xuống ngang tầm vũng lầy của họ.",
        "Ranh giới giữa ngưỡng mộ và đố kỵ rất mong manh; khi nhận ra mình bất lực không thể vươn tới tầm cao của người khác, kẻ hẹp hòi sẽ chuyển từ thán phục sang khao khát nhìn thấy thần tượng của mình vấy bẩn."
    ],
    [
        "Đố kỵ với người gần gũi",
        "Ta không bao giờ ghen tị với những vĩ nhân xa xôi trên sách báo.",
        "Ta chỉ âm thầm cay đắng trước thành công của người bạn cùng bàn, người đồng nghiệp cùng phòng hoặc người họ hàng trạc tuổi.",
        "Sự vượt trội của kẻ gần gũi là chiếc gương phản chiếu rõ nhất sự tầm thường của ta.",
        "Ta hiếm khi đố kỵ với những tỷ phú xa xôi; ta chỉ cay đắng trước sự thăng tiến của người bạn cùng trang lứa; sự vượt trội của kẻ sát bên là chiếc gương tàn nhẫn phơi bày sự giẫm chân tại chỗ của chính mình."
    ],
    [
        "Lời chúc mừng gượng gạo",
        "Có những người ngoài miệng luôn nói lời chúc phúc cho bạn.",
        "Nhưng trong ánh mắt họ lại ánh lên một sự nhẹ nhõm vô thức mỗi khi nghe tin bạn gặp trục trặc hay thất bại trong công việc.",
        "Hãy quan sát nụ cười của người khác khi bạn gặp khó khăn; đó là lúc chiếc mặt nạ rơi xuống.",
        "Nhiều người nói chúc mừng bạn bằng đôi môi nhưng lại thở phào nhẹ nhõm trong tim khi thấy bạn vấp ngã; thước đo tình bạn không nằm ở lúc cùng chia vui, mà ở việc ai thực sự đau lòng khi thấy bạn thất bại."
    ],
    [
        "Bới lông tìm vết để an ủi bản thân",
        "Khi một người đạt được thành tựu rực rỡ, đám đông sẽ lập tức đi tìm khuyết điểm của họ.",
        "Họ bới móc đời tư, phóng đại lỗi lầm cũ, chỉ để tự an ủi rằng: 'Hắn ta cũng chẳng hơn gì mình, chẳng qua là may mắn thôi'.",
        "Hạ bệ người khác là cách hèn nhát nhất để nâng cao lòng tự trọng của kẻ bất tài.",
        "Kẻ bất tài luôn tìm kiếm vết nhơ trên áo người thành công để tự xoa dịu nỗi tự ti của mình; hạ bệ người khác là phương thức rẻ rúng nhất để kẻ tầm thường tìm kiếm cảm giác cân bằng tâm lý."
    ],
    [
        "Thoát khỏi cạm bẫy so sánh",
        "Sự đố kỵ là ngọn lửa thiêu đốt chính kẻ nuôi dưỡng nó trước khi làm bỏng người khác.",
        "Bình yên chỉ thực sự đến khi bạn hiểu rằng cuộc đời không phải một đường chạy đua tập thể; bông hoa nở rộ không cần phải cạnh tranh với ánh trăng trên bầu trời.",
        "Trân trọng hành trình riêng là phương thuốc duy nhất chữa lành lòng đố kỵ.",
        "Lòng đố kỵ là chất độc ta tự uống nhưng lại mong kẻ khác chết; bình yên chỉ bắt đầu khi ta ngừng so sánh hành trình của mình với ánh hào quang của người khác và tập trung vun vén mảnh vườn của riêng mình."
    ],

    # 15. CROWD
    [
        "Sự can đảm của bầy đàn",
        "Một lời kết án có thể nghe rất hào hùng khi được nói giữa hàng ngàn người cùng gật đầu.",
        "Nhưng sự can đảm nương tựa vào số đông thực chất chỉ là một sự hèn nhát tập thể, nơi không một cá nhân nào dám chịu trách nhiệm cho hậu quả của hòn đá mình ném đi.",
        "Đám đông luôn mang lại ảo tưởng về sức mạnh và sự đúng đắn tuyệt đối.",
        "Sự can đảm nương tựa vào bầy đàn thực chất chỉ là sự hèn nhát được nhân bản; khi đứng lẫn trong đám đông cuồng nộ, người ta ném đá không phải vì công lý, mà vì biết chắc mình sẽ không bị trừng phạt đích danh."
    ],
    [
        "Đám đông không có trí tuệ",
        "Khi nhiều người cùng tập hợp lại một chỗ, chỉ số cảm xúc tăng vọt nhưng trí tuệ lại giảm xuống mức thấp nhất.",
        "Họ dễ dàng bị dẫn dắt bởi những khẩu hiệu mị dân, những nỗi sợ hãi hoang đường và cơn khát tìm kiếm một kẻ thù chung để cấu xé.",
        "Hãy cẩn trọng trước bất kỳ phong trào nào đòi hỏi bạn phải tắt đi tư duy phản biện.",
        "Đám đông là một thực thể khổng lồ mang sức mạnh hủy diệt nhưng có khối óc của một đứa trẻ bốc đồng; nó dễ dàng bị thao túng bởi những khẩu hiệu rẻ tiền và sẵn sàng dẫm đạp lên chân lý để thỏa mãn cơn khát bạo lực."
    ],
    [
        "Cái giá của sự khác biệt",
        "Người dám bước ra khỏi hàng ngũ bầy đàn sẽ lập tức trở thành mục tiêu tấn công.",
        "Bởi vì sự tỉnh táo của một cá nhân độc lập là sự sỉ nhục ngầm đối với sự mê muội và phục tùng của cả tập thể xung quanh.",
        "Dám đứng một mình giữa bão tố là phẩm chất hiếm hoi nhất của một con người tự do.",
        "Kẻ dám từ chối hòa tan vào đám đông sẽ luôn là kẻ bị tấn công dữ dội nhất; bởi vì sự độc lập của một cá nhân tự do là chiếc gương tàn nhẫn phơi bày sự nhu nhược của những kẻ chỉ dám sống theo bầy đàn."
    ],
    [
        "Nghi thức săn phù thủy thời hiện đại",
        "Thời trung cổ người ta đốt phù thủy trên giàn hỏa; thời nay người ta đấu tố nhau trên không gian mạng.",
        "Hình thức có thể thay đổi nhưng bản chất vẫn y nguyên: đám đông luôn khao khát một nghi thức hiến tế để xả bớt sự bất mãn và cảm thấy mình đạo đức hơn nạn nhân.",
        "Ngày hôm nay bạn là kẻ ném đá; ngày mai bạn hoàn toàn có thể là kẻ bị trói trên cột.",
        "Các cuộc thanh trừng đạo đức trên mạng xã hội là phiên bản hiện đại của trò săn phù thủy cổ xưa; đám đông chỉ cần một cái cớ để thỏa mãn bản năng bạo lực, và kẻ hôm nay cầm đá hoàn toàn có thể là nạn nhân của ngày mai."
    ],
    [
        "Giữ lòng trắc ẩn giữa sự cuồng nộ",
        "Thước đo bản lĩnh của một con người là giữ được sự bình tĩnh khi xung quanh đều hoảng loạn.",
        "Và giữ được lòng trắc ẩn khi cả đám đông đang say máu đòi trừng phạt một đồng loại.",
        "Đừng để ngọn lửa phẫn nộ của người khác thiêu rụi phần người trong trái tim bạn.",
        "Thước đo phẩm giá tối thượng của một con người là giữ được lòng trắc ẩn ngay giữa cơn cuồng nộ của bầy đàn; khi cả thế giới hò reo đòi giết chết một kẻ sa cơ, người có lương tri sẽ biết cách dừng tay và suy ngẫm."
    ],

    # 16. SUFFERING
    [
        "Biến nỗi đau thành danh tính",
        "Có những người bám chặt lấy vết thương của mình như báu vật quý giá nhất.",
        "Bởi vì nếu vết thương ấy lành lại, họ sẽ mất đi cái cớ để trốn tránh trách nhiệm trưởng thành và mất đi chiếc vương miện của kẻ chịu nhiều bất hạnh nhất trần gian.",
        "Đừng biến bi kịch cá nhân thành chiếc khiên che chở cho sự lười biếng của tâm hồn.",
        "Nhiều người từ chối việc chữa lành vì nỗi đau đã trở thành danh tính duy nhất của họ; họ thích đóng vai nạn nhân của số phận để hợp thức hóa sự yếu đuối và đòi hỏi sự nhượng bộ vô điều kiện từ người đời."
    ],
    [
        "Khổ đau không tự động làm ta cao quý",
        "Nhiều người tin rằng trải qua nhiều đau khổ sẽ tự động biến họ thành người thông thái.",
        "Sự thật là khổ đau nếu không đi kèm với sự phản tư sâu sắc sẽ chỉ tạo ra những con người cay nghiệt, hẹp hòi và đầy lòng oán thán với cuộc đời.",
        "Chỉ có vết thương được thấu hiểu mới có thể hóa thành đóa hoa của sự thấu cảm.",
        "Khổ đau tự thân nó không mang lại sự cao quý; nếu không có sự chiêm nghiệm tỉnh táo, nghịch cảnh chỉ tạo ra những tâm hồn tàn nhẫn và cay độc luôn muốn cả thế giới phải nếm trải nỗi đau giống như mình."
    ],
    [
        "Trốn tránh khổ đau là cội nguồn bi kịch",
        "Con người sẵn sàng làm những điều điên rồ nhất chỉ để né tránh một thoáng buồn bã tự nhiên.",
        "Họ lao vào chất kích thích, mua sắm vô độ hoặc những mối quan hệ độc hại, để rồi nhận ra mình vừa đổi một nỗi đau nhỏ lấy một địa ngục lâu dài.",
        "Chấp nhận ngồi yên với nỗi buồn là bước đầu tiên để vượt qua nó.",
        "Nỗ lực tuyệt vọng để chạy trốn nỗi buồn thường dẫn con người vào những ngõ cụt tăm tối hơn; chấp nhận đối diện với sự đau đớn là con đường duy nhất giúp tâm hồn trưởng thành và ngừng hoảng loạn trước bão giông."
    ],
    [
        "Nỗi đau vay mượn từ quá khứ",
        "Sự việc tồi tệ chỉ xảy ra một lần trong quá khứ.",
        "Nhưng bạn lại bắt tâm trí mình phải nếm trải lại nó hàng ngàn lần qua những ký ức dằn vặt và sự oán hận không chịu buông tha.",
        "Kẻ giam cầm bạn trong đau khổ hôm nay không phải là kẻ đã làm tổn thương bạn năm xưa; đó chính là sự cố chấp của bạn.",
        "Kẻ làm tổn thương bạn chỉ ra tay một lần, nhưng chính bạn lại là kẻ cầm dao tự đâm vào tim mình hàng ngàn lần qua sự hồi tưởng cay đắng; buông bỏ quá khứ không phải là tha thứ cho kẻ thù, mà là giải thoát cho chính mình."
    ],
    [
        "Vết nứt nơi ánh sáng đi vào",
        "Đừng oán trách những đổ vỡ và thất bại đã ghé thăm cuộc đời bạn.",
        "Chính những vết rạn nứt trên lớp vỏ bọc hoàn hảo của cái tôi mới là nơi ánh sáng của sự tỉnh thức và lòng khiêm nhường có thể lọt vào tâm hồn.",
        "Một trái tim chưa từng tan vỡ là một trái tim chưa từng thực sự biết yêu thương.",
        "Những đổ vỡ đau đớn nhất lại chính là cơ hội để ánh sáng tỉnh thức chiếu rọi vào góc khuất tâm hồn; một nhân cách không tì vết thường là một nhân cách xơ cứng, chỉ có trái tim từng rạn vỡ mới thấu hiểu nỗi đau của nhân loại."
    ],

    # 17. IDENTITY
    [
        "Ta là ai khi không còn khán giả",
        "Hãy thử tước bỏ chức danh, mạng xã hội và những lời tán tụng xung quanh.",
        "Điều gì còn lại bên trong bạn khi cánh cửa phòng khép lại và bạn chỉ còn một mình trong đêm tối?",
        "Nếu bạn cảm thấy trống rỗng đến ngạt thở, điều đó có nghĩa là bạn chưa từng thực sự tồn tại như một cá nhân độc lập.",
        "Khi ánh đèn sân khấu tắt ngấm và những lời tung hô chìm vào im lặng, con người thật của bạn mới lộ diện; nếu cảm thấy hoảng loạn trước sự tĩnh lặng ấy, bạn chỉ là một con rối sống nhờ sự chú ý của tha nhân."
    ],
    [
        "Bản sắc được chắp vá từ người khác",
        "Hầu hết những điều bạn tin tưởng, khao khát và theo đuổi hôm nay đều không phải của bạn.",
        "Chúng là những kỳ vọng của cha mẹ, định kiến của xã hội và những mẩu quảng cáo đã được cấy ghép vào đầu bạn từ khi bạn còn chưa kịp biết tư duy.",
        "Hành trình thức tỉnh bắt đầu từ việc gỡ bỏ những mảnh ghép vay mượn ấy.",
        "Phần lớn những thứ ta gọi là lý tưởng sống thực chất chỉ là ước mơ của cha mẹ, định kiến của thời đại và sự nhồi sọ của truyền thông; thức tỉnh là quá trình can đảm lột bỏ từng lớp vỏ vay mượn để tìm lại chính mình."
    ],
    [
        "Trao quyền chấm điểm cho người lạ",
        "Tại sao một lời chê bai từ một kẻ không quen biết trên mạng lại có thể phá hỏng cả ngày của bạn?",
        "Bởi vì bạn chưa từng tự xây dựng cho mình một nền tảng giá trị vững chắc, nên buộc phải sống bấp bênh theo từng nút like và từng ánh nhìn phán xét của thiên hạ.",
        "Kẻ sống nhờ lời khen sẽ chết chìm trong lời phán xét.",
        "Khi một lời bình phẩm ác ý của kẻ xa lạ có thể làm bạn sụp đổ, bạn đã trao quyền sinh sát tâm hồn mình cho thiên hạ; kẻ sống dựa vào sự tán dương của người đời sẽ mãi là con tin của những ánh nhìn phán xét."
    ],
    [
        "Ảo tưởng về sự độc nhất vô nhị",
        "Ai cũng muốn chứng minh mình là một cá thể đặc biệt và khác biệt với phần còn lại của thế giới.",
        "Nhưng nghịch lý là người ta lại dùng chính những công thức rập khuôn, những món đồ hiệu giống nhau và những câu nói thịnh hành để thể hiện sự độc bản của mình.",
        "Sự độc đáo chân chính nằm ở chiều sâu nhận thức, không nằm ở vẻ bề ngoài khác lạ.",
        "Người ta khao khát chứng tỏ mình khác biệt nhưng lại đồng loạt bắt chước những trào lưu giống hệt nhau; sự độc bản chân chính không nằm ở thời trang hay phát ngôn gây sốc, mà nằm ở một tâm hồn tự do không bị định hình bởi số đông."
    ],
    [
        "Vững chãi như ngọn núi",
        "Người thực sự biết rõ giá trị của mình không cần phải lớn tiếng tranh cãi hay thanh minh.",
        "Họ như ngọn núi đứng sừng sững giữa đất trời; bão tố có thể quét qua những tán cây, nhưng không bao giờ có thể làm lung lay nền móng vững chắc bên dưới.",
        "Sự im lặng tự tin luôn quyền uy hơn sự ồn ào giận dữ.",
        "Kẻ thấu hiểu giá trị của mình không cần thanh minh trước những lời đàm tiếu; ngọn núi không tranh luận với cơn gió thoảng qua, nó chỉ lặng lẽ tồn tại và để thời gian chứng minh sự vững chãi của bản thân."
    ],

    # 18. MEANING
    [
        "Vũ trụ không nợ bạn ý nghĩa",
        "Con người luôn đau đáu đi tìm ý nghĩa cuộc đời như thể nó là một kho báu bị giấu kín.",
        "Sự thật là cuộc đời tự thân nó không có sẵn bất kỳ mục đích nào; nó là một trang giấy trắng trống rỗng và lạnh lùng.",
        "Chính những hành động, sự lựa chọn và sự dấn thân của bạn hôm nay mới là thứ tạo nên ý nghĩa cho nó.",
        "Cuộc đời không nợ ta một ý nghĩa có sẵn để kiếm tìm; vũ trụ này hoàn toàn thờ ơ trước sự tồn tại của con người; chính lòng can đảm lựa chọn và dấn thân của ta mới là thứ thổi linh hồn vào sự hư vô của kiếp sống."
    ],
    [
        "Ảo tưởng về luật nhân quả sòng phẳng",
        "Ta thường tin rằng người tốt luôn gặp lành và kẻ ác chắc chắn sẽ gặp quả báo ngay lập tức.",
        "Nhưng hiện thực cuộc sống thường xuyên tát vào mặt ta những bất công phi lý, nơi kẻ lương thiện chịu thiệt thòi còn kẻ toan tính lại nhởn nhơ.",
        "Sống tử tế không phải để đổi lấy phần thưởng của số phận; sống tử tế là vì ta không muốn trở thành một phần của sự tàn nhẫn ấy.",
        "Thế giới không vận hành theo đạo diễn công lý của con người; sống tử tế giữa một thực tại phi lý không phải để đổi chác sự may mắn từ trời cao, mà là để bảo vệ phẩm giá con người trước sự tha hóa của hoàn cảnh."
    ],
    [
        "Cái chết mang lại sức nặng cho sự sống",
        "Nếu con người sống bất tử, cuộc đời này sẽ biến thành một trò chơi vô vị và nhạt nhẽo nhất.",
        "Chính sự hữu hạn của thời gian, chính việc ta biết mình chắc chắn sẽ chết vào một ngày nào đó, mới biến từng cái ôm, từng hơi thở và từng khoảnh khắc hiện tại thành vô giá.",
        "Hãy sống như thể mỗi ngày đều là một lời tạm biệt thanh thản.",
        "Cái chết không phải là kẻ thù phá hủy sự sống, mà là chiếc khung tranh định hình giá trị cho bức tranh cuộc đời; chính vì thời gian có hạn nên từng giây phút ta chọn yêu thương và sống thật mới trở nên thiêng liêng đến thế."
    ],
    [
        "Ý nghĩa trong những điều bình dị",
        "Ta mải miết đi tìm những sứ mệnh vĩ đại để thấy cuộc đời mình đáng giá.",
        "Để rồi bỏ quên niềm vui giản dị của một chén trà sớm, một cơn gió mát hay một ánh mắt chân thành của người thân yêu.",
        "Hạnh phúc không nằm ở đỉnh núi cao; hạnh phúc nằm ở từng bước chân nhẫn nại trên sườn dốc.",
        "Con người mải mê săn đuổi những ảo vọng vĩ đại để rồi đánh mất sự rung động trước một buổi hoàng hôn; ý nghĩa cuộc đời không nằm ở đích đến xa xôi, mà nằm ở năng lực cảm nhận trọn vẹn từng khoảnh khắc bình dị của thực tại."
    ],
    [
        "Nụ cười của kẻ đẩy đá",
        "Cuộc đời giống như hình tượng Sisyphus cả đời đẩy tảng đá lên đỉnh núi rồi nhìn nó lăn xuống.",
        "Nếu bạn xem việc đá lăn xuống là thất bại, bạn sẽ chìm trong tuyệt vọng; nhưng nếu bạn mỉm cười chấp nhận sự phi lý ấy và tiếp tục bước xuống đón lấy tảng đá, bạn đã chiến thắng số phận.",
        "Sức mạnh tối thượng của con người là mỉm cười trước nghịch cảnh.",
        "Bi kịch lớn nhất là khi ta đẩy tảng đá số phận trong sự oán hận; chiến thắng tối thượng của con người là mỉm cười đón nhận sự phi lý của cuộc đời và tìm thấy niềm vui ngay trong chính hành trình nhọc nhằn ấy."
    ],

    # 19. SOLITUDE
    [
        "Cô độc và cô đơn",
        "Có một sự khác biệt sâu sắc giữa việc cảm thấy cô đơn và việc tận hưởng sự cô độc.",
        "Cô đơn là tiếng kêu cứu tuyệt vọng của kẻ không thể chịu nổi chính mình; còn cô độc là thiên đường bình yên của người đã tìm thấy sự hòa hợp với tâm hồn.",
        "Người biết sống một mình mới là người có thể yêu thương người khác một cách trọn vẹn.",
        "Cô đơn là sự trừng phạt dành cho kẻ luôn cần tiếng ồn bên ngoài để quên đi sự bất an nội tại; còn cô độc là đặc ân dành cho tâm hồn đã tự đủ đầy và không còn cần ăn xin sự chú ý từ đám đông."
    ],
    [
        "Nỗi sợ tiếng nghĩ của chính mình",
        "Tại sao khi bước vào một căn phòng vắng, hành động đầu tiên của ta là với tay lấy điện thoại?",
        "Bởi vì khi mọi âm thanh bên ngoài tắt ngấm, căn phòng sẽ buộc ta phải nghe thấy tiếng nghĩ, những câu hỏi chưa có lời đáp và những nỗi ân hận mà ta hằng trốn tránh.",
        "Sự tĩnh lặng là chiếc gương phản chiếu trung thực nhất mà ta luôn muốn đập vỡ.",
        "Ta bật tivi, lướt điện thoại và nói những chuyện vô thưởng vô phạt không phải vì rảnh rỗi, mà vì khi sự tĩnh lặng ập xuống, ta kinh hãi khi phải lắng nghe những tiếng thở dài và sự dằn vặt của chính tâm hồn mình."
    ],
    [
        "Lạc lõng giữa đám đông ồn ào",
        "Cảm giác cô độc buốt giá nhất không phải là khi bạn ở một mình trong rừng sâu.",
        "Đó là khi bạn đang ngồi giữa một bàn tiệc rộn rã tiếng cười, nhưng nhận ra không một ai trong số họ thực sự hiểu được nỗi đau mà bạn đang mang trong lồng ngực.",
        "Hòa nhập sai chỗ còn tàn nhẫn hơn sự cô lập.",
        "Sự cô độc cùng cực nhất là khi ta phải gượng cười giữa một đám đông náo nhiệt nhưng hoàn toàn xa lạ về tâm hồn; thà can đảm rút lui vào sự im lặng còn hơn tự đày đọa mình trong những cuộc vui giả tạo."
    ],
    [
        "Học cách làm bạn với chính mình",
        "Nếu bạn không thể ngồi uống một tách cà phê trong an yên với chính mình, bạn sẽ không thể mang lại bình an cho bất kỳ ai.",
        "Mọi mối quan hệ của bạn lúc ấy sẽ bị biến thành công cụ cứu cánh để xua đuổi bóng ma cô độc.",
        "Hãy học cách tự chữa lành trước khi mong cầu người khác cứu rỗi.",
        "Nếu không thể tự tìm thấy niềm vui trong sự tĩnh lặng của chính mình, bạn sẽ luôn bước vào tình yêu với tâm thế của một kẻ ăn mày cảm xúc; tự chữa lành là điều kiện tiên quyết để xây dựng một mối quan hệ lành mạnh."
    ],
    [
        "Sức mạnh của sự trầm lặng",
        "Người nông cạn thường sợ hãi sự im lặng và luôn tìm cách lấp đầy nó bằng những lời ba hoa.",
        "Người từng trải hiểu rằng sự im lặng có sức nặng hơn ngàn lời giải thích; kẻ hiểu bạn không cần bạn nói nhiều, kẻ định kiến sẽ bóp méo mọi điều bạn thanh minh.",
        "Im lặng đúng lúc là sự khôn ngoan đỉnh cao của phẩm giá.",
        "Sự im lặng có sức mạnh hủy diệt những thị phi lớn hơn mọi lời phân trần giận dữ; kẻ có nội lực vững vàng sẽ biết khi nào nên mỉm cười bước qua và để sự thật tự cất lên tiếng nói theo thời gian."
    ],

    # 20. STATUS
    [
        "Cơn khát sự công nhận của xã hội",
        "Con người sẵn sàng vắt kiệt sức lao động để kiếm tiền mua những món đồ mình không cần.",
        "Chỉ nhằm mục đích gây ấn tượng với những kẻ mà trong lòng họ vốn dĩ không hề tôn trọng hay yêu quý.",
        "Sự phù phiếm là chiếc cối xay gió nghiền nát sự bình yên đích thực của cuộc đời.",
        "Nghịch lý lớn nhất của con người hiện đại là làm việc kiệt sức để mua những thứ xa xỉ nhằm khoe khoang với những kẻ xa lạ; ta tự đày đọa cuộc đời mình chỉ để đổi lấy vài giây thèm muốn từ ánh mắt người đời."
    ],
    [
        "Cái giá của chiếc ngai vàng",
        "Càng leo lên những bậc thang danh vọng cao hơn, bạn sẽ càng thấy không khí loãng dần và gió lạnh buốt hơn.",
        "Những nụ cười xung quanh bạn sẽ ngày càng tươi hơn, nhưng những cái ôm sẽ ngày càng mang nhiều mùi vị của sự toan tính và vụ lợi.",
        "Đỉnh cao của quyền lực thường là khởi đầu của sự cô lập tuyệt đối.",
        "Càng bước lên đỉnh cao danh vọng, vòng tròn những người chân thành xung quanh bạn càng thu hẹp lại; chiếc ngai vàng quyền lực luôn được xây dựng trên một vùng đất cô độc và đầy rẫy sự đề phòng."
    ],
    [
        "Khiêm nhường như một nước cờ quyền lực",
        "Có những kẻ dùng sự khiêm tốn như một chiến lược thao túng tinh vi nhất.",
        "Họ chủ động nhận phần thiệt, lùi lại phía sau và nói những lời nhún nhường, chỉ để ru ngủ đối thủ và chờ thời cơ tung ra đòn quyết định.",
        "Hãy cảnh giác với những kẻ quá hoàn hảo trong vai diễn của sự nhường nhịn.",
        "Sự khiêm nhường có tính toán là vũ khí lợi hại nhất của kẻ tham vọng; họ cúi đầu nhẫn nhịn không phải vì nhân từ, mà để tích lũy lợi thế và chờ đợi khoảnh khắc đối phương sơ hở để đoạt lấy toàn bộ ván cờ."
    ],
    [
        "Nạn nhân của ánh hào quang",
        "Danh tiếng là thứ phù hoa nguy hiểm nhất mà con người từng phát minh ra.",
        "Đám đông có thể tung hô bạn lên mây xanh hôm nay chỉ vì một thành tích, và chính họ sẽ dùng những lời lẽ độc địa nhất để dẫm đạp bạn xuống đất bùn vào ngày mai.",
        "Đừng bao giờ xây dựng ngôi nhà hạnh phúc của mình trên bãi cát lún của dư luận.",
        "Đám đông nâng bạn lên được thì cũng sẵn sàng dẫm đạp bạn xuống bùn sâu một cách tàn nhẫn nhất; kẻ gửi gắm lòng tự trọng vào sự tung hô của dư luận đang xây lâu đài trên một bãi cát lún không đáy."
    ],
    [
        "Phẩm giá nội tại vượt trên danh vị",
        "Đẳng cấp thực sự của một con người không nằm ở chức danh trên danh thiếp hay số dư trong tài khoản.",
        "Nó nằm ở cách họ đối xử với người phục vụ bàn, ở sự điềm tĩnh khi bị tước bỏ toàn bộ đặc quyền, và ở phẩm giá bất biến khi đứng trước những cám dỗ thấp hèn.",
        "Vàng thật không sợ lửa; nhân cách thật không cần danh vị để chứng minh.",
        "Phẩm giá đích thực của một con người bộc lộ rõ nhất khi họ bị tước bỏ mọi danh vị và quyền lực bên ngoài; kẻ có cốt cách cao quý vẫn giữ được sự đĩnh đạc và lòng nhân từ ngay cả khi đứng giữa bùn lầy."
    ]
]

def build_100_posts():
    posts = []
    post_idx = 1
    start_date = datetime(2026, 11, 16)
    time_slots = ["11:30 - 12:30 (Trưa)", "19:30 - 20:30 (Tối)", "21:00 - 22:30 (Đêm chiêm nghiệm)"]

    for t_idx, (t_code, t_name) in enumerate(THEMES):
        for item_idx in range(5):
            p_title, p_s1, p_s2, p_s3, p_full = ALL_100_POSTS[t_idx * 5 + item_idx]
            
            post_id = f"TXT-{post_idx:04d}"
            curr_date = start_date + timedelta(days=post_idx - 1)
            date_str = curr_date.strftime("%Y-%m-%d")
            weekday_str = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"][curr_date.weekday()]
            full_date_label = f"{weekday_str} ({curr_date.strftime('%d/%m')})"
            time_slot = time_slots[post_idx % len(time_slots)]
            fmt = "Slide 3 trang (Đọc sâu 7-9s)"

            hashtags = f"#hiyuabyss #{t_code.lower()} #tamlyhoc #trietngon #darkpsychology #bocchuan #gocnhin #phanthu"
            visual = f"Tone tối giản Dark Mode, nhạc piano/ambient trầm, chữ sans-serif trắng trên nền xám than, hiệu ứng fade chậm"

            posts.append([
                post_idx,
                full_date_label,
                date_str,
                time_slot,
                post_id,
                p_title,
                f"{t_code} ({t_name})",
                fmt,
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
        "Trang 1 (Hook Mở Màn - Câu Hoàn Chỉnh)",
        "Trang 2 (Cú Lật Bóc Trần - Câu Hoàn Chỉnh)",
        "Trang 3 (Chiếc Gương Phản Tư - Đọng Lại)",
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

    print(f"Đã tạo thành công {len(posts)} bài triết ngôn độc bản tại {out_csv}")

if __name__ == "__main__":
    main()
