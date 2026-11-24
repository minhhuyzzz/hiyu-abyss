#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Applies compressed, audited text fixes to posts 401-450
"""
import json

with open('scripts/posts_401_450.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

for p in posts:
    pid = p['id']
    stt = p['stt']
    
    if stt == 407:
        p['twist'] = "Kỷ luật tài chính là cách bạn tôn trọng tương lai hơn những món đồ phù phiếm hôm nay."
    elif stt == 408:
        p['twist'] = "Bạn không hề tiết kiệm được nửa giá; bạn vừa ném đi số tiền còn lại cho thứ không cần thiết."
    elif stt == 410:
        p['id'] = "TXT-0410"
    elif stt == 412:
        p['twist'] = "Không phải đồ xa xỉ phô bày ra ngoài. Sự giàu có là khoản tiền chưa tiêu và sự an tâm trong giấc ngủ."
    elif stt == 413:
        p['twist'] = "Là trí tuệ của chính bạn. Thị trường biến động, nhưng năng lực độc bản là tài sản không ai tước đoạt nổi."
    elif stt == 418:
        p['caption'] = p['caption'].replace("không chỉ là con số trong tài khoản ngân hàng", "vượt xa một con số ngân hàng đơn thuần")
    elif stt == 419:
        p['twist'] = "Ví dày không thể chữa lành tâm hồn rỗng tuếch. Của cải nhiều không làm bạn trở thành con người vĩ đại."
    elif stt == 420:
        p['hook'] = "Tiền bạc là người đầy tớ trung thành, nhưng là ông chủ tàn nhẫn nhất nếu bạn để nó làm chủ."
        p['full_text'] = p['hook']
    elif stt == 421:
        p['twist'] = "Cảnh giác với tiếng vỗ tay nồng nhiệt. Kẻ tâng bốc bạn nhanh nhất cũng là kẻ đạp bạn đầu tiên khi ngã."
    elif stt == 422:
        p['twist'] = "Không có gì miễn phí trên đời. Món quà quá hời luôn kèm cái giá đắt đỏ đòi hỏi sự phục tùng."
    elif stt == 424:
        p['mirror'] = "Hành vi quá khứ là tấm gương chuẩn xác nhất phản chiếu bản chất thật mà không lời hứa nào che giấu nổi."
    elif stt == 425:
        p['twist'] = "Họ kể xấu người khác với bạn, thì cũng sẵn sàng đem bí mật của bạn đi rêu rao cho kẻ khác."
    elif stt == 428:
        p['twist'] = "Kẻ hèn chỉ hung hăng khi núp bóng bầy đàn. Sự hung tợn đó chỉ che giấu nỗi sợ đơn độc."
    elif stt == 430:
        p['twist'] = "Dao sắc giấu trong bao để không làm cùn lưỡi. Kẻ thích khoe khoang sự sắc sảo thường chuốc lấy tai họa."
    elif stt == 432:
        p['hook'] = "Lời xin lỗi lặp lại lần thứ ba là sự cố tình xem thường giới hạn của bạn."
        p['full_text'] = p['hook']
    elif stt == 433:
        p['mirror'] = "Kẻ châm ngòi thường đứng ngoài vỗ tay hòa giải. Nhận diện kẻ giật dây để không làm con tốt thí."
    elif stt == 434:
        p['twist'] = "Sĩ diện rỗng tuếch làm bạn kiệt quệ tài chính. Người khôn ngoan chỉ tập trung vào thực lực và sự an yên."
    elif stt == 437:
        p['twist'] = "Họ muốn bạn nổi giận để cướp đi sự sáng suốt. Nụ cười bình thản bẻ gãy mọi trò khiêu khích."
    elif stt == 438:
        p['hook'] = "Đừng cầu xin sự công bằng từ kẻ hưởng lợi bất công; hãy tự xây dựng thực lực để không ai chèn ép bạn."
        p['full_text'] = p['hook']
    elif stt == 439:
        p['twist'] = "Kẻ hay đóng vai nạn nhân thường là người bòn rút và đối xử tệ bạc nhất với người thân."
        p['mirror'] = "Họ đòi hỏi sự hy sinh nhưng không hề biết ơn. Giữ khoảng cách trước khi bạn bị vắt kiệt."
    elif stt == 441:
        p['twist'] = "Càng dễ dãi gật đầu, lòng tốt càng bị xem thường. Người ta sẽ mặc định sự hy sinh của bạn là nghĩa vụ."
    elif stt == 442:
        p['hook'] = "Sợ lập ranh giới sẽ mất bạn bè?......"
        p['twist'] = "Ranh giới không phải xây tường cô lập, mà là cánh cửa có khóa để bảo vệ sự bình yên của bạn."
    elif stt == 444:
        p['twist'] = "Giải thích dài dòng là mời họ thương lượng. Kẻ bòn rút luôn biết cách bẻ gãy mọi lý do của bạn."
    elif stt == 447:
        p['twist'] = "Mập mờ mới là thứ bóp chết tình bạn. Khi một bên ấm ức gánh chịu chi phí, sự tôn trọng đã tan biến."
    elif stt == 448:
        p['hook'] = "Bị hỏi dồn dập chuyện đời tư?......"
        p['twist'] = "Đừng cười gượng trả lời. Một nụ cười nhạt và câu chuyển đề tài sẽ buộc kẻ tò mò phải tự biết ngượng."

with open('scripts/posts_401_450.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("Applied fixes to scripts/posts_401_450.json successfully.")
