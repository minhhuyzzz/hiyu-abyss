// website/src/lib/i18n.ts - Comprehensive Full-Site Bilingual System (VI / EN)

export type Language = 'vi' | 'en';

export const i18nDict: Record<Language, Record<string, string>> = {
  vi: {
    // Navigation
    'nav.library': 'Thư Viện',
    'nav.mirror': 'Chiếc Gương',
    'nav.themes': 'Chủ Đề',
    'nav.search': 'Tìm Kiếm',
    'nav.saved': 'Kho Lưu Trữ',
    'nav.savedShort': 'Kho',

    // Hero
    'hero.badge': 'KIỆT TÁC GIÁM TUYỂN',
    'hero.readMore': 'Đọc Chiêm Nghiệm',
    'hero.mirrorBtn': 'Chiếc Gương Phản Tư',
    'hero.subtext': 'Hiyu Abyss bảo tồn di sản tư tưởng triết học và mỹ học cổ điển. Nơi tâm lý học hành vi đối thoại cùng các kiệt tác hội họa qua hàng thế kỷ để khơi gợi sự tự soi chiếu nội tâm.',

    // Common Buttons & Actions
    'btn.copy': 'Sao Chép Triết Ngôn',
    'btn.copied': 'Đã sao chép ✓',
    'btn.save': 'Lưu Chiêm Nghiệm',
    'btn.saved': 'Đã Lưu Vào Kho',
    'btn.share': 'Chia Sẻ',
    'btn.readDeep': 'Chiêm nghiệm →',
    'btn.viewArt': 'Thưởng Lãm Cận Cảnh',
    'btn.close': 'Đóng',
    'btn.clearAll': 'Xóa toàn bộ',
    'btn.resetFilter': 'Đặt lại bộ lọc',

    // Detail Page
    'detail.readingTime': 'Khoảng 2 phút chiêm nghiệm',
    'detail.initiator': 'Luận điểm khởi xướng:',
    'detail.commentary': 'Bóc Tách Tâm Lý & Chiêm Nghiệm',
    'detail.counterpoint': 'Phản Đề Tự Soi Chiếu (Counterpoint)',
    'detail.prevWork': 'Tác phẩm trước',
    'detail.nextWork': 'Tác phẩm kế tiếp',
    'detail.relatedWorks': 'Tác Phẩm Chiêm Nghiệm Liên Quan',
    'detail.relatedSub': 'Khám phá các góc nhìn tâm lý và hội họa tương đồng',

    // Search Page
    'search.archive': 'SEARCH ARCHIVE',
    'search.curated': 'TÁC PHẨM ĐÃ GIÁM TUYỂN',
    'search.title': 'Tìm Kiếm Toàn Văn',
    'search.subtitle': 'Tra cứu theo từ khóa tâm lý, tác giả (Nietzsche, Jung, Freud, Epictetus...) hoặc khái niệm triết học.',
    'search.placeholder': 'Nhập từ khóa (thao túng, bản ngã, sự thật, tự do, cô độc...)',
    'search.suggestions': 'Gợi ý từ khóa:',
    'search.allTopics': 'Tất cả chủ đề',
    'search.allTypes': 'Tất cả phân loại',
    'search.noResults': 'Không tìm thấy kết quả phù hợp',
    'search.resetHint': 'Hãy thử tìm kiếm với từ khóa ngắn gọn hơn hoặc đặt lại các bộ lọc.',

    // Library Page
    'library.title': 'Kho Tàng Triết Ngôn & Mỹ Học Cổ Điển',
    'library.subtitle': 'Kho lưu trữ tư tưởng triết học và tâm lý học hành vi đối thoại cùng kiệt tác hội họa bảo tàng quốc tế.',
    'library.all': 'Tất cả',
    'library.viewEditorial': 'Thưởng lãm',
    'library.viewGallery': 'Phòng tranh',
    'library.viewIndex': 'Chỉ mục',

    // Saved Drawer
    'drawer.title': 'Kho Lưu Trữ Cá Nhân',
    'drawer.emptyTitle': 'Chưa có tác phẩm nào được lưu',
    'drawer.emptyDesc': 'Khi bắt gặp một triết ngôn sâu sắc, hãy bấm nút "Lưu Chiêm Nghiệm" để giữ lại trong buồng tĩnh tâm của riêng bạn.',
    'drawer.explore': 'Khám Phá Thư Viện',

    // Footer
    'footer.mission': 'Không gian lưu giữ và giám tuyển tư tưởng triết học, tâm lý học hành vi và mỹ học cổ điển. Nơi câu chữ sâu lắng đối thoại cùng các kiệt tác bảo tàng để khơi gợi sự tự soi chiếu nội tâm.',
    'footer.stats': 'KHO LƯU TRỮ ĐANG MỞ RỘNG LIÊN TỤC',
    'footer.nav': 'Điều Hướng',
    'footer.tiktok': 'Kênh TikTok @hiyuabyss',
    'footer.copyright': 'Bảo tồn di sản tư tưởng & mỹ học cổ điển.',
  },
  en: {
    // Navigation
    'nav.library': 'The Library',
    'nav.mirror': 'The Mirror',
    'nav.themes': 'Themes',
    'nav.search': 'Search',
    'nav.saved': 'Saved Archive',
    'nav.savedShort': 'Saved',

    // Hero
    'hero.badge': 'CURATED MASTERPIECE',
    'hero.readMore': 'Read Commentary',
    'hero.mirrorBtn': 'The Mirror',
    'hero.subtext': 'Hiyu Abyss preserves philosophical heritage and classical museum aesthetics. Where behavioral psychology dialogues with centuries-old masterworks to provoke introspection.',

    // Common Buttons & Actions
    'btn.copy': 'Copy Aphorism',
    'btn.copied': 'Copied ✓',
    'btn.save': 'Save Aphorism',
    'btn.saved': 'Saved in Archive',
    'btn.share': 'Share',
    'btn.readDeep': 'Read more →',
    'btn.viewArt': 'View Fullscreen',
    'btn.close': 'Close',
    'btn.clearAll': 'Clear all',
    'btn.resetFilter': 'Reset filters',

    // Detail Page
    'detail.readingTime': '~2 min contemplation',
    'detail.initiator': 'Initiating Mind:',
    'detail.commentary': 'Psychological Commentary & Deconstruction',
    'detail.counterpoint': 'Dialectical Counterpoint',
    'detail.prevWork': 'Previous Work',
    'detail.nextWork': 'Next Work',
    'detail.relatedWorks': 'Related Works of Contemplation',
    'detail.relatedSub': 'Explore converging psychological themes and classical paintings',

    // Search Page
    'search.archive': 'SEARCH ARCHIVE',
    'search.curated': 'CURATED WORKS',
    'search.title': 'Full-Text Search',
    'search.subtitle': 'Search by psychological keywords, authors (Nietzsche, Jung, Freud, Epictetus...) or philosophical concepts.',
    'search.placeholder': 'Enter keyword (manipulation, ego, truth, freedom, solitude...)',
    'search.suggestions': 'Keyword suggestions:',
    'search.allTopics': 'All Themes',
    'search.allTypes': 'All Classifications',
    'search.noResults': 'No matching works found',
    'search.resetHint': 'Try searching with shorter keywords or resetting filters.',

    // Library Page
    'library.title': 'The Living Archive of Thought & Classical Art',
    'library.subtitle': '100 aphorisms on behavioral psychology and existential thought in dialogue with museum masterpieces.',
    'library.all': 'All',
    'library.viewEditorial': 'Editorial',
    'library.viewGallery': 'Gallery',
    'library.viewIndex': 'Index',

    // Saved Drawer
    'drawer.title': 'Personal Saved Archive',
    'drawer.emptyTitle': 'No saved works yet',
    'drawer.emptyDesc': 'When encountering a profound aphorism, click "Save Aphorism" to preserve it in your contemplative sanctuary.',
    'drawer.explore': 'Explore Library',

    // Footer
    'footer.mission': 'A sanctuary preserving philosophical thought, behavioral psychology, and classical museum aesthetics. Where profound aphorisms dialogue with masterworks to awaken introspection.',
    'footer.stats': 'CONTINUOUS LIVING ARCHIVE',
    'footer.nav': 'Navigation',
    'footer.tiktok': 'TikTok Channel @hiyuabyss',
    'footer.copyright': 'Preserving philosophical heritage & classical aesthetics.',
  },
};
