-- Migration 0006: Seed Initial Museum Categories & Tags
INSERT OR IGNORE INTO categories (id, slug, title, description, cover_art_ref, cover_art_title, cover_art_artist, position, locked, created_at)
VALUES 
('cat-philosophy', 'goc-nhin-va-cuoc-song', 'Góc nhìn & Cuộc sống', 'Những góc nhìn sâu sắc về nhận thức, cách nhìn nhận cuộc sống và hành trình thấu hiểu chính mình.', '/images/themes/theme_08/slide_1_establishing.jpg', 'Người quan sát trầm tư bên bức tượng', 'Rembrandt van Rijn (1653)', 1, 0, 1731672000),
('cat-literature-art', 'van-hoc-va-nghe-thuat', 'Văn học & Nghệ thuật', 'Đối thoại về cái đẹp, tác phẩm kinh điển, mỹ học cổ điển và sức mạnh của ngôn từ.', '/images/themes/theme_71/slide_1_establishing.jpg', 'Cô gái đọc thư bên cửa sổ mở', 'Johannes Vermeer (1659)', 2, 0, 1731672000),
('cat-psychology', 'tam-ly-va-hanh-vi', 'Tâm lý & Hành vi', 'Khám phá các cơ chế phòng vệ, bản ngã, nỗi sợ, sự tự lừa dối và động cơ ẩn giấu.', '/images/themes/theme_03/slide_1_establishing.jpg', 'Kẻ lãng du trên biển sương mù', 'Caspar David Friedrich (1818)', 3, 0, 1731672000),
('cat-history-memory', 'lich-su-va-ky-uc', 'Lịch sử & Ký ức', 'Những lát cắt thời gian, ký ức tập thể và bài học lịch sử phản chiếu hiện tại.', '/images/themes/theme_68/slide_1_establishing.jpg', 'Nhà thiên văn học trầm tư', 'Johannes Vermeer (1668)', 4, 0, 1731672000),
('cat-life-dialogue', 'cuoc-song-va-doi-thoai', 'Cuộc sống & Đối thoại', 'Khúc mắc đời thường, các mối quan hệ, ranh giới cá nhân và tìm kiếm bình yên.', '/images/themes/theme_01/slide_1_establishing.jpg', 'Trường học Athens', 'Raphael (1511)', 5, 0, 1731672000),
('cat-weekly-prompt', 'goi-mo-tuan-nay', 'Gợi mở tuần này', 'Chủ đề đối thoại tiêu điểm do ban biên tập Hiyu Abyss khởi xướng.', '/images/themes/theme_15/slide_1_establishing.jpg', 'Đêm đầy sao trên sông Rhône', 'Vincent van Gogh (1888)', 6, 0, 1731672000);

INSERT OR IGNORE INTO tags (id, slug, label) VALUES
('tag-truth', 'su-that', 'Sự thật'),
('tag-peace', 'binh-yen', 'Bình yên'),
('tag-ego', 'ban-nga', 'Bản ngã'),
('tag-solitude', 'co-doc', 'Cô độc'),
('tag-boundaries', 'ranh-gioi', 'Ranh giới'),
('tag-morality', 'dao-duc', 'Đạo đức'),
('tag-love', 'tinh-yeu', 'Tình yêu'),
('tag-suffering', 'kho-dau', 'Khổ đau'),
('tag-meaning', 'y-nghia', 'Ý nghĩa cuộc sống');
