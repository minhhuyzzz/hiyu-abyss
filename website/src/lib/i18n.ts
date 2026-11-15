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
    'hero.badge': 'CÂU NÓI NỔI BẬT',
    'hero.readMore': 'Đọc Thêm',
    'hero.mirrorBtn': 'Chiếc Gương',
    'hero.subtext': 'Hiyu Abyss lưu giữ những câu nói hay, sâu sắc về tâm lý và cuộc đời được biên soạn tinh tế, đồng hành cùng tranh cổ điển chọn lọc.',

    // Common Buttons & Actions
    'btn.copy': 'Sao Chép Câu Nói',
    'btn.copied': 'Đã sao chép ✓',
    'btn.save': 'Lưu Vào Kho',
    'btn.saved': 'Đã Lưu Vào Kho',
    'btn.share': 'Chia Sẻ',
    'btn.readDeep': 'Xem tiếp →',
    'btn.viewArt': 'Xem Tranh Cận Cảnh',
    'btn.close': 'Đóng',
    'btn.clearAll': 'Xóa toàn bộ',
    'btn.resetFilter': 'Đặt lại bộ lọc',

    // Detail Page
    'detail.readingTime': 'Khoảng 2 phút đọc',
    'detail.initiator': 'Tác giả:',
    'detail.commentary': 'Góc Nhìn & Suy Ngẫm',
    'detail.counterpoint': 'Một Góc Nhìn Khác',
    'detail.prevWork': 'Câu trước',
    'detail.nextWork': 'Câu kế tiếp',
    'detail.relatedWorks': 'Những Câu Nói Cùng Chủ Đề',
    'detail.relatedSub': 'Khám phá các góc nhìn tâm lý và cảm xúc tương đồng',

    // Search Page
    'search.archive': 'TÌM KIẾM',
    'search.curated': 'CÂU NÓI CHỌN LỌC',
    'search.title': 'Tìm Kiếm Câu Nói',
    'search.subtitle': 'Tìm câu nói theo từ khóa (ranh giới, lòng tốt, bản ngã, sự thật, cô độc...), tác giả hoặc chủ đề bạn quan tâm.',
    'search.placeholder': 'Nhập từ khóa (ranh giới, sự thật, lòng tốt, tự do, cô độc...)',
    'search.suggestions': 'Gợi ý từ khóa:',
    'search.allTopics': 'Tất cả chủ đề',
    'search.allTypes': 'Tất cả phân loại',
    'search.noResults': 'Không tìm thấy kết quả phù hợp',
    'search.resetHint': 'Hãy thử tìm kiếm với từ khóa ngắn gọn hơn hoặc chọn lại chủ đề.',

    // Library Page
    'library.title': 'Những Câu Nói Hay & Góc Nhìn Sâu Sắc',
    'library.subtitle': 'Nơi lưu giữ những câu nói ý nghĩa về tâm lý và cuộc sống, kết hợp cùng tranh nghệ thuật cổ điển chọn lọc.',
    'library.all': 'Tất cả',
    'library.viewEditorial': 'Tạp chí',
    'library.viewGallery': 'Phòng tranh',
    'library.viewIndex': 'Danh mục',

    // Saved Drawer
    'drawer.title': 'Kho Lưu Trữ Cá Nhân',
    'drawer.emptyTitle': 'Chưa có câu nói nào được lưu',
    'drawer.emptyDesc': 'Khi bắt gặp một câu nói chạm đến lòng bạn, hãy bấm nút "Lưu Vào Kho" để xem lại bất cứ khi nào bạn muốn.',
    'drawer.explore': 'Khám Phá Thư Viện',

    // Footer
    'footer.mission': 'Không gian lưu giữ những câu nói hay, sâu sắc về cuộc sống và tâm lý con người bên cạnh tranh nghệ thuật cổ điển. Đọc để nhìn thế giới khác đi, suy ngẫm để hiểu mình rõ hơn.',
    'footer.stats': 'KHO LƯU TRỮ ĐANG MỞ RỘNG LIÊN TỤC',
    'footer.nav': 'Điều Hướng',
    'footer.tiktok': 'Kênh TikTok @hiyuabyss',
    'footer.copyright': 'Tuyển tập những câu nói hay & tranh nghệ thuật cổ điển.',
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
    'library.subtitle': 'A living archive of behavioral psychology and existential thought in dialogue with museum masterpieces.',
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
