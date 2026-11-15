import { z } from 'zod';

export const createThreadSchema = z.object({
  categoryId: z.string().min(1, 'Vui lòng chọn danh mục'),
  title: z
    .string()
    .min(15, 'Tiêu đề cần tối thiểu 15 ký tự')
    .max(150, 'Tiêu đề tối đa 150 ký tự'),
  body: z
    .string()
    .min(30, 'Nội dung chia sẻ cần tối thiểu 30 ký tự')
    .max(10000, 'Nội dung tối đa 10.000 ký tự'),
  tagIds: z.array(z.string()).max(5, 'Tối đa 5 thẻ tags').optional().default([]),
  draftId: z.string().optional().nullable(),
});

export const updateThreadSchema = z.object({
  title: z.string().min(15).max(150).optional(),
  body: z.string().min(30).max(10000).optional(),
  categoryId: z.string().optional(),
  status: z.enum(['ACTIVE', 'LOCKED', 'PINNED', 'DELETED']).optional(),
});

export const createCommentSchema = z.object({
  contextType: z.enum(['THREAD', 'LIBRARY']),
  contextId: z.string().min(1, 'Thiếu ID bối cảnh'),
  parentId: z.string().optional().nullable(),
  body: z
    .string()
    .min(2, 'Bình luận cần tối thiểu 2 ký tự')
    .max(4000, 'Bình luận tối đa 4.000 ký tự'),
});

export const createReportSchema = z.object({
  targetType: z.enum(['THREAD', 'COMMENT', 'USER']),
  targetId: z.string().min(1, 'Thiếu mục tiêu báo cáo'),
  reason: z.enum(['SPAM', 'HARASSMENT', 'MISINFORMATION', 'POLICY_VIOLATION', 'OTHER']),
  detail: z.string().max(1000).optional(),
});

export const updateProfileSchema = z.object({
  displayName: z.string().min(2, 'Tên hiển thị ít nhất 2 ký tự').max(50, 'Tên hiển thị tối đa 50 ký tự'),
  bio: z.string().max(240, 'Mô tả cá nhân tối đa 240 ký tự').optional(),
  avatarPreset: z.string().max(50).optional(),
});

export const reactionSchema = z.object({
  targetType: z.enum(['THREAD', 'COMMENT']),
  targetId: z.string().min(1),
  kind: z.literal('LIKE').default('LIKE'),
});

export const bookmarkSchema = z.object({
  targetType: z.enum(['LIBRARY', 'THREAD']),
  targetId: z.string().min(1),
});

export type CreateThreadInput = z.infer<typeof createThreadSchema>;
export type CreateCommentInput = z.infer<typeof createCommentSchema>;
export type CreateReportInput = z.infer<typeof createReportSchema>;
export type UpdateProfileInput = z.infer<typeof updateProfileSchema>;
