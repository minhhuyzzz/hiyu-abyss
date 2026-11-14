#!/usr/bin/env python3
"""
Hiyu Abyss — Integrity & Hard Gate Validation Script
Tuân thủ tiêu chuẩn HYA-04 & HYA-06.
"""

import os
import re
import sys
import yaml
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

APPROVED_TOPIC_CODES = {
    "HYPOCRISY", "DOUBLE_STANDARD", "MORALITY", "EGO", "SELF_DECEPTION",
    "SHADOW", "MASK", "POWER", "MANIPULATION", "FREEDOM",
    "TRUTH", "LOVE", "LOYALTY", "ENVY", "CROWD",
    "SUFFERING", "IDENTITY", "MEANING", "SOLITUDE", "STATUS"
}

VALID_RECORD_TYPES = {"SOURCE", "READING_NOTE", "CONCEPT", "IDEA", "CONTENT", "RESEARCH_RUN"}
VALID_SOURCE_TYPES = {"BOOK", "PRIMARY_TEXT", "STUDY", "ACADEMIC_OVERVIEW", "ESSAY", "SOCIAL_POST", "OTHER"}
VALID_ACCESS_LEVELS = {"FOUND_METADATA", "PARTIAL_TEXT", "READ_SOURCE", "CONTEXT_CHECKED"}
VALID_EVIDENCE_STATUSES = {"VERIFIED_TEXT", "VERIFIED_IDEA", "NEEDS_REVIEW", "UNVERIFIED", "DISPUTED"}
VALID_CONTENT_TYPES = {"DIRECT_QUOTE", "PARAPHRASE", "INSPIRED_ORIGINAL", "INDEPENDENT_ORIGINAL"}
VALID_TXT_STATUSES = {"DRAFT", "IN_REVIEW", "NEEDS_SOURCE", "APPROVED", "PUBLISHED", "REJECTED", "ARCHIVED"}
VALID_IDEA_STATUSES = {"CAPTURED", "RESEARCHED", "SELECTED", "PARKED", "REJECTED"}
VALID_RUN_STATUSES = {"COMPLETE", "PARTIAL", "BLOCKED"}

ID_PATTERNS = {
    "SOURCE": re.compile(r"^SRC-\d{4}$"),
    "READING_NOTE": re.compile(r"^NOTE-\d{4}$"),
    "CONCEPT": re.compile(r"^CON-\d{4}$"),
    "IDEA": re.compile(r"^IDEA-\d{4}$"),
    "CONTENT": re.compile(r"^TXT-\d{4}$"),
    "RESEARCH_RUN": re.compile(r"^RUN-\d{4}$"),
}

RECORD_DIRS = {
    "SOURCE": ROOT_DIR / "knowledge" / "sources",
    "READING_NOTE": ROOT_DIR / "knowledge" / "notes",
    "CONCEPT": ROOT_DIR / "knowledge" / "concepts",
    "IDEA": ROOT_DIR / "editorial" / "ideas",
    "CONTENT": ROOT_DIR / "editorial" / "content",
    "RESEARCH_RUN": ROOT_DIR / "knowledge" / "runs",
}

def extract_frontmatter(file_path):
    """Trích xuất và parse phần YAML frontmatter từ file Markdown."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if not content.startswith("---"):
        return None, "File không bắt đầu bằng YAML frontmatter ('---')"
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, "YAML frontmatter không đóng bằng '---'"
    
    yaml_text = parts[1]
    body_text = parts[2]
    try:
        data = yaml.safe_load(yaml_text)
        return data, body_text
    except yaml.YAMLError as e:
        return None, f"Lỗi cú pháp YAML: {e}"

def validate_all_records():
    """Quét và kiểm tra toàn bộ các hồ sơ trong knowledge và editorial."""
    errors = []
    warnings = []
    records_by_id = {}
    records_by_type = {k: {} for k in RECORD_DIRS.keys()}

    # 1. Quét và nạp dữ liệu
    for record_type, dir_path in RECORD_DIRS.items():
        if not dir_path.exists():
            continue
        for file_path in dir_path.glob("*.md"):
            rel_path = file_path.relative_to(ROOT_DIR)
            data, body_or_err = extract_frontmatter(file_path)
            if data is None:
                errors.append(f"[{rel_path}] {body_or_err}")
                continue
            
            rec_id = data.get("id")
            if not rec_id:
                errors.append(f"[{rel_path}] Thiếu trường 'id'")
                continue
            
            if rec_id in records_by_id:
                errors.append(f"[{rel_path}] Trùng lặp ID '{rec_id}' (đã có ở {records_by_id[rec_id]['path']})")
                continue
            
            # Khớp tên file với ID
            expected_filename = f"{rec_id}.md"
            if file_path.name != expected_filename:
                errors.append(f"[{rel_path}] Tên file '{file_path.name}' không khớp với ID '{rec_id}' (phải là '{expected_filename}')")
            
            records_by_id[rec_id] = {
                "path": rel_path,
                "abs_path": file_path,
                "data": data,
                "body": body_or_err,
                "type": record_type
            }
            records_by_type[record_type][rec_id] = records_by_id[rec_id]

    # 2. Kiểm tra chi tiết từng hồ sơ
    for rec_id, rec in records_by_id.items():
        data = rec["data"]
        rel_path = rec["path"]
        rec_type = data.get("record_type")

        # Kiểm tra record_type
        if rec_type not in VALID_RECORD_TYPES:
            errors.append(f"[{rel_path}] record_type không hợp lệ: '{rec_type}'")
            continue

        # Kiểm tra ID pattern
        if not ID_PATTERNS[rec_type].match(rec_id):
            errors.append(f"[{rel_path}] ID '{rec_id}' không đúng định dạng chuẩn cho {rec_type}")

        # Kiểm tra theo từng loại hồ sơ
        if rec_type == "SOURCE":
            src_type = data.get("source_type")
            if src_type not in VALID_SOURCE_TYPES:
                errors.append(f"[{rel_path}] source_type không hợp lệ: '{src_type}'")
            
            access_lvl = data.get("access_level")
            if access_lvl not in VALID_ACCESS_LEVELS:
                errors.append(f"[{rel_path}] access_level không hợp lệ: '{access_lvl}'")
            
            if not data.get("title"):
                errors.append(f"[{rel_path}] Thiếu title")
            
            links = data.get("links")
            if links is None or not isinstance(links, list):
                errors.append(f"[{rel_path}] 'links' phải là danh sách các URL")

        elif rec_type == "READING_NOTE":
            src_id = data.get("source_id")
            if not src_id:
                errors.append(f"[{rel_path}] Thiếu source_id")
            elif src_id not in records_by_id:
                errors.append(f"[{rel_path}] source_id '{src_id}' không tồn tại trên hệ thống (Hard Gate G4)")
            else:
                src_rec = records_by_id[src_id]
                # Kiểm tra mức truy cập giữa Source và Note
                note_access = data.get("access_level")
                src_access = src_rec["data"].get("access_level")
                if src_access == "FOUND_METADATA" and note_access in {"READ_SOURCE", "CONTEXT_CHECKED"}:
                    errors.append(f"[{rel_path}] Mâu thuẫn: Source {src_id} chỉ có mức 'FOUND_METADATA' nhưng Note ghi '{note_access}' (Ca T01)")
            
            ev_status = data.get("evidence_status")
            if ev_status not in VALID_EVIDENCE_STATUSES:
                errors.append(f"[{rel_path}] evidence_status không hợp lệ: '{ev_status}'")
            
            if not data.get("locator"):
                errors.append(f"[{rel_path}] Thiếu 'locator' định vị vị trí văn bản")

        elif rec_type == "CONCEPT":
            topics = data.get("topic_codes", [])
            for t in topics:
                if t not in APPROVED_TOPIC_CODES:
                    errors.append(f"[{rel_path}] topic_code không hợp lệ: '{t}'")
            
            for s_id in data.get("source_ids", []):
                if s_id not in records_by_id:
                    errors.append(f"[{rel_path}] source_id tham chiếu '{s_id}' không tồn tại")
            for n_id in data.get("note_ids", []):
                if n_id not in records_by_id:
                    errors.append(f"[{rel_path}] note_id tham chiếu '{n_id}' không tồn tại")

        elif rec_type == "IDEA":
            topics = data.get("topic_codes", [])
            for t in topics:
                if t not in APPROVED_TOPIC_CODES:
                    errors.append(f"[{rel_path}] topic_code không hợp lệ: '{t}'")
            
            idea_status = data.get("status")
            if idea_status not in VALID_IDEA_STATUSES:
                errors.append(f"[{rel_path}] status của IDEA không hợp lệ: '{idea_status}'")
            
            for c_id in data.get("concept_ids", []):
                if c_id not in records_by_id:
                    errors.append(f"[{rel_path}] concept_id tham chiếu '{c_id}' không tồn tại")

        elif rec_type == "CONTENT":
            c_type = data.get("content_type")
            if c_type not in VALID_CONTENT_TYPES:
                errors.append(f"[{rel_path}] content_type không hợp lệ: '{c_type}'")
            
            ev_status = data.get("evidence_status")
            if ev_status not in VALID_EVIDENCE_STATUSES:
                errors.append(f"[{rel_path}] evidence_status không hợp lệ: '{ev_status}'")
            
            txt_status = data.get("status")
            if txt_status not in VALID_TXT_STATUSES:
                errors.append(f"[{rel_path}] status của TXT không hợp lệ: '{txt_status}'")
            
            # Kiểm tra Hard Gate G1: DIRECT_QUOTE phải có nguồn và VERIFIED_TEXT
            if c_type == "DIRECT_QUOTE":
                if ev_status != "VERIFIED_TEXT":
                    errors.append(f"[{rel_path}] DIRECT_QUOTE bắt buộc phải có evidence_status là 'VERIFIED_TEXT' (Hard Gate G1)")
                if not data.get("source_ids"):
                    errors.append(f"[{rel_path}] DIRECT_QUOTE bắt buộc phải có source_ids (Hard Gate G1)")
            
            # Kiểm tra Hard Gate G5: Quyền duyệt con người
            if txt_status == "APPROVED":
                if not data.get("approved_by") or not data.get("approved_at"):
                    errors.append(f"[{rel_path}] status là 'APPROVED' nhưng thiếu approved_by hoặc approved_at (Hard Gate G5, Ca T14)")
            
            if txt_status == "PUBLISHED":
                if not data.get("published_at"):
                    errors.append(f"[{rel_path}] status là 'PUBLISHED' nhưng thiếu published_at (Hard Gate G5)")

            # Kiểm tra liên kết tham chiếu
            for i_id in data.get("idea_ids", []):
                if i_id not in records_by_id:
                    errors.append(f"[{rel_path}] idea_id tham chiếu '{i_id}' không tồn tại")
            for s_id in data.get("source_ids", []):
                if s_id not in records_by_id:
                    errors.append(f"[{rel_path}] source_id tham chiếu '{s_id}' không tồn tại")

        elif rec_type == "RESEARCH_RUN":
            run_status = data.get("status")
            if run_status not in VALID_RUN_STATUSES:
                errors.append(f"[{rel_path}] status của RUN không hợp lệ: '{run_status}'")
            
            for s_id in data.get("found_source_ids", []):
                if s_id not in records_by_id:
                    errors.append(f"[{rel_path}] found_source_id tham chiếu '{s_id}' không tồn tại")
            for n_id in data.get("created_note_ids", []):
                if n_id not in records_by_id:
                    errors.append(f"[{rel_path}] created_note_id tham chiếu '{n_id}' không tồn tại")

    return errors, warnings, records_by_id

def main():
    print("=== HIYU ABYSS: KIỂM ĐỊNH TÍNH TOÀN VẸN & HARD GATES ===")
    errors, warnings, records = validate_all_records()
    print(f"Tổng số hồ sơ phát hiện: {len(records)}")
    
    if warnings:
        print(f"\n[CẢNH BÁO ({len(warnings)})]:")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print(f"\n[LỖI PHÁT HIỆN ({len(errors)})]:")
        for e in errors:
            print(f"  - {e}")
        print("\n=> KẾT QUẢ: THẤT BẠI (INTEGRITY FAILED)")
        sys.exit(1)
    else:
        print("\n=> KẾT QUẢ: THÀNH CÔNG (Tất cả hồ sơ hợp lệ, vượt qua Hard Gates)")
        sys.exit(0)

if __name__ == "__main__":
    main()
