// website/src/lib/agora/service.ts
// Business Logic Layer for The Agora & Library Comments

import { getD1Database, type D1DatabaseLike } from './db';
import type { CreateThreadInput, CreateCommentInput, CreateReportInput } from './schemas';

export interface Category {
  id: string;
  slug: string;
  title: string;
  description: string;
  cover_art_ref: string;
  cover_art_title: string;
  cover_art_artist: string;
  position: number;
  locked: number;
  thread_count?: number;
}

export interface Thread {
  id: string;
  category_id: string;
  category_title?: string;
  category_slug?: string;
  author_id: string;
  author_handle: string;
  author_display_name: string;
  author_avatar?: string;
  title: string;
  slug: string;
  body_md: string;
  status: 'ACTIVE' | 'LOCKED' | 'PINNED' | 'DELETED';
  pinned: number;
  locked: number;
  reply_count: number;
  likes_count?: number;
  is_liked?: boolean;
  is_followed?: boolean;
  last_activity_at: number;
  created_at: number;
  updated_at?: number;
}

export interface CommentItem {
  id: string;
  context_type: 'THREAD' | 'LIBRARY';
  context_id: string;
  parent_id?: string | null;
  author_id: string;
  author_handle: string;
  author_display_name: string;
  author_avatar?: string;
  body_md: string;
  status: 'ACTIVE' | 'FLAGGED' | 'HIDDEN' | 'DELETED';
  likes_count: number;
  is_liked?: boolean;
  created_at: number;
  replies?: CommentItem[];
}

export function generateSlug(text: string): string {
  return text
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[đĐ]/g, 'd')
    .replace(/[^a-z0-9\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .slice(0, 80);
}

export class AgoraService {
  private db: D1DatabaseLike;

  constructor(env?: any) {
    this.db = getD1Database(env);
  }

  // 1. Categories
  async getCategories(): Promise<Category[]> {
    const res = await this.db
      .prepare('SELECT * FROM categories ORDER BY position ASC')
      .all<Category>();
    return res.results || [];
  }

  async getCategoryBySlug(slug: string): Promise<Category | null> {
    return await this.db
      .prepare('SELECT * FROM categories WHERE slug = ? LIMIT 1')
      .bind(slug)
      .first<Category>();
  }

  // 2. Threads
  async getThreads(options: {
    categoryId?: string;
    filter?: 'NEW' | 'FEATURED' | 'UNANSWERED';
    limit?: number;
  }): Promise<Thread[]> {
    const limit = options.limit || 20;

    if (options.categoryId) {
      const res = await this.db
        .prepare(
          'SELECT * FROM threads WHERE category_id = ? AND status != "DELETED" ORDER BY pinned DESC, last_activity_at DESC LIMIT ?'
        )
        .bind(options.categoryId, limit)
        .all<Thread>();
      return res.results || [];
    }

    if (options.filter === 'UNANSWERED') {
      const res = await this.db
        .prepare(
          'SELECT * FROM threads WHERE reply_count = 0 AND status != "DELETED" ORDER BY created_at DESC LIMIT ?'
        )
        .bind(limit)
        .all<Thread>();
      return res.results || [];
    }

    const res = await this.db
      .prepare(
        'SELECT * FROM threads WHERE status != "DELETED" ORDER BY pinned DESC, last_activity_at DESC LIMIT ?'
      )
      .bind(limit)
      .all<Thread>();
    return res.results || [];
  }

  async getThreadById(id: string): Promise<Thread | null> {
    return await this.db
      .prepare('SELECT * FROM threads WHERE id = ? AND status != "DELETED" LIMIT 1')
      .bind(id)
      .first<Thread>();
  }

  async createThread(
    input: CreateThreadInput,
    author: { id: string; handle: string; displayName: string }
  ): Promise<Thread> {
    const threadId = `th_${Date.now()}_${Math.random().toString(36).slice(2, 7)}`;
    const slug = generateSlug(input.title);
    const now = Math.floor(Date.now() / 1000);

    await this.db
      .prepare(
        'INSERT INTO threads (id, category_id, author_id, title, slug, body_md, status, pinned, locked, reply_count, last_activity_at, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, "ACTIVE", 0, 0, 0, ?, ?, ?)'
      )
      .bind(
        threadId,
        input.categoryId,
        author.id,
        input.title,
        slug,
        input.body,
        now,
        now,
        now
      )
      .run();

    return {
      id: threadId,
      category_id: input.categoryId,
      author_id: author.id,
      author_handle: author.handle,
      author_display_name: author.displayName,
      title: input.title,
      slug,
      body_md: input.body,
      status: 'ACTIVE',
      pinned: 0,
      locked: 0,
      reply_count: 0,
      last_activity_at: now,
      created_at: now,
    };
  }

  // 3. Comments (Tree Structured for Library and Thread)
  async getComments(
    contextType: 'THREAD' | 'LIBRARY',
    contextId: string
  ): Promise<CommentItem[]> {
    const res = await this.db
      .prepare(
        'SELECT * FROM comments WHERE context_type = ? AND context_id = ? AND status = "ACTIVE" ORDER BY created_at ASC'
      )
      .bind(contextType, contextId)
      .all<CommentItem>();

    const rawList = res.results || [];

    // Assemble hierarchical 2-level visual comment tree
    const rootComments: CommentItem[] = [];
    const commentMap = new Map<string, CommentItem>();

    rawList.forEach((c) => {
      commentMap.set(c.id, { ...c, replies: [] });
    });

    rawList.forEach((c) => {
      const item = commentMap.get(c.id)!;
      if (c.parent_id && commentMap.has(c.parent_id)) {
        const parent = commentMap.get(c.parent_id)!;
        parent.replies = parent.replies || [];
        parent.replies.push(item);
      } else {
        rootComments.push(item);
      }
    });

    return rootComments;
  }

  async createComment(
    input: CreateCommentInput,
    author: { id: string; handle: string; displayName: string }
  ): Promise<CommentItem> {
    const commentId = `cm_${Date.now()}_${Math.random().toString(36).slice(2, 7)}`;
    const now = Math.floor(Date.now() / 1000);

    await this.db
      .prepare(
        'INSERT INTO comments (id, context_type, context_id, parent_id, author_id, body_md, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, "ACTIVE", ?, ?)'
      )
      .bind(
        commentId,
        input.contextType,
        input.contextId,
        input.parentId || null,
        author.id,
        input.body,
        now,
        now
      )
      .run();

    return {
      id: commentId,
      context_type: input.contextType,
      context_id: input.contextId,
      parent_id: input.parentId || null,
      author_id: author.id,
      author_handle: author.handle,
      author_display_name: author.displayName,
      body_md: input.body,
      status: 'ACTIVE',
      likes_count: 0,
      created_at: now,
      replies: [],
    };
  }

  // 4. Reports (Community Safety & Moderation)
  async createReport(input: CreateReportInput, reporterId: string): Promise<void> {
    const reportId = `rep_${Date.now()}_${Math.random().toString(36).slice(2, 7)}`;
    const now = Math.floor(Date.now() / 1000);

    await this.db
      .prepare(
        'INSERT INTO reports (id, reporter_id, target_type, target_id, reason, detail, status, created_at) VALUES (?, ?, ?, ?, ?, ?, "OPEN", ?)'
      )
      .bind(
        reportId,
        reporterId,
        input.targetType,
        input.targetId,
        input.reason,
        input.detail || null,
        now
      )
      .run();
  }
}
