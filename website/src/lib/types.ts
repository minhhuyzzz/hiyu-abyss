// types.ts - Cấu trúc dữ liệu Thư Viện Nghệ Thuật & The Mirror V3
export type QuoteType = 'DIRECT_QUOTE' | 'PARAPHRASE' | 'INSPIRED_ORIGINAL' | 'INDEPENDENT_ORIGINAL';

export type VerificationStatus = 
  | 'VERIFIED_SOURCE'         // Đã đối chiếu ấn bản, số trang/chương cụ thể
  | 'PENDING_VERIFICATION'    // Đang đối chiếu tài liệu ấn bản gốc
  | 'INSPIRED_ORIGINAL'       // Sáng tác lấy cảm hứng từ tư tưởng
  | 'INDEPENDENT_ORIGINAL';   // Đúc kết sáng tác độc lập Hiyu Abyss

export interface ScholarlySource {
  work?: string;               // Tên tác phẩm / ấn bản gốc
  work_original?: string;      // Tên tác phẩm theo ngôn ngữ gốc
  location?: string;           // Vị trí (chương, đoạn, trang, số hiệu châm ngôn)
  source_url?: string;         // URL đối chiếu bản in số hóa (Gutenberg, BnF Gallica, Archive.org...)
  original_text?: string;      // Câu nguyên tác (tiếng Pháp, Đức, Hy Lạp, Anh...)
  translation_note?: string;   // Ghi chú dịch thuật
  verification_status: VerificationStatus;
  verified_at?: string;        // Ngày kiểm chứng
}

export type ArtworkProvenanceType = 
  | 'ORIGINAL_MUSEUM_SCAN'        // Ảnh chụp/scan nguyên bản từ bảo tàng
  | 'TRANSFORMED_PUBLIC_DOMAIN'    // Tranh cổ điển Public Domain chuẩn hóa bố cục 9:16 & thớ toan hữu cơ (HYA-08)
  | 'COMMISSIONED_DERIVATIVE'      // Tác phẩm phái sinh/sáng tác nội bộ của dự án
  | 'HISTORICAL_DOCUMENT';         // Bản khắc, tài liệu cổ

export interface ArtMasterpiece {
  art_id: string;
  title: string;
  title_original?: string;
  artist: string;
  year: string;
  museum: string;
  license: string;
  provenance_type?: ArtworkProvenanceType;
  source_institution_url?: string;
  curation_note?: string;
  alt_vi: string;
  slides: {
    slide_1: string;
    slide_2: string;
    slide_3: string;
  };
}

export interface PublicQuote {
  id: string;
  slug: string;
  title: string;
  cleanTitle: string;
  intentBadge?: string;
  content: string;
  description: string;
  author: string;
  quoteType: QuoteType;
  quoteTypeLabel: string;
  scholarlySource?: ScholarlySource;
  topicCodes: string[];
  primaryTopic: string;
  primaryTopicTitle: string;
  imageRef: string;
  artInfo?: ArtMasterpiece;
  slides: {
    slide_1: string;
    slide_2: string;
    slide_3: string;
    slide_4: string;
  };
  slideFormat: string;
  isFeatured: boolean;
  publishedAt: string;
}

export interface TopicDefinition {
  code: string;
  slug: string;
  title: string;
  description: string;
  count: number;
}

// ==========================================
// THE MIRROR V3: DIRECTED SCENE GRAPH ENGINE
// ==========================================
export type SceneNodeType = 'intro' | 'statement' | 'choice' | 'counterpoint' | 'ending';

export interface SceneChoice {
  id: string;
  label: string;
  to: string;
  editorialIntent?: string;
}

export interface SceneNode {
  type: SceneNodeType;
  title: string;
  body?: string;
  scenePreset?: string;
  motionPreset?: string;
  artwork_ref?: string;
  artwork_title?: string;
  artwork_artist?: string;
  closingQuestion?: string;
  relatedTopic?: string;
  choices?: SceneChoice[];
  next?: string;
}

// Backwards compatibility choice structure for V2
export interface MirrorChoice {
  id: string;
  label: string;
  reflection_text: string;
  reflection_subtext?: string;
  artwork_ref?: string;
}

export interface MirrorStepCounterpoint {
  text: string;
  subtext?: string;
  question: string;
}

export interface MirrorStepOpenEnding {
  prompt: string;
  closing_note: string;
  related_topics: { code: string; title: string; slug: string }[];
  suggested_quotes?: string[];
}

export interface MirrorJourneyData {
  id: string;
  slug: string;
  version?: number;
  status?: string;
  title: string;
  subtitle: string;
  artwork_id?: string;
  artwork_url?: string;
  artwork_title?: string;
  artwork_artist?: string;
  estimated_minutes?: number;
  entry?: string;
  nodes?: Record<string, SceneNode>;

  // Legacy V2 fields (optional fallback)
  intro?: {
    lead: string;
    description: string;
    button_label: string;
  };
  question?: {
    prompt: string;
    context?: string;
    choices: MirrorChoice[];
  };
  counterpoint?: MirrorStepCounterpoint;
  open_ending?: MirrorStepOpenEnding;
}
