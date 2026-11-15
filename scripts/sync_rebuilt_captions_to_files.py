import json
import csv
import os
import re

def main():
    json_path = 'scripts/rebuilt_150_captions.json'
    csv_path = 'scripts/tiktok_200_posts.csv'
    editorial_dir = 'editorial/content'

    with open(json_path, 'r', encoding='utf-8') as f:
        captions = json.load(f)

    print(f"Loaded {len(captions)} rebuilt captions.")

    # 1. Update CSV
    rows = []
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows.append(header)
        updated_csv_count = 0
        for row in reader:
            if not row:
                continue
            stt = row[0].strip()
            if stt in captions:
                row[3] = captions[stt]
                updated_csv_count += 1
            rows.append(row)

    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print(f"Updated {updated_csv_count} rows in {csv_path}.")

    # 2. Update Markdown files TXT-0001 to TXT-0150
    updated_md_count = 0
    missing_md_count = 0

    for stt_num in range(1, 151):
        stt_str = str(stt_num)
        id_str = f"TXT-{stt_num:04d}"
        md_path = os.path.join(editorial_dir, f"{id_str}.md")

        if not os.path.exists(md_path):
            missing_md_count += 1
            print(f"Warning: {md_path} does not exist.")
            continue

        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_caption = captions[stt_str]

        # Replace ## Diễn Giải & Chiêm Nghiệm Biên Tập block
        # Regex to match ## Diễn Giải & Chiêm Nghiệm Biên Tập up to the next ## header
        pattern = r'(## Diễn Giải & Chiêm Nghiệm Biên Tập\r?\n)([\s\S]*?)(?=\r?\n##)'
        
        if re.search(pattern, content):
            new_content = re.sub(pattern, rf'\g<1>{new_caption}\n', content)
            # Update updated_at if exists
            new_content = re.sub(r'updated_at:\s*".*?"', 'updated_at: "2026-11-15"', new_content)

            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_md_count += 1
        else:
            print(f"Header not matched in {id_str}.md")

    print(f"Updated {updated_md_count} markdown files in {editorial_dir} (Missing: {missing_md_count}).")

if __name__ == '__main__':
    main()
