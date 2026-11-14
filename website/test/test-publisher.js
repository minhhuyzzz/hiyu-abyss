import { getAllPublishedQuotes, getAllTopics, getFeaturedQuotes } from '../src/lib/content-publisher.ts';

console.log('[*] Đang kiểm tra Content Publisher Adapter...');
const quotes = getAllPublishedQuotes();
console.log(`[✓] Tổng số tác phẩm đã phê duyệt xuất bản: ${quotes.length} / 100`);

if (quotes.length !== 100) {
  console.error(`[!] LỖI: Dự kiến 100 bài nhưng nhận được ${quotes.length}`);
  process.exit(1);
}

const topics = getAllTopics();
console.log(`[✓] Tổng số chủ đề mở trích xuất được: ${topics.length}`);
topics.forEach(t => console.log(`   - ${t.title} (${t.code}): ${t.count} tác phẩm`));

const featured = getFeaturedQuotes();
console.log(`[✓] Số tác phẩm tiêu biểu (Featured): ${featured.length}`);

// Sample check row 0
const q0 = quotes[0];
console.log(`[✓] Mẫu tác phẩm đầu tiên: ${q0.id} - ${q0.cleanTitle}`);
console.log(`    Tác giả: ${q0.author} | Loại: ${q0.quoteTypeLabel} | Phôi: ${q0.imageRef}`);
if (q0.artInfo) {
  console.log(`    Tranh bảo tàng: "${q0.artInfo.title}" - ${q0.artInfo.artist} (${q0.artInfo.museum})`);
}

console.log('[✓] CHECKPOINT 2 ĐẠT CHUẨN 100%!');
