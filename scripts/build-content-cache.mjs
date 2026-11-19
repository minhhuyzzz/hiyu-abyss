// scripts/build-content-cache.mjs
// Pre-compiles markdown content files into static JSON cache for instant, zero-I/O Cloudflare Workers execution.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import yaml from '../website/node_modules/js-yaml/index.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..');
const manifestPath = path.resolve(rootDir, 'website/publication-manifest.yaml');
const contentDir = path.resolve(rootDir, 'editorial/content');
const journeysDir = path.resolve(rootDir, 'website/journeys');
const artCatalogPath = path.resolve(rootDir, 'website/src/data/asset-catalog.json');
const outputQuotesPath = path.resolve(rootDir, 'website/src/data/published-quotes.json');
const outputJourneysPath = path.resolve(rootDir, 'website/src/data/published-journeys.json');

const TOPIC_NAMES = {
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
  COMMUNICATION: { title: 'Giao Tiếp & Thấu Cảm', desc: 'Nghệ thuật đối thoại chân thành, tháo gỡ hiểu lầm và vượt qua sự thoái thác cảm xúc.' },
  EXPECTATION: { title: 'Kỳ Vọng & Thất Vọng', desc: 'Nhìn nhận khoảng cách giữa kỳ vọng chủ quan và thực tế đời sống.' },
  ATTRACTION: { title: 'Sức Hút & Tâm Lý Tình Cảm', desc: 'Khám phá các quy luật tâm lý trong sự thu hút, gắn bó và ranh giới tình cảm.' },
  SELF_COMPASSION: { title: 'Tự Trắc Ẩn & Bao Dung', desc: 'Học cách hòa giải với chính mình và tha thứ cho những bất toàn nội tâm.' },
  STOIC_SERENITY: { title: 'Khắc Kỷ & Định Tâm', desc: 'Bình thản trước nghịch cảnh và tập trung vào những điều ta có thể kiểm soát.' },
  AUTHENTIC_CONNECTION: { title: 'Gắn Kết Chân Thật', desc: 'Xây dựng những mối quan hệ sâu sắc không vụ lợi hay giả tạo.' },
  MEANING_RESILIENCE: { title: 'Lẽ Sống & Phục Hồi', desc: 'Vượt qua chông gai, tìm kiếm ý nghĩa và thắp sáng nội lực bản thân.' },
};

const QUOTE_TYPE_LABELS = {
  DIRECT_QUOTE: 'Trích dẫn nguyên văn',
  PARAPHRASE: 'Diễn giải & Biên soạn',
  INSPIRED_ORIGINAL: 'Lấy cảm hứng từ ý tưởng',
  INDEPENDENT_ORIGINAL: 'Đúc kết Hiyu Abyss',
};

const artCatalog = fs.existsSync(artCatalogPath) ? JSON.parse(fs.readFileSync(artCatalogPath, 'utf8')) : {};
const manifest = fs.existsSync(manifestPath) ? yaml.load(fs.readFileSync(manifestPath, 'utf8')) : {};

const publicIds = manifest.public_content_ids || [];
const featuredIds = manifest.featured_content_ids || [];

const quotes = [];

for (const id of publicIds) {
  const filePath = path.join(contentDir, `${id}.md`);
  if (!fs.existsSync(filePath)) continue;

  const fileContent = fs.readFileSync(filePath, 'utf-8');
  const match = fileContent.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/);
  if (!match) continue;

  const frontmatter = yaml.load(match[1]) || {};
  const body = match[2];

  const status = frontmatter?.status?.toUpperCase();
  if (status !== 'APPROVED' && status !== 'PUBLISHED' && status !== 'SẴN SÀNG' && status !== 'READY') {
    continue;
  }

  const quoteMatch = body.match(/^>\s*(.+)$/m);
  const content = quoteMatch ? quoteMatch[1].trim() : frontmatter?.title || '';

  const descMatch = body.match(/## Diễn Giải & Chiêm Nghiệm Biên Tập\r?\n([\s\S]*?)(?=\r?\n##|$)/);
  const description = descMatch ? descMatch[1].trim() : '';

  const s1Match = body.match(/- \*\*Trang 1 \(Hook\):\*\* (.+)$/m);
  const s2Match = body.match(/- \*\*Trang 2 \(Cú lật\):\*\* (.+)$/m);
  const s3Match = body.match(/- \*\*Trang 3 \(Phản tư\):\*\* (.+)$/m);
  const s4Match = body.match(/- \*\*Trang 4 \(Đúc kết\):\*\* (.+)$/m);

  const rawTitle = frontmatter?.title || '';
  let cleanTitle = rawTitle;
  let intentBadge = '';
  const bracketMatch = rawTitle.match(/^\[(.*?)\]\s*(.*)$/);
  if (bracketMatch) {
    intentBadge = bracketMatch[1];
    cleanTitle = bracketMatch[2];
  }

  const topicCodes = Array.isArray(frontmatter?.topic_codes) ? frontmatter.topic_codes : ['PSYCHOLOGY'];
  const primaryTopic = topicCodes[0] || 'PSYCHOLOGY';
  const primaryTopicTitle = TOPIC_NAMES[primaryTopic]?.title || primaryTopic;
  const quoteType = frontmatter?.content_type || 'PARAPHRASE';

  const imageRef = frontmatter?.image_ref || 'theme_01';
  const rawArt = artCatalog[imageRef];
  const artInfo = rawArt ? { ...rawArt, provenance_type: rawArt.provenance_type || 'TRANSFORMED_PUBLIC_DOMAIN' } : undefined;

  let verificationStatus = 'PENDING_VERIFICATION';
  if (quoteType === 'INSPIRED_ORIGINAL') {
    verificationStatus = 'INSPIRED_ORIGINAL';
  } else if (quoteType === 'INDEPENDENT_ORIGINAL') {
    verificationStatus = 'INDEPENDENT_ORIGINAL';
  } else if (frontmatter?.verification_status) {
    verificationStatus = frontmatter.verification_status;
  } else if (frontmatter?.source_work && frontmatter?.source_location && frontmatter?.source_url) {
    verificationStatus = 'VERIFIED_SOURCE';
  }

  const scholarlySource = {
    work: frontmatter?.source_work || undefined,
    work_original: frontmatter?.source_work_original || undefined,
    location: frontmatter?.source_location || undefined,
    source_url: frontmatter?.source_url || undefined,
    original_text: frontmatter?.original_text || undefined,
    translation_note: frontmatter?.translation_note || undefined,
    verification_status: verificationStatus,
    verified_at: frontmatter?.verified_at || undefined,
  };

  quotes.push({
    id,
    slug: id.toLowerCase(),
    title: rawTitle,
    cleanTitle,
    intentBadge,
    content,
    description,
    author: frontmatter?.author_attribution || 'Khuyết danh',
    quoteType,
    quoteTypeLabel: QUOTE_TYPE_LABELS[quoteType] || 'Chiêm nghiệm',
    scholarlySource,
    topicCodes,
    primaryTopic,
    primaryTopicTitle,
    imageRef,
    artInfo,
    slides: {
      slide_1: s1Match ? s1Match[1].trim() : '-',
      slide_2: s2Match ? s2Match[1].trim() : '-',
      slide_3: s3Match ? s3Match[1].trim() : '-',
      slide_4: s4Match ? s4Match[1].trim() : '-',
    },
    slideFormat: frontmatter?.slide_format || 'Carousel',
    isFeatured: featuredIds.includes(id),
    publishedAt: frontmatter?.created_at || '2026-11-14',
  });
}

// Journeys
const journeyIds = manifest.public_journey_ids || [];
const journeys = [];
for (const jid of journeyIds) {
  const jfile = path.join(journeysDir, `${jid}.yaml`);
  if (fs.existsSync(jfile)) {
    try {
      const jdata = yaml.load(fs.readFileSync(jfile, 'utf8'));
      if (jdata && jdata.id) journeys.push(jdata);
    } catch (e) {
      console.error(`Failed to parse journey ${jid}:`, e);
    }
  }
}

fs.writeFileSync(outputQuotesPath, JSON.stringify(quotes, null, 2), 'utf8');
fs.writeFileSync(outputJourneysPath, JSON.stringify(journeys, null, 2), 'utf8');
console.log(`[build-content-cache] Successfully compiled ${quotes.length} quotes and ${journeys.length} journeys to JSON!`);
