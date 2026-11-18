import type { PublicQuote, TopicDefinition, QuoteType, MirrorJourneyData, ScholarlySource, VerificationStatus } from './types';
import rawQuotes from '../data/published-quotes.json';
import rawJourneys from '../data/published-journeys.json';

const TOPIC_NAMES: Record<string, { title: string; desc: string }> = {
  HYPOCRISY: { title: 'Đạo Đức Giả & Giả Tạo', desc: 'Nhìn nhận sự khác biệt giữa lời nói đẹp đẽ và những toan tính thật sự bên trong.' },
  DOUBLE_STANDARD: { title: 'Tiêu Chuẩn Kép', desc: 'Sự bất công vi mô khi phán xét kẻ khác nghiêm khắc và nuông chiều chính mình.' },
  MORALITY: { title: 'Lòng Tốt & Điều Kiện Ngầm', desc: 'Khoản nợ ân tình độc hại và ranh giới của sự giúp đỡ chân thành.' },
  EGO: { title: 'Bản Ngã & Hơn Người', desc: 'Chiếc bẫy của nhu cầu luôn muốn mình đúng và vượt trội hơn kẻ khác.' },
  SELF_DECEPTION: { title: 'Tự Lừa Dối', desc: 'Vùng an toàn tâm lý giả tạo và cái giá của việc chối bỏ sự thật.' },
  SHADOW: { title: 'Bóng Tối Nội Tâm (Shadow)', desc: 'Góc khuất tâm hồn theo Carl Jung và hành trình hòa giải với phần tối.' },
  MASK: { title: 'Mặt Nạ Xã Hội', desc: 'Sự kiệt sức của việc gồng mình làm hài lòng kỳ vọng của đám đông.' },
  POWER: { title: 'Quyền Lực & Kiểm Soát', desc: 'Tâm lý học quyền lực ngầm và sự thao túng trong các mối quan hệ.' },
  MANIPULATION: { title: 'Thao Túng Cảm Xúc', desc: 'Chiếc bẫy tội lỗi (Guilt-trip), gaslighting và cách bảo vệ ranh giới.' },
  FREEDOM: { title: 'Tự Do & Tự Chủ', desc: 'Hiểu về quyền tự do đích thực và dũng cảm chịu trách nhiệm cho cuộc đời mình.' },
  TRUTH: { title: 'Sự Thật Mất Lòng', desc: 'Sức mạnh của việc đối diện sự thật trần trụi thay vì lời dối gian êm tai.' },
  LOVE: { title: 'Tình Yêu Trưởng Thành', desc: 'Phân định giữa sự chiếm hữu ích kỷ và tình yêu đích thực giữa hai tâm hồn độc lập.' },
  LOYALTY: { title: 'Lòng Trung Thành', desc: 'Ranh giới giữa sự tận tụy đáng quý và lòng trung thành mù quáng tự hủy hoại.' },
  ENVY: { title: 'Đố Kỵ Ngầm', desc: 'Chiếc bẫy so sánh và sự ghen tị âm ỉ làm xói mòn bình yên nội tại.' },
  CROWD: { title: 'Tâm Lý Đám Đông', desc: 'Hiệu ứng bầy đàn và dũng khí giữ vững tư duy độc lập trước số đông.' },
  SUFFERING: { title: 'Vượt Lên Nghịch Cảnh', desc: 'Tâm lý nạn nhân và sức mạnh phục hồi để trưởng thành sau thương đau.' },
  IDENTITY: { title: 'Bản Sắc Cá Nhân', desc: 'Bạn là ai khi ở một mình và không có bất kỳ ai quan sát.' },
  MEANING: { title: 'Ý Nghĩa Cuộc Sống', desc: 'Tìm kiếm niềm tin và ý nghĩa sống giữa những giai đoạn chênh vênh.' },
  SOLITUDE: { title: 'Nghệ Thuật Cô Độc', desc: 'Sự tĩnh lặng nuôi dưỡng tâm hồn, phân biệt giữa cô đơn và cô độc lành mạnh.' },
  STATUS: { title: 'Danh Vọng & Khiêm Nhường', desc: 'Bản chất của sự thừa nhận xã hội và trò trình diễn khiêm tốn giả tạo.' },
  BOUNDARIES: { title: 'Ranh Giới Cá Nhân', desc: 'Thiết lập ranh giới lành mạnh và dũng khí bảo vệ sự độc lập nội tâm.' },
  SERENITY: { title: 'Thanh Thản & Tĩnh Lặng', desc: 'Bình yên vững chãi trước những biến động và áp lực đời sống.' },
  RESILIENCE: { title: 'Kiên Cường & Nghị Lực', desc: 'Sức mạnh phục hồi và sự trưởng thành sau đau thương.' },
  CONNECTION: { title: 'Kết Nối & Tình Bạn', desc: 'Nghệ thuật thấu cảm và những mối quan hệ chân thành, sâu sắc.' },
  TRANSCENDENCE: { title: 'Vượt Lên Phán Xét', desc: 'Thoát khỏi chiếc lồng công nhận của miệng đời và ánh nhìn số đông.' },
  EXISTENCE: { title: 'Lẽ Sống & Lựa Chọn', desc: 'Học cách chấp nhận thực tế và can đảm đưa ra những lựa chọn cho bản thân.' },
  BAD_FAITH: { title: 'Trốn Tránh Trách Nhiệm', desc: 'Nhìn nhận thói quen đổ lỗi cho hoàn cảnh để không phải thay đổi.' },
  BIAS: { title: 'Thiên Kiến & Tự Biện Hộ', desc: 'Những chiếc bẫy nhận thức và sự ngụy biện xoa dịu bản ngã.' },
  PSYCHOLOGY: { title: 'Tâm Lý Con Người', desc: 'Khám phá những cơ chế tâm lý điều hướng hành vi trong cuộc sống.' },
};

const quotes: PublicQuote[] = rawQuotes as PublicQuote[];
const journeys: MirrorJourneyData[] = rawJourneys as MirrorJourneyData[];

export function getAllPublishedQuotes(): PublicQuote[] {
  return quotes;
}

export function getQuoteBySlug(slug: string): PublicQuote | undefined {
  return quotes.find((q) => q.slug === slug.toLowerCase() || q.id.toLowerCase() === slug.toLowerCase());
}

export function getFeaturedQuotes(): PublicQuote[] {
  return quotes.filter((q) => q.isFeatured);
}

export function getAllTopics(): TopicDefinition[] {
  const counts: Record<string, number> = {};

  for (const q of quotes) {
    for (const code of q.topicCodes) {
      counts[code] = (counts[code] || 0) + 1;
    }
  }

  return Object.keys(counts).map((code) => ({
    code,
    slug: code.toLowerCase().replace(/_/g, '-'),
    title: TOPIC_NAMES[code]?.title || code,
    description: TOPIC_NAMES[code]?.desc || `Các tác phẩm chiêm nghiệm thuộc dòng chủ đề ${code}`,
    count: counts[code],
  }));
}

export function getQuotesByTopic(topicCode: string): PublicQuote[] {
  const upper = topicCode.toUpperCase().replace(/-/g, '_');
  return quotes.filter((q) => q.topicCodes.map((c) => c.toUpperCase()).includes(upper));
}

export function getRandomQuote(): PublicQuote {
  const idx = Math.floor(Math.random() * quotes.length);
  return quotes[idx];
}

export function getPublicJourneys(): MirrorJourneyData[] {
  return journeys;
}

export function getJourneyBySlug(slug: string): MirrorJourneyData | undefined {
  return journeys.find((j) => j.slug === slug || j.id.toLowerCase() === slug.toLowerCase());
}
