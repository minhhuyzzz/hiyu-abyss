#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

with open('scripts/posts_451_500.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

for p in posts:
    stt = p['stt']
    if stt == 452:
        p['twist'] = "Sự bực dọc là vấn đề của họ. Bạn không có nghĩa vụ làm vật tế thần cho sự cáu kỉnh của người khác."
    elif stt == 454:
        p['hook'] = "Tha thứ có đồng nghĩa nối lại quan hệ?......"
    elif stt == 458:
        p['twist'] = "Ngọt ngào giả tạo là thuốc độc. Lời từ chối thẳng thắn giúp cả hai bên không lãng phí thời gian."
    elif stt == 460:
        p['twist'] = "Họ không cần giải pháp; họ cần sự chú ý. Bạn sẽ sớm trở thành kẻ có lỗi trong mắt họ."
    elif stt == 465:
        p['hook'] = "Sợ một mình nên cam chịu độc hại?......"
        p['twist'] = "Ở cạnh kẻ vô tâm còn cô đơn gấp bội. Đừng để nỗi sợ thành chiếc xích giam cầm cuộc đời."
    elif stt == 466:
        p['hook'] = "Đứa trẻ bên trong bạn không cần tán dương giả tạo; nó cần bạn đủ dũng cảm để bảo vệ nó."
        p['full_text'] = p['hook']
    elif stt == 467:
        p['hook'] = "Sợ cô đơn nên luôn tìm đám đông?......"
        p['twist'] = "Ngồi giữa đám đông giả tạo chỉ thêm trống rỗng. Cô đơn chất lượng cao giúp bạn tìm lại chính mình."
        p['mirror'] = "Dành thời gian cho nội tâm. Khi hòa giải với chính mình, sự cô đơn sẽ trở thành sức mạnh."
    elif stt == 470:
        p['twist'] = "Ảo tưởng bận rộn ru ngủ bạn. Nghỉ ngơi không phải tội lỗi; đó là quyền tái sinh tự nhiên."
        p['mirror'] = "Thả lỏng cơ thể. Bình yên không phải phần thưởng sau thành công, nó là điều kiện để sống trọn vẹn."
    elif stt == 476:
        p['twist'] = "Bất toàn là bản chất tự nhiên. Gồng mình hoàn hảo chỉ chuốc lấy sự kiệt quệ và giả tạo."
    elif stt == 479:
        p['mirror'] = "Dịu dàng vỗ về sau mỗi cú vấp. Đó là mảnh đất màu mỡ để lòng kiên cường nảy mầm."
    elif stt == 480:
        p['hook'] = "Bạn có giá trị vì chính sự tồn tại độc bản của mình, không cần chứng minh qua bất kỳ cúp danh vọng nào."
        p['full_text'] = p['hook']
    elif stt == 481:
        p['twist'] = "Sự nổi giận là thứ họ muốn. Nụ cười bình thản và đôi mắt tĩnh lặng sẽ biến trò khiêu khích thành trò hề."
    elif stt == 482:
        p['twist'] = "Buông bỏ điều ngoài tầm với. Dồn toàn lực cho suy nghĩ và hành động của chính mình để tìm tự do."
    elif stt == 484:
        p['twist'] = "Dừng lại 3 giây hít sâu. Đừng để một phút bốc đồng phá hủy toàn bộ thành quả bấy lâu."
    elif stt == 485:
        p['hook'] = "Gặp nghịch cảnh và than trách số phận?......"
    elif stt == 487:
        p['twist'] = "Họ không cần khoe mẽ cơ bắp. Sự điềm đạm, đôi mắt thấu suốt và kết quả là minh chứng lớn nhất."
    elif stt == 489:
        p['hook'] = "Đừng để lời khen làm bạn say sưa, đừng để tiếng chê làm bạn gục ngã; giá trị nằm ở bên trong."
        p['full_text'] = p['hook']
    elif stt == 492:
        p['hook'] = "Nhận thức cái chết có thể đến bất cứ lúc nào là cách tốt nhất để sống đời trọn vẹn không tiếc nuối."
        p['full_text'] = p['hook']
    elif stt == 494:
        p['twist'] = "Vượt qua nỗi sợ bị phán xét. Khi không còn điều gì đe dọa được bạn, bạn nắm trong tay tự do."
    elif stt == 496:
        p['twist'] = "Đổ lỗi biến bạn thành kẻ bất lực. Dám nhận trách nhiệm cho đời mình là bước ngoặt trưởng thành."
    elif stt == 497:
        p['hook'] = "Bi kịch ập đến và gục ngã?......"
        p['caption'] = p['caption'].replace("Không chỉ chịu đựng số phận mà hãy yêu thương lấy nó", "Hãy can đảm đón nhận và yêu thương lấy số phận")
    elif stt == 500:
        p['twist'] = "Đi qua bóng tối để không ngây thơ trước mưu mô, nhưng không để lòng mình chai sạn thành thù hận."
        p['mirror'] = "Dựng xây ranh giới thép bảo vệ nhân cách, nhưng luôn giữ trái tim ấm áp để yêu thương cuộc đời."

with open('scripts/posts_451_500.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("Applied fixes to scripts/posts_451_500.json successfully.")
