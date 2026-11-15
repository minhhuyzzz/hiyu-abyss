import csv
import json

def main():
    rows = list(csv.reader(open('scripts/tiktok_200_posts.csv', encoding='utf-8-sig')))
    batch_rows = rows[201:251]
    print(f"Number of rows to write: {len(batch_rows)}")
    print(f"First row (STT, ID, Title): {batch_rows[0][0]}, {batch_rows[0][1]}, {batch_rows[0][2][:30]}...")
    print(f"Last row (STT, ID, Title): {batch_rows[-1][0]}, {batch_rows[-1][1]}, {batch_rows[-1][2][:30]}...")

    req = [{
        "op": "write",
        "range": "'Kế Hoạch 200 Bài (TikTok Pipeline)'!A202:Q251",
        "data": batch_rows
    }]

    with open('scripts/sheet_batch_201_250.json', 'w', encoding='utf-8') as f:
        json.dump(req, f, ensure_ascii=False, indent=2)

    print("Successfully created scripts/sheet_batch_201_250.json")

if __name__ == '__main__':
    main()
