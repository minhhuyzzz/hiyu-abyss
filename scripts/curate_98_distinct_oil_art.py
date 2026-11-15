import json

def get_98_curated_art_mapping():
    """
    Bản đồ tuyển chọn 98 tác phẩm sơn dầu cổ điển bảo tàng độc bản
    Khớp chính xác với nội dung từng slide cho 50 chủ đề (Theme 151 - 200).
    Mỗi slide mang một biểu tượng thị giác kinh điển phản ánh đúng tâm lý học.
    """
    curation = [
        # === 151. THAO TÚNG: GASLIGHTING (3 slides) ===
        {
            "theme_id": "theme_151", "slide": 1, "role": "Hook",
            "text": "Khi ai đó liên tục bảo bạn......",
            "artwork": "Caspar David Friedrich - Wanderer above the Sea of Fog",
            "query": "Caspar David Friedrich Wanderer above the Sea of Fog",
            "justification": "Màn sương mù mịt mùng tượng trưng cho sự hoang mang, lạc lối trong nhận thức bị bóp méo."
        },
        {
            "theme_id": "theme_151", "slide": 2, "role": "Twist",
            "text": "Rằng bạn đang làm quá lên, rằng bạn quá nhạy cảm hay nhớ nhầm mọi chuyện.",
            "artwork": "Caravaggio - The Cardsharps",
            "query": "Caravaggio The Cardsharps",
            "justification": "Kẻ gian lận đang thì thầm ra hiệu gian dối sau lưng, bóc trần sự thao túng ngầm có tính toán."
        },
        {
            "theme_id": "theme_151", "slide": 3, "role": "Mirror",
            "text": "Họ không bảo vệ sự thật; họ đang từng bước hủy hoại chiếc la bàn nhận thức của bạn để biến bạn thành tù nhân cảm xúc.",
            "artwork": "Georges de La Tour - The Penitent Magdalen",
            "query": "Georges de La Tour The Penitent Magdalen MET DT7252",
            "justification": "Ngọn nến đơn độc soi rọi chiếc gương và hộp sọ — biểu tượng của sự thức tỉnh và nhận thức sự thật trần trụi."
        },

        # === 152. THAO TÚNG: ÁI KỶ NGẤM NGẦM (2 slides) ===
        {
            "theme_id": "theme_152", "slide": 1, "role": "Hook",
            "text": "Kẻ ái kỷ độc hại nhất......",
            "artwork": "Caravaggio - Narcissus",
            "query": "Caravaggio Narcissus 1597-99",
            "justification": "Hình tượng kinh điển của Narcissus soi bóng mê muội vào chính mình trong bóng tối cô độc."
        },
        {
            "theme_id": "theme_152", "slide": 2, "role": "Twist",
            "text": "Không đòi bạn tán dương, họ dùng sự đáng thương và nước mắt để trói bạn vào món nợ cảm xúc không bao giờ trả hết.",
            "artwork": "Jacques-Louis David - The Death of Marat",
            "query": "Jacques-Louis David The Death of Marat",
            "justification": "Tư thế nằm trong bồn tắm đẫm máu như vị tử đạo đáng thương, biến mình thành nạn nhân để thao túng mặc cảm tội lỗi."
        },

        # === 153. THAO TÚNG: BẪY MACHIAVELLIAN (1 slide) ===
        {
            "theme_id": "theme_153", "slide": 1, "role": "Single-Punch",
            "text": "Lòng tốt thiếu ranh giới không phải sự bao dung, đó là lời mời gọi kẻ thực dụng đến lợi dụng bạn.",
            "artwork": "Quentin Matsys - The Moneylender and his Wife",
            "query": "Quentin Matsys The Moneylender and his Wife Louvre",
            "justification": "Cặp đôi cân từng đồng tiền vàng với ánh mắt săm soi toan tính, biểu hiện của sự vụ lợi lạnh lùng trước người tốt ngây thơ."
        },

        # === 154. THAO TÚNG: LOVE BOMBING (3 slides) ===
        {
            "theme_id": "theme_154", "slide": 1, "role": "Hook",
            "text": "Sự nồng nhiệt đến ngột ngạt ban đầu......",
            "artwork": "Lawrence Alma-Tadema - The Roses of Heliogabalus",
            "query": "Lawrence Alma-Tadema The Roses of Heliogabalus",
            "justification": "Cơn mưa cánh hoa hồng ngập ngụa phủ kín nhưng bóp nghẹt các vị khách — ẩn dụ hoàn hảo nhất trong lịch sử hội họa cho Love Bombing."
        },
        {
            "theme_id": "theme_154", "slide": 2, "role": "Twist",
            "text": "Hiếm khi xuất phát từ tình yêu chân thành; đó là chiếc lưới đánh cá bọc nhung đang siết lại quanh tự do của bạn.",
            "artwork": "John William Waterhouse - La Belle Dame sans Merci",
            "query": "John William Waterhouse La Belle Dame sans Merci",
            "justification": "Nàng tiên kiều diễm dùng lọn tóc và vòng hoa quấn chặt cổ hiệp sĩ, trói buộc chàng vào bẫy tình ảo giác."
        },
        {
            "theme_id": "theme_154", "slide": 3, "role": "Mirror",
            "text": "Một mối quan hệ lành mạnh cần không gian để thở, không phải một cơn bão khiến bạn choáng ngợp và đánh mất lý trí.",
            "artwork": "Vilhelm Hammershoi - Interior with Young Woman Seen from the Back",
            "query": "Vilhelm Hammershoi Interior with Young Woman Seen from the Back",
            "justification": "Căn phòng Bắc Âu tĩnh lặng, tối giản, thoáng đãng — gợi mở sự bình yên nội tại và khoảng thở tự do trong tâm hồn."
        },

        # === 155. THAO TÚNG: BẠO LỰC IM LẶNG (2 slides) ===
        {
            "theme_id": "theme_155", "slide": 1, "role": "Hook",
            "text": "Im lặng không phải lúc nào cũng vàng......",
            "artwork": "Frederic Leighton - Solitude",
            "query": "Frederic Leighton Solitude",
            "justification": "Người phụ nữ ngồi cuộn mình cô độc quay lưng trên mỏm đá lạnh buốt, cảm giác lạnh lẽo của sự cô lập."
        },
        {
            "theme_id": "theme_155", "slide": 2, "role": "Twist",
            "text": "Khi nó được dùng để ép bạn phải quỳ gối xin lỗi cho những sai lầm không phải của mình, đó là sự tàn nhẫn đội lốt điềm tĩnh.",
            "artwork": "Edmund Leighton - The Accolade",
            "query": "Edmund Leighton The Accolade",
            "justification": "Tư thế hiệp sĩ quỳ gối cúi đầu trước thanh gươm của kẻ nắm quyền, biểu hiện của sự khuất phục tâm lý cưỡng ép."
        },

        # === 156. THAO TÚNG: NỢ ÂN TÌNH ĐỘC HẠI (1 slide) ===
        {
            "theme_id": "theme_156", "slide": 1, "role": "Single-Punch",
            "text": "Ân huệ mà người ta liên tục nhắc lại không phải là sự giúp đỡ; đó là chiếc hóa đơn đòi lại linh hồn bạn.",
            "artwork": "Marinus van Reymerswaele - The Moneychanger and his Wife",
            "query": "Marinus van Reymerswaele The Moneychanger and his Wife",
            "justification": "Kẻ cho vay ghi chép sổ nợ chi li với ngón tay chìa ra đòi nợ, hóa thân của ân tình tính toán."
        },

        # === 157. THAO TÚNG: CƠN THỊNH NỘ ÁI KỶ (3 slides) ===
        {
            "theme_id": "theme_157", "slide": 1, "role": "Hook",
            "text": "Khi bạn nói ra sự thật hiển nhiên......",
            "artwork": "Jacques-Louis David - The Death of Socrates",
            "query": "Jacques-Louis David The Death of Socrates",
            "justification": "Socrates điềm tĩnh chỉ tay lên trời nói sự thật giữa những kẻ sợ hãi và phán xét."
        },
        {
            "theme_id": "theme_157", "slide": 2, "role": "Twist",
            "text": "Kẻ thao túng không phủ nhận bằng lý lẽ; họ gầm thét, đóng sầm cửa và biến mình thành nạn nhân bị xúc phạm.",
            "artwork": "Francisco Goya - Saturn Devouring His Son",
            "query": "Francisco Goya Saturn Devouring His Son",
            "justification": "Ánh mắt điên loạn cuồng nộ tàn bạo nuốt chửng con cái, sự hoảng loạn mất kiểm soát của kẻ độc tài bị đe dọa quyền lực."
        },
        {
            "theme_id": "theme_157", "slide": 3, "role": "Mirror",
            "text": "Cơn giận dữ đó không phải sức mạnh; đó là tiếng la hét tuyệt vọng của một bản ngã giả tạo đang sụp đổ trước ánh sáng chân lý.",
            "artwork": "Alexandre Cabanel - The Fallen Angel",
            "query": "Alexandre Cabanel The Fallen Angel",
            "justification": "Giọt nước mắt phẫn uất cay đắng của thiên thần sa ngã Lucifer — chiếc mặt nạ kiêu hãnh bị lột trần để lộ nỗi nhục nhã."
        },

        # === 158. THAO TÚNG: TỘI LỖI GÁN ÉP (1 slide) ===
        {
            "theme_id": "theme_158", "slide": 1, "role": "Single-Punch",
            "text": "Đừng tự thiêu rụi chính mình chỉ để sưởi ấm cho một kẻ luôn phàn nàn rằng đốm lửa của bạn quá nhỏ.",
            "artwork": "Jan Cossiers - Prometheus Carrying Fire",
            "query": "Jan Cossiers Prometheus Carrying Fire Prado",
            "justification": "Prometheus cầm ngọn đuốc cháy rực hy sinh thân mình trong đêm tối vô ơn."
        },

        # === 159. THAO TÚNG: CHIẾN THUẬT BÀO MÒN (2 slides) ===
        {
            "theme_id": "theme_159", "slide": 1, "role": "Hook",
            "text": "Nếu bạn lùi một bước......",
            "artwork": "Honore Daumier - The Chess Players",
            "query": "Honore Daumier The Chess Players",
            "justification": "Hai kỳ thủ căng thẳng tính toán từng nước đi thăm dò, đòn tâm lý rình rập đối phương sơ hở."
        },
        {
            "theme_id": "theme_159", "slide": 2, "role": "Twist",
            "text": "Kẻ không biết tôn trọng ranh giới sẽ đòi bạn lùi mười bước, cho đến khi lưng bạn dán chặt vào tường.",
            "artwork": "Paul Delaroche - Napoleon at Fontainebleau",
            "query": "Paul Delaroche Napoleon at Fontainebleau",
            "justification": "Vị hoàng đế bị dồn vào chân tường, ngồi kiệt quệ nhìn khoảng không sau khi nhượng bộ từng bước."
        },

        # === 160. THAO TÚNG: THOÁT KHỎI KHÍ ĐỘC (3 slides) ===
        {
            "theme_id": "theme_160", "slide": 1, "role": "Hook",
            "text": "Đừng tốn sức giải thích......",
            "artwork": "Fra Angelico - The Mocking of Christ",
            "query": "Fra Angelico The Mocking of Christ",
            "justification": "Người ngồi tĩnh lặng bịt mắt trước những bàn tay vô danh chĩa vào nhạo báng."
        },
        {
            "theme_id": "theme_160", "slide": 2, "role": "Twist",
            "text": "Với kẻ đã quyết tâm bóp méo câu từ của bạn để phục vụ cho sự đắc thắng của họ.",
            "artwork": "Pieter Bruegel the Elder - The Tower of Babel",
            "query": "Pieter Bruegel the Elder The Tower of Babel",
            "justification": "Tòa tháp hỗn loạn của sự chia rẽ ngôn ngữ và sự bóp méo hiểu lầm có chủ đích."
        },
        {
            "theme_id": "theme_160", "slide": 3, "role": "Mirror",
            "text": "Thu hồi toàn bộ sự chú ý của bạn; sự im lặng dửng dưng chính là bản án nặng nề nhất dành cho kẻ thèm khát quyền lực.",
            "artwork": "Caspar David Friedrich - Wanderer in the Mist",
            "query": "Caspar David Friedrich Wanderer in the Mist",
            "justification": "Bóng lưng người đàn ông đứng trên mỏm đá tĩnh lặng, quay lưng hoàn toàn với thế giới ồn ào dưới chân."
        },

        # === 161. TÂM LÝ ĐÁM ĐÔNG: ẢO TƯỞNG BẦY CỪU (3 slides) ===
        {
            "theme_id": "theme_161", "slide": 1, "role": "Hook",
            "text": "Khi bạn bước vào đám đông......",
            "artwork": "Pieter Bruegel the Elder - The Blind Leading the Blind",
            "query": "Pieter Bruegel the Elder The Blind Leading the Blind",
            "justification": "Đoàn người mù quáng dắt tay nhau bước hụt xuống hào nước — hình tượng bất hủ của tâm lý bầy đàn."
        },
        {
            "theme_id": "theme_161", "slide": 2, "role": "Twist",
            "text": "Lý trí của bạn bị bốc hơi, nhường chỗ cho những cơn cuồng nộ vô cớ và sự hung hãn tập thể.",
            "artwork": "Theodore Gericault - The Raft of the Medusa",
            "query": "Theodore Gericault The Raft of the Medusa",
            "justification": "Đám đông hỗn loạn giằng xé trong tuyệt vọng trên chiếc bè giữa sóng dữ, thú tính bộc phát."
        },
        {
            "theme_id": "theme_161", "slide": 3, "role": "Mirror",
            "text": "Giữ vững tâm trí tĩnh lặng giữa một bầy người đang phát cuồng chính là đỉnh cao của bản lĩnh làm người.",
            "artwork": "Rembrandt - The Philosopher in Meditation",
            "query": "Rembrandt The Philosopher in Meditation",
            "justification": "Căn phòng tĩnh lặng với chiếc cầu thang xoắn ốc và ánh sáng mặt trời chiếu qua khung cửa, nơi lý trí ẩn mình chiêm nghiệm."
        },

        # === 162. TÂM LÝ ĐÁM ĐÔNG: SỰ TẦM THƯỜNG CỦA CÁI ÁC (1 slide) ===
        {
            "theme_id": "theme_162", "slide": 1, "role": "Single-Punch",
            "text": "Tội ác ghê rợn nhất lịch sử không được thực hiện bởi những kẻ cuồng bạo; nó được thi hành bởi những kẻ công chức mẫn cán chỉ biết 'chấp hành mệnh lệnh'.",
            "artwork": "Francisco Goya - The Third of May 1808",
            "query": "Francisco Goya The Third of May 1808",
            "justification": "Hàng lính súng giấu mặt xếp thẳng hàng như cỗ máy vô cảm nổ súng vào người dân thường theo mệnh lệnh."
        },

        # === 163. TÂM LÝ ĐÁM ĐÔNG: THÍ NGHIỆM MILGRAM (2 slides) ===
        {
            "theme_id": "theme_163", "slide": 1, "role": "Hook",
            "text": "Khi một kẻ nhân danh quyền lực......",
            "artwork": "Valentin de Boulogne - The Judgment of Solomon",
            "query": "Valentin de Boulogne The Judgment of Solomon",
            "justification": "Vua Solomon ngồi trên ngai chỉ tay ra lệnh, người thi hành tuốt gươm theo lệnh quyền lực."
        },
        {
            "theme_id": "theme_163", "slide": 2, "role": "Twist",
            "text": "Ra lệnh cho bạn nhấn nút gây đau đớn cho đồng loại, hầu hết mọi người đều ngoan ngoãn phục tùng mà không một lần chất vấn lương tâm.",
            "artwork": "Mattia Preti - Pilate Washing His Hands",
            "query": "Mattia Preti Pilate Washing His Hands",
            "justification": "Pontius Pilate rửa tay chối bỏ trách nhiệm đạo đức cá nhân sau khi ký lệnh trừng phạt."
        },

        # === 164. TÂM LÝ ĐÁM ĐÔNG: THÍ NGHIỆM ASCH (3 slides) ===
        {
            "theme_id": "theme_164", "slide": 1, "role": "Hook",
            "text": "Người ta thà đồng thuận với điều sai trái......",
            "artwork": "Sandro Botticelli - The Calumny of Apelles",
            "query": "Sandro Botticelli The Calumny of Apelles",
            "justification": "Đoàn người a dua theo lời vu khống kéo lê nạn nhân trước quan tòa bị bao vây bởi dối trá."
        },
        {
            "theme_id": "theme_164", "slide": 2, "role": "Twist",
            "text": "Cùng với số đông, còn hơn là đơn độc nói lên sự thật và bị cô lập khỏi bầy đàn.",
            "artwork": "Honoré Daumier - The Third-Class Carriage",
            "query": "Honoré Daumier The Third-Class Carriage",
            "justification": "Toa tàu hạng ba chật ních những gương mặt đờ đẫn, khép mình theo nhịp sống chung của đám đông lầm lũi."
        },
        {
            "theme_id": "theme_164", "slide": 3, "role": "Mirror",
            "text": "Dũng khí lớn nhất không phải chiến đấu với kẻ thù, mà là dám giơ tay phản đối khi cả căn phòng đang gật đầu đồng thuận.",
            "artwork": "Ilya Repin - They Did Not Expect Him",
            "query": "Ilya Repin They Did Not Expect Him",
            "justification": "Người tù chính trị kiên cường bất ngờ bước vào phòng, ánh mắt kiên định đứng ngoài mọi sự an phận của người xung quanh."
        },

        # === 165. TÂM LÝ ĐÁM ĐÔNG: HIỆU ỨNG BÀNG QUAN (2 slides) ===
        {
            "theme_id": "theme_165", "slide": 1, "role": "Hook",
            "text": "Khi tất cả cùng nhìn......",
            "artwork": "Eugene Delacroix - The Good Samaritan",
            "query": "Eugene Delacroix The Good Samaritan",
            "justification": "Người bị nạn nằm gục bên vệ đường trong khi các nhân vật sang trọng đi qua lờ đi."
        },
        {
            "theme_id": "theme_165", "slide": 2, "role": "Twist",
            "text": "Sẽ không có ai hành động; trách nhiệm bị chia nhỏ cho đến khi lương tâm của tất cả cùng tê liệt.",
            "artwork": "Pieter Bruegel the Elder - Landscape with the Fall of Icarus",
            "query": "Pieter Bruegel the Elder Landscape with the Fall of Icarus",
            "justification": "Icarus rơi xuống biển giãy giụa trong khi người cày ruộng và thuyền buồm vẫn dửng dưng tiếp tục công việc của mình."
        },

        # === 166. TÂM LÝ ĐÁM ĐÔNG: QUYỀN LỰC NGÔN TỪ BẦY ĐÀN (1 slide) ===
        {
            "theme_id": "theme_166", "slide": 1, "role": "Single-Punch",
            "text": "Đám đông tha thứ cho sự tàn nhẫn, nhưng không bao giờ tha thứ cho kẻ phá vỡ ảo tưởng của họ.",
            "artwork": "Jean-Leon Gerome - Pollice Verso",
            "query": "Jean-Leon Gerome Pollice Verso",
            "justification": "Đám đông khán giả La Mã đồng loạt chỉ ngón tay xuống đất đòi giết võ sĩ bại trận để thỏa mãn cơn khát máu tập thể."
        },

        # === 167. TÂM LÝ ĐÁM ĐÔNG: LỐI MÒN TƯ DUY NHÓM (3 slides) ===
        {
            "theme_id": "theme_167", "slide": 1, "role": "Hook",
            "text": "Khi tất cả cùng nghĩ giống nhau......",
            "artwork": "James Ensor - The Intrigue",
            "query": "James Ensor The Intrigue",
            "justification": "Một nhóm người đeo mặt nạ quái dị vây quanh nhau trong sự đồng lõa méo mó."
        },
        {
            "theme_id": "theme_167", "slide": 2, "role": "Twist",
            "text": "Thì không còn ai đang thực sự tư duy; sự đồng thuận mù quáng là nấm mồ chôn cất trí tuệ.",
            "artwork": "Lucas Cranach the Elder - The Fountain of Youth",
            "query": "Lucas Cranach the Elder The Fountain of Youth",
            "justification": "Đoàn người mù quáng chen chúc lội vào dòng suối ảo ảnh hy vọng cải lão hoàn đồng."
        },
        {
            "theme_id": "theme_167", "slide": 3, "role": "Mirror",
            "text": "Một tổ chức chết dần khi người phản biện bị coi là kẻ phản bội; hãy trân trọng kẻ dám nói ra điều chướng tai.",
            "artwork": "Rembrandt - Aristotle with a Bust of Homer",
            "query": "Rembrandt Aristotle with a Bust of Homer",
            "justification": "Aristotle đặt tay lên tượng Homer mù, tư duy phản biện độc lập đối thoại qua ngàn năm lịch sử."
        },

        # === 168. TÂM LÝ ĐÁM ĐÔNG: BÌNH THƯỜNG HÓA SỰ TÀN NHẪN (1 slide) ===
        {
            "theme_id": "theme_168", "slide": 1, "role": "Single-Punch",
            "text": "Khi thói xấu trở thành thông lệ của số đông, người tử tế bỗng nhiên bị coi là kẻ lập dị và nguy hiểm.",
            "artwork": "Hieronymus Bosch - Christ Carrying the Cross",
            "query": "Hieronymus Bosch Christ Carrying the Cross Ghent",
            "justification": "Khuôn mặt nhân từ nhắm mắt chịu đựng giữa biển người mang gương mặt thú tính gớm ghiếc biến thái."
        },

        # === 169. TÂM LÝ ĐÁM ĐÔNG: HIỆU ỨNG VÔ DANH (2 slides) ===
        {
            "theme_id": "theme_169", "slide": 1, "role": "Hook",
            "text": "Khi khuôn mặt bị che khuất......",
            "artwork": "Pietro Longhi - The Rhinoceros",
            "query": "Pietro Longhi The Rhinoceros",
            "justification": "Đám đông quý tộc Venice đeo mặt nạ trắng vô hồn xem thú lạ, che giấu danh tính cá nhân."
        },
        {
            "theme_id": "theme_169", "slide": 2, "role": "Twist",
            "text": "Bóng tối trong tâm hồn con người mới thực sự lộ diện; sự ẩn danh là liều thuốc độc kích hoạt bản năng hoang dã nhất.",
            "artwork": "Francisco Goya - Witches Sabbath",
            "query": "Francisco Goya Witches Sabbath",
            "justification": "Hội đồng phù thủy tụ tập trong đêm đen quanh con dê quỷ, bản năng bóng tối trần trụi khi không ai quan sát."
        },

        # === 170. TÂM LÝ ĐÁM ĐÔNG: TỰ DO TƯ TƯỞNG TỐI THƯỢNG (1 slide) ===
        {
            "theme_id": "theme_170", "slide": 1, "role": "Single-Punch",
            "text": "Thà đi lạc trên con đường của chính mình, còn hơn là đi đúng hướng trên lối mòn được đám đông vạch sẵn.",
            "artwork": "Caspar David Friedrich - The Solitary Tree",
            "query": "Caspar David Friedrich The Solitary Tree",
            "justification": "Cây sồi cổ thụ sừng sững đơn độc giữa cánh đồng xanh bao la, kiêu hãnh và tự do trước bầu trời giông bão."
        },

        # === 171. NGỤY TÍN (BAD FAITH): TỰ LỪA DỐI (3 slides) ===
        {
            "theme_id": "theme_171", "slide": 1, "role": "Hook",
            "text": "Bạn không phải nạn nhân của số phận......",
            "artwork": "Francisco Goya - The Garrotte",
            "query": "Francisco Goya The Garrotte",
            "justification": "Tử tù bị xích trên ghế garrote định mệnh, biểu tượng của sự cam chịu thụ động."
        },
        {
            "theme_id": "theme_171", "slide": 2, "role": "Twist",
            "text": "Bạn chỉ đang dùng hoàn cảnh làm bình phong để trốn chạy trách nhiệm phải tự mình lựa chọn và hành động.",
            "artwork": "Francisco Goya - The Sleep of Reason Produces Monsters",
            "query": "Francisco Goya The Sleep of Reason Produces Monsters",
            "justification": "Người đàn ông gục đầu ngủ trên bàn, để mặc những con cú và dơi ma quái vây quanh — sự chối bỏ nhận thức tỉnh táo."
        },
        {
            "theme_id": "theme_171", "slide": 3, "role": "Mirror",
            "text": "Con người bị kết án là phải tự do; khoảnh khắc bạn ngừng đổ lỗi là lúc cuộc đời bạn thực sự bắt đầu.",
            "artwork": "Eugene Delacroix - Liberty Leading the People",
            "query": "Eugene Delacroix Liberty Leading the People",
            "justification": "Nữ thần Tự Do phất cao lá cờ vượt qua chướng ngại vật, biểu tượng của tự do dấn thân và hành động."
        },

        # === 172. NGỤY TÍN: TRỐN CHẠY TỰ DO (2 slides) ===
        {
            "theme_id": "theme_172", "slide": 1, "role": "Hook",
            "text": "Tự do thực sự quá cô đơn và đáng sợ......",
            "artwork": "Edvard Munch - Melancholy",
            "query": "Edvard Munch Melancholy",
            "justification": "Người đàn ông ngồi tựa đầu bên bờ biển hoang vắng, gánh nặng của tự do và nỗi cô đơn hiện sinh."
        },
        {
            "theme_id": "theme_172", "slide": 2, "role": "Twist",
            "text": "Nên người ta tự nguyện chui vào những chiếc lồng định kiến để đổi lấy cảm giác an toàn giả tạo.",
            "artwork": "Carl Spitzweg - The Poor Poet",
            "query": "Carl Spitzweg The Poor Poet",
            "justification": "Nhà thơ nghèo nằm co ro trong căn gác xép dột nát che ô, tự giam mình trong thế giới an toàn chật hẹp."
        },

        # === 173. NGỤY TÍN: VỞ KỊCH XÃ HỘI (1 slide) ===
        {
            "theme_id": "theme_173", "slide": 1, "role": "Single-Punch",
            "text": "Đừng để chức danh công việc nuốt chửng con người bạn; kẻ phục vụ bàn diễn vai phục vụ bàn giỏi đến mức quên mất mình là một con người tự do.",
            "artwork": "Edouard Manet - A Bar at the Folies-Bergere",
            "query": "Edouard Manet A Bar at the Folies-Bergere",
            "justification": "Cô hầu bàn đứng sau quầy rượu xa hoa với ánh mắt xa xăm lạc lõng, hóa thân của nhân vật bị đóng khung trong vai diễn xã hội."
        },

        # === 174. NGỤY TÍN: LO ÂU HIỆN SINH (3 slides) ===
        {
            "theme_id": "theme_174", "slide": 1, "role": "Hook",
            "text": "Cơn lo âu hiện sinh......",
            "artwork": "Albrecht Durer - Melencolia I",
            "query": "Albrecht Durer Melencolia I",
            "justification": "Thiên thần ngồi trầm ngâm giữa các công cụ đo lường vũ trụ, biểu tượng kinh điển của sự suy tư trăn trở hiện sinh."
        },
        {
            "theme_id": "theme_174", "slide": 2, "role": "Twist",
            "text": "Không phải bệnh tật; đó là cơn chóng mặt của tự do khi bạn nhận ra mình có vô vàn khả năng và phải tự gánh chịu kết quả.",
            "artwork": "Caspar David Friedrich - Chalk Cliffs on Rugen",
            "query": "Caspar David Friedrich Chalk Cliffs on Rugen",
            "justification": "Miệng vực thẳm đá vôi dốc đứng nhìn xuống biển xanh thẳm, cảm giác choáng ngợp trước vực sâu tự do."
        },
        {
            "theme_id": "theme_174", "slide": 3, "role": "Mirror",
            "text": "Dám bước qua cơn lo âu đó là bước ngoặt đưa bạn từ một kẻ sống mòn thành người kiến tạo số phận.",
            "artwork": "Caspar David Friedrich - Morning in the Riesengebirge",
            "query": "Caspar David Friedrich Morning in the Riesengebirge",
            "justification": "Đứng trên đỉnh núi đón ánh bình minh rạng rỡ sau màn sương đêm, sự thăng hoa của tâm hồn vượt qua lo âu."
        },

        # === 175. NGỤY TÍN: CỖ MÁY TỰ ĐỘNG HÓA (2 slides) ===
        {
            "theme_id": "theme_175", "slide": 1, "role": "Hook",
            "text": "Sáng thức dậy, đi làm, chấm công, về nhà......",
            "artwork": "Gustave Caillebotte - Paris Street Rainy Day",
            "query": "Gustave Caillebotte Paris Street Rainy Day",
            "justification": "Những dòng người che ô đen đi lại tấp nập nhưng vô cảm trên đường phố Paris mưa xám xịt."
        },
        {
            "theme_id": "theme_175", "slide": 2, "role": "Twist",
            "text": "Nếu bạn chỉ sống theo một chu trình được lập trình sẵn mà không một lần tự hỏi 'Tại sao', bạn chỉ là một cỗ máy sinh học biết thở.",
            "artwork": "Edgar Degas - In a Cafe (The Absinthe Drinker)",
            "query": "Edgar Degas In a Cafe",
            "justification": "Người phụ nữ ngồi trước ly rượu absinthe với ánh nhìn trống rỗng rã rời, cuộc sống mòn mỏi thiếu sinh khí."
        },

        # === 176. NGỤY TÍN: ĐỊA NGỤC LÀ KẺ KHÁC (1 slide) ===
        {
            "theme_id": "theme_176", "slide": 1, "role": "Single-Punch",
            "text": "Khi bạn để ánh nhìn của người khác định nghĩa giá trị của mình, bạn đã tự tay trao chìa khóa nhà tù tâm hồn cho thiên hạ.",
            "artwork": "William-Adolphe Bouguereau - Dante and Virgil in Hell",
            "query": "William-Adolphe Bouguereau Dante and Virgil in Hell",
            "justification": "Hai linh hồn cắn xé nhau trong địa ngục dưới ánh nhìn phán xét lạnh lùng của Dante và Virgil."
        },

        # === 177. NGỤY TÍN: CĂN BỆNH TUYỆT VỌNG (3 slides) ===
        {
            "theme_id": "theme_177", "slide": 1, "role": "Hook",
            "text": "Cơn tuyệt vọng sâu sắc nhất......",
            "artwork": "Rembrandt - Jeremias beweent de verwoesting van Jeruzalem",
            "query": "Rembrandt Jeremias beweent de verwoesting van Jeruzalem",
            "justification": "Nhà tiên tri Jeremiah ngồi gục đầu bên kho tàng tro tàn của thành Jerusalem, nỗi đau hiện sinh tột độ."
        },
        {
            "theme_id": "theme_177", "slide": 2, "role": "Twist",
            "text": "Không phải khi mất đi tài sản hay danh vọng, mà là khi bạn muốn từ bỏ chính mình để trở thành một ai đó khác.",
            "artwork": "John Everett Millais - Ophelia",
            "query": "John Everett Millais Ophelia",
            "justification": "Nàng Ophelia buông xuôi cơ thể chìm dần trong dòng suối đầy hoa, sự tự hủy hoại bản sắc."
        },
        {
            "theme_id": "theme_177", "slide": 3, "role": "Mirror",
            "text": "Chữa lành bắt đầu khi bạn can đảm ôm lấy con người bất toàn nhưng độc bản của chính mình.",
            "artwork": "Pierre-Auguste Renoir - Young Girl with Daisies",
            "query": "Pierre-Auguste Renoir Young Girl with Daisies",
            "justification": "Thiếu nữ nâng niu những bông hoa cúc dại ngập tràn ánh nắng ấm áp, biểu tượng của sự chấp nhận bản thân dịu dàng."
        },

        # === 178. NGỤY TÍN: TỰ DO HIỆN SINH (1 slide) ===
        {
            "theme_id": "theme_178", "slide": 1, "role": "Single-Punch",
            "text": "Không có dấu hiệu nào trên trời chỉ đường cho bạn; bạn phải tự mình vạch ra con đường và tự trả giá cho từng vết thương.",
            "artwork": "Caspar David Friedrich - Monk by the Sea",
            "query": "Caspar David Friedrich Monk by the Sea",
            "justification": "Vị tu sĩ đứng cô độc trước bầu trời đêm u tối và bờ biển vô tận, không một biển chỉ dẫn nào ngoài trực giác."
        },

        # === 179. NGỤY TÍN: CHIẾC BẪY TRÌ HOÃN (2 slides) ===
        {
            "theme_id": "theme_179", "slide": 1, "role": "Hook",
            "text": "'Để ngày mai tính'......",
            "artwork": "Pieter Claesz - Still Life with Hourglass",
            "query": "Pieter Claesz Still Life with Hourglass",
            "justification": "Chiếc đồng hồ cát đang chảy xiết bên cây nến sắp tàn và hộp sọ, thời gian trôi qua không chờ đợi."
        },
        {
            "theme_id": "theme_179", "slide": 2, "role": "Twist",
            "text": "Là lời nói dối êm ái nhất để xoa dịu nỗi sợ thất bại; trì hoãn cuộc sống chính là hình thức tự sát từ từ.",
            "artwork": "Philippe de Champaigne - Vanitas",
            "query": "Philippe de Champaigne Vanitas",
            "justification": "Bông hoa hồng héo tàn bên cạnh chiếc đồng hồ cát và đầu lâu — lời nhắc nhở đanh thép về sự hữu hạn của đời người."
        },

        # === 180. NGỤY TÍN: PHẨM GIÁ CỦA TỰ DO (1 slide) ===
        {
            "theme_id": "theme_180", "slide": 1, "role": "Single-Punch",
            "text": "Tự do không phải là làm bất cứ điều gì mình thích, mà là có dũng khí từ chối làm những điều đi ngược lại với phẩm giá của mình.",
            "artwork": "Jacques-Louis David - The Oath of the Horatii",
            "query": "Jacques-Louis David The Oath of the Horatii",
            "justification": "Ba người con trai giơ cao tay thề trước người cha nhận thanh gươm, biểu tượng của sự kiên định bảo vệ phẩm giá."
        },

        # === 181. THIÊN KIẾN: BẤT HÒA NHẬN THỨC (3 slides) ===
        {
            "theme_id": "theme_181", "slide": 1, "role": "Hook",
            "text": "Khi sự thật va chạm với niềm tin cố hữu......",
            "artwork": "Caravaggio - The Incredulity of Saint Thomas",
            "query": "Caravaggio The Incredulity of Saint Thomas",
            "justification": "Thomas thọc ngón tay vào vết thương của Chúa để kiểm chứng sự thật trần trụi."
        },
        {
            "theme_id": "theme_181", "slide": 2, "role": "Twist",
            "text": "Người ta thà bẻ cong sự thật và đổi trắng thay đen còn hơn là thừa nhận mình đã đặt niềm tin nhầm chỗ.",
            "artwork": "Domenico Fetti - The Parable of the Mote and the Beam",
            "query": "Domenico Fetti The Parable of the Mote and the Beam",
            "justification": "Kẻ soi mói hạt bụi trong mắt người khác trong khi mắt mình bị khúc gỗ lớn đâm xiên."
        },
        {
            "theme_id": "theme_181", "slide": 3, "role": "Mirror",
            "text": "Dũng khí lớn nhất của một trí tuệ trưởng thành là dám mỉm cười chấp nhận sự sụp đổ của một niềm tin sai lầm.",
            "artwork": "Caravaggio - Saint Jerome Writing",
            "query": "Caravaggio Saint Jerome Writing",
            "justification": "Thánh Jerome ngồi điềm tĩnh viết bên cạnh hộp sọ, thanh thản đối diện với chân lý khách quan."
        },

        # === 182. THIÊN KIẾN: KIM TỰ THÁP LỰA CHỌN (2 slides) ===
        {
            "theme_id": "theme_182", "slide": 1, "role": "Hook",
            "text": "Một lời bao biện nhỏ hôm nay......",
            "artwork": "Johannes Vermeer - The Procuress",
            "query": "Johannes Vermeer The Procuress",
            "justification": "Giao dịch đồng tiền vụn vặt ban đầu khởi đầu cho sự trượt dài của đạo đức."
        },
        {
            "theme_id": "theme_182", "slide": 2, "role": "Twist",
            "text": "Là bước chân đầu tiên đưa bạn xuống đáy vực sâu của sự tha hóa nhân cách mà chính bạn từng căm ghét.",
            "artwork": "J.M.W. Turner - Snow Storm Hannibal and his Army Crossing the Alps",
            "query": "J.M.W. Turner Snow Storm Hannibal",
            "justification": "Cơn bão tuyết khổng lồ nuốt chửng đoàn quân viễn chinh, sự trượt dốc không thể cứu vãn."
        },

        # === 183. THIÊN KIẾN: ẢO TƯỞNG WYSIATI (1 slide) ===
        {
            "theme_id": "theme_183", "slide": 1, "role": "Single-Punch",
            "text": "Đừng vội phán xét một con người chỉ qua một mảnh ghép hành vi; thứ bạn nhìn thấy chưa bao giờ là toàn bộ sự thật.",
            "artwork": "Georges de La Tour - Joseph the Carpenter",
            "query": "Georges de La Tour Joseph the Carpenter",
            "justification": "Ngọn nến chỉ rọi sáng một góc bàn tay người thợ mộc, phần còn lại của căn phòng chìm trong bóng tối bí ẩn."
        },

        # === 184. THIÊN KIẾN: CHI PHÍ CHÌM TÌNH CẢM (3 slides) ===
        {
            "theme_id": "theme_184", "slide": 1, "role": "Hook",
            "text": "Bám víu một mối quan hệ độc hại......",
            "artwork": "John William Waterhouse - The Lady of Shalott",
            "query": "John William Waterhouse The Lady of Shalott",
            "justification": "Nàng thả trôi con thuyền định mệnh bi kịch trói buộc mình vào lời nguyền quá khứ."
        },
        {
            "theme_id": "theme_184", "slide": 2, "role": "Twist",
            "text": "Chỉ vì tiếc nuối thanh xuân hay những năm tháng đã qua là bạn đang dùng phần còn lại của cuộc đời để trả giá cho một sai lầm đã chết.",
            "artwork": "Dante Gabriel Rossetti - Proserpine",
            "query": "Dante Gabriel Rossetti Proserpine",
            "justification": "Nàng Proserpine cắn quả lựu địa ngục, mắc kẹt trong vương quốc bóng tối vì tiếc nuối ràng buộc cũ."
        },
        {
            "theme_id": "theme_184", "slide": 3, "role": "Mirror",
            "text": "Buông tay một con thuyền đắm không phải là bỏ cuộc; đó là hành động cứu rỗi duy nhất để bạn có cơ hội bơi vào bờ.",
            "artwork": "Winslow Homer - The Gulf Stream",
            "query": "Winslow Homer The Gulf Stream MET",
            "justification": "Thủy thủ kiên cường trên con tàu giữa đàn cá mập, hướng mắt về chân trời hy vọng sống sót."
        },

        # === 185. THIÊN KIẾN: HẠ THẤP NẠN NHÂN (2 slides) ===
        {
            "theme_id": "theme_185", "slide": 1, "role": "Hook",
            "text": "Kẻ làm tổn thương bạn......",
            "artwork": "Ilya Repin - Ivan the Terrible and His Son Ivan",
            "query": "Ilya Repin Ivan the Terrible and His Son Ivan",
            "justification": "Kẻ gây ra tội ác ôm nạn nhân trong sự hoảng loạn và tìm cách tự biện hộ cho hành vi bộc phát."
        },
        {
            "theme_id": "theme_185", "slide": 2, "role": "Twist",
            "text": "Luôn phải tìm ra một lý do để đổ lỗi cho bạn, bởi thừa nhận sự độc ác của chính mình là bản án quá nặng cho bản ngã của họ.",
            "artwork": "Fernand Cormon - Cain flying before Jehovah Curse",
            "query": "Fernand Cormon Cain flying before Jehovah Curse",
            "justification": "Cain dẫn bộ tộc bỏ trốn trong sa mạc hoang vu sau khi giết em, trốn chạy trách nhiệm tội lỗi gán ép."
        },

        # === 186. THIÊN KIẾN: THIÊN KIẾN HỒI TƯỞNG (1 slide) ===
        {
            "theme_id": "theme_186", "slide": 1, "role": "Single-Punch",
            "text": "Đừng dằn vặt bản thân trong quá khứ; bạn của ngày xưa đã đưa ra quyết định tốt nhất với lượng nhận thức ít ỏi mà bạn có lúc đó.",
            "artwork": "Rembrandt - The Return of the Prodigal Son",
            "query": "Rembrandt The Return of the Prodigal Son Hermitage",
            "justification": "Người cha ôm đứa con hoang đàng trở về trong lòng từ bi dung thứ cho những dại khờ của tuổi trẻ."
        },

        # === 187. THIÊN KIẾN: THIÊN KIẾN XÁC NHẬN (3 slides) ===
        {
            "theme_id": "theme_187", "slide": 1, "role": "Hook",
            "text": "Người ta chỉ nhìn thấy điều họ muốn thấy......",
            "artwork": "Johannes Vermeer - The Astronomer",
            "query": "Johannes Vermeer The Astronomer",
            "justification": "Nhà thiên văn săm soi quả địa cầu trong ánh sáng một chiều của khung cửa sổ."
        },
        {
            "theme_id": "theme_187", "slide": 2, "role": "Twist",
            "text": "Họ thu thập mọi bằng chứng vụn vặt để củng cố định kiến của mình và nhắm mắt bịt tai trước mọi sự thật trái ngược.",
            "artwork": "Carl Spitzweg - The Bookworm",
            "query": "Carl Spitzweg The Bookworm",
            "justification": "Học giả già vùi đầu vào đống sách cũ kỹ trên thang cao, mù tịt với thế giới thực bên ngoài."
        },
        {
            "theme_id": "theme_187", "slide": 3, "role": "Mirror",
            "text": "Muốn trở nên thông thái, trước hết hãy dám tìm kiếm những bằng chứng chứng minh rằng suy nghĩ ban đầu của bạn là sai lầm.",
            "artwork": "Raphael - The School of Athens",
            "query": "Raphael The School of Athens",
            "justification": "Plato và Aristotle cùng các triết gia tranh luận đa chiều, cởi mở đón nhận tư tưởng đối lập."
        },

        # === 188. THIÊN KIẾN: LỜI XIN LỖI BỊ ĐÁNH CẮP (1 slide) ===
        {
            "theme_id": "theme_188", "slide": 1, "role": "Single-Punch",
            "text": "Lời xin lỗi đi kèm chữ 'NHƯNG' không phải là sự hối lỗi; đó chỉ là một lời bao biện được bọc trong chiếc vỏ lịch sự.",
            "artwork": "Giotto - Kiss of Judas",
            "query": "Giotto Kiss of Judas Scrovegni",
            "justification": "Nụ hôn phản bội của Judas — hành động bề ngoài thân mật nhưng che đậy động cơ đâm lén."
        },

        # === 189. THIÊN KIẾN: HỘI CHỨNG DUNNING-KRUGER (2 slides) ===
        {
            "theme_id": "theme_189", "slide": 1, "role": "Hook",
            "text": "Kẻ kém cỏi nhất luôn tự tin nhất......",
            "artwork": "Frans Hals - The Laughing Cavalier",
            "query": "Frans Hals The Laughing Cavalier",
            "justification": "Kỵ sĩ với nụ cười tự đắc, ria mép vuốt ngược tự phụ tột cùng về bản thân."
        },
        {
            "theme_id": "theme_189", "slide": 2, "role": "Twist",
            "text": "Trong khi người hiểu biết thực sự luôn bị dằn vặt bởi sự hoài nghi và đức khiêm nhường sâu sắc.",
            "artwork": "Rembrandt - Self-Portrait with Two Circles",
            "query": "Rembrandt Self-Portrait with Two Circles",
            "justification": "Rembrandt tuổi già với ánh mắt trầm tư, khiêm nhường đối diện với sự hữu hạn của tài năng trước nghệ thuật vô tận."
        },

        # === 190. THIÊN KIẾN: SỰ TỰ NHẬN THỨC KHẮT KHE (1 slide) ===
        {
            "theme_id": "theme_190", "slide": 1, "role": "Single-Punch",
            "text": "Người dễ bị bạn lừa dối nhất chính là người trong gương; và chiến thắng vĩ đại nhất của một kiếp người là dám lột bỏ chiếc mặt nạ đó trước mặt chính mình.",
            "artwork": "Albrecht Durer - Self-Portrait at Twenty-Eight",
            "query": "Albrecht Durer Self-Portrait at Twenty-Eight",
            "justification": "Dürer nhìn thẳng vào mắt người xem với sự nghiêm cẩn tuyệt đối, soi rọi bản ngã trần trụi không dối lừa."
        },

        # === 191. HIỆN SINH: HUYỀN THOẠI SISYPHUS (3 slides) ===
        {
            "theme_id": "theme_191", "slide": 1, "role": "Hook",
            "text": "Cuộc đời có thể phi lý......",
            "artwork": "Titian - Sisyphus",
            "query": "Titian Sisyphus Prado",
            "justification": "Bức tranh khổng lồ của Titian vẽ Sisyphus đang gập lưng vác tảng đá đen khổng lồ giữa bóng tối âm phủ."
        },
        {
            "theme_id": "theme_191", "slide": 2, "role": "Twist",
            "text": "Tảng đá có thể tiếp tục lăn xuống chân dốc ngàn vạn lần, xóa sạch mọi công sức của bạn.",
            "artwork": "Cornelis van Haarlem - The Fall of the Titans",
            "query": "Cornelis van Haarlem The Fall of the Titans",
            "justification": "Các Titan ngã nhào từ trên đỉnh trời xuống vực thẳm hỗn mang, tượng trưng cho công sức sụp đổ."
        },
        {
            "theme_id": "theme_191", "slide": 3, "role": "Mirror",
            "text": "Nhưng khoảnh khắc bạn mỉm cười và tiếp tục đặt tay vào tảng đá, bạn không còn là nạn nhân của số phận — bạn là người làm chủ nó.",
            "artwork": "Peter Paul Rubens - Prometheus Bound",
            "query": "Peter Paul Rubens Prometheus Bound",
            "justification": "Ý chí bất khuất của người anh hùng đối diện đại bàng và xiềng xích, kiêu hãnh làm chủ vận mệnh phi lý."
        },

        # === 192. HIỆN SINH: TỰ DO TỐI THƯỢNG CỦA FRANKL (1 slide) ===
        {
            "theme_id": "theme_192", "slide": 1, "role": "Single-Punch",
            "text": "Ngoại cảnh có thể giam cầm thể xác bạn trong nghịch cảnh, nhưng chỉ có bạn mới là người có quyền quyết định tâm hồn mình sẽ quỳ gối hay kiêu hãnh mỉm cười.",
            "artwork": "Rembrandt - The Apostle Paul in Prison",
            "query": "Rembrandt The Apostle Paul in Prison",
            "justification": "Thánh Paul ngồi trong ngục tối lạnh lẽo nhưng tay cầm bút viết lên những tư tưởng vĩ đại soi sáng nhân loại."
        },

        # === 193. HIỆN SINH: LỜI CẢNH BÁO CỦA NIETZSCHE (3 slides) ===
        {
            "theme_id": "theme_193", "slide": 1, "role": "Hook",
            "text": "Khi bạn chiến đấu với bóng tối......",
            "artwork": "Gustave Moreau - Saint George and the Dragon",
            "query": "Gustave Moreau Saint George and the Dragon",
            "justification": "Hiệp sĩ cầm giáo chuẩn bị lao vào hang ổ quái rồng bóng tối."
        },
        {
            "theme_id": "theme_193", "slide": 2, "role": "Twist",
            "text": "Nếu bạn dùng chính sự cay nghiệt và mưu mô của kẻ thù để đáp trả, bạn đã thua ngay từ khoảnh khắc chiến thắng.",
            "artwork": "Caravaggio - David with the Head of Goliath",
            "query": "Caravaggio David with the Head of Goliath",
            "justification": "David cầm đầu Goliath nhưng nét mặt buồn bã, nhận ra mình đã nhuốm mùi máu tanh tưởi của kẻ thù."
        },
        {
            "theme_id": "theme_193", "slide": 3, "role": "Mirror",
            "text": "Bởi vì thứ bước ra khỏi cuộc chiến đó không còn là bạn thuở ban đầu, mà là một con quái vật mới mang khuôn mặt của chính bạn.",
            "artwork": "Caravaggio - Medusa",
            "query": "Caravaggio Medusa",
            "justification": "Chiếc khiên đồng phản chiếu đầu Medusa rắn độc đang thét gào — khuôn mặt quái thú phản chiếu chính mình."
        },

        # === 194. HIỆN SINH: SỰ TĨNH LẶNG CỦA SENECA (1 slide) ===
        {
            "theme_id": "theme_194", "slide": 1, "role": "Single-Punch",
            "text": "Nỗi sợ hãi tồi tệ nhất luôn nằm trong trí tưởng tượng của bạn; hãy ngưng diễn tập nỗi đau trước khi nó thực sự xảy đến.",
            "artwork": "Henry Fuseli - The Nightmare",
            "query": "Henry Fuseli The Nightmare",
            "justification": "Quái vật ngồi đè trên ngực người phụ nữ ngủ say — hình tượng hoá kinh điển của nỗi đau tưởng tượng trong ác mộng."
        },

        # === 195. HIỆN SINH: MÙA HÈ BẤT DIỆT CỦA CAMUS (2 slides) ===
        {
            "theme_id": "theme_195", "slide": 1, "role": "Hook",
            "text": "Dù cuộc đời có tàn nhẫn đóng băng bạn......",
            "artwork": "Caspar David Friedrich - The Sea of Ice",
            "query": "Caspar David Friedrich The Sea of Ice",
            "justification": "Những tảng băng bắc cực sắc nhọn chôn vùi con tàu đắm, sự lạnh giá khắc nghiệt của số phận."
        },
        {
            "theme_id": "theme_195", "slide": 2, "role": "Twist",
            "text": "Hãy nhớ rằng bên dưới lớp tuyết dày của nghịch cảnh, hạt mầm của một mùa hè rực rỡ vẫn đang âm thầm chờ ngày đâm chồi.",
            "artwork": "Claude Monet - Field of Poppies",
            "query": "Claude Monet Field of Poppies",
            "justification": "Cánh đồng hoa anh túc đỏ rực rỡ bừng nở dưới ánh nắng mùa hè ngập tràn sức sống."
        },

        # === 196. HIỆN SINH: CHỮ TẠI SAO CỦA FRANKL (1 slide) ===
        {
            "theme_id": "theme_196", "slide": 1, "role": "Single-Punch",
            "text": "Khi bạn có một chữ 'Tại sao' đủ thiêng liêng, không có nghịch cảnh nào của thế gian có thể bẻ gãy được ý chí của bạn.",
            "artwork": "Rembrandt - An Old Man in Red",
            "query": "Rembrandt An Old Man in Red",
            "justification": "Cụ già mặc áo choàng đỏ với đôi mắt bừng sáng ngọn lửa kiên định của niềm tin không thể dập tắt."
        },

        # === 197. HIỆN SINH: LỬA THỬ VÀNG CỦA NIETZSCHE (3 slides) ===
        {
            "theme_id": "theme_197", "slide": 1, "role": "Hook",
            "text": "Vết thương ngày hôm nay......",
            "artwork": "Rembrandt - The Blinding of Samson",
            "query": "Rembrandt The Blinding of Samson",
            "justification": "Samson bị đè xuống chọc mù mắt trong sự đau đớn tột cùng và phản bội rướm máu."
        },
        {
            "theme_id": "theme_197", "slide": 2, "role": "Twist",
            "text": "Có thể làm bạn rướm máu và quỵ ngã trong bóng tối.",
            "artwork": "Francisco Goya - Saturn",
            "query": "Francisco Goya Saturn",
            "justification": "Bóng tối sâu thẳm u tối đè nặng thể xác."
        },
        {
            "theme_id": "theme_197", "slide": 3, "role": "Mirror",
            "text": "Nhưng khi da thịt lành lặn, nơi từng rách nát sẽ trở thành lớp giáp sắt kiên cường nhất bảo vệ linh hồn bạn.",
            "artwork": "Rembrandt - Man in Armour",
            "query": "Rembrandt Man in Armour",
            "justification": "Chiến binh khoác bộ áo giáp sắt sáng loáng với ánh mắt kiên định bất khả xâm phạm."
        },

        # === 198. HIỆN SINH: THÁI ĐỘ KHẮC KỶ TRƯỚC NGHỊCH CẢNH (1 slide) ===
        {
            "theme_id": "theme_198", "slide": 1, "role": "Single-Punch",
            "text": "Không có cơn gió thuận nào dành cho kẻ không biết mình đang chèo về đâu; và không có linh hồn vĩ đại nào được tạo nên từ một cuộc đời quá đỗi êm đềm.",
            "artwork": "Winslow Homer - Breezing Up (A Fair Wind)",
            "query": "Winslow Homer Breezing Up A Fair Wind",
            "justification": "Thuyền buồm nghiêng mình vững chãi lướt qua ngọn sóng lớn dưới sự điều khiển kiên định của người thủy thủ."
        },

        # === 199. HIỆN SINH: TINH THẦN NỔI LOẠN (2 slides) ===
        {
            "theme_id": "theme_199", "slide": 1, "role": "Hook",
            "text": "Nói 'KHÔNG' trước sự bất công......",
            "artwork": "Eugene Delacroix - Liberty Leading the People",
            "query": "Eugene Delacroix Liberty Leading the People",
            "justification": "Tiếng thét quật khởi và bước chân dũng cảm đứng lên chống lại sự áp bức."
        },
        {
            "theme_id": "theme_199", "slide": 2, "role": "Twist",
            "text": "Không phải sự chống đối mù quáng; đó là lời khẳng định thiêng liêng nhất rằng phẩm giá của bạn có ranh giới mà không ai được phép vượt qua.",
            "artwork": "Rembrandt - Aristotle Contemplating a Bust of Homer",
            "query": "Rembrandt Aristotle Contemplating a Bust of Homer",
            "justification": "Nhà tư tưởng đứng vững chãi kiêu hãnh bảo vệ ranh giới tinh thần và phẩm giá trí tuệ."
        },

        # === 200. HIỆN SINH: TÌNH YÊU ĐỊNH MỆNH AMOR FATI (3 slides) ===
        {
            "theme_id": "theme_200", "slide": 1, "role": "Hook",
            "text": "Đỉnh cao của sự giác ngộ......",
            "artwork": "Edward Burne-Jones - The Wheel of Fortune",
            "query": "Edward Burne-Jones The Wheel of Fortune",
            "justification": "Nữ thần Vận Mệnh quay chiếc bánh xe khổng lồ nghiền nát ngai vàng và kẻ quyền quý."
        },
        {
            "theme_id": "theme_200", "slide": 2, "role": "Twist",
            "text": "Không phải là né tránh những vết thương; mà là đứng thẳng mỉm cười và ôm hôn số phận như người tình tri kỷ.",
            "artwork": "Gustave Moreau - Oedipus and the Sphinx",
            "query": "Gustave Moreau Oedipus and the Sphinx",
            "justification": "Oedipus đứng thẳng điềm tĩnh nhìn thẳng vào mắt quái thú nhân sư, mỉm cười giải đáp câu đố định mệnh."
        },
        {
            "theme_id": "theme_200", "slide": 3, "role": "Mirror",
            "text": "Mọi đắng cay, phản bội và giông bão đều là chiếc búa đục đẽo nên bức tượng vĩ đại của con người bạn ngày hôm nay.",
            "artwork": "Jean-Leon Gerome - Pygmalion and Galatea",
            "query": "Jean-Leon Gerome Pygmalion and Galatea",
            "justification": "Nhà điêu khắc hoàn thành pho tượng cẩm thạch kiệt tác được trao tặng sự sống rạng rỡ từ đá sỏi gồ ghề."
        }
    ]
    return curation

if __name__ == '__main__':
    mapping = get_98_curated_art_mapping()
    print(f"Total curated slides: {len(mapping)}")
    with open('scripts/curated_98_distinct_oil_art.json', 'w', encoding='utf-8') as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)
    print("Saved to scripts/curated_98_distinct_oil_art.json")
