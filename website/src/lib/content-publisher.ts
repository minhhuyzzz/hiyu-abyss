import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import yaml from 'js-yaml';
import type { PublicQuote, TopicDefinition, QuoteType, MirrorJourneyData, ScholarlySource, VerificationStatus } from './types';
import artCatalog from '../data/asset-catalog.json';

// Resolving cross-platform relative paths with multiple candidate fallbacks
const currentDir = path.dirname(fileURLToPath(import.meta.url));

const possibleManifestPaths = [
  path.resolve(currentDir, '../../publication-manifest.yaml'),
  path.resolve(process.cwd(), 'publication-manifest.yaml'),
  path.resolve(process.cwd(), 'website/publication-manifest.yaml'),
];
const manifestPath = possibleManifestPaths.find((p) => fs.existsSync(p)) || possibleManifestPaths[0];

const possibleContentDirs = [
  path.resolve(currentDir, '../../../editorial/content'),
  path.resolve(process.cwd(), '../editorial/content'),
  path.resolve(process.cwd(), 'editorial/content'),
];
const contentDir = possibleContentDirs.find((p) => fs.existsSync(p)) || possibleContentDirs[0];

const possibleJourneysDirs = [
  path.resolve(currentDir, '../../journeys'),
  path.resolve(process.cwd(), 'journeys'),
  path.resolve(process.cwd(), 'website/journeys'),
];
const journeysDir = possibleJourneysDirs.find((p) => fs.existsSync(p)) || possibleJourneysDirs[0];

const TOPIC_NAMES: Record<string, { title: string; desc: string }> = {
  HYPOCRISY: { title: 'Đạo Đức Giả & Giả Tạo', desc: 'Bóc tách sự chênh lệch giữa lời nói hoa mỹ và động cơ trục lợi ẩn giấu.' },
  DOUBLE_STANDARD: { title: 'Tiêu Chuẩn Kép', desc: 'Sự bất công vi mô khi phán xét kẻ khác nghiêm khắc và nuông chiều chính mình.' },
  MORALITY: { title: 'Lòng Tốt & Điều Kiện Ngầm', desc: 'Khoản nợ ân tình độc hại và ranh giới của sự giúp đỡ chân thành.' },
  EGO: { title: 'Bản Ngã & Hơn Người', desc: 'Chiếc bẫy của nhu cầu luôn muốn mình đúng và vượt trội hơn kẻ khác.' },
  SELF_DECEPTION: { title: 'Tự Lừa Dối', desc: 'Vùng an toàn tâm lý giả tạo và cái giá của việc chối bỏ sự thật.' },
  SHADOW: { title: 'Bóng Tối Nội Tâm (Shadow)', desc: 'Góc khuất tâm hồn theo Carl Jung và hành trình hòa giải với phần tối.' },
  MASK: { title: 'Mặt Nạ Xã Hội', desc: 'Sự kiệt sức của việc gồng mình làm hài lòng kỳ vọng của đám đông.' },
  POWER: { title: 'Quyền Lực & Kiểm Soát', desc: 'Tâm lý học quyền lực ngầm và sự thao túng trong các mối quan hệ.' },
  MANIPULATION: { title: 'Thao Túng Cảm Xúc', desc: 'Chiếc bẫy tội lỗi (Guilt-trip), gaslighting và cách bảo vệ ranh giới.' },
  FREEDOM: { title: 'Tự Do Hiện Sinh', desc: 'Nghịch lý của tự do và nỗi sợ phải tự chịu trách nhiệm cho cuộc đời.' },
  TRUTH: { title: 'Sự Thật Mất Lòng', desc: 'Sức mạnh của việc đối diện sự thật trần trụi thay vì lời dối gian êm tai.' },
  LOVE: { title: 'Tình Yêu Trưởng Thành', desc: 'Phân định giữa sự chiếm hữu ích kỷ và tình yêu đích thực giữa hai tâm hồn độc lập.' },
  LOYALTY: { title: 'Lòng Trung Thành', desc: 'Ranh giới giữa sự tận tụy đáng quý và lòng trung thành mù quáng tự hủy hoại.' },
  ENVY: { title: 'Đố Kỵ Ngầm', desc: 'Chiếc bẫy so sánh và sự ghen tị âm ỉ làm xói mòn bình yên nội tại.' },
  CROWD: { title: 'Tâm Lý Đám Đông', desc: 'Hiệu ứng bầy đàn và dũng khí giữ vững tư duy độc lập trước số đông.' },
  SUFFERING: { title: 'Vượt Lên Nghịch Cảnh', desc: 'Tâm lý nạn nhân và sức mạnh phục hồi để trưởng thành sau thương đau.' },
  IDENTITY: { title: 'Bản Sắc Cá Nhân', desc: 'Bạn là ai khi ở một mình và không có bất kỳ ai quan sát.' },
  MEANING: { title: 'Ý Nghĩa Cuộc Sống', desc: 'Vượt qua cảm giác trống rỗng hiện sinh theo tinh thần Viktor Frankl.' },
  SOLITUDE: { title: 'Nghệ Thuật Cô Độc', desc: 'Sự tĩnh lặng nuôi dưỡng tâm hồn, phân biệt giữa cô đơn và cô độc lành mạnh.' },
  STATUS: { title: 'Danh Vọng & Khiêm Nhường', desc: 'Bản chất của sự thừa nhận xã hội và trò trình diễn khiêm tốn giả tạo.' },
  BOUNDARIES: { title: 'Ranh Giới Cá Nhân', desc: 'Thiết lập ranh giới lành mạnh và dũng khí bảo vệ sự độc lập nội tâm.' },
  SERENITY: { title: 'Thanh Thản & Tĩnh Lặng', desc: 'Bình yên vững chãi trước những biến động và áp lực đời sống.' },
  RESILIENCE: { title: 'Kiên Cường & Nghị Lực', desc: 'Sức mạnh phục hồi và sự trưởng thành sau đau thương.' },
  CONNECTION: { title: 'Kết Nối & Tình Bạn', desc: 'Nghệ thuật thấu cảm và những mối quan hệ chân thành, sâu sắc.' },
  TRANSCENDENCE: { title: 'Vượt Lên Phán Xét', desc: 'Thoát khỏi chiếc lồng công nhận của miệng đời và ánh nhìn số đông.' },
  EXISTENCE: { title: 'Hiện Sinh & Lựa Chọn', desc: 'Sức bật nội tại và đối diện với những nghịch lý của sự tồn tại.' },
  BAD_FAITH: { title: 'Ngụy Tín (Bad Faith)', desc: 'Nỗi sợ tự do và cơ chế trốn tránh trách nhiệm cá nhân theo Jean-Paul Sartre.' },
  BIAS: { title: 'Thiên Kiến & Tự Biện Hộ', desc: 'Những chiếc bẫy nhận thức và sự ngụy biện xoa dịu bản ngã.' },
  PSYCHOLOGY: { title: 'Tâm Lý Học Hành Vi', desc: 'Khám phá những cơ chế tâm lý điều hướng hành vi con người.' },
};

const QUOTE_TYPE_LABELS: Record<QuoteType, string> = {
  DIRECT_QUOTE: 'Trích dẫn nguyên văn',
  PARAPHRASE: 'Diễn giải tư tưởng',
  INSPIRED_ORIGINAL: 'Sáng tác lấy cảm hứng',
  INDEPENDENT_ORIGINAL: 'Sáng tác Hiyu Abyss',
};

// Cache to prevent redundant filesystem reads
let cachedQuotes: PublicQuote[] | null = null;

function getManifestData(): any {
  if (fs.existsSync(manifestPath)) {
    const manifestContent = fs.readFileSync(manifestPath, 'utf-8');
    return (yaml.load(manifestContent) as any) || {};
  }
  return {};
}

function parseMarkdownFile(filePath: string): { frontmatter: any; body: string } {
  const fileContent = fs.readFileSync(filePath, 'utf-8');
  const match = fileContent.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/);
  if (!match) {
    return { frontmatter: {}, body: fileContent };
  }
  const frontmatter = yaml.load(match[1]) as any;
  const body = match[2];
  return { frontmatter, body };
}

export function getAllPublishedQuotes(): PublicQuote[] {
  if (cachedQuotes) return cachedQuotes;

  // 1. Read Manifest
  let publicIds: string[] = [];
  let featuredIds: string[] = [];

  if (fs.existsSync(manifestPath)) {
    const manifestContent = fs.readFileSync(manifestPath, 'utf-8');
    const parsed = yaml.load(manifestContent) as any;
    publicIds = parsed?.public_content_ids || [];
    featuredIds = parsed?.featured_content_ids || [];
  }

  // 2. Read Content Files
  const quotes: PublicQuote[] = [];

  for (const id of publicIds) {
    const filePath = path.join(contentDir, `${id}.md`);
    if (!fs.existsSync(filePath)) continue;

    const { frontmatter, body } = parseMarkdownFile(filePath);

    // GATE CHECK: Must be APPROVED, PUBLISHED, or SẴN SÀNG
    const status = frontmatter?.status?.toUpperCase();
    if (status !== 'APPROVED' && status !== 'PUBLISHED' && status !== 'SẴN SÀNG' && status !== 'READY') {
      continue;
    }

    // Extract content & commentary
    const quoteMatch = body.match(/^>\s*(.+)$/m);
    const content = quoteMatch ? quoteMatch[1].trim() : frontmatter?.title || '';

    const descMatch = body.match(/## Diễn Giải & Chiêm Nghiệm Biên Tập\r?\n([\s\S]*?)(?=\r?\n##|$)/);
    const description = descMatch ? descMatch[1].trim() : '';

    const s1Match = body.match(/- \*\*Trang 1 \(Hook\):\*\* (.+)$/m);
    const s2Match = body.match(/- \*\*Trang 2 \(Cú lật\):\*\* (.+)$/m);
    const s3Match = body.match(/- \*\*Trang 3 \(Phản tư\):\*\* (.+)$/m);
    const s4Match = body.match(/- \*\*Trang 4 \(Đúc kết\):\*\* (.+)$/m);

    // Parse clean title and intent badge
    const rawTitle = frontmatter?.title || '';
    let cleanTitle = rawTitle;
    let intentBadge = '';
    const bracketMatch = rawTitle.match(/^\[(.*?)\]\s*(.*)$/);
    if (bracketMatch) {
      intentBadge = bracketMatch[1];
      cleanTitle = bracketMatch[2];
    }

    const topicCodes: string[] = Array.isArray(frontmatter?.topic_codes)
      ? frontmatter.topic_codes
      : ['PSYCHOLOGY'];
    const primaryTopic = topicCodes[0] || 'PSYCHOLOGY';
    const primaryTopicTitle = TOPIC_NAMES[primaryTopic]?.title || primaryTopic;

    const quoteType: QuoteType = frontmatter?.content_type || 'PARAPHRASE';
    const imageRef = frontmatter?.image_ref || 'theme_01';
    const rawArt = (artCatalog as any)[imageRef];
    const artInfo = rawArt
      ? {
          ...rawArt,
          provenance_type: rawArt.provenance_type || 'TRANSFORMED_PUBLIC_DOMAIN',
        }
      : undefined;

    // Academic Rigor: Build ScholarlySource per HYA-02 (P0-01)
    let verificationStatus: VerificationStatus = 'PENDING_VERIFICATION';
    if (quoteType === 'INSPIRED_ORIGINAL') {
      verificationStatus = 'INSPIRED_ORIGINAL';
    } else if (quoteType === 'INDEPENDENT_ORIGINAL') {
      verificationStatus = 'INDEPENDENT_ORIGINAL';
    } else if (frontmatter?.verification_status) {
      verificationStatus = frontmatter.verification_status;
    } else if (frontmatter?.source_work && frontmatter?.source_location && frontmatter?.source_url) {
      verificationStatus = 'VERIFIED_SOURCE';
    } else {
      verificationStatus = 'PENDING_VERIFICATION';
    }

    const scholarlySource: ScholarlySource = {
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

  cachedQuotes = quotes;
  return cachedQuotes;
}

export function getQuoteBySlug(slug: string): PublicQuote | undefined {
  const all = getAllPublishedQuotes();
  return all.find((q) => q.slug === slug.toLowerCase() || q.id.toLowerCase() === slug.toLowerCase());
}

export function getFeaturedQuotes(): PublicQuote[] {
  const all = getAllPublishedQuotes();
  return all.filter((q) => q.isFeatured);
}

export function getAllTopics(): TopicDefinition[] {
  const quotes = getAllPublishedQuotes();
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
  const all = getAllPublishedQuotes();
  const upper = topicCode.toUpperCase().replace(/-/g, '_');
  return all.filter((q) => q.topicCodes.map((c) => c.toUpperCase()).includes(upper));
}

export function getRandomQuote(): PublicQuote {
  const all = getAllPublishedQuotes();
  const idx = Math.floor(Math.random() * all.length);
  return all[idx];
}

export function getPublicJourneys(): MirrorJourneyData[] {
  const manifest = getManifestData();
  const journeyIds = manifest.public_journey_ids || [];
  const journeys: MirrorJourneyData[] = [];

  for (const id of journeyIds) {
    const journeyFile = path.join(journeysDir, `${id}.yaml`);
    if (fs.existsSync(journeyFile)) {
      try {
        const raw = fs.readFileSync(journeyFile, 'utf-8');
        const data = yaml.load(raw) as MirrorJourneyData;
        if (data && data.id) {
          journeys.push(data);
        }
      } catch (e) {
        console.error(`Failed to parse journey ${id}:`, e);
      }
    }
  }

  return journeys;
}

export function getJourneyBySlug(slug: string): MirrorJourneyData | undefined {
  const journeys = getPublicJourneys();
  return journeys.find((j) => j.slug === slug || j.id.toLowerCase() === slug.toLowerCase());
}

