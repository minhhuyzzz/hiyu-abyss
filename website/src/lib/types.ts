// types.ts - Định nghĩa cấu trúc dữ liệu cho Thư Viện Nghệ Thuật Hiyu Abyss

export type QuoteType = 'DIRECT_QUOTE' | 'PARAPHRASE' | 'INSPIRED_ORIGINAL' | 'INDEPENDENT_ORIGINAL';

export interface ArtMasterpiece {
  art_id: string;
  title: string;
  artist: string;
  year: string;
  museum: string;
  license: string;
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
  title: string;
  subtitle: string;
  artwork_id?: string;
  artwork_url?: string;
  artwork_title?: string;
  artwork_artist?: string;
  estimated_minutes: number;
  intro: {
    lead: string;
    description: string;
    button_label: string;
  };
  question: {
    prompt: string;
    context?: string;
    choices: MirrorChoice[];
  };
  counterpoint: MirrorStepCounterpoint;
  open_ending: MirrorStepOpenEnding;
}

