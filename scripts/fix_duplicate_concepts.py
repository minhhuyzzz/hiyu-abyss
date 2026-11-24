import json

with open('scripts/posts_451_500.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

for p in posts:
    if p['stt'] == 487:
        p['concept'] = "Bộ 3 tranh sơn dầu: Slide 1: Jean-Léon Gérôme - Sư tử trầm mặc trong hoàng cung cổ kính với ánh nhìn thấu suốt | Slide 2: Thomas Gainsborough - Dáng đứng kiên định điềm tĩnh tuyệt đối trong y phục thanh lịch | Slide 3: Caspar David Friedrich - Cây sồi cổ thụ ngàn năm sừng sững giữa trời tuyết bao la"
    elif p['stt'] == 493:
        # Was: Slide 2: Camille Corot - Dòng nước trong veo soi bóng rặng liễu rủ
        p['concept'] = "Bộ 3 tranh sơn dầu: Slide 1: Odilon Redon - Đôi mắt chiêm niệm tĩnh mịch giữa màn đêm huyền ảo | Slide 2: Gustave Caillebotte - Mặt sông Yerres êm đềm đón những giọt mưa rào mùa hạ trong trẻo | Slide 3: Vilhelm Hammershøi - Khung cửa ngập tràn ánh nắng thanh bình của sớm mai"
    elif p['stt'] == 500:
        p['concept'] = "Bộ 4 tranh sơn dầu: Slide 1: Rembrandt - Cối xay gió cổ kính sừng sững trong hoàng hôn bão tố | Slide 2: J.M.W. Turner - Con tàu huyền thoại kiêu hãnh lướt sóng về phía ánh hoàng hôn vàng son | Slide 3: Claude Monet - Cây cầu gỗ uốn cong giữa đầm hoa súng thanh tịnh ngập tràn nắng mai | Slide 4: Frederic Edwin Church - Thung lũng Andes tráng lệ đón luồng ánh sáng thần thánh chiếu rọi muôn loài"

with open('scripts/posts_451_500.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("Fixed duplicate concepts in scripts/posts_451_500.json.")
