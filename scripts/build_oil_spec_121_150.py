#!/usr/bin/env python3
# scripts/build_oil_spec_121_150.py - Tạo đặc tả HYA-08 và manifest 47 prompts cho 30 bài 121-150
import json
import os

with open('scripts/posts_121_150_data.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

BASE_MEDIUM = "Vertical 9:16 classical fine art oil painting, authentic visible heavy impasto brushstrokes, tactile oil canvas weave texture"
BASE_SAFE_ZONE = "Atmospheric fine art composition with quiet, generous negative space in the middle-to-lower third for elegant editorial reading, strictly clean with NO text, NO lettering, NO watermarks, NO digital CGI rendering, traditional museum oil on canvas"

PROMPT_DEFINITIONS = {
    # 121 - KIÊN CƯỜNG (2 slides)
    "TXT-0121": [
        {
            "slide": 1,
            "role": "Hook: Bóng tối quái thú đe dọa",
            "concept": "Bóng đen huyền bí ẩn hiện trong màn sương mù u tối trên đỉnh núi đá",
            "prompt": f"{BASE_MEDIUM}. A mysterious mythical dragon-like shadow veiled inside dense mountain mist at twilight. Deep charcoal, slate gray, and moody Prussian blue tones. Atmospheric tension, brooding quietude. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Nàng công chúa và lòng trắc ẩn",
            "concept": "Bóng dáng thanh thoát giữa khu vườn hoa dại ngập tràn nắng vàng ấm áp",
            "prompt": f"{BASE_MEDIUM}. A gentle ethereal figure in flowing classical robes surrounded by sunlit wildflowers in an open alpine meadow. Golden morning hour, radiant warm amber hues, gentle compassion, transformative emotional healing. {BASE_SAFE_ZONE}."
        }
    ],
    # 122 - KIÊN CƯỜNG (1 slide)
    "TXT-0122": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Cây cổ thụ hiên ngang trên vách đá sau cơn bão lớn",
            "prompt": f"{BASE_MEDIUM}. A solitary ancient oak tree rooted fiercely into craggy mountain rock after a furious thunderstorm. Dramatic sunbeams breaking through receding dark clouds, illuminating resilient twisted bark and fresh green shoots. Friedrich-inspired sublime endurance. {BASE_SAFE_ZONE}."
        }
    ],
    # 123 - KIÊN CƯỜNG (2 slides)
    "TXT-0123": [
        {
            "slide": 1,
            "role": "Hook: Bị tước đoạt ngoại cảnh",
            "concept": "Cánh cửa sắt nhà giam cũ kỹ nhìn ra vùng đất mùa đông hoang vu",
            "prompt": f"{BASE_MEDIUM}. Heavy rustic wrought-iron bars overlooking a bleak, frozen winter landscape at dusk. Melancholic muted zinc gray and cool cobalt shadows, somber contemplation. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Tự do lựa chọn thái độ bên trong",
            "concept": "Ngọn nến kiên định soi sáng pho tượng đá bình thản trong hốc đá",
            "prompt": f"{BASE_MEDIUM}. A steady, radiant candle flame inside a stone sanctuary, softly illuminating a calm classical sculpted stone bust. Warm golden chiaroscuro glow, unassailable inner citadel, sovereign inner freedom. {BASE_SAFE_ZONE}."
        }
    ],
    # 124 - KIÊN CƯỜNG (1 slide)
    "TXT-0124": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Dòng sông mùa thu phẳng lặng cuốn trôi lá vàng",
            "prompt": f"{BASE_MEDIUM}. A serene, mirror-smooth autumn river quietly carrying away fallen golden ochre leaves. Distant gentle misty hills under a pale lavender sky. Stoic acceptance, peaceful surrender to natural law, timeless tranquility. {BASE_SAFE_ZONE}."
        }
    ],
    # 125 - KẾT NỐI (2 slides)
    "TXT-0125": [
        {
            "slide": 1,
            "role": "Hook: Tình yêu bám víu non nớt",
            "concept": "Cây tầm gửi yếu ớt quấn chặt cành khô trong bóng tối",
            "prompt": f"{BASE_MEDIUM}. Tangled ivy clinging tightly to a brittle withered branch in shadowed woods. Damp earthy umber tones, clinging vulnerability, somber mood. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Tình yêu trưởng thành của hai cây cổ thụ",
            "concept": "Hai cây sồi độc lập sừng sững bên nhau trên thảo nguyên ngập nắng",
            "prompt": f"{BASE_MEDIUM}. Two majestic companion oak trees standing side by side in a lush golden meadow under an open sunny sky. Gentle morning light filtering through expansive leafy canopies, mutual reverence, mature and whole love. {BASE_SAFE_ZONE}."
        }
    ],
    # 126 - KẾT NỐI (1 slide)
    "TXT-0126": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Hai ngọn hải đăng soi sáng vịnh biển đêm thanh tĩnh",
            "prompt": f"{BASE_MEDIUM}. Two distant stone lighthouses across a calm coastal bay under a starry twilight sky, each casting warm beams of light across peaceful waters. Sacred boundaries, mutual protection, solitary dignity in harmonious connection. {BASE_SAFE_ZONE}."
        }
    ],
    # 127 - KẾT NỐI (2 slides)
    "TXT-0127": [
        {
            "slide": 1,
            "role": "Hook: Đám đông ồn ào trốn chạy cô đơn",
            "concept": "Quảng trường mờ mịt đông đúc người qua lại trong sương chiều",
            "prompt": f"{BASE_MEDIUM}. A shadowy 19th-century European city street filled with hurried, blurry figures carrying umbrellas in rainy dusk. Wet cobblestones reflecting gas lamps, lonely crowd melancholy. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: An ổn một mình là cội nguồn tình yêu",
            "concept": "Ban công hoa hồng yên ả đón nắng sớm với tách trà và quyển sách mở",
            "prompt": f"{BASE_MEDIUM}. A peaceful sun-drenched private stone balcony with blooming pink climbing roses. A simple wooden table holds an open book and porcelain teacup. Contentment in solitary existence, radiant inner wholeness. {BASE_SAFE_ZONE}."
        }
    ],
    # 128 - KẾT NỐI (1 slide)
    "TXT-0128": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Hai vật phẩm quý phản chiếu ánh nến tương hỗ trên bàn tiệc",
            "prompt": f"{BASE_MEDIUM}. A polished silver chalice and a delicate porcelain vase resting together on rich dark velvet under soft candlelight. Warm highlights, chemical harmony of souls, Chardin-inspired quiet still life. {BASE_SAFE_ZONE}."
        }
    ],
    # 129 - KẾT NỐI (3 slides)
    "TXT-0129": [
        {
            "slide": 1,
            "role": "Hook: Câu hỏi về tình bạn tri kỷ",
            "concept": "Hai người lữ hành đồng điệu bước đi trên con đường rợp bóng cây",
            "prompt": f"{BASE_MEDIUM}. Two solitary wanderers walking quietly side by side along a grand tree-lined country avenue in soft afternoon haze. Atmospheric depth, nostalgic warmth. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Bởi vì đó là người ấy, và bởi vì đó là tôi",
            "concept": "Bàn cờ gỗ mộc mạc và hai tách trà bên lò sưởi ấm",
            "prompt": f"{BASE_MEDIUM}. A rustic wooden chessboard with carved pieces set beside two warm earthen mugs near a glowing stone hearth. Intimate camaraderie, pure unpretentious kinship. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 3,
            "role": "Chiếc gương: Nhận ra nhau giữa biển người",
            "concept": "Hai con thuyền nhỏ neo đậu cạnh nhau trên vịnh biển hoàng hôn",
            "prompt": f"{BASE_MEDIUM}. Two classic wooden fishing boats resting quietly together in a tranquil sheltered lagoon at golden sunset. Gentle rippling water, mutual recognition across vast oceans. {BASE_SAFE_ZONE}."
        }
    ],
    # 130 - KẾT NỐI (1 slide)
    "TXT-0130": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Bàn tay nâng niu bông hoa nở rộ trong nắng sớm",
            "prompt": f"{BASE_MEDIUM}. A delicate blossoming white camellia opening its petals to morning sunlight in a serene secluded garden. Soft dewdrops, generous warmth, open-hearted courage to love. {BASE_SAFE_ZONE}."
        }
    ],
    # 131 - KẾT NỐI (2 slides)
    "TXT-0131": [
        {
            "slide": 1,
            "role": "Hook: Trụ cột của ngôi đền",
            "concept": "Hai cây cột đá cổ điển đứng vững chãi giữa không gian lộng gió",
            "prompt": f"{BASE_MEDIUM}. Two monumental classical stone pillars standing upright beneath a vast azure sky, separated by breathing space. Enduring strength, noble balance, monumental architecture. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Làn gió thiên đường nhảy múa ở giữa",
            "concept": "Cánh đồng lúa mì vàng óng lượn sóng trong làn gió mát lành",
            "prompt": f"{BASE_MEDIUM}. A golden wheat field swaying rhythmically under an open breezy sky. Summer sunlight dancing between the stalks, freedom within unity, lyrical pastoral serenity. {BASE_SAFE_ZONE}."
        }
    ],
    # 132 - KẾT NỐI (1 slide)
    "TXT-0132": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Khu vườn được vun xới chu đáo và hoa nở ngát hương",
            "prompt": f"{BASE_MEDIUM}. A thriving walled cottage garden with blooming peonies and medicinal herbs receiving gentle morning irrigation. Nourishing care, active love for growth, Monet-inspired impressionist warmth. {BASE_SAFE_ZONE}."
        }
    ],
    # 133 - BẢN SẮC (2 slides)
    "TXT-0133": [
        {
            "slide": 1,
            "role": "Hook: Người nhìn ra ngoài mơ mộng viển vông",
            "concept": "Cửa kính đọng hơi sương mờ mịt nhìn ra đêm tối đầy ánh sáng phù du",
            "prompt": f"{BASE_MEDIUM}. A frosted windowpane looking out into a misty nocturnal street with blurred, distant lanterns. Cool cerulean and smoky indigo tones, illusory longing. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Người nhìn vào trong thức tỉnh chân tâm",
            "concept": "Chiếc đèn dầu bằng đồng soi rọi trang sách cổ và gương soi nội tâm",
            "prompt": f"{BASE_MEDIUM}. A warm brass oil lamp illuminating an open leather diary and an oval polished bronze mirror in a quiet private study. Deep chiaroscuro, contemplative awakening, luminous self-knowledge. {BASE_SAFE_ZONE}."
        }
    ],
    # 134 - BẢN SẮC (1 slide)
    "TXT-0134": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Pho tượng cẩm thạch hoàn mỹ đơn độc trong gian phòng bảo tàng",
            "prompt": f"{BASE_MEDIUM}. An exquisite classical marble sculpture standing alone in a high-arched gallery illuminated by natural northern skylight. Timeless nobility, authentic individuation, unyielding selfhood. {BASE_SAFE_ZONE}."
        }
    ],
    # 135 - BẢN SẮC (2 slides)
    "TXT-0135": [
        {
            "slide": 1,
            "role": "Hook: Kho báu phủ bụi của kẻ ham sở hữu",
            "concept": "Rương vàng bạc cổ phủ đầy bụi bặm trong căn phòng tối hoang tàn",
            "prompt": f"{BASE_MEDIUM}. An opulent iron-bound treasure chest overflowing with tarnished gold coins and ornate goblets covered in spiderwebs. Dark gloomy chamber, vanitas allegory of hollow possessions. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Niềm vui tồn tại thuần khiết của người thợ thủ công",
            "concept": "Người thợ chạm khắc gỗ thư thái bên cửa sổ ngập nắng",
            "prompt": f"{BASE_MEDIUM}. A sun-filled artisan workshop with fragrant wood shavings, chisels, and a half-carved musical instrument on a sturdy workbench. Golden amber sunlight, pride in authentic being, honest craftsmanship. {BASE_SAFE_ZONE}."
        }
    ],
    # 136 - BẢN SẮC (1 slide)
    "TXT-0136": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Cổ thụ tùng ngàn năm tĩnh tọa bên khe suối trong vắt",
            "prompt": f"{BASE_MEDIUM}. An ancient weathered pine tree rooted beside a crystal mountain stream flowing over smooth pebbles. Soft morning mist, Taoist clarity, self-mastery as supreme enlightenment. {BASE_SAFE_ZONE}."
        }
    ],
    # 137 - BẢN SẮC (2 slides)
    "TXT-0137": [
        {
            "slide": 1,
            "role": "Hook: Sân khấu kịch của những vai diễn giả tạo",
            "concept": "Khán phòng nhà hát xa hoa với những chiếc mặt nạ hóa trang rơi rụng",
            "prompt": f"{BASE_MEDIUM}. A dramatic opera box with velvet curtains and discarded Venetian carnival masks on plush crimson seating. Flickering gas chandeliers, superficial social performance. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Gian phòng thí nghiệm nội tâm của Montaigne",
            "concept": "Góc bàn làm việc trên gác chuông với giá sách và chiếc kính lúp cổ",
            "prompt": f"{BASE_MEDIUM}. A secluded circular tower library with floor-to-ceiling books, a solid walnut desk, antique quill, and parchment. Warm afternoon window light, sanctuary of authentic thought. {BASE_SAFE_ZONE}."
        }
    ],
    # 138 - BẢN SẮC (1 slide)
    "TXT-0138": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Mỏm đá hoa cương sừng sững giữa biển mây cuồn cuộn",
            "prompt": f"{BASE_MEDIUM}. A monumental granite peak piercing majestically through swirling sea of white clouds under brilliant sunlight. Emersonian non-conformist triumph, steadfast individual sovereignty. {BASE_SAFE_ZONE}."
        }
    ],
    # 139 - BẢN SẮC (3 slides)
    "TXT-0139": [
        {
            "slide": 1,
            "role": "Hook: Kẻ được muôn người biết đến nhưng lạc lối",
            "concept": "Ngai vàng tráng lệ nhưng bóng dáng hoàng tộc trĩu nặng u sầu",
            "prompt": f"{BASE_MEDIUM}. An imposing golden royal throne in a grand shadow-draped palace hall. Heavy gilded columns, cold majesty, profound inner alienation. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Chết đi như một kẻ xa lạ với chính mình",
            "concept": "Chiếc mặt nạ vàng rơi vỡ trên phiến đá lạnh bên ngọn nến tàn",
            "prompt": f"{BASE_MEDIUM}. A cracked golden mask resting beside an extinguished candle and a wilting white lily on cold dark marble. Tragic realization of an unlived, performative life. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 3,
            "role": "Chiếc gương: Trở về với sự chân thật mộc mạc",
            "concept": "Bát gốm thô mộc và quả táo chín trên mặt bàn gỗ mộc",
            "prompt": f"{BASE_MEDIUM}. A simple rustic earthenware bowl with ripe wild apples on unpolished oak wood. Warm natural daylight, Chardin-style sacred simplicity, return to the genuine self. {BASE_SAFE_ZONE}."
        }
    ],
    # 140 - BẢN SẮC (1 slide)
    "TXT-0140": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Pháo đài nội tâm uy nghiêm trên đỉnh đồi xanh",
            "prompt": f"{BASE_MEDIUM}. A solitary medieval stone fortress standing resolute atop a verdant hill under a clear autumn sky. Impregnable walls, serene detachment, the Stoic inner citadel. {BASE_SAFE_ZONE}."
        }
    ],
    # 141 - BẢN SẮC (1 slide)
    "TXT-0141": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Giọt sương sớm tinh khôi đọng trên lá sen trong hồ nước tĩnh",
            "prompt": f"{BASE_MEDIUM}. A pure crystalline dewdrop resting peacefully on a broad green lotus leaf in a tranquil garden pond. Soft radiant dawn light, immaculate conscience, undisturbed serenity. {BASE_SAFE_ZONE}."
        }
    ],
    # 142 - VƯỢT PHÁN XÉT (2 slides)
    "TXT-0142": [
        {
            "slide": 1,
            "role": "Hook: Chọn cách không cảm thấy bị tổn thương",
            "concept": "Chiếc khiên đồng cổ điển đứng vững trước những mũi tên rơi vô hại",
            "prompt": f"{BASE_MEDIUM}. An ancient bronze shield resting firmly against a stone column, with fallen arrows lying harmlessly on the flagstone floor. Quiet dignity, sovereign refusal of injury. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Không lời miệt thị nào chạm tới phẩm giá",
            "concept": "Bầu trời trong xanh bao la nhìn từ đỉnh núi tuyết",
            "prompt": f"{BASE_MEDIUM}. A vast panoramic mountain vista of snow-capped peaks under an immense, cloudless azure sky. Pure crystalline air, absolute stillness, invulnerable higher perspective. {BASE_SAFE_ZONE}."
        }
    ],
    # 143 - VƯỢT PHÁN XÉT (1 slide)
    "TXT-0143": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Chiếc đồng hồ cát cổ chảy êm đềm bên án thư tĩnh mịch",
            "prompt": f"{BASE_MEDIUM}. An antique brass and glass hourglass with golden sand trickling peacefully onto a leather-topped desk beside closed books. Deep warm light, wisdom of ignoring frivolous gossip, preciousness of time. {BASE_SAFE_ZONE}."
        }
    ],
    # 144 - VƯỢT PHÁN XÉT (3 slides)
    "TXT-0144": [
        {
            "slide": 1,
            "role": "Hook: Ảo tưởng về những vầng hào quang",
            "concept": "Những bức vẽ hào quang vàng son rực rỡ nhưng trống rỗng",
            "prompt": f"{BASE_MEDIUM}. A gilded theatrical altar with overly ornate faux halos and superficial gilding in cold artificial light. Shallow spiritual vanity. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Dũng cảm soi rọi bóng tối bên trong",
            "concept": "Ngọn đuốc rực sáng soi rõ từng ngóc ngách hang đá sâu thẳm",
            "prompt": f"{BASE_MEDIUM}. A blazing resin torch held inside a profound subterranean cavern, illuminating ancient stalactites and deep shadowed recesses with warm fiery light. Courage to meet the Jungian shadow. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 3,
            "role": "Chiếc gương: Thấu hiểu sự bất toàn để bao dung",
            "concept": "Chiếc cân đồng thau cân bằng hoàn hảo trong ánh sáng ban mai",
            "prompt": f"{BASE_MEDIUM}. A vintage brass apothecary balance scale resting in perfect equilibrium on a polished marble tabletop under gentle morning sun. Equanimity, profound compassion born of self-awareness. {BASE_SAFE_ZONE}."
        }
    ],
    # 145 - VƯỢT PHÁN XÉT (1 slide)
    "TXT-0145": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Thanh kiếm thép sáng phản chiếu ánh trăng tự bảo vệ",
            "prompt": f"{BASE_MEDIUM}. An antique polished steel rapier resting peacefully beside a leather scabbard and a small oil lamp. Pure tempered metal, self-knowledge as invincible psychological armor. {BASE_SAFE_ZONE}."
        }
    ],
    # 146 - VƯỢT PHÁN XÉT (2 slides)
    "TXT-0146": [
        {
            "slide": 1,
            "role": "Hook: Tự giam mình trong chiếc lồng công nhận",
            "concept": "Chiếc lồng chim bằng vàng chạm khắc cầu kỳ mở cửa nhưng lạnh lẽo",
            "prompt": f"{BASE_MEDIUM}. An ornate gilded birdcage hanging in a shadowed aristocratic parlor, with its door standing wide open. Intricate bars, bittersweet captive beauty. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Cánh chim tung cánh bay về phía rặng núi tự do",
            "concept": "Đại bàng sải cánh bay cao qua thung lũng mờ sương hướng về mặt trời",
            "prompt": f"{BASE_MEDIUM}. A majestic eagle soaring high over misty mountain valleys toward a radiant rising sun. Expansive horizon, untethered freedom, breaking out of societal approval. {BASE_SAFE_ZONE}."
        }
    ],
    # 147 - VƯỢT PHÁN XÉT (1 slide)
    "TXT-0147": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Người lữ hành rẽ lối đi riêng trên đồi hoa ngập nắng",
            "prompt": f"{BASE_MEDIUM}. A solitary traveler with a walking staff pausing on a sun-drenched winding hill path dotted with wild poppies, while distant flock grazes down in shadowed fog. Emersonian self-reliance, escaping the herd mentality. {BASE_SAFE_ZONE}."
        }
    ],
    # 148 - VƯỢT PHÁN XÉT (2 slides)
    "TXT-0148": [
        {
            "slide": 1,
            "role": "Hook: Chợ đời ồn ào và những lời phán xét",
            "concept": "Góc chợ phiên châu Âu thế kỷ 18 tấp nập người qua lại tranh cãi",
            "prompt": f"{BASE_MEDIUM}. A bustling 18th-century European town square with energetic market stalls, animated merchants, and bustling crowds under overcast skies. Sensory noise and social spectacle. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Gian phòng nội tâm bất khả xâm phạm",
            "concept": "Góc phòng làm việc tĩnh lặng nhìn qua vòm cửa sổ ra khu vườn thanh bình",
            "prompt": f"{BASE_MEDIUM}. A peaceful stone study room with an arched window opening to a quiet green orchard. An antique desk, inkwell, and open manuscript bathed in soft natural light. Montaigne's back-shop of absolute peace. {BASE_SAFE_ZONE}."
        }
    ],
    # 149 - VƯỢT PHÁN XÉT (1 slide)
    "TXT-0149": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Cây gai nhọn soi bóng xuống vũng nước đục",
            "prompt": f"{BASE_MEDIUM}. A solitary thorny bramble bush growing beside a murky puddle on rocky ground under stormy clouds. Somber Chiaroscuro, psychological allegory of self-hatred projected outwardly. {BASE_SAFE_ZONE}."
        }
    ],
    # 150 - VƯỢT PHÁN XÉT (1 slide)
    "TXT-0150": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Mặt biển bao la phẳng lặng tuyệt đối dưới ánh hoàng hôn",
            "prompt": f"{BASE_MEDIUM}. An immense, mirror-flat ocean horizon under a soft lavender and rose gold twilight. No ripples, absolute stillness, sublime peace of walking unharmed through the world's clamor. Turner-inspired luminous stillness. {BASE_SAFE_ZONE}."
        }
    ],
}

# 1. Save manifest
with open('scripts/oil_suites_121_150_prompts_manifest.json', 'w', encoding='utf-8') as f:
    json.dump(PROMPT_DEFINITIONS, f, ensure_ascii=False, indent=2)

total_slides = sum(len(slides) for slides in PROMPT_DEFINITIONS.values())
print(f"Generated manifest with {len(PROMPT_DEFINITIONS)} posts and {total_slides} slides.")

# 2. Build Markdown specification document
spec_md = []
spec_md.append("# ĐẶC TẢ MỸ THUẬT SƠN DẦU HYA-08 & 47 SLIDE ĐỘC BẢN (THEME 121–150)")
spec_md.append("")
spec_md.append("> **Mã quy chuẩn:** `HYA-08` | **Dự án:** Hiyu Abyss Living Library & TikTok Publishing")
spec_md.append("> **Cương lĩnh cốt lõi:** *Mỗi slide là một kiệt tác sơn dầu độc lập — Chấm dứt hoàn toàn trò lặp ảnh crop/zoom.*")
spec_md.append("")
spec_md.append("---")
spec_md.append("")
spec_md.append("## 1. CÔNG THỨC SƠN DẦU MASTER (THE MASTER OIL FORMULA)")
spec_md.append("")
spec_md.append("Mọi hình ảnh sinh ra cho bài 121 đến 150 phải tuân thủ tuyệt đối cấu trúc 5 tầng:")
spec_md.append("1. **Chất liệu hội họa vật lý (Medium & Texture):** Tỷ lệ dọc `9:16`, sơn dầu cổ điển (*classical fine art oil painting*), vân cọ đắp nổi dày dặn (*heavy impasto brushstrokes*), toan vải dệt hữu cơ (*tactile oil canvas weave*).")
spec_md.append("2. **Khử hoàn toàn dấu vết AI (Anti-AI Standard):** Không da nhựa sáp 3D, không hào quang neon rực rỡ, không chữ hay ký tự giả nguệch ngoạc.")
spec_md.append("3. **Ý niệm thị giác đặc thù (Visual Metaphor):** Bám sát linh hồn từng bài viết, chuyển dịch triết lý thành hình ảnh ẩn dụ giàu sức gợi.")
spec_md.append("4. **Bảng màu theo cụm tư tưởng (Palette):**")
spec_md.append("   - **Kiên cường (121–124):** Xám đá, xanh giông bão, ánh vàng bình minh sau mây.")
spec_md.append("   - **Kết nối (125–132):** Nắng sớm ấm áp, hổ phách, hồng phấn, xanh thảo nguyên Monet/Renoir.")
spec_md.append("   - **Bản sắc (133–141):** Nâu sồi ấm, vàng nến Chiaroscuro, xanh ngọc bích, cẩm thạch trắng.")
spec_md.append("   - **Vượt phán xét (142–150):** Đồng thau, xanh chân trời bao la, tím hoàng hôn phẳng lặng.")
spec_md.append("5. **Vùng an toàn cho chữ (Text Safe Zone):** Chừa 40% diện tích thoáng đãng, sắc độ êm dịu ở trung tâm/dưới để biên tập chữ TikTok.")
spec_md.append("")
spec_md.append("---")
spec_md.append("")
spec_md.append("## 2. DANH MỤC 47 SLIDE ĐỘC BẢN CHI TIẾT (STT 121–150)")
spec_md.append("")

for p in posts:
    pid = p["id"]
    stt = p["stt"]
    t_key = p["theme_key"]
    slides = PROMPT_DEFINITIONS.get(pid, [])
    
    spec_md.append(f"### ❖ Bài {stt}: {pid} — {t_key.upper()}")
    spec_md.append(f"- **Chủ đề hạt nhân:** `{p['theme']}`")
    spec_md.append(f"- **Nguồn tác giả:** *{p['author']}*")
    spec_md.append(f"- **Định dạng slide:** `{p['format']}` ({len(slides)} slide độc bản)")
    spec_md.append(f"- **Văn bản hoàn chỉnh:** *\"{p['full_quote']}\"*")
    spec_md.append("")
    
    for s in slides:
        spec_md.append(f"#### Slide {s['slide']}: {s['role']}")
        spec_md.append(f"- **Ý niệm nghệ thuật:** {s['concept']}")
        spec_md.append(f"- **Prompt đặc tả Master:**")
        spec_md.append(f"  ```text")
        spec_md.append(f"  {s['prompt']}")
        spec_md.append(f"  ```")
        spec_md.append("")

with open('docs/09_HIYU_ABYSS_OIL_PAINTING_SUITES_121_150_SPEC.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(spec_md))

print("Created docs/09_HIYU_ABYSS_OIL_PAINTING_SUITES_121_150_SPEC.md successfully!")
