#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss — Build Healing Oil Painting Suites Spec & Manifest (Theme 251 - 300)
Tạo tài liệu đặc tả mỹ thuật HYA-08 docs/11_HIYU_ABYSS_HEALING_OIL_SUITES_251_300_SPEC.md
và tệp manifest JSON scripts/oil_suites_251_300_manifest.json (đúng 103 slides độc lập).
"""

import json
import os
import re

POSTS_PATH = "scripts/posts_251_300.json"
SPEC_PATH = "docs/11_HIYU_ABYSS_HEALING_OIL_SUITES_251_300_SPEC.md"
MANIFEST_PATH = "scripts/oil_suites_251_300_manifest.json"

BASE_MEDIUM = "Vertical 9:16 classical fine art oil painting, authentic visible heavy impasto brushstrokes, tactile oil canvas weave texture"
BASE_SAFE_ZONE = "Atmospheric fine art composition with quiet, generous negative space in the middle-to-lower third for elegant editorial reading, strictly clean with NO text, NO lettering, NO watermarks, NO digital CGI rendering, traditional museum oil on canvas"

# Bảng phân bổ 103 tác phẩm hội họa cổ điển bảo tàng tương ứng chính xác theo format của từng bài
SLIDE_ART_MAPPINGS = {
    # 251: Carousel 3 trang (3 slides)
    251: [
        {
            "artist": "Caspar David Friedrich",
            "artwork": "Woman at a Window",
            "metaphor": "Một bóng người đứng lặng lẽ bên khung cửa sổ cổ kính mờ sương trong sớm đông, ánh sáng lạnh lẽo bao trùm sự dằn vặt nội tâm",
            "lighting": "Subtle winter morning chiaroscuro, cool misty greys and muted blues"
        },
        {
            "artist": "Claude Monet",
            "artwork": "Morning on the Seine, Clear Weather",
            "metaphor": "Dòng sông êm đềm buổi sớm mai, những tia nắng vàng ấm áp đầu tiên bắt đầu xuyên qua làn sương mù mỏng xua tan lạnh lẽo",
            "lighting": "Luminous pale amber morning sunbeams breaking through mist, soft pastel reflections on water"
        },
        {
            "artist": "Pierre-Auguste Renoir",
            "artwork": "Woman with a Parasol in a Garden",
            "metaphor": "Một khu vườn tràn ngập ánh nắng vàng mật ong, muôn hoa cúc dại và mẫu đơn nở rộ, bầu không khí bao dung và bình yên tuyệt đối",
            "lighting": "Vibrant warm golden sunlight, lush emerald greens, soft rosy pinks and honey ochres"
        }
    ],
    # 252: Carousel 2 trang (2 slides)
    252: [
        {
            "artist": "Vilhelm Hammershøi",
            "artwork": "Interior with a Woman Reading",
            "metaphor": "Một căn phòng cổ điển yên tĩnh với ánh nắng thanh nhẹ rọi qua cửa kính, người phụ nữ lặng lẽ tháo bỏ chiếc áo khoác nặng nề",
            "lighting": "Contemplative northern morning light, pearl grey, warm cream and soft wood tones"
        },
        {
            "artist": "John Singer Sargent",
            "artwork": "Carnation, Lily, Lily, Rose",
            "metaphor": "Khu vườn chạng vạng ấm áp thắp sáng bởi những chiếc đèn lồng giấy huyền ảo, hoa loa kèn trắng nở rộ biểu trưng cho sự gắn kết chân thành",
            "lighting": "Magical twilight glow, warm amber lantern illumination, deep lilac and rose hues"
        }
    ],
    # 253: Single-Punch (1 trang / 1 slide)
    253: [
        {
            "artist": "Claude Monet",
            "artwork": "Water Lilies (The Clouds)",
            "metaphor": "Mặt hồ sen tĩnh lặng phản chiếu mây trời xanh ngắt, biểu tượng của sự chấp nhận bản thân trọn vẹn để mở ra cánh cửa chuyển hóa kỳ diệu",
            "lighting": "Tranquil shimmering azure water, soft ivory blossoms, golden celestial cloud reflections"
        }
    ],
    # 254: Carousel 3 trang (3 slides)
    254: [
        {
            "artist": "Camille Pissarro",
            "artwork": "The Garden of the Tuileries on a Winter Morning",
            "metaphor": "Khu vườn mùa đông trong sương sớm, một người bước đi chậm rãi trên con đường sỏi mờ sương, học cách quan sát đám mây tiêu cực trôi qua",
            "lighting": "Soft silvery winter daylight, pale ochre, muted lavender and gentle pearl tones"
        },
        {
            "artist": "Claude Monet",
            "artwork": "Path through the Corn at Pourville",
            "metaphor": "Con đường mòn rực rỡ uốn lượn qua đồng cỏ hoa ven bờ biển xanh thẳm ngập tràn ánh nắng trưa mùa hạ, không đồng nhất mình với cơn giông",
            "lighting": "Brilliant coastal sunshine, turquoise sea, golden wheat and cobalt skies"
        },
        {
            "artist": "Jean-Baptiste-Camille Corot",
            "artwork": "Souvenir de Mortefontaine",
            "metaphor": "Cây sồi cổ thụ nghiêng mình bên mặt hồ phẳng lặng, người mẹ hiền từ hái hoa dại cho đứa con nhỏ trong bình minh êm dịu, thực hành 4 bước RAIN chữa lành",
            "lighting": "Dreamy silvery morning mist, soft olive greens, gentle diffuse sunlight"
        }
    ],
    # 255: Carousel 2 trang (2 slides)
    255: [
        {
            "artist": "Berthe Morisot",
            "artwork": "The Cradle",
            "metaphor": "Người mẹ ngồi lặng lẽ bên chiếc nôi trắng tinh khôi, ánh mắt yêu thương vô bờ bến ôm lấy đứa trẻ từng chịu tổn thương",
            "lighting": "Soft filtered interior window light, delicate white drapery, warm ochre and rosy tones"
        },
        {
            "artist": "Mary Cassatt",
            "artwork": "Mother and Child",
            "metaphor": "Cái ôm ấm áp, dịu dàng vô điều kiện trong một căn phòng mộc mạc ngập tràn ánh sáng ban mai xua tan mọi nỗi sợ bị bỏ rơi",
            "lighting": "Gentle morning sunbeams, soft blush pinks, tender cream and warm linen textures"
        }
    ],
    # 256: Single-Punch (1 trang / 1 slide)
    256: [
        {
            "artist": "Caspar David Friedrich",
            "artwork": "The Morning Star",
            "metaphor": "Một người lữ khách đứng giữa cánh đồng hoang sơ ngắm nhìn ngôi sao mai rạng ngời nơi chân trời hừng đông, đón nhận sự bất toàn với lòng kiêu hãnh",
            "lighting": "Ethereal pre-dawn twilight transitioning into soft amber horizon, deep navy blues"
        }
    ],
    # 257: Carousel 2 trang (2 slides)
    257: [
        {
            "artist": "Thomas Cole",
            "artwork": "The Arcadian State",
            "metaphor": "Cảnh tượng thanh bình bên bờ suối rừng nguyên sinh, khói lam chiều bảng lảng bay lên từ mái nhà gỗ mộc mạc, lời nhắc nhở nghỉ ngơi",
            "lighting": "Warm late afternoon golden haze, tranquil cerulean water, rich moss greens"
        },
        {
            "artist": "Asher Brown Durand",
            "artwork": "Kindred Spirits",
            "metaphor": "Hai người bạn đồng hành đứng trên mỏm đá ngắm nhìn thung lũng hùng vĩ và thác nước tuôn chảy mát lành trong sự tĩnh tại",
            "lighting": "Crisp mountain morning illumination, golden yellow foliage, expansive blue vista"
        }
    ],
    # 258: Carousel 3 trang (3 slides)
    258: [
        {
            "artist": "Carl Larsson",
            "artwork": "Breakfast Under the Big Birch",
            "metaphor": "Bàn trà nhỏ dưới bóng cây bạch dương xanh mát bên hồ, nơi con người học cách dừng lại tháo bỏ chiếc khiên cầu toàn nặng nề",
            "lighting": "Playful dappled sunlight filtering through green leaves, fresh morning air, pristine white tablecloth"
        },
        {
            "artist": "Joaquín Sorolla",
            "artwork": "Sunlight in the Garden",
            "metaphor": "Vườn cam Seville ngập tràn ánh nắng vàng rực rỡ, vòi phun nước mát lành phun lên những bọt nước lấp lánh như ngọc trai",
            "lighting": "Radiant Mediterranean sun, terracotta tiles, glowing orange fruits, sparkling water splashes"
        },
        {
            "artist": "Claude Monet",
            "artwork": "The Water-Lily Pond",
            "metaphor": "Cây cầu gỗ Nhật Bản bắc qua hồ sen nở rộ, mặt nước phẳng lặng chứa chan sự bao dung với những vết nứt bất toàn",
            "lighting": "Gentle diffused summer daylight, harmonious greens, weeping willow fronds and pink blossoms"
        }
    ],
    # 259: Single-Punch (1 trang / 1 slide)
    259: [
        {
            "artist": "John Frederick Kensett",
            "artwork": "Lake George",
            "metaphor": "Mặt hồ tĩnh lặng tuyệt đối như một tấm gương khổng lồ soi bóng núi non trùng điệp dưới bầu trời xanh ngắt, giá trị tự thân bất biến",
            "lighting": "Pure crystal morning clarity, serene pastel reflections, untouched stillness"
        }
    ],
    # 260: Carousel 2 trang (2 slides)
    260: [
        {
            "artist": "Sanford Robinson Gifford",
            "artwork": "A Gorge in the Mountains",
            "metaphor": "Hẻm núi đá sâu thẳm nơi dòng suối róc rách chảy qua, từng bước chân chậm rãi trên phiến đá rêu phong, không ghen tị với đỉnh cao",
            "lighting": "Subtle crepuscular rays piercing deep forest canopy, earthy sienna and lichen green"
        },
        {
            "artist": "Jean-Baptiste-Camille Corot",
            "artwork": "A Morning, Dance of the Nymphs",
            "metaphor": "Bình minh dịu dàng trên đồng cỏ ven rừng, những sinh linh tự do nhảy múa trong sự thảnh thơi không vướng bận đích đến",
            "lighting": "Luminous silver-rose sunrise, soft airy foliage, gossamer atmospheric mist"
        }
    ],
    # 261: Carousel 3 trang (3 slides)
    261: [
        {
            "artist": "Camille Pissarro",
            "artwork": "Landscape at Valhermeil",
            "metaphor": "Đồi cỏ xanh mướt với những bụi cây dại nở hoa tím mọc chen chúc giữa những tảng đá mộc mạc, hạt mầm kiên nhẫn trong lòng đất",
            "lighting": "Crisp morning breeze, vibrant spring greens, soft yellow morning glow"
        },
        {
            "artist": "Pierre-Auguste Renoir",
            "artwork": "Springtime Landscape",
            "metaphor": "Thảm cỏ xanh non trải dài tới chân trời, nơi những bông hoa anh túc đỏ thắm mọc lên kiêu hãnh theo đúng thời điểm của tự nhiên",
            "lighting": "Warm cheerful noon sun, brilliant scarlet accents, expansive azure sky"
        },
        {
            "artist": "Claude Monet",
            "artwork": "Field of Poppies near Giverny",
            "metaphor": "Cánh đồng hoa anh túc bạt ngàn đón làn gió thoảng nhẹ, biểu tượng cho việc kiên nhẫn với hành trình chữa lành của chính mình",
            "lighting": "Radiant golden hour backlight, waving grasses, joyful summer luminescence"
        }
    ],
    # 262: Single-Punch (1 trang / 1 slide)
    262: [
        {
            "artist": "Albert Bierstadt",
            "artwork": "Sunlight and Shadow",
            "metaphor": "Khoảng sân nhà thờ cổ kính rợp bóng mát, nơi ánh nắng và bóng râm hòa quyện tạo nên vẻ đẹp sâu sắc của một trái tim biết rung cảm",
            "lighting": "Contrasting yet harmonious golden afternoon sun and cool stone shadows"
        }
    ],
    # 263: Carousel 2 trang (2 slides)
    263: [
        {
            "artist": "Henri Le Sidaner",
            "artwork": "The Table by the Window",
            "metaphor": "Bàn trà nhỏ bên ô cửa sổ nhìn ra khu vườn chiều tĩnh lặng, sự điềm tĩnh và tin tưởng vào năng lực tự thân",
            "lighting": "Intimate twilight atmosphere, warm interior candlelight contrasting cool dusk outside"
        },
        {
            "artist": "Pierre-Auguste Renoir",
            "artwork": "The Reader (La Liseuse)",
            "metaphor": "Người phụ nữ ngồi đọc sách bên khung cửa sổ ngập nắng vàng, ánh sáng nội tại thắp lên niềm tin vững chắc",
            "lighting": "Luminous facial glow, warm golden hair highlights, quiet contemplative setting"
        }
    ],
    # 264: Carousel 3 trang (3 slides)
    264: [
        {
            "artist": "Caspar David Friedrich",
            "artwork": "Wanderer above the Sea of Fog",
            "metaphor": "Người lữ khách đứng uy nghi trên đỉnh núi đá cao, nhìn xuống biển mây cuồn cuộn dưới chân với sự bình thản tuyệt đối",
            "lighting": "Crisp morning sunrise rays illuminating mountain crags, expansive misty horizon"
        },
        {
            "artist": "Thomas Cole",
            "artwork": "Morning over the Kaaterskill Clove",
            "metaphor": "Thung lũng núi hoang sơ đón ánh mặt trời đầu ngày, buông bỏ những thứ nằm ngoài vòng tay kiểm soát",
            "lighting": "Warm fiery orange dawn cresting granite peaks, deep purple valley shadows"
        },
        {
            "artist": "Claude Monet",
            "artwork": "Cliffs at Pourville in the Fog",
            "metaphor": "Vách đá sừng sững bên bờ biển lớn, những đợt sóng bạc đầu xô vào rồi tan biến, biểu tượng của sự tự do nội tâm",
            "lighting": "Ethereal maritime luminescence, soft pearl mist, sturdy ochre cliffs"
        }
    ],
    # 265: Carousel 2 trang (2 slides)
    265: [
        {
            "artist": "J.M.W. Turner",
            "artwork": "Sun Rising through Vapour",
            "metaphor": "Mặt trời đỏ rực từ từ nhô lên xua tan sương mù dày đặc trên mặt biển, nhận định sáng tỏ rằng sự kiện bên ngoài không thể làm đau tâm trí",
            "lighting": "Luminous circular solar core, pearlescent vapour, golden sea reflections"
        },
        {
            "artist": "Caspar David Friedrich",
            "artwork": "The Solitary Tree",
            "metaphor": "Cây sồi cô đơn đứng sừng sững giữa cánh đồng cỏ rộng lớn, cành lá vươn cao bình thản trước gió giông",
            "lighting": "Calm pastoral afternoon light, blue mountainous backdrop, resolute organic strength"
        }
    ],
    # 266: Single-Punch (1 trang / 1 slide)
    266: [
        {
            "artist": "George Inness",
            "artwork": "The Home of the Heron",
            "metaphor": "Khu rừng thông ngập ánh nắng chiều tà u tịch, chú chim diệc đứng tĩnh tại không bị quấy rầy bởi những điều tưởng tượng huyễn hoặc",
            "lighting": "Warm monochromatic amber haze, mysterious deep greens, meditative quietude"
        }
    ],
    # 267: Carousel 3 trang (3 slides)
    267: [
        {
            "artist": "J.M.W. Turner",
            "artwork": "The Fighting Temeraire",
            "metaphor": "Con tàu kiêu hãnh xuôi dòng trên mặt nước dát vàng dưới ánh hoàng hôn rực lửa, đón nhận sự đổi thay của thời cuộc với lòng tôn nghiêm",
            "lighting": "Magnificent blazing golden sunset, glowing vermilion and cadmium skies, reflective water"
        },
        {
            "artist": "Frederic Edwin Church",
            "artwork": "Twilight in the Wilderness",
            "metaphor": "Bầu trời hoàng hôn rực lửa soi bóng xuống mặt hồ hoang sơ, yêu tha thiết cả nghịch cảnh định mệnh trao tặng",
            "lighting": "Blazing crimson and golden amber horizon, tranquil glass-like wilderness lake"
        },
        {
            "artist": "Claude Monet",
            "artwork": "Haystacks, Sunset",
            "metaphor": "Đụn rơm vàng óng ả trên cánh đồng sau mùa gặt dưới bầu trời hoàng hôn rực rỡ, ngọn lửa lớn biến mọi trở ngại thành nhiên liệu",
            "lighting": "Enchanting twilight glow, violet-pink skies, warm copper and amber straw textures"
        }
    ],
    # 268: Carousel 2 trang (2 slides)
    268: [
        {
            "artist": "John Singer Sargent",
            "artwork": "The Fountain, Villa Torlonia",
            "metaphor": "Bức tường đá cổ kính với giàn dây leo xanh mướt, nơi chướng ngại trên con đường trở thành chính con đường đi",
            "lighting": "Dazzling Mediterranean sunlight, cool shaded balustrade, sparkling water drops"
        },
        {
            "artist": "Thomas Cole",
            "artwork": "Home in the Woods",
            "metaphor": "Ngôi nhà gỗ ấm cúng bên bìa rừng nguyên sinh, làn khói bếp bảng lảng bay lên hòa vào ráng chiều, biến thách thức thành sức bật",
            "lighting": "Warm rustic hearth glow, peaceful sunset reflections on forest pond"
        }
    ],
    # 269: Single-Punch (1 trang / 1 slide)
    269: [
        {
            "artist": "Caspar David Friedrich",
            "artwork": "Giant Mountains",
            "metaphor": "Dãy núi sừng sững cao vút chạm tới những tầng mây trắng, giữ nguyên phẩm giá thanh khiết của viên ngọc bích trước miệng đời",
            "lighting": "Crisp alpine morning daylight, pale cyan skies, rugged weathered stone"
        }
    ],
    # 270: Carousel 3 trang (3 slides)
    270: [
        {
            "artist": "Vilhelm Hammershøi",
            "artwork": "Sunshine in the Drawing Room",
            "metaphor": "Tia nắng rọi xiên qua ô cửa sổ cổ điển chiếu lên sàn gỗ, nhận thức sâu sắc về sự hữu hạn quý giá của từng hơi thở",
            "lighting": "Geometric dust-mote sunbeams cutting through serene airy room, warm amber wood"
        },
        {
            "artist": "Carl Larsson",
            "artwork": "Flowers on the Windowsill",
            "metaphor": "Những chậu hoa nở rộ bên khung cửa sổ tràn ngập ánh sáng, buông bỏ việc lãng phí thời gian vào những vụn vặt giận hờn",
            "lighting": "Bright cheerful morning daylight, vivid red blossoms, pristine Nordic domestic bliss"
        },
        {
            "artist": "Albert Bierstadt",
            "artwork": "Looking Down Yosemite Valley",
            "metaphor": "Thung lũng Yosemite hùng vĩ ngập tràn ánh nắng trưa rực rỡ, sống trọn vẹn từng ngày như thể đó là kiệt tác cuối cùng",
            "lighting": "Majestic golden atmosphere, soaring granite cliffs, crystal clear mountain air"
        }
    ],
    # 271: Carousel 2 trang (2 slides)
    271: [
        {
            "artist": "Claude Monet",
            "artwork": "Grainstacks at the End of Summer",
            "metaphor": "Đụn rơm vững chãi đón nhận ánh nắng ấm áp của ngày tàn, khoảng dừng tỉnh thức giữa kích thích và phản ứng",
            "lighting": "Late summer golden hour, dusty ochre fields, warm purple mountain silhouettes"
        },
        {
            "artist": "Camille Pissarro",
            "artwork": "Sunset at Saint-Charles, Eragny",
            "metaphor": "Bầu trời hoàng hôn rực rỡ dát vàng đồng quê, người nông dân thong thả dắt bò về chuồng trong sự tĩnh tại làm chủ",
            "lighting": "Luminous orange and rose sky, peaceful elongated shadows across fertile soil"
        }
    ],
    # 272: Single-Punch (1 trang / 1 slide)
    272: [
        {
            "artist": "John Frederick Kensett",
            "artwork": "Sunset on the Sea",
            "metaphor": "Mặt biển bao la lúc hoàng hôn buông xuống, không một gợn sóng dữ, sự từ chối cảm xúc tổn thương là sự bảo vệ tối thượng",
            "lighting": "Minimalist soothing pastel gradient, coral and lilac horizon, mirror-like ocean"
        }
    ],
    # 273: Carousel 2 trang (2 slides)
    273: [
        {
            "artist": "John Singer Sargent",
            "artwork": "A Gust of Wind",
            "metaphor": "Một phụ nữ đứng kiêu hãnh trên đồi cỏ cao đón cơn gió lớn, giữ vững chiếc khăn và ánh nhìn điềm tĩnh, nhận diện kỳ vọng bất thành",
            "lighting": "Dynamic high-contrast daylight, rushing wind visible in fabric, vast open sky"
        },
        {
            "artist": "Caspar David Friedrich",
            "artwork": "Morning in the Mountains",
            "metaphor": "Đỉnh núi hùng vĩ đón nhận ánh bình minh rạng ngời, buông bỏ việc bắt thế gian phải phục tùng ý mình",
            "lighting": "Triumphant golden dawn breaking over misty valleys, sublime granite presence"
        }
    ],
    # 274: Carousel 3 trang (3 slides)
    274: [
        {
            "artist": "Jean-Baptiste-Camille Corot",
            "artwork": "The Lake at Ville-d'Avray",
            "metaphor": "Mặt hồ phẳng lặng phản chiếu bóng liễu rủ và bầu trời êm dịu, nghèo khó thực sự là lòng tham không đáy",
            "lighting": "Soft silvery-grey harmony, gentle ambient daylight, timeless pastoral quietude"
        },
        {
            "artist": "Claude Monet",
            "artwork": "The Artist's Garden at Giverny",
            "metaphor": "Khu vườn hoa ngập tràn ánh nắng rực rỡ, biết đủ với những gì hiện hữu xung quanh mình",
            "lighting": "Dappled afternoon sunlight, deep violet iris hues, vibrant emerald and golden leaf canopy"
        },
        {
            "artist": "George Inness",
            "artwork": "Peace and Plenty",
            "metaphor": "Cánh đồng lúa mì vàng óng ả bát ngát dưới ánh nắng chiều tà êm dịu, đỉnh cao của sự giàu có nội tâm",
            "lighting": "Bountiful golden harvest light, deep leafy elms, harmonious rural abundance"
        }
    ],
    # 275: Single-Punch (1 trang / 1 slide)
    275: [
        {
            "artist": "Albert Bierstadt",
            "artwork": "Among the Sierra Nevada Mountains",
            "metaphor": "Hồ nước trong veo trên đỉnh núi cao phản chiếu dãy núi tuyết hùng vĩ và bầy nai thanh thản gặm cỏ trong ánh bình minh đón ngày mới",
            "lighting": "Glorious heavenly sunbeams piercing mountain clouds, pristine turquoise alpine lake"
        }
    ],
    # 276: Carousel 3 trang (3 slides)
    276: [
        {
            "artist": "Mary Cassatt",
            "artwork": "The Tea",
            "metaphor": "Hai người phụ nữ ngồi trò chuyện bên bàn trà chiều thanh lịch, nhìn xuyên qua vẻ ngoài gai góc để thấy sự bất an bên trong",
            "lighting": "Warm afternoon drawing-room light, delicate porcelain, rich velvet and lace textures"
        },
        {
            "artist": "John Singer Sargent",
            "artwork": "A Dinner Table at Night",
            "metaphor": "Bàn ăn ấm cúng dưới ánh nến lung linh đỏ ấm, nơi nhu cầu chính đáng được gọi tên một cách chân thành",
            "lighting": "Warm glowing crimson lampshade, intimate dinner-table shadows, fine glassware"
        },
        {
            "artist": "Camille Pissarro",
            "artwork": "The Garden at Eragny",
            "metaphor": "Khu vườn đầy hoa trái xum xuê bao bọc trong nắng ấm, giao tiếp trắc ẩn hóa giải ngọn lửa giận dữ và hàn gắn kết nối",
            "lighting": "Bright sunny afternoon, lush green orchard, warm wooden fence textures"
        }
    ],
    # 277: Carousel 2 trang (2 slides)
    277: [
        {
            "artist": "Vilhelm Hammershøi",
            "artwork": "Interior, Ray of Sunlight",
            "metaphor": "Căn phòng tĩnh lặng với tia nắng rọi xiên, người lắng nghe buông bỏ sự phán xét và chuẩn bị lời bào chữa",
            "lighting": "Pure luminous diagonal sunbeam, dusty air, understated minimalist elegance"
        },
        {
            "artist": "Carl Larsson",
            "artwork": "Quiet Afternoon",
            "metaphor": "Góc đọc sách yên ả bên hiên nhà gỗ mộc mạc, sự thấu cảm thuần khiết khi lắng nghe trọn vẹn bằng cả trái tim",
            "lighting": "Gentle late afternoon shadow, warm wood tones, peaceful solitary presence"
        }
    ],
    # 278: Single-Punch (1 trang / 1 slide)
    278: [
        {
            "artist": "Berthe Morisot",
            "artwork": "Reading in the Garden",
            "metaphor": "Người phụ nữ ngồi đọc sách tĩnh lặng dưới bóng cây trong vườn, tình yêu trưởng thành xuất phát từ sự trọn vẹn của chính mình",
            "lighting": "Filtered daylight through green foliage, soft lilac dress, peaceful seclusion"
        }
    ],
    # 279: Carousel 3 trang (3 slides)
    279: [
        {
            "artist": "Pierre-Auguste Renoir",
            "artwork": "The Luncheon of the Boating Party",
            "metaphor": "Bàn tiệc vui vẻ của những người bạn tri kỷ ven sông, những cử chỉ quan tâm nhỏ bé thường nhật",
            "lighting": "Festive striped awning, warm golden river reflections, joyful candid camaraderie"
        },
        {
            "artist": "Joaquín Sorolla",
            "artwork": "Walk on the Beach",
            "metaphor": "Hai mẹ con tản bộ bên bờ biển lộng gió ngập nắng vàng, sự kết nối được vun đắp qua từng ánh nhìn ấm áp",
            "lighting": "Brilliant coastal sunlight, dazzling white fabric reflections, turquoise waves"
        },
        {
            "artist": "Claude Monet",
            "artwork": "The Garden of Monet at Argenteuil",
            "metaphor": "Khu vườn hoa hướng dương rực rỡ dưới bầu trời xanh thẳm, quy tắc vàng 5:1 của Gottman giúp mối quan hệ luôn tràn ngập sinh khí",
            "lighting": "Radiant midsummer sun, towering golden sunflowers, vibrant blue skies"
        }
    ],
    # 280: Carousel 2 trang (2 slides)
    280: [
        {
            "artist": "Mary Cassatt",
            "artwork": "Young Woman in a Green Outdoor Vest",
            "metaphor": "Người phụ nữ nhìn thẳng với ánh mắt chân thành, tháo gỡ chữ 'nhưng' phòng vệ để nhận lãnh trách nhiệm thực sự",
            "lighting": "Natural outdoor portrait lighting, fresh floral background, warm approachable gaze"
        },
        {
            "artist": "Henri Le Sidaner",
            "artwork": "The White Tablecloth",
            "metaphor": "Bàn ăn dọn sẵn trên hiên nhà nhìn ra vườn hoa hoàng hôn ấm áp, hàn gắn sự tin cậy sau tổn thương",
            "lighting": "Twilight blue hour, glowing lantern on white cloth, fragrant floral surroundings"
        }
    ],
    # 281: Single-Punch (1 trang / 1 slide)
    281: [
        {
            "artist": "Carl Larsson",
            "artwork": "The Sun Bath",
            "metaphor": "Khu vườn đầy hoa bên bờ suối nơi con người hòa mình vào ánh nắng ấm, chiếc ly đầy tự nhiên tràn ra tình yêu thương cho thế gian",
            "lighting": "Brilliant summer sunlight, blooming garden borders, clear rippling water"
        }
    ],
    # 282: Carousel 3 trang (3 slides)
    282: [
        {
            "artist": "John Singer Sargent",
            "artwork": "Monet Painting by the Edge of a Wood",
            "metaphor": "Hai nghệ sĩ đồng hành bên bìa rừng mùa thu, tôn trọng khoảng không gian tự do riêng biệt của nhau",
            "lighting": "Autumnal golden light filtering through beech leaves, rustic forest edge"
        },
        {
            "artist": "Claude Monet",
            "artwork": "Camille Monet in the Garden at Argenteuil",
            "metaphor": "Người phụ nữ ngồi bên luống hoa rực rỡ, tình yêu như đại dương dạt dào giữa hai bến bờ tự do",
            "lighting": "Warm afternoon sun, vibrant red geraniums, gentle breeze in trees"
        },
        {
            "artist": "Frederic Edwin Church",
            "artwork": "The Heart of the Andes",
            "metaphor": "Hai ngọn núi hùng vĩ cùng vươn cao đón ánh nắng bình minh, nâng đỡ mái đền tình yêu mà không đứng dưới bóng râm của nhau",
            "lighting": "Epic sweeping morning illumination, vibrant flora, crystalline cascading waters"
        }
    ],
    # 283: Carousel 2 trang (2 slides)
    283: [
        {
            "artist": "Joaquín Sorolla",
            "artwork": "Valencia Fishermen",
            "metaphor": "Bờ biển sớm mai mát lành, người ngư dân bình tĩnh trước cơn sóng dữ, dùng dòng nước thấu cảm để dập tắt ngọn lửa giận",
            "lighting": "Glorious early morning Mediterranean backlight, wet sand mirror reflections"
        },
        {
            "artist": "Pierre-Auguste Renoir",
            "artwork": "A Bouquet of Roses",
            "metaphor": "Bình hoa hồng tươi thắm rực rỡ trên bàn gỗ, biểu tượng của sự kiên nhẫn và bình tĩnh bảo tồn mối quan hệ",
            "lighting": "Velvety petals catching morning light, delicate glass vase, vibrant warm tones"
        }
    ],
    # 284: Single-Punch (1 trang / 1 slide)
    284: [
        {
            "artist": "Jean-Baptiste-Camille Corot",
            "artwork": "Morning with Nymphs",
            "metaphor": "Dòng sông êm đềm buổi sớm mai nơi cây cối nghiêng mình chào đón ngày mới, thước đo độ cao thượng là sự điềm tĩnh và bao dung",
            "lighting": "Silvery morning mist, tranquil riverbank, soft diffused golden horizon"
        }
    ],
    # 285: Carousel 3 trang (3 slides)
    285: [
        {
            "artist": "John Singer Sargent",
            "artwork": "Morning Walk",
            "metaphor": "Một cô gái trẻ cầm ô tản bộ bên bờ sông mùa hè, tình cảm như bến cảng bình yên cho tâm hồn neo đậu",
            "lighting": "Crisp morning coastal light, white cotton dress, peaceful shimmering water"
        },
        {
            "artist": "Camille Pissarro",
            "artwork": "Morning, Sunlight, Eragny",
            "metaphor": "Cây cối trổ hoa rực rỡ trong ánh bình minh, nơi bạn có thể cởi bỏ áo giáp và trở về là chính mình",
            "lighting": "Pointillist-like shimmering morning light, pastel meadow flowers, fresh morning breeze"
        },
        {
            "artist": "Mary Cassatt",
            "artwork": "Breakfast in Bed",
            "metaphor": "Khoảnh khắc bình yên sớm mai, gắn kết an toàn tiếp thêm đôi cánh tự tin khám phá thế giới rộng lớn",
            "lighting": "Soft white linen daylight, tender expression, warm comforting interior"
        }
    ],
    # 286: Carousel 2 trang (2 slides)
    286: [
        {
            "artist": "Pierre-Auguste Renoir",
            "artwork": "The Skiff (La Yole)",
            "metaphor": "Chiếc thuyền nhỏ lướt đi nhẹ nhàng trên dòng sông Seine xanh biếc, sự tử tế với những người lữ khách cùng chuyến đò đời",
            "lighting": "Dazzling blue water, glowing orange boat hull, joyful impressionist brushwork"
        },
        {
            "artist": "Claude Monet",
            "artwork": "Antibes Seen from the Salis Gardens",
            "metaphor": "Hàng cây ô liu cổ thụ nhìn ra vịnh biển xanh ngắt và dãy Alps xa xa phủ tuyết, lòng nhân từ thắp sáng thế giới xung quanh",
            "lighting": "Brilliant southern sun, turquoise sea, silver-green olive leaves, warm terracotta rooftops"
        }
    ],
    # 287: Single-Punch (1 trang / 1 slide)
    287: [
        {
            "artist": "Carl Larsson",
            "artwork": "Around the Lamp",
            "metaphor": "Cả gia đình quây quần ấm cúng quanh chiếc đèn bàn dầu trong đêm đông, một vài người bạn tri kỷ thấu hiểu tâm can giá trị hơn vạn lượt tương tác ảo",
            "lighting": "Intense warm yellow lamplight casting circular radiance, cozy domestic harmony"
        }
    ],
    # 288: Carousel 3 trang (3 slides)
    288: [
        {
            "artist": "Henri Le Sidaner",
            "artwork": "Evening Light in the Courtyard",
            "metaphor": "Khoảng sân nhỏ lát đá cổ với bàn trà dưới giàn nho hoàng hôn, trân trọng những điều giản dị đang có",
            "lighting": "Lyrical twilight atmosphere, glowing amber lantern, deep blue sky"
        },
        {
            "artist": "John Singer Sargent",
            "artwork": "Dolce Far Niente",
            "metaphor": "Nhóm bạn trẻ thư thái nghỉ ngơi trên bãi cỏ dưới ánh nắng vàng, niềm hạnh phúc hiện diện trong từng phút giây",
            "lighting": "Lush summer afternoon sunlight, draped fabrics, harmonious communal warmth"
        },
        {
            "artist": "Joaquín Sorolla",
            "artwork": "The Bathing Hour",
            "metaphor": "Trẻ em nô đùa trên sóng biển ngập nắng vàng, lòng biết ơn chủ động biến những điều bình dị thành điều kỳ diệu",
            "lighting": "Glittering Mediterranean sun on azure waves, golden wet sand, joyous splash highlights"
        }
    ],
    # 289: Carousel 3 trang (3 slides)
    289: [
        {
            "artist": "Viktor Frankl / Classical Homage",
            "artwork": "The Dawn After Darkness",
            "metaphor": "Một hàng rào thép gai cũ kỹ bị rỉ sét, từ kẽ đất nứt nẻ bên dưới mọc lên một nhành hoa cúc dại vàng rực đón ánh bình minh",
            "lighting": "Dramatic transition from dark smoky greys into blazing radiant sunrise gold"
        },
        {
            "artist": "Caspar David Friedrich",
            "artwork": "The Cross in the Mountains",
            "metaphor": "Cây thánh giá bằng gỗ mộc trên đỉnh vách đá cao, chiếu rọi bởi những tia nắng hoàng hôn rực rỡ, biến nghịch cảnh thành sứ mệnh",
            "lighting": "Solemn yet uplifting golden-purple twilight, majestic rocky peak"
        },
        {
            "artist": "Albert Bierstadt",
            "artwork": "A Storm in the Rocky Mountains",
            "metaphor": "Cơn bão đen ngòm tan dần trên rặng núi cao, chiếc cầu vồng rực rỡ xuất hiện vắt ngang qua bầu trời xanh thẳm, con người kiến tạo ý nghĩa sống",
            "lighting": "Dramatic contrast between receding thunderstorm clouds and vibrant prismatic rainbow light"
        }
    ],
    # 290: Carousel 2 trang (2 slides)
    290: [
        {
            "artist": "Japanese Kintsugi / Master Homage",
            "artwork": "Golden Seams of Healing",
            "metaphor": "Chiếc bát gốm cổ màu men ngọc bích bị nứt vỡ được hàn gắn bằng những đường chỉ vàng rực rỡ Kintsugi trên bàn trà gỗ mộc",
            "lighting": "Warm focused soft lighting, gleaming metallic gold veins, serene tea-ceremony atmosphere"
        },
        {
            "artist": "Frederic Edwin Church",
            "artwork": "Twilight in the Wilderness",
            "metaphor": "Bầu trời hoàng hôn rực lửa soi bóng xuống mặt hồ hoang sơ, những vết sẹo tổn thương trở thành chứng chỉ kiêu hãnh của sự sống",
            "lighting": "Blazing crimson and golden amber horizon, tranquil glass-like wilderness lake"
        }
    ],
    # 291: Single-Punch (1 trang / 1 slide)
    291: [
        {
            "artist": "J.M.W. Turner",
            "artwork": "Norham Castle, Sunrise",
            "metaphor": "Lâu đài cổ sừng sững trên đỉnh đồi mờ ảo trong ánh bình minh vàng rực rỡ, lạc quan tỉnh thức dám nhìn thẳng vào hiện thực và hành động",
            "lighting": "Sublime dissolved golden atmosphere, blue-grey silhouette, meditative serenity"
        }
    ],
    # 292: Carousel 3 trang (3 slides)
    292: [
        {
            "artist": "Claude Monet",
            "artwork": "Poplars on the Epte",
            "metaphor": "Hàng cây dương liễu cao vút soi bóng xuống dòng sông êm đềm, sự hiện diện trọn vẹn trong khoảnh khắc của hiện tại",
            "lighting": "Rhythmic vertical tree trunks catching morning sun, shimmering water reflections"
        },
        {
            "artist": "Thomas Cole",
            "artwork": "The Oxbow",
            "metaphor": "Khúc quanh ngoạn mục của dòng sông sau cơn giông bão, người họa sĩ ngồi tĩnh lặng phác họa thiên nhiên trong trạng thái Dòng Chảy",
            "lighting": "Vivid contrast of retreating storm clouds and pastoral sunshine over winding river"
        },
        {
            "artist": "George Inness",
            "artwork": "Peace and Plenty",
            "metaphor": "Cánh đồng lúa mì vàng óng ả bát ngát dưới ánh nắng chiều tà êm dịu, sự viên mãn khi quên đi bản ngã và hòa vào công việc",
            "lighting": "Bountiful golden harvest light, deep leafy elms, harmonious rural abundance"
        }
    ],
    # 293: Carousel 2 trang (2 slides)
    293: [
        {
            "artist": "Leonard Cohen / Master Homage",
            "artwork": "The Crack Where Light Enters",
            "metaphor": "Một bức tường đá cổ kính với vết nứt dài, từ kẽ nứt đó một luồng ánh sáng mặt trời vàng óng rọi thẳng vào xua tan bóng tối",
            "lighting": "Stunning beam of golden volumetric light cutting through ancient stone shadows"
        },
        {
            "artist": "Frederic Edwin Church",
            "artwork": "Aurora Borealis",
            "metaphor": "Dải cực quang rực rỡ màu xanh ngọc và tím biếc tỏa sáng trên bầu trời đêm bắc cực, sang chấn trở thành hạt mầm của sự trưởng thành vĩ đại",
            "lighting": "Ethereal celestial auroral glow illuminating icy peaks, awe-inspiring luminescence"
        }
    ],
    # 294: Single-Punch (1 trang / 1 slide)
    294: [
        {
            "artist": "J.M.W. Turner",
            "artwork": "Light and Colour (Goethe's Theory)",
            "metaphor": "Vòng xoáy ánh sáng vàng rực rỡ tinh khiết xua tan bóng tối hỗn mang, biểu tượng cho ý chí tự do bất khuất của tâm hồn thuyền trưởng số phận",
            "lighting": "Radiant vortex of golden and amber celestial light, supreme spiritual transcendence"
        }
    ],
    # 295: Carousel 2 trang (2 slides)
    295: [
        {
            "artist": "Claude Monet",
            "artwork": "The Cliff at Étretat, Sunset",
            "metaphor": "Cổng vòm đá tự nhiên Étretat sừng sững bên bờ biển lớn dưới ánh hoàng hôn dát vàng, trở thành một con người có giá trị và phẩm giá",
            "lighting": "Fiery orange and mauve sunset sky, majestic natural rock arch, surging turquoise sea"
        },
        {
            "artist": "Albert Bierstadt",
            "artwork": "Emerald Pool, Yellowstone",
            "metaphor": "Hồ nước nóng màu xanh ngọc bích tuyệt đẹp bốc làn khói mờ ảo giữa khung cảnh thiên nhiên kỳ vĩ, sự cống hiến vượt lên tư lợi cá nhân",
            "lighting": "Vibrant mineral emerald water, gentle rising steam, warm geothermal earth tones"
        }
    ],
    # 296: Carousel 3 trang (3 slides)
    296: [
        {
            "artist": "Camille Pissarro",
            "artwork": "The Garden of the Tuileries on a Winter Morning",
            "metaphor": "Cảnh tượng mùa đông băng giá lạnh buốt, nhưng sâu trong lòng đất những rễ cây đang âm thầm tích lũy dưỡng chất",
            "lighting": "Crisp winter frost, pale silvery daylight, enduring organic vitality"
        },
        {
            "artist": "Albert Camus / Master Homage",
            "artwork": "The Invincible Summer Within",
            "metaphor": "Giữa khung cảnh tuyết trắng, một mầm xanh vươn lên đón nhận ánh mặt trời vàng ấm áp bất diệt ẩn sâu trong tâm hồn",
            "lighting": "Warm golden sunbeam melting snow, vibrant young green leaves, hopeful contrast"
        },
        {
            "artist": "Pierre-Auguste Renoir",
            "artwork": "Bal du moulin de la Galette",
            "metaphor": "Quang cảnh buổi khiêu vũ ngoài trời rộn rã tiếng cười dưới những đốm nắng vàng nhảy múa, mùa hè bất khả chiến bại luôn ngự trị trong bạn",
            "lighting": "Playful dappled afternoon sun, colorful attire, lively joyous atmosphere"
        }
    ],
    # 297: Single-Punch (1 trang / 1 slide)
    297: [
        {
            "artist": "Frederic Edwin Church",
            "artwork": "Cotopaxi",
            "metaphor": "Ngọn núi hùng vĩ đón ánh bình minh rực lửa, một hồ nước êm đềm bên dưới phản chiếu trọn vẹn cảnh tượng kiêu hãnh của một cuộc đời dám sống trọn vẹn",
            "lighting": "Magnificent sunrise over majestic volcanic peak, blazing crimson and ochre sky, tranquil water"
        }
    ],
    # 298: Carousel 2 trang (2 slides)
    298: [
        {
            "artist": "Claude Monet",
            "artwork": "San Giorgio Maggiore at Dusk",
            "metaphor": "Nhà thờ Venice mờ ảo trong ánh hoàng hôn tím vàng huyền diệu soi bóng xuống mặt nước, giữ vững sự bình an giữa biến động",
            "lighting": "Breathtaking iridescent dusk sky, deep violet silhouette, shimmering golden water"
        },
        {
            "artist": "Albert Bierstadt",
            "artwork": "Rainbow over the Sierra Nevada",
            "metaphor": "Cầu vồng bảy sắc rực rỡ vắt ngang qua bầu trời xanh trong vắt ngay sau cơn mưa rào mùa hạ, chọn tập trung vào ánh sáng sau mây đen",
            "lighting": "Vibrant spectral rainbow arching over sunlit granite peaks, fresh rain-washed air"
        }
    ],
    # 299: Carousel 3 trang (3 slides)
    299: [
        {
            "artist": "Lewis Smedes / Master Homage",
            "artwork": "Unchaining the Prisoner",
            "metaphor": "Một chiếc lồng sắt cũ kỹ được mở toang cửa bên khung cửa sổ ngập nắng, chiếc dây xích thù hận rỉ sét rơi xuống sàn gỗ",
            "lighting": "Warm morning sunlight illuminating empty cage, open window looking onto expansive blue sky"
        },
        {
            "artist": "Jean-Baptiste-Camille Corot",
            "artwork": "The Bridge at Narni",
            "metaphor": "Chiếc cầu đá cổ bắc qua dòng sông xanh mát dưới bầu trời ngập nắng hè, buông bỏ quá khứ để hàn gắn tâm hồn",
            "lighting": "Golden Italian daylight, weathered ancient stone arches, calm flowing river"
        },
        {
            "artist": "J.M.W. Turner",
            "artwork": "The Morning after the Deluge",
            "metaphor": "Bình minh rực rỡ sau trận đại hồng thủy, ánh sáng vàng thuần khiết bao trùm vạn vật, kẻ tù nhân được giải thoát chính là bạn",
            "lighting": "Transcendent golden celestial vortex, pure luminous liberation, sublime awakening"
        }
    ],
    # 300: Carousel 3 trang (3 slides)
    300: [
        {
            "artist": "Marcus Aurelius & Carl Rogers / Master Homage",
            "artwork": "The Luminous Horizon at 300",
            "metaphor": "Một người lữ khách đứng bên cây cầu đá cổ kính nhìn lại con đường quanh co đã đi qua dưới bóng hoàng hôn ấm áp, lòng biết ơn sâu sắc hành trình 300 triết ngôn",
            "lighting": "Rich golden hour light illuminating the winding trail, sense of profound retrospective gratitude"
        },
        {
            "artist": "Claude Monet",
            "artwork": "Water Lilies (Harmony in Blue and Gold)",
            "metaphor": "Mặt hồ sen nở rộ hoa trắng tinh khôi phản chiếu bầu trời xanh ngắt và ánh nắng vàng mật ong, nhìn thấu sự bất toàn để bao dung hơn với thế gian",
            "lighting": "Serene turquoise and lapis lazuli water, glowing amber highlights, pristine white blossoms"
        },
        {
            "artist": "Albert Bierstadt & Frederic Edwin Church",
            "artwork": "The Summit of Wisdom and Compassion",
            "metaphor": "Đỉnh núi hùng vĩ đón ánh bình minh rạng rỡ dát vàng, một con suối mát lành tuôn chảy tưới mát cả thung lũng hoa nở rộ bên dưới, bước ra ánh sáng của lòng từ bi",
            "lighting": "Triumphant celestial dawn, radiant golden light bathing mountain summits, lush blooming valley"
        }
    ]
}

def main():
    print("=== TẠO ĐẶC TẢ MỸ THUẬT HYA-08 & MANIFEST (THEME 251 - 300 / 103 SLIDES) ===")
    
    with open(POSTS_PATH, "r", encoding="utf-8") as f:
        posts = json.load(f)
        
    manifest = {}
    spec_sections = []
    total_slides_count = 0

    for p in posts:
        stt = int(p["stt"])
        tid = p["id"]
        theme_id = f"theme_{stt}"
        title = p["title"]
        author = p["author"]
        topic = p["topic"]
        slide_fmt = p["format"]
        quote = p["caption"]
        
        art_slides_info = SLIDE_ART_MAPPINGS.get(stt, [])
        num_slides = len(art_slides_info)
        total_slides_count += num_slides
        
        slides_payload = []
        md_slides_sec = []
        
        for idx, art in enumerate(art_slides_info, 1):
            artist = art["artist"]
            artwork = art["artwork"]
            metaphor = art["metaphor"]
            lighting = art["lighting"]
            
            # Phân loại role theo nhịp
            if num_slides == 1:
                role = "Tác Phẩm Độc Bản (Single-Punch 1.0x)"
                slide_text = p["hook"]
            elif num_slides == 2:
                if idx == 1:
                    role = "Trang 1: Khởi Điểm Nỗi Trăn Trở (Tension / Dilemma)"
                    slide_text = p["hook"]
                else:
                    role = "Trang 2: Cú Lật & Ánh Sáng Thấu Suốt (Revelation / Illumination)"
                    slide_text = p["twist"]
            elif num_slides == 3:
                if idx == 1:
                    role = "Trang 1: Hiện Tượng Đời Thường (Phenomenon / Hook)"
                    slide_text = p["hook"]
                elif idx == 2:
                    role = "Trang 2: Căn Nguyên & Cú Lật Nhận Thức (Turning Point / Insight)"
                    slide_text = p["twist"]
                else:
                    role = "Trang 3: Chiếc Gương Phản Tư & Hòa Giải (Mirror / Serenity)"
                    slide_text = p["mirror"]
                    
            wikimedia_query = f"{artist} {artwork}"
            
            master_prompt = (
                f"{BASE_MEDIUM}. Masterpiece inspired by '{artwork}' by {artist}. "
                f"{metaphor}. {lighting}. {BASE_SAFE_ZONE}."
            )
            
            slide_obj = {
                "slide_index": idx,
                "page_role": role,
                "content_text": slide_text,
                "artist": artist,
                "artwork_title": artwork,
                "visual_metaphor": metaphor,
                "lighting_palette": lighting,
                "wikimedia_query": wikimedia_query,
                "prompt": master_prompt
            }
            slides_payload.append(slide_obj)
            
            md_slide_block = f"""#### Slide {idx}: {role}
- **Nội dung trang:** *"{slide_text}"*
- **Danh tác & Nghệ sĩ:** *{artwork}* — **{artist}**
- **Ý niệm thị giác:** {metaphor}
- **Bảng màu & Ánh sáng:** {lighting}
- **Truy vấn CCO bảo tàng:** `{wikimedia_query}`
- **Master Prompt (9:16):**
  ```text
  {master_prompt}
  ```
"""
            md_slides_sec.append(md_slide_block)
            
        manifest[tid] = {
            "stt": stt,
            "theme_id": theme_id,
            "title": title,
            "topic": topic,
            "author": author,
            "slide_format": slide_fmt,
            "slide_count": num_slides,
            "slides": slides_payload
        }
        
        # Build Markdown section
        theme_md = f"""### ❖ Bài {stt}: {tid} — {theme_id.upper()}
- **Chủ đề hạt nhân:** `{topic}`
- **Nguồn tác giả:** *{author}*
- **Định dạng bài:** `{slide_fmt}` ({num_slides} slide tranh sơn dầu độc lập)
- **Chiêm nghiệm biên tập:** *"{quote}"*

{"".join(md_slides_sec)}
---
"""
        spec_sections.append(theme_md)

    print(f"Tổng số theme xử lý: {len(manifest)}")
    print(f"Tổng số slide tranh độc lập được sinh: {total_slides_count}")
    assert total_slides_count == 103, f"Expected 103 slides, got {total_slides_count}"

    # 1. Lưu file manifest JSON
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã lưu Manifest JSON: {MANIFEST_PATH}")

    # 2. Lưu file đặc tả Markdown
    spec_header = f"""# ĐẶC TẢ MỸ THUẬT SƠN DẦU HYA-08 & 50 BỘ SUITES (THEME 251–300)

> **Mã quy chuẩn:** `HYA-08` | **Dự án:** Hiyu Abyss Living Library & TikTok Publishing  
> **Cương lĩnh cốt lõi:**  
> 1. *100% Hội họa sơn dầu bảo tàng đích thực (Monet, Renoir, Friedrich, Turner, Corot, Sorolla, Sargent, Cole, Bierstadt).*  
> 2. *Khử hoàn toàn dấu vết AI: Không da nhựa sáp 3D, không hào quang neon rực rỡ, không ký tự giả mạo, tỷ lệ chuẩn dọc 9:16.*  
> 3. *Nguyên tắc tác phẩm độc lập theo từng slide: Mỗi trang trong bài là một tác phẩm hội họa riêng biệt chuyển tải đúng nhịp điệu tư tưởng (Hiện tượng $\\rightarrow$ Cú lật $\\rightarrow$ Chiếc gương).*  
> 4. *Tổng quy mô chế tác: Đúng 103 slide tranh sơn dầu độc lập (15 bài x 1 + 17 bài x 2 + 18 bài x 3 = 103 slides).*

---

## 1. CÔNG THỨC SƠN DẦU MASTER (THE MASTER OIL FORMULA)

Mọi hình ảnh sinh ra cho bài 251 đến 300 phải tuân thủ tuyệt đối cấu trúc 5 tầng:
1. **Chất liệu hội họa vật lý (Medium & Texture):** Tỷ lệ dọc `9:16` (1080x1920), sơn dầu cổ điển (*classical fine art oil painting*), vân cọ đắp nổi dày dặn (*heavy impasto brushstrokes*), toan vải dệt hữu cơ (*tactile oil canvas weave texture*).
2. **Khử hoàn toàn dấu vết AI (Anti-AI Standard):** Tuyệt đối không bề mặt sáp/nhựa 3D, không ánh sáng neon phát sáng ảo, không chữ hay ký tự giả mạo, không dị tật giải phẫu.
3. **Ý niệm thị giác theo từng slide (Slide-Specific Visual Metaphor):** Chuyển dịch chính xác nhịp điệu tâm lý của trang đó thành hình ảnh hội họa giàu sức gợi và tính biểu tượng.
4. **Bảng màu theo cụm tư tưởng (Palette):**
   - **Tự Trắc Ẩn (251–263):** Vàng mật ong, hồng phấn, xanh ngọc bích, ánh nắng sớm xua tan sương mù dày đặc.
   - **Bình Thản Khắc Kỷ (264–275):** Xanh lam rạng đông, xám đá hoa cương ấm, mặt hồ phẳng lặng, vách đá sừng sững.
   - **Kết Nối Lành Mạnh (276–288):** Trắng ngọc trai, cam đất nung, xanh ô liu, bờ biển ngập nắng vàng, ánh nến bàn trà ấm cúng.
   - **Ý Nghĩa Sống & Sức Bật (289–300):** Vàng hổ phách rực rỡ, ánh sáng rọi qua kẽ đá nứt, đỉnh núi đón bình minh rạng ngời.
5. **Vùng an toàn cho chữ (Text Safe Zone):** Chừa 40% diện tích thoáng đãng, sắc độ êm dịu ở trung tâm/dưới để biên tập chữ TikTok.

---

## 2. DANH MỤC 50 BỘ SUITES CHI TIẾT (STT 251–300 / 103 SLIDES)

"""
    full_spec_content = spec_header + "\n".join(spec_sections)
    with open(SPEC_PATH, "w", encoding="utf-8") as f:
        f.write(full_spec_content)
    print(f"✅ Đã lưu Đặc tả mỹ thuật Markdown: {SPEC_PATH}")

if __name__ == '__main__':
    main()
