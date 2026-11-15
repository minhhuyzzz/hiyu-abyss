// website/src/lib/agora/db.ts
// Cloudflare D1 unified query client with graceful edge fallback

export interface D1DatabaseLike {
  prepare(query: string): D1PreparedStatementLike;
  batch<T = unknown>(statements: D1PreparedStatementLike[]): Promise<D1Result<T>[]>;
}

export interface D1PreparedStatementLike {
  bind(...values: unknown[]): D1PreparedStatementLike;
  first<T = unknown>(colName?: string): Promise<T | null>;
  all<T = unknown>(): Promise<D1Result<T>>;
  run(): Promise<D1Response>;
}

export interface D1Result<T = unknown> {
  results?: T[];
  success: boolean;
  meta?: any;
  error?: string;
}

export interface D1Response {
  success: boolean;
  meta?: any;
  error?: string;
}

// In-memory fallback database for local development without live D1
class MemoryD1Fallback implements D1DatabaseLike {
  private categories = [
    {
      id: 'cat-philosophy',
      slug: 'goc-nhin-va-cuoc-song',
      title: 'Góc nhìn & Cuộc sống',
      description: 'Những góc nhìn sâu sắc về nhận thức, cách nhìn nhận cuộc sống và hành trình thấu hiểu chính mình.',
      cover_art_ref: '/images/themes/theme_08/slide_1_establishing.jpg',
      cover_art_title: 'Người quan sát trầm tư bên bức tượng',
      cover_art_artist: 'Rembrandt van Rijn (1653)',
      position: 1,
      locked: 0,
      created_at: 1731672000,
    },
    {
      id: 'cat-literature-art',
      slug: 'van-hoc-va-nghe-thuat',
      title: 'Văn học & Nghệ thuật',
      description: 'Đối thoại về cái đẹp, tác phẩm kinh điển, mỹ học cổ điển và sức mạnh của ngôn từ.',
      cover_art_ref: '/images/themes/theme_71/slide_1_establishing.jpg',
      cover_art_title: 'Cô gái đọc thư bên cửa sổ mở',
      cover_art_artist: 'Johannes Vermeer (1659)',
      position: 2,
      locked: 0,
      created_at: 1731672000,
    },
    {
      id: 'cat-psychology',
      slug: 'tam-ly-va-hanh-vi',
      title: 'Tâm lý & Hành vi',
      description: 'Khám phá các cơ chế phòng vệ, bản ngã, nỗi sợ, sự tự lừa dối và động cơ ẩn giấu.',
      cover_art_ref: '/images/themes/theme_03/slide_1_establishing.jpg',
      cover_art_title: 'Kẻ lãng du trên biển sương mù',
      cover_art_artist: 'Caspar David Friedrich (1818)',
      position: 3,
      locked: 0,
      created_at: 1731672000,
    },
    {
      id: 'cat-history-memory',
      slug: 'lich-su-va-ky-uc',
      title: 'Lịch sử & Ký ức',
      description: 'Những lát cắt thời gian, ký ức tập thể và bài học lịch sử phản chiếu hiện tại.',
      cover_art_ref: '/images/themes/theme_68/slide_1_establishing.jpg',
      cover_art_title: 'Nhà thiên văn học trầm tư',
      cover_art_artist: 'Johannes Vermeer (1668)',
      position: 4,
      locked: 0,
      created_at: 1731672000,
    },
    {
      id: 'cat-life-dialogue',
      slug: 'cuoc-song-va-doi-thoai',
      title: 'Cuộc sống & Đối thoại',
      description: 'Khúc mắc đời thường, các mối quan hệ, ranh giới cá nhân và tìm kiếm bình yên.',
      cover_art_ref: '/images/themes/theme_01/slide_1_establishing.jpg',
      cover_art_title: 'Trường học Athens',
      cover_art_artist: 'Raphael (1511)',
      position: 5,
      locked: 0,
      created_at: 1731672000,
    },
    {
      id: 'cat-weekly-prompt',
      slug: 'goi-mo-tuan-nay',
      title: 'Gợi mở tuần này',
      description: 'Chủ đề đối thoại tiêu điểm do ban biên tập Hiyu Abyss khởi xướng.',
      cover_art_ref: '/images/themes/theme_15/slide_1_establishing.jpg',
      cover_art_title: 'Đêm đầy sao trên sông Rhône',
      cover_art_artist: 'Vincent van Gogh (1888)',
      position: 6,
      locked: 0,
      created_at: 1731672000,
    },
  ];

  private threads: any[] = [
    {
      id: 'th_demo_01',
      category_id: 'cat-philosophy',
      author_id: 'usr_curator',
      author_handle: 'hiyu_abyss',
      author_display_name: 'Hiyu Abyss',
      author_avatar: 'monogram',
      title: 'Có phải mọi sự thật đều cần được nói ra trước một thời điểm nhất định?',
      slug: 'co-phai-moi-su-that-deu-can-duoc-noi-ra',
      body_md: 'Đứng trước một người bạn đang tràn đầy hy vọng về quyết định của mình, nhưng bạn biết một thông tin bất lợi. Liệu sự thật được nói ra trong lúc này là lòng dũng cảm, hay chỉ là nhu cầu trút bỏ sự bất an của chính ta?',
      status: 'ACTIVE',
      pinned: 1,
      locked: 0,
      reply_count: 3,
      last_activity_at: Math.floor(Date.now() / 1000),
      created_at: Math.floor(Date.now() / 1000) - 86400,
    },
  ];

  private comments: any[] = [
    {
      id: 'cm_demo_01',
      context_type: 'LIBRARY',
      context_id: 'txt-0001',
      parent_id: null,
      author_id: 'usr_guest_01',
      author_handle: 'minh_nguyen',
      author_display_name: 'Minh Nguyễn',
      author_avatar: 'monogram',
      body_md: 'Câu nói này chạm đúng lúc tôi đang phân vân giữa việc giữ khoảng cách hay nói thẳng với đồng nghiệp. Cảm ơn Hiyu Abyss.',
      status: 'ACTIVE',
      likes_count: 5,
      created_at: Math.floor(Date.now() / 1000) - 7200,
    },
    {
      id: 'cm_demo_02',
      context_type: 'LIBRARY',
      context_id: 'txt-0001',
      parent_id: 'cm_demo_01',
      author_id: 'usr_guest_02',
      author_handle: 'thu_ha',
      author_display_name: 'Thu Hà',
      author_avatar: 'monogram',
      body_md: 'Đôi khi giữ lại một khoảng im lặng không phải hèn nhát, mà là sự tôn trọng thời điểm của người khác bạn nhỉ.',
      status: 'ACTIVE',
      likes_count: 2,
      created_at: Math.floor(Date.now() / 1000) - 3600,
    },
    {
      id: 'cm_demo_03',
      context_type: 'THREAD',
      context_id: 'th_demo_01',
      parent_id: null,
      author_id: 'usr_guest_03',
      author_handle: 'le_khang',
      author_display_name: 'Lê Khang',
      author_avatar: 'monogram',
      body_md: 'Tôi từng vội vã nói ra sự thật vì nghĩ mình thành thật, nhưng hậu quả để lại là người kia mất niềm tin vào mọi thứ. Giờ tôi học cách im lặng và quan sát nhiều hơn.',
      status: 'ACTIVE',
      likes_count: 8,
      created_at: Math.floor(Date.now() / 1000) - 1800,
    },
  ];

  private reactions: any[] = [];
  private bookmarks: any[] = [];
  private follows: any[] = [];
  private notifications: any[] = [];
  private reports: any[] = [];

  prepare(sql: string): D1PreparedStatementLike {
    let boundParams: any[] = [];
    const self = this;

    const stmt: D1PreparedStatementLike = {
      bind(...values: unknown[]) {
        boundParams = values;
        return stmt;
      },
      async first<T = unknown>(): Promise<T | null> {
        const res = await stmt.all<T>();
        return res.results && res.results.length > 0 ? res.results[0] : null;
      },
      async all<T = unknown>(): Promise<D1Result<T>> {
        const clean = sql.trim().toUpperCase();

        if (clean.startsWith('SELECT') && clean.includes('FROM CATEGORIES')) {
          if (clean.includes('WHERE SLUG =')) {
            const slug = boundParams[0];
            const found = self.categories.find((c) => c.slug === slug);
            return { success: true, results: (found ? [found] : []) as T[] };
          }
          return { success: true, results: [...self.categories] as T[] };
        }

        if (clean.startsWith('SELECT') && clean.includes('FROM THREADS')) {
          if (clean.includes('WHERE ID =')) {
            const id = boundParams[0];
            const found = self.threads.find((t) => t.id === id);
            return { success: true, results: (found ? [found] : []) as T[] };
          }
          if (clean.includes('WHERE CATEGORY_ID =')) {
            const catId = boundParams[0];
            const found = self.threads.filter((t) => t.category_id === catId);
            return { success: true, results: found as T[] };
          }
          return { success: true, results: [...self.threads] as T[] };
        }

        if (clean.startsWith('SELECT') && clean.includes('FROM COMMENTS')) {
          const cType = boundParams[0];
          const cId = boundParams[1];
          const found = self.comments.filter(
            (c) => c.context_type === cType && c.context_id === cId && c.status === 'ACTIVE'
          );
          return { success: true, results: found as T[] };
        }

        return { success: true, results: [] };
      },
      async run(): Promise<D1Response> {
        const clean = sql.trim().toUpperCase();

        if (clean.startsWith('INSERT INTO COMMENTS')) {
          const newComment = {
            id: boundParams[0],
            context_type: boundParams[1],
            context_id: boundParams[2],
            parent_id: boundParams[3],
            author_id: boundParams[4],
            author_handle: 'nguoi_dong_hanh',
            author_display_name: 'Người Đồng Hành',
            author_avatar: 'monogram',
            body_md: boundParams[5],
            status: 'ACTIVE',
            likes_count: 0,
            created_at: Math.floor(Date.now() / 1000),
          };
          self.comments.push(newComment);

          // Update thread reply count if thread
          if (newComment.context_type === 'THREAD') {
            const th = self.threads.find((t) => t.id === newComment.context_id);
            if (th) th.reply_count = (th.reply_count || 0) + 1;
          }
          return { success: true };
        }

        if (clean.startsWith('INSERT INTO THREADS')) {
          const newThread = {
            id: boundParams[0],
            category_id: boundParams[1],
            author_id: boundParams[2],
            author_handle: 'nguoi_dong_hanh',
            author_display_name: 'Người Đồng Hành',
            author_avatar: 'monogram',
            title: boundParams[3],
            slug: boundParams[4],
            body_md: boundParams[5],
            status: 'ACTIVE',
            pinned: 0,
            locked: 0,
            reply_count: 0,
            last_activity_at: Math.floor(Date.now() / 1000),
            created_at: Math.floor(Date.now() / 1000),
          };
          self.threads.unshift(newThread);
          return { success: true };
        }

        if (clean.startsWith('INSERT INTO REPORTS')) {
          self.reports.push({
            id: boundParams[0],
            reporter_id: boundParams[1],
            target_type: boundParams[2],
            target_id: boundParams[3],
            reason: boundParams[4],
            detail: boundParams[5],
            status: 'OPEN',
            created_at: Math.floor(Date.now() / 1000),
          });
          return { success: true };
        }

        return { success: true };
      },
    };

    return stmt;
  }

  async batch<T = unknown>(statements: D1PreparedStatementLike[]): Promise<D1Result<T>[]> {
    const results: D1Result<T>[] = [];
    for (const stmt of statements) {
      results.push(await stmt.all<T>());
    }
    return results;
  }
}

// Global fallback singleton for local SSR/dev
const fallbackDb = new MemoryD1Fallback();

export function getD1Database(runtimeEnv?: any): D1DatabaseLike {
  if (runtimeEnv && runtimeEnv.DB) {
    const liveDb = runtimeEnv.DB as D1DatabaseLike;
    return {
      prepare(query: string) {
        let boundValues: unknown[] = [];
        let liveStmt = liveDb.prepare(query);
        let fallbackStmt = fallbackDb.prepare(query);

        const wrapper: D1PreparedStatementLike = {
          bind(...values: unknown[]) {
            boundValues = values;
            liveStmt = liveDb.prepare(query).bind(...values);
            fallbackStmt = fallbackDb.prepare(query).bind(...values);
            return wrapper;
          },
          async first<T = unknown>(colName?: string): Promise<T | null> {
            try {
              return await liveStmt.first<T>(colName);
            } catch (err: any) {
              if (err?.message?.includes('no such table') || err?.message?.includes('SQLITE_ERROR')) {
                return await fallbackStmt.first<T>(colName);
              }
              throw err;
            }
          },
          async all<T = unknown>(): Promise<D1Result<T>> {
            try {
              const res = await liveStmt.all<T>();
              if (!res.success && res.error?.includes('no such table')) {
                return await fallbackStmt.all<T>();
              }
              return res;
            } catch (err: any) {
              if (err?.message?.includes('no such table') || err?.message?.includes('SQLITE_ERROR')) {
                return await fallbackStmt.all<T>();
              }
              throw err;
            }
          },
          async run(): Promise<D1Response> {
            try {
              return await liveStmt.run();
            } catch (err: any) {
              if (err?.message?.includes('no such table') || err?.message?.includes('SQLITE_ERROR')) {
                return await fallbackStmt.run();
              }
              throw err;
            }
          },
        };

        return wrapper;
      },
      async batch<T = unknown>(statements: D1PreparedStatementLike[]): Promise<D1Result<T>[]> {
        try {
          return await liveDb.batch<T>(statements);
        } catch (err: any) {
          if (err?.message?.includes('no such table') || err?.message?.includes('SQLITE_ERROR')) {
            return await fallbackDb.batch<T>(statements);
          }
          throw err;
        }
      },
    };
  }
  return fallbackDb;
}
