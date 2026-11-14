import csv

with open("scripts/tiktok_100_posts.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    headers = next(reader)
    print("Old headers:")
    for idx, h in enumerate(headers):
        print(f"  {chr(65+idx)}: {h}")
    rows = list(reader)
    print(f"\nTotal rows in old csv: {len(rows)}")
    for r in range(5):
        row = rows[r]
        print(f"Row {r+1}:")
        print(f"  Col I ({headers[8]}): {row[8]}")
        print(f"  Col K ({headers[10]}): {row[10]}")
        print(f"  Col O ({headers[14]}): {row[14]}")
