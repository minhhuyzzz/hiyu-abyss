# HIYU ABYSS — DELIVERY BACKLOG V3.0

**Companion:** `HIYU_ABYSS_MASTERPLAN_V3.md`  
**Vai trò:** Backlog có thể giao cho Antigravity; mỗi task yêu cầu PR/commit, ảnh before/after, self-review, tests.

**Quy định mức ưu tiên:** `P0` = chặn phát hành; `P1` = nâng cấp cốt lõi; `P2` = lớp hoàn thiện. **Chỉ đánh dấu hoàn thành sau khi nghiệm thu thực tế.** Không cần làm hết P2 mới public V3.

## PHASE 0 — PROJECT AUDIT & SOURCE PROTECTION

- [ ] **A01 [P0] Repo baseline & screenshots** — chụp 390/768/1440 px ở cả Dark/Light cho Home, Library, Detail, Mirror; lưu screenshots để so sánh, log commit hash. **Pass:** có bảng trang/ảnh và danh mục lỗi; không phá production.
- [ ] **A02 [P0] Content audit** — kiểm tra `DIRECT_QUOTE`, nguồn nguyên tác, bản dịch/đoạn cụ thể; kiểm tra `TXT-0001` trước. **Pass:** quote thiếu chứng cứ bị hạ nhãn hoặc ẩn, không tự bịa nguồn.
- [ ] **A03 [P0] Asset rights audit** — bổ sung `source_url`, `license_evidence_url`, curator, allowed transformations/crops. **Pass:** artwork public có bằng chứng nguồn và quyền dùng.
- [ ] **A04 [P0] Route / SEO baseline** — inventory route hiện tại, canonical/OG, 404, internal links. **Pass:** không còn domain mismatch trên production.
- [ ] **A05 [P0] Approvals gate audit** — lọc manifest + status + evidence, không hard-code `100` làm điều kiện pass. **Pass:** DRAFT thiếu nguồn không được xuất HTML/index.

## PHASE 1 — DESIGN & INTERACTION SYSTEM

- [ ] **D01 [P0] Visual art direction boards** — 2 concepts Dark/Light, font sample tiếng Việt, 5 nhịp editorial, kiểu ảnh và caption; 1440/390. **Pass:** chủ dự án duyệt 1 hướng, ghi lý do loại các mẫu SaaS.
- [ ] **D02 [P0] Theme tokens** — token semantic, image overlay, outline/focus, background of light; dark/light đều không lóa, đủ contrast. **Pass:** ít nhất 10 UI states ở 2 theme.
- [ ] **D03 [P0] Type scale & grid** — Cormorant/Literata/Be Vietnam Pro, hero 36–80px fluid, prose 17–19px, line height 1.6–1.85, grid 12/6/4. **Pass:** 320px không overflow; dấu tiếng Việt chuẩn.
- [ ] **D04 [P0] Component inventory** — chỉ dùng card khi có chức năng; xây `EditorialSpread`, `ArtworkCaption`, `QuietQuote`, `SectionIndex`, `RelatedReading`, `ArtLightbox`. **Pass:** không copy cùng 1 card để làm toàn bộ trang.
- [ ] **D05 [P1] Motion grammar** — token 180/280/420/650ms, ease, reveal, scene swaps, reduced motion. **Pass:** có document animation map; animation không cản nội dung.
- [ ] **D06 [P1] Header/footer responsive** — compact sticky, mobile nav accessible, Explore submenu, footer biên tập + about/source/contact. **Pass:** dùng bằng bàn phím, focus rõ, không mất menu sau chuyển trang.

## PHASE 2 — LANDING PAGE V3 / 12 EDITORIAL SCENES

- [ ] **H01 [P0] Entrance** — full-bleed art + thật ít chữ + Library/Mirror CTA, đáp ứng 390/1440 & cả 2 theme. **Pass:** nội dung chính thấy ngay, không phải card hai cột thuần.
- [ ] **H02 [P1] Daily Inscription** — 1 quote được duyệt, link nguồn, art direction chữ lớn. **Pass:** không có câu giả hoặc 'anonymous' do mặc định.
- [ ] **H03 [P1] Curator's Selection** — 3–5 bài, layout bất đối xứng với kích thước khác nhau. **Pass:** mobile là sequence có thứ tự rõ.
- [ ] **H04 [P1] Library Threshold** — cho người đọc hiểu đi vào thư viện được gì. **Pass:** CTA đi đúng route, ảnh gắn thật với nội dung.
- [ ] **H05 [P1] Atlas of Ideas** — 6–12 chủ đề động và artwork minh họa, điều hướng không cần hover. **Pass:** thêm 1 chủ đề không sửa layout code.
- [ ] **H06 [P1] One Work / Many Interpretations** — 1 tác phẩm + detail + góc nhìn đối lập + nguồn. **Pass:** có 3 panel với dữ liệu được duyệt.
- [ ] **H07 [P0] Mirror Portal** — visual mirror-threshold có motion dễ chịu + journey preview. **Pass:** người chưa biết The Mirror hiểu cơ chế trong một màn hình.
- [ ] **H08 [P2] Long Read Feature** — bài luận dài có ảnh, reading time, excerpt. **Pass:** ẩn hợp lệ khi chưa có essay approved.
- [ ] **H09 [P2] Thinkers & Works** — trưng bày tác giả/tác phẩm đủ nguồn. **Pass:** không link tới danh mục rỗng.
- [ ] **H10 [P1] Artworks in Dialogue** — gallery ít nhất 4 ảnh có provenance link, responsive. **Pass:** không che chú thích hoặc nén méo tranh.
- [ ] **H11 [P1] A Question to Carry** — khối typography + link Mirror. **Pass:** không làm bài test giả trên landing.
- [ ] **H12 [P0] Closing & global review** — tuyên ngôn + footer; test 12 section, không hai section liền nhau cùng layout. **Pass:** 4 screenshots desktop/mobile Dark/Light được duyệt.

## PHASE 3 — THE LIBRARY / DETAIL / COLLECTIONS

- [ ] **L01 [P0] Editorial index view** — layout gallery editorial có featured works. **Pass:** khác `QuoteCard` 3-col hiện tại về cấu trúc và thứ bậc.
- [ ] **L02 [P1] Gallery view** — art-first, caption/provenance, ảnh tỉ lệ đa dạng. **Pass:** responsive, đầy đủ alt/link.
- [ ] **L03 [P1] Compact index view** — text-first list gọn có title/topic/author/type. **Pass:** scan được 100+ entries.
- [ ] **L04 [P0] Filters + sort + URL state** — topic/type/author/search, clear filter, empty state; hạn chế filter chưa đủ metadata. **Pass:** copy URL mở lại cùng kết quả, back/forward đúng.
- [ ] **L05 [P1] Pagination / lazy loading** — 12/24 per page; ảnh dưới fold lazy và `srcset`. **Pass:** initial load không tải tất cả artwork.
- [ ] **L06 [P1] Curated collections** — YAML/MD collections có intro/hero/ordered IDs; không tạo bộ sưu tập bằng đếm ID. **Pass:** hiển thị ít nhất 2 collection được biên tập.
- [ ] **L07 [P0] Detail redesign** — 10 khối: breadcrumb, artwork, text, context, counterpoint, exact source, details, connections, actions, reading path. **Pass:** bản đọc đi từ tranh → suy ngẫm → nguồn → tiếp tục.
- [ ] **L08 [P0] Provenance component** — source cụ thể, quote kind, artwork rights/URL; chưa có evidence thì không để nhãn verified. **Pass:** kiểm `TXT-0001` như edge case.
- [ ] **L09 [P1] Saved / share / copy** — localStorage only, toast dễ tiếp cận, native share fallback; không có login. **Pass:** refresh vẫn thấy saved trên cùng thiết bị, private tab không crash.
- [ ] **L10 [P1] Relatedness engine** — curated relationships from tags/source IDs, không tự gán inference vô căn cứ. **Pass:** 3 related assets có nội dung thật hoặc fallback.

## PHASE 4 — MIRROR ENGINE & NARRATIVE DESIGN

- [ ] **M01 [P0] Scene graph schema** — `nodes`, `entry`, `type`, `choices`, `to`, `artworkId`, `motionPreset`, `ending` typed Zod; upgrade `MirrorJourneyData`. **Pass:** JSON/YAML graph valid.
- [ ] **M02 [P0] Graph validator** — IDs unique, edges valid, accessible endings, no infinite loop, minimum 2 decisions per route. **Pass:** invalid graphs fail build with exact error.
- [ ] **M03 [P0] React state engine** — `currentNodeId`, `history`, choice keys, undo/back, restart, exit; không dùng enum 5 bước. **Pass:** Back từ mọi nhánh không lẫn state.
- [ ] **M04 [P0] MIR-0001 narrative rewrite** — tối thiểu 4 kết thúc và 2 decision points mỗi route; counterpoint khác thực chất; giới hạn độ dài mỗi scene. **Pass:** script tự duyệt được 4 terminal routes.
- [ ] **M05 [P1] Scene composition** — các scene template khác nhau (threshold, choice wall, reflection, counterpoint, ending) + artwork cắt/điều tiết. **Pass:** không phải mọi scene là cùng khung text + button.
- [ ] **M06 [P1] Motion architecture** — Motion for React AnimatePresence; scene transitions 180–420ms, crossfade artwork, stagger ngắn; no WebGL requirement. **Pass:** 60fps mục tiêu trên mobile thường, không giật/nhảy layout.
- [ ] **M07 [P0] Accessibility + controls** — keyboard selection, visible focus, screen reader announcements, reduced-motion, skip animations, back/exit/restart. **Pass:** toàn hành trình dùng được không chuột và không animation.
- [ ] **M08 [P1] Mirror portal redesign** — ấn phẩm gallery, mô tả journey length/branching, art preview, không card nhân bản. **Pass:** user nhìn thấy sự khác nhau giữa hành trình.
- [ ] **M09 [P2] Two additional journeys** — viết `MIR-0002/0003` thuộc 2 lĩnh vực khác nhau, review triết học, hình ảnh và nguồn. **Pass:** không 3 journey cùng câu hỏi/logic.
- [ ] **M10 [P0] E2E all pathways** — Playwright matrix 4 endings + back/forward/restart/exit/responsive/themes/reduced-motion. **Pass:** automated pass trong CI hoặc staging local, có video/screenshot demo.

## PHASE 5 — EXPLORE / RESEARCH & VISUAL ARCHIVE

- [ ] **E01 [P0] Open taxonomy source** — subject metadata từ YAML/MD thay vì `TOPIC_NAMES` hard-code. **Pass:** thêm chủ đề không sửa TS map.
- [ ] **E02 [P1] Themes atlas & detail** — constellations accessible list + thematic essays/art. **Pass:** không chỉ lưới 20 card.
- [ ] **E03 [P1] Thinkers pages** — directory/detail, reliable source URLs and works. **Pass:** không gắn direct quote thiếu evidence.
- [ ] **E04 [P1] Works pages** — books/works, editions, languages, passages, connections. **Pass:** metadata bibliographic đầy đủ với vài bản mẫu.
- [ ] **E05 [P1] Essays reading templates** — markdown/MDX per policy, TOC, footnotes, in-body art. **Pass:** 2 essays chất lượng đã duyệt trước publish route.
- [ ] **E06 [P1] Artwork archive** — gallery/filter/provenance/lightbox (nếu asset rights pass). **Pass:** mỗi ảnh có source/rights evidence hoặc chỉ rõ là artwork nguyên bản của dự án.
- [ ] **E07 [P1] About & editorial policy** — tuyên ngôn, quy trình phân loại nguồn, báo lỗi và liên hệ. **Pass:** mọi claim cụ thể có nội dung chứng minh.
- [ ] **E08 [P1] Unified search** — Pagefind public pages + type filter + tiếng Việt. **Pass:** tìm không dấu/có dấu qua toàn trang, không index DRAFT.

## PHASE 6 — TECHNICAL PRODUCTION, SEO, PERFORMANCE

- [ ] **T01 [P0] Astro build & config** — `SITE_URL`, production base, canonical, social cards/OG, static URLs, indexability. **Pass:** staging và production URL hợp lệ.
- [ ] **T02 [P0] Responsive image pipeline** — imported asset, metadata, variants WebP/AVIF, width/height/alt, `srcset`. **Pass:** mobile không tải 180 ảnh khi mở home.
- [ ] **T03 [P0] Reduced motion & event lifecycle** — Astro transitions opt-in tested, scripts reinitialize properly, no duplicate event handlers. **Pass:** navigation repeatedly without break.
- [ ] **T04 [P0] Keyboard & WCAG audit** — color tokens over images, focus, semantics, headings, mobile touch, 320px. **Pass:** automated + manual issues resolved.
- [ ] **T05 [P1] Performance budget** — measure mobile LCP, INP, CLS; no bloated client JS; font subsets. **Pass:** report baseline vs new with recommendations.
- [ ] **T06 [P0] Safe content rendering** — no untrusted `innerHTML` from source; schema validation, no private notes in output. **Pass:** script scans generated HTML/JS for restricted fields.
- [ ] **T07 [P0] Clean install & deploy test** — `npm ci`, build Linux from full repo, route traversal, no DB/API key. **Pass:** preview deploy reproducible by new contributor.

## PHASE 7 — FINAL EDITORIAL QA & DEPLOY

- [ ] **Q01 [P0] Visual sign-off** — screenshots home/library/detail/mirror/themes/search desktop/mobile Dark/Light with before/after; owner approves.
- [ ] **Q02 [P0] Content & licensing sign-off** — sampled direct quotes + artwork metadata checked; unsupported claims removed.
- [ ] **Q03 [P0] Browser smoke tests** — Chromium/Firefox/WebKit, mobile sizes, 4 mirror routes, source links, bookmarks, search; no errors.
- [ ] **Q04 [P0] Release notes / rollback** — PR, changelog, preview, rollback strategy. **Pass:** deploy mới không làm mất phiên bản ổn định.

---

## DEFINITION OF DONE — KHÔNG CHẤP NHẬN “XONG” CHỈ VÌ BUILD SUCCESS

Mỗi task phải có: (a) commit + file thay đổi, (b) link/screenshot desktop & mobile, (c) Dark/Light check, (d) keyboard/reduced-motion khi tương tác, (e) data-source/rights QA khi liên quan, (f) test report. Với P0 không bỏ qua bất kỳ mục nào có liên quan.

## THỨ TỰ TRIỂN KHAI KHUYẾN NGHỊ

A01–A05 → D01–D06 → H01/H07/H12 trước (visual prototypes) → L07/L08 (detail chuẩn) → L01–L06 → M01–M08/M10 → H02–H11 (đầy đủ landing) → E01–E08 → T01–T07 → Q01–Q04. Ưu tiên nội dung thật và minh bạch trước khi mở hàng loạt trang mới.

## LỆNH GIAO ANTIGRAVITY (BẢN NGẮN)

> Đọc `HIYU_ABYSS_MASTERPLAN_V3.md`, `HIYU_ABYSS_TASKS_V3.md` và HYA-01 đến HYA-07; rà repo `website/` trước. Nâng cấp **toàn bộ** homepage, Library/Detail, Mirror, Themes, Search, Thinkers, Works, Essays, Artworks, About. Giữ Astro Static-First + Markdown/YAML/GitHub + không database/không API trả phí. Không làm lại bằng template/dashboard AI. Xây design prototypes 1440/390 Dark/Light trước rồi thực hiện theo phases; Mirror dùng scene graph phân nhánh thật ≥4 endings với scene animations và reduced-motion; Library có Editorial/Gallery/Index, filters URL, source & art provenance. Giữ gate xuất bản và không tự tạo trích dẫn/nguồn. Mỗi phase báo file thay đổi, screenshot, test và xin phê duyệt ở milestone chính, không thay production khi chưa qua QA.
