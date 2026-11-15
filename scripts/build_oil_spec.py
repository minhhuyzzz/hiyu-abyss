#!/usr/bin/env python3
# scripts/build_oil_spec.py - Sinh toàn bộ đặc tả HYA-08 và manifest prompt 51 slides
import json
import os

with open('scripts/posts_91_120_data.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Master Oil Formula components
BASE_MEDIUM = "Vertical 9:16 classical fine art oil painting, authentic visible heavy impasto brushstrokes, tactile oil canvas weave texture"
BASE_SAFE_ZONE = "Atmospheric fine art composition with quiet, generous negative space in the middle-to-lower third for elegant editorial reading, strictly clean with NO text, NO lettering, NO watermarks, NO digital CGI rendering, traditional museum oil on canvas"

# Specific visual metaphors for each of the 30 posts and their slides
PROMPT_DEFINITIONS = {
    # 91 - SOLITUDE (1 slide)
    "TXT-0091": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Ngọn nến đơn độc trong thư viện cổ ban đêm",
            "prompt": f"{BASE_MEDIUM}. A solitary burning beeswax candle on an antique wooden table inside a dimly lit ancient private library. Surrounding leather-bound tomes rest peacefully in warm amber candlelight. Deep Prussian blue shadows fill the background. Contemplative, sacred quietude. {BASE_SAFE_ZONE}."
        }
    ],
    # 92 - SOLITUDE (2 slides)
    "TXT-0092": [
        {
            "slide": 1,
            "role": "Hook: Bàn tiệc ồn ào giả tạo",
            "concept": "Bàn tiệc xa hoa với những chiếc ly thủy tinh lấp lánh nhưng lạnh lẽo",
            "prompt": f"{BASE_MEDIUM}. An opulent banquet table with overflowing wine goblets and wilting flowers in dramatic Rembrandt chiaroscuro. The festive scene feels distant, hollow, and chaotic with flickering candelabras and heavy shadows. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Tĩnh lặng một mình bên lò sưởi",
            "concept": "Chiếc ghế bành gỗ mộc mạc bên lò sưởi ấm cúng và tách trà nóng",
            "prompt": f"{BASE_MEDIUM}. A cozy, warm reading armchair beside a gentle stone fireplace with crackling amber embers. A steaming porcelain teacup rests on a small side table beside an open journal. Peaceful, restorative sanctuary. {BASE_SAFE_ZONE}."
        }
    ],
    # 93 - SOLITUDE (1 slide)
    "TXT-0093": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Mặt hồ tĩnh mịch phản chiếu bầu trời đêm thanh khiết",
            "prompt": f"{BASE_MEDIUM}. An undisturbed glassy mountain lake at twilight, perfectly mirroring pale mist and a crescent moon. Soft ripples lap gently against a solitary weathered boulder. Serene, unshakeable dignity. {BASE_SAFE_ZONE}."
        }
    ],
    # 94 - SOLITUDE (2 slides)
    "TXT-0094": [
        {
            "slide": 1,
            "role": "Hook: Chiếc gương nứt nẻ tìm kiếm sự công nhận",
            "concept": "Gương cổ viền đồng mạ rạn nứt phản chiếu bóng người mờ ảo",
            "prompt": f"{BASE_MEDIUM}. An antique bronze vanity mirror with delicate hairline fractures, resting on a dusty dressing table. Soft dusky twilight filters through lace curtains. Introspective longing and quiet fragility. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Tâm hồn tự tại, đủ đầy bên khung cửa sổ",
            "concept": "Chậu hoa nhỏ và bình gốm đón tia nắng sớm bên bậc cửa",
            "prompt": f"{BASE_MEDIUM}. A sunlit terracotta pot with flourishing white blossoms resting on a sun-drenched stone windowsill. Golden morning dust motes dance in warm atmospheric light. Wholeness, self-sufficiency, radiant peace. {BASE_SAFE_ZONE}."
        }
    ],
    # 95 - SOLITUDE (3 slides)
    "TXT-0095": [
        {
            "slide": 1,
            "role": "Slide 1: Hiện tượng - Đám đông huyên náo",
            "concept": "Đám đông mờ ảo chen chúc dưới ánh đèn lồng đường phố thế kỷ 19",
            "prompt": f"{BASE_MEDIUM}. A crowded 19th-century cobblestone street in heavy autumn rain, figures moving with umbrellas under hazy streetlamps. Impressionistic, bustling, dizzying social noise. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Slide 2: Căn nguyên - Thư phòng nghệ nhân lúc nửa đêm",
            "concept": "Bàn vẽ kiến trúc với bản thảo, compa và ngọn đèn dầu đơn độc",
            "prompt": f"{BASE_MEDIUM}. An artist or scholar's wooden workbench deep in the night, illuminated by a single warm oil lamp. Scattered parchment sketches, brass compasses, and quill pens. The fertile womb of deep creation. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 3,
            "role": "Slide 3: Chiếc gương - Kiệt tác sinh ra từ cô độc",
            "concept": "Bức tượng điêu khắc cẩm thạch hoàn mỹ hiện lên giữa bóng tối",
            "prompt": f"{BASE_MEDIUM}. A classical unfinished white marble sculpture rising from rough stone, bathed in a soft beam of dawn light cutting through high studio rafters. Sublime artistic triumph, serene solitude. {BASE_SAFE_ZONE}."
        }
    ],
    # 96 - STATUS (1 slide)
    "TXT-0096": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Vương miện vàng ròng rạn nứt trên gối nhung đỏ phủ bụi",
            "prompt": f"{BASE_MEDIUM}. An ornate baroque golden crown with tarnished gold leaf and loose jewels, resting neglected upon a dusty crimson velvet cushion in a ruined palace hall. Vanitas aesthetic, tragic emptiness of boastful pride. {BASE_SAFE_ZONE}."
        }
    ],
    # 97 - STATUS (2 slides)
    "TXT-0097": [
        {
            "slide": 1,
            "role": "Hook: Mặt nạ vàng nụ cười khiêm nhường giả tạo",
            "concept": "Mặt nạ quý tộc Venetian mạ vàng với nét cười gượng gạo",
            "prompt": f"{BASE_MEDIUM}. A lavish Venetian gilded carnival mask hanging on a dark wood-paneled wall, adorned with theatrical smile and gold filigree. Subtle theatrical hypocrisy, calculated public modesty. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Chiếc bóng thật sự ngạo mạn phía sau",
            "concept": "Chiếc bóng phóng đại của nhân vật kiêu hãnh trên bức tường đá",
            "prompt": f"{BASE_MEDIUM}. A towering, dramatic shadow cast against a rustic stone wall by a small oil lamp, revealing the exaggerated silhouette of an arrogant posture. Stark chiaroscuro, unmasking covert ego. {BASE_SAFE_ZONE}."
        }
    ],
    # 98 - STATUS (1 slide)
    "TXT-0098": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Ngai vàng trống rỗng trong đại sảnh cung điện hoang tàn",
            "prompt": f"{BASE_MEDIUM}. A grand gilded baroque throne standing completely empty in a decaying, overgrown palace ballroom. Pale sunlight cuts through shattered stained-glass windows onto cracked marble floors. The fleeting illusion of worldly status. {BASE_SAFE_ZONE}."
        }
    ],
    # 99 - STATUS (2 slides)
    "TXT-0099": [
        {
            "slide": 1,
            "role": "Hook: Tiếng vỗ tay và khán đài rực rỡ nhưng tạm bợ",
            "concept": "Rèm nhung nhà hát đỏ thẫm buông xuống sau buổi diễn",
            "prompt": f"{BASE_MEDIUM}. A heavy crimson theatre curtain falling upon a dimly lit stage floor strewn with wilting rose bouquets. The lingering echo of hollow applause, the void after spectacle. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Khi tấm màn buông xuống, chỉ còn lại sự cô quạnh",
            "concept": "Hóa trang bị cởi bỏ trên bàn gỗ mộc bên tấm gương mờ",
            "prompt": f"{BASE_MEDIUM}. Backstage dressing mirror with discarded theatrical makeup pots and a plain cotton towel. A gentle cool breeze moves the window drape. The naked truth of self when audience departs. {BASE_SAFE_ZONE}."
        }
    ],
    # 100 - STATUS (3 slides)
    "TXT-0100": [
        {
            "slide": 1,
            "role": "Slide 1: Hiện tượng - Bức chân dung quyền uy mạ vàng",
            "concept": "Chân dung lãnh chúa uy quyền lồng khung vàng đồ sộ",
            "prompt": f"{BASE_MEDIUM}. A formal oil portrait of an arrogant aristocrat in heavy gold frame, adorned with medals and velvet robe. Formalistic social posturing, rigid hierarchy. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Slide 2: Căn nguyên - Đồng hồ cát và cát vàng rơi nhanh",
            "concept": "Đồng hồ cát bằng đồng cổ với những hạt cát thời gian chảy xiết",
            "prompt": f"{BASE_MEDIUM}. A brass antique hourglass on a worn mahogany desk, golden grains of sand relentlessly trickling down. Inexorable passage of time eroding human titles. Memento mori. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 3,
            "role": "Slide 3: Chiếc gương - Người làm vườn thanh thản bên đất mẹ",
            "concept": "Bàn tay chai sạn của người thợ làm vườn chăm sóc luống hoa đất ẩm",
            "prompt": f"{BASE_MEDIUM}. Sun-bronzed, weathered hands of a humble gardener tending fresh green sprouts in dark fertile soil under warm morning sunshine. Genuine dignity, peace far beyond social validation. {BASE_SAFE_ZONE}."
        }
    ],
    # 101 - RANH GIỚI (2 slides)
    "TXT-0101": [
        {
            "slide": 1,
            "role": "Hook: Cánh cửa mở toang khiến cỏ dại tràn vào nhà",
            "concept": "Cửa gỗ mở toang trước gió lốc và lá khô cuộn vào sàn",
            "prompt": f"{BASE_MEDIUM}. A rustic wooden cottage door blown wide open by wind, dry leaves and dust swirling across polished floorboards. The vulnerability of having no personal boundary. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Cánh cổng sắt rèn kiên cố bảo vệ khu vườn tĩnh tại",
            "concept": "Cổng sắt rèn hoa văn cổ kính khép kín giữa bờ rào đá rêu phong",
            "prompt": f"{BASE_MEDIUM}. An elegant, heavy wrought-iron garden gate securely latched within a moss-covered ancient stone wall. Behind the gate blooms a serene, protected garden in golden mist. Sacred boundaries, inner peace. {BASE_SAFE_ZONE}."
        }
    ],
    # 102 - RANH GIỚI (1 slide)
    "TXT-0102": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Ngọn hải đăng kiên định giữa muôn trùng sóng vỗ",
            "prompt": f"{BASE_MEDIUM}. A solitary rugged granite lighthouse standing immovable upon black coastal rocks, stormy sea waves breaking harmlessly against its foundation. A clear guiding light cutting through twilight fog. Unshakable self-sovereignty. {BASE_SAFE_ZONE}."
        }
    ],
    # 103 - RANH GIỚI (2 slides)
    "TXT-0103": [
        {
            "slide": 1,
            "role": "Hook: Chiếc áo giáp kim loại nặng nề kiệt sức",
            "concept": "Bộ giáp hiệp sĩ sắt đen gỉ sét đổ gục trong góc tối",
            "prompt": f"{BASE_MEDIUM}. A heavy, rusted iron knight's suit of armor resting against a cold stone dungeon wall. The exhausting toll of defensive over-reaction and endless people-pleasing. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Tấm khiên trong suốt của sự điềm tĩnh",
            "concept": "Mặt nước hồ trong veo tĩnh lặng, sỏi đá nằm yên đáy nước",
            "prompt": f"{BASE_MEDIUM}. A calm, crystal-clear forest spring pool over smooth river pebbles, untouched by autumn wind. Soft dappled sunlight through beech leaves. The calm invulnerability of quiet self-assurance. {BASE_SAFE_ZONE}."
        }
    ],
    # 104 - RANH GIỚI (1 slide)
    "TXT-0104": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Bức tường đá tự nhiên phân định ranh giới giữa rừng cây và thung lũng",
            "prompt": f"{BASE_MEDIUM}. An ancient dry-stone wall winding gracefully across green rolling hills in soft Celtic morning light. Wildflowers bloom naturally on both sides. Respectful demarcation, peaceful coexistence. {BASE_SAFE_ZONE}."
        }
    ],
    # 105 - RANH GIỚI (3 slides)
    "TXT-0105": [
        {
            "slide": 1,
            "role": "Slide 1: Hiện tượng - Sự xâm lấn và ngột ngạt",
            "concept": "Dây leo chằng chịt thắt nghẹt khung cửa sổ gỗ",
            "prompt": f"{BASE_MEDIUM}. Thick, thorny creeping ivy suffocating an antique arched window, blocking out natural light in gloomy twilight. Encroachment, emotional manipulation, suffocating boundaries. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Slide 2: Căn nguyên - Chiếc kéo tỉa cành và sự dứt khoát",
            "concept": "Kéo tỉa vườn bằng thép rèn đặt trên bàn gỗ bên nhánh cây vừa cắt",
            "prompt": f"{BASE_MEDIUM}. Heavy blacksmith forged pruning shears beside freshly cut thorny stems on an old wooden table. Daylight breaking cleanly through trimmed branches. The painful yet liberating act of saying NO. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 3,
            "role": "Slide 3: Chiếc gương - Khu vườn thở lại trong nắng mai",
            "concept": "Khoảng vườn thoáng đãng ngập tràn ánh nắng và hoa thơm",
            "prompt": f"{BASE_MEDIUM}. A revitalized, sun-drenched courtyard garden with tidy gravel paths and thriving rose bushes under clear azure sky. Breathable space, autonomy, joyous self-respect. {BASE_SAFE_ZONE}."
        }
    ],
    # 106 - RANH GIỚI (1 slide)
    "TXT-0106": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Cánh chim ưng sải cánh bay vút lên bầu trời tự do",
            "prompt": f"{BASE_MEDIUM}. A majestic hawk ascending gracefully into crisp autumn mountain air above towering pine ridges. Expansive cloudscape bathed in cool northern light. Fearless sovereignty, refusal to be domesticated. {BASE_SAFE_ZONE}."
        }
    ],
    # 107 - RANH GIỚI (2 slides)
    "TXT-0107": [
        {
            "slide": 1,
            "role": "Hook: Chiếc lồng son mạ vàng sang trọng",
            "concept": "Lồng chim mạ vàng tinh xảo treo giữa phòng khách quý tộc",
            "prompt": f"{BASE_MEDIUM}. An elaborate gilded Victorian birdcage hanging in a dim luxury parlor, its door swinging slightly open. The seduction of comfort traded for personal freedom. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Cành thông hoang dã vươn mình đón gió",
            "concept": "Cành thông bách xanh rì vươn ra từ vách núi đá hoa cương",
            "prompt": f"{BASE_MEDIUM}. A resilient mountain pine rooted firmly in bare granite rock, leaning fearlessly over a deep misty gorge into golden sunset. Self-authorship, raw authenticity. {BASE_SAFE_ZONE}."
        }
    ],
    # 108 - RANH GIỚI (1 slide)
    "TXT-0108": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Bàn cờ vua bằng đá cẩm thạch với quân Vua đứng vững chãi",
            "prompt": f"{BASE_MEDIUM}. A heavy marble chessboard in quiet candlelight, the lone King piece standing firm at the center of the board surrounded by quiet space. Strategic clarity, mental independence. {BASE_SAFE_ZONE}."
        }
    ],
    # 109 - THANH THẢN (2 slides)
    "TXT-0109": [
        {
            "slide": 1,
            "role": "Hook: Cơn bão ảo ảnh trong tâm trí",
            "concept": "Mây đen cuồn cuộn và sóng biển gầm rú dữ dội",
            "prompt": f"{BASE_MEDIUM}. A violent, dark sea storm with crashing waves under thunderous charcoal clouds in J.M.W. Turner aesthetic. The agonizing paralysis of catastrophic overthinking. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Thực tại tĩnh lặng, tách trà bốc khói",
            "concept": "Góc phòng yên bình nhìn ra vườn mưa qua ô kính trong",
            "prompt": f"{BASE_MEDIUM}. A quiet wooden table by a rain-streaked window pane with a steaming ceramic cup and an open book. Soft warm lamp interior contrasted against peaceful rain outside. Reality is far kinder than imagination. {BASE_SAFE_ZONE}."
        }
    ],
    # 110 - THANH THẢN (1 slide)
    "TXT-0110": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Bình nước thủy tinh để bùn lắng xuống đáy, nước trong suốt",
            "prompt": f"{BASE_MEDIUM}. A clear glass carafe filled with pure water standing on an ancient wooden windowsill, sediment settled completely at the bottom in crystal clarity. Morning light shining straight through. Stoic patience: let muddy water settle. {BASE_SAFE_ZONE}."
        }
    ],
    # 111 - THANH THẢN (3 slides)
    "TXT-0111": [
        {
            "slide": 1,
            "role": "Slide 1: Hiện tượng - Chạy trốn tìm kiếm bình yên bên ngoài",
            "concept": "Người lữ hành mải miết đi trên con đường đá dốc quanh co",
            "prompt": f"{BASE_MEDIUM}. A lone wanderer walking an endless, dusty mountain road at dusk seeking shelter under brooding sky. Restless search for external salvation. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Slide 2: Căn nguyên - Nhận ra nơi trú ẩn nằm ở bên trong",
            "concept": "Ngôi đền đá cổ tĩnh lặng ẩn mình sâu trong rừng trúc xanh",
            "prompt": f"{BASE_MEDIUM}. An ancient mossy stone sanctuary hidden among quiet bamboo grove, bathed in dappled morning light and rising incense smoke. The discovery of inner fortress. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 3,
            "role": "Slide 3: Chiếc gương - Sự an lạc tự tâm vững như núi đá",
            "concept": "Đỉnh núi phủ tuyết trắng sừng sững trên biển mây",
            "prompt": f"{BASE_MEDIUM}. A majestic snow-capped alpine peak rising serenely above an ocean of clouds in pure golden dawn light. Unmovable composure, eternal peace within. {BASE_SAFE_ZONE}."
        }
    ],
    # 112 - THANH THẢN (1 slide)
    "TXT-0112": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Chiếc bát gốm mộc mạc và nhành hoa dại bên bàn gỗ",
            "prompt": f"{BASE_MEDIUM}. A simple handmade ceramic bowl and a sprig of wild dried lavender on a rustic oak table. Chardin still life aesthetic, rich earthy umber and warm ochre tones. The profound wealth of needing little. {BASE_SAFE_ZONE}."
        }
    ],
    # 113 - THANH THẢN (2 slides)
    "TXT-0113": [
        {
            "slide": 1,
            "role": "Hook: Căn phòng chật chội đồ đạc phù phiếm",
            "concept": "Kho phòng bừa bộn những rương hòm và đồ xa xỉ phủ bụi",
            "prompt": f"{BASE_MEDIUM}. A cluttered, suffocating antique room packed with heavy velvet chests, gilded clocks, and dusty bric-a-brac in dim claustrophobic lighting. The burden of excessive possessions. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Không gian tối giản thênh thang tràn ngập ánh sáng",
            "concept": "Căn phòng trống trải với sàn gỗ sồi sạch sẽ và ánh nắng ngập tràn",
            "prompt": f"{BASE_MEDIUM}. A spacious, minimalist sunlit room with clean polished floorboards, open timber window frames, and sheer white curtains swaying in gentle breeze. Pure lightness of being. {BASE_SAFE_ZONE}."
        }
    ],
    # 114 - THANH THẢN (1 slide)
    "TXT-0114": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Lăng kính quang học tách chùm ánh sáng thành dải cầu vồng",
            "prompt": f"{BASE_MEDIUM}. A triangular glass prism on a dark velvet surface refracts a single ray of sunlight into a brilliant subtle spectrum. Marcus Aurelius wisdom: events do not disturb us, our judgment does. {BASE_SAFE_ZONE}."
        }
    ],
    # 115 - THANH THẢN (2 slides)
    "TXT-0115": [
        {
            "slide": 1,
            "role": "Hook: Đám rơm bùng cháy dữ dội rồi tàn lụi",
            "concept": "Đống rơm khô bùng cháy ngọn lửa lớn trong bóng đêm",
            "prompt": f"{BASE_MEDIUM}. A dramatic flare of dry straw burning intensely with crackling sparks against black night, quickly turning to ash. Fleeting emotional reactivity, shallow excitement. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Hòn than âm ỉ giữ nhiệt suốt mùa đông",
            "concept": "Khối than hồng đượm ấm áp tỏa nhiệt sâu trong lò sưởi",
            "prompt": f"{BASE_MEDIUM}. Deep, steady glowing coals in a cast-iron hearth, radiating enduring gentle warmth across a stone hearth. Quiet resilience, unshakeable equanimity. {BASE_SAFE_ZONE}."
        }
    ],
    # 116 - THANH THẢN (1 slide)
    "TXT-0116": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Dòng sông êm đềm uốn lượn qua thung lũng xanh ngát",
            "prompt": f"{BASE_MEDIUM}. A peaceful winding river flowing effortlessly through a lush emerald valley beneath soft afternoon clouds. Constable landscape aesthetic. Acceptance of natural flow, non-resistance. {BASE_SAFE_ZONE}."
        }
    ],
    # 117 - KIÊN CƯỜNG (2 slides)
    "TXT-0117": [
        {
            "slide": 1,
            "role": "Hook: Cơn sóng thần ập vào bờ đá",
            "concept": "Ngọn sóng biển dữ dội chồm lên mỏm đá nhọn",
            "prompt": f"{BASE_MEDIUM}. A ferocious ocean swell cresting against dark jagged coastal crags under stormy overcast skies. Raw primal power of life's unpredictable shocks. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Twist: Mỏm đá ngàn năm vẫn trơ gan cùng tuế nguyệt",
            "concept": "Mỏm đá granite sừng sững sau khi sóng tan thành bọt trắng",
            "prompt": f"{BASE_MEDIUM}. The same solid granite cliff standing unchanged and immovable, seafoam draining silently back into deep blue waters under breaking sunbeams. Invincible character forged by trials. {BASE_SAFE_ZONE}."
        }
    ],
    # 118 - KIÊN CƯỜNG (1 slide)
    "TXT-0118": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Giọt nước bền bỉ chảy mòn tảng đá cứng",
            "prompt": f"{BASE_MEDIUM}. A steady, crystalline stream of water carving a smooth groove through solid ancient river rock over centuries. Lao Tzu truth: the softest overcomes the hardest. Deep persistent resilience. {BASE_SAFE_ZONE}."
        }
    ],
    # 119 - KIÊN CƯỜNG (3 slides)
    "TXT-0119": [
        {
            "slide": 1,
            "role": "Slide 1: Hiện tượng - Vết thương rỉ máu và sự vụn vỡ",
            "concept": "Chiếc bình gốm cổ vỡ đôi trên nền đá",
            "prompt": f"{BASE_MEDIUM}. A fractured ancient ceramic vessel cracked in two upon a weathered stone flagstone, dramatic side lighting highlighting the sharp split. Trauma, raw heartbreak, vulnerability. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 2,
            "role": "Slide 2: Căn nguyên - Nghệ thuật hàn gắn bằng vàng (Kintsugi)",
            "concept": "Bàn tay nghệ nhân tỉ mỉ gắn các mảnh vỡ bằng sơn mài vàng ròng",
            "prompt": f"{BASE_MEDIUM}. Skilled hands of a master artisan applying luminous gold lacquer to repair the ceramic fracture in warm workshop lamplight. Wounds becoming the source of golden strength. {BASE_SAFE_ZONE}."
        },
        {
            "slide": 3,
            "role": "Slide 3: Chiếc gương - Tác phẩm hồi sinh đẹp hơn xưa",
            "concept": "Chiếc bình hàn vàng Kintsugi tỏa sáng kiêu hãnh trên bệ gỗ",
            "prompt": f"{BASE_MEDIUM}. The completed Kintsugi ceramic vase standing proudly on a polished wooden pedestal, shimmering gold veins running through porcelain like sacred scars. More beautiful and resilient because of its fractures. {BASE_SAFE_ZONE}."
        }
    ],
    # 120 - KIÊN CƯỜNG (1 slide)
    "TXT-0120": [
        {
            "slide": 1,
            "role": "Single-Punch",
            "concept": "Thỏi thép rực lửa trên đe rèn của người thợ rèn",
            "prompt": f"{BASE_MEDIUM}. A glowing orange steel billet on an iron blacksmith's anvil, sparks frozen in mid-air under dramatic furnace chiaroscuro. 'Lửa thử vàng, gian nan thử sức'. Unbreakable spirit hammered into greatness. {BASE_SAFE_ZONE}."
        }
    ]
}

# Save prompt manifest JSON
with open('scripts/oil_suites_prompts_manifest.json', 'w', encoding='utf-8') as f:
    json.dump(PROMPT_DEFINITIONS, f, ensure_ascii=False, indent=2)

print(f"Generated manifest for {len(PROMPT_DEFINITIONS)} posts with {sum(len(v) for v in PROMPT_DEFINITIONS.values())} total slides!")

# Build markdown specification document
spec_md = []
spec_md.append("# HIYU ABYSS — ĐẶC TẢ MỸ THUẬT SƠN DẦU (HYA-08)")
spec_md.append("## HỆ THỐNG 30 BỘ ẢNH NGHỆ THUẬT ĐA TÁC PHẨM (SUITES 91–120)")
spec_md.append("")
spec_md.append("> **Mã quy chuẩn:** `HYA-08`  ")
spec_md.append("> **Căn cứ pháp quy:** Bổ sung trực tiếp vào chuỗi quy chuẩn `HYA-01` $\\\\rightarrow$ `HYA-07`.  ")
spec_md.append("> **Tuyên ngôn tư duy:** *Chấm dứt hoàn toàn trò crop/zoom từ một bức tranh duy nhất. Mỗi slide là một kiệt tác sơn dầu độc lập, kết nối bằng dòng chảy triết học và tâm lý học.*  ")
spec_md.append("> **Phạm vi dữ liệu:** 30 bài đăng từ dòng 91 đến 120 trên Google Sheet (`TXT-0091` $\\\\rightarrow$ `TXT-0120`).  ")
spec_md.append("")
spec_md.append("---")
spec_md.append("")
spec_md.append("## 1. Cương Lĩnh Mỹ Thuật & Công Thức Cốt Lõi (The Master Oil Formula)")
spec_md.append("")
spec_md.append("Mọi prompt sinh ảnh trong hệ thống đều tuân thủ cấu trúc 5 tầng chuẩn mực:")
spec_md.append("")
spec_md.append("$$\\\\text{Prompt} = \\\\text{Aspect Ratio (9:16)} + \\\\text{Medium & Texture} + \\\\text{Subject & Metaphor} + \\\\text{Lighting & Palette} + \\\\text{Text Safe Zone Composition}$$")
spec_md.append("")
spec_md.append("1. **Medium & Texture (Chất liệu cốt lõi):**  ")
spec_md.append("   `Vertical 9:16 classical fine art oil painting, authentic visible heavy impasto brushstrokes, tactile canvas weave texture, rich oil glazes.`")
spec_md.append("2. **Text Safe Zone (Vùng an toàn chèn chữ):**  ")
spec_md.append("   `Spacious, quiet negative space in the middle-to-lower third with subdued painterly shadows, strictly clean with NO text, NO watermarks, NO signatures, NO digital CGI rendering.`")
spec_md.append("3. **Lighting & Color Calibrations (Bảng màu theo 5 nhóm chủ đề):**  ")
spec_md.append("   - **SOLITUDE (91–95):** Ánh nến vàng hổ phách ấm áp (`warm candlelit glow`, `deep indigo and amber`), thư phòng cổ, tĩnh vật đêm tĩnh mịch.")
spec_md.append("   - **STATUS (96–100):** Vàng mạ rạn nứt (`tarnished cracked gold leaf`, `crumbling baroque halls`, `deep velvet crimson and bronze`).")
spec_md.append("   - **RANH GIỚI (101–108):** Tường đá cổ phủ rêu, cổng sắt rèn trong sương mù (`mossy stone boundary walls`, `ancient iron gate in mist`, `slate and forest tones`).")
spec_md.append("   - **THANH THẢN (109–116):** Hồ nước phẳng lặng, bàn gỗ ngập nắng mai (`mirror-still lake`, `sun-drenched oak desk`, `warm earth and sage ochre`).")
spec_md.append("   - **KIÊN CƯỜNG (117–120):** Mầm xanh vượt đá tảng, cây cổ thụ trước bão giông (`green shoot breaking granite rock`, `cliffside ancient pine in tempest`, `raw umber and fiery embers`).")
spec_md.append("")
spec_md.append("---")
spec_md.append("")
spec_md.append("## 2. Bảng Phân Bổ 30 Bộ Ảnh (51 Tranh Sơn Dầu Độc Bản)")
spec_md.append("")
spec_md.append("| STT | Mã ID | Chủ Đề Hạt Nhân | Định Dạng Slide | Số Tranh | Ý Niệm Thị Giác & Ẩn Dụ Sơn Dầu |")
spec_md.append("|:---:|:---:|---|:---:|:---:|---|")

for p in posts:
    stt = p['stt']
    mid = p['id']
    theme = p['theme'].split('(')[0].strip()
    fmt = p['format']
    slides = PROMPT_DEFINITIONS.get(mid, [])
    concepts = ' $\\rightarrow$ '.join([f"S{s['slide']}: {s['concept']}" for s in slides])
    spec_md.append(f"| {stt} | `{mid}` | **{theme}** | {fmt} | **{len(slides)}** | {concepts} |")

spec_md.append("")
spec_md.append("---")
spec_md.append("")
spec_md.append("## 3. Đặc Tả Chi Tiết Prompt Từng Bài (30 Bộ x 51 Slides)")
spec_md.append("")

for p in posts:
    mid = p['id']
    stt = p['stt']
    title = p['title']
    author = p['author']
    theme = p['theme']
    fmt = p['format']
    slides = PROMPT_DEFINITIONS.get(mid, [])
    
    spec_md.append(f"### Bài {stt} — `{mid}`: {title}")
    spec_md.append(f"- **Chủ đề:** {theme}")
    spec_md.append(f"- **Nguồn tư tưởng:** {author}")
    spec_md.append(f"- **Định dạng:** {fmt} ({len(slides)} slide sơn dầu độc lập)")
    spec_md.append("")
    
    for s in slides:
        s_num = s['slide']
        role = s['role']
        concept = s['concept']
        prompt = s['prompt']
        spec_md.append(f"#### Slide {s_num} — {role}")
        spec_md.append(f"- **Visual Concept:** {concept}")
        spec_md.append(f"- **Master Prompt:**")
        spec_md.append(f"  ```text\n  {prompt}\n  ```")
        spec_md.append("")
    spec_md.append("---")
    spec_md.append("")

with open('docs/08_HIYU_ABYSS_OIL_PAINTING_SUITES_SPEC.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(spec_md))

print("Created docs/08_HIYU_ABYSS_OIL_PAINTING_SUITES_SPEC.md successfully!")
