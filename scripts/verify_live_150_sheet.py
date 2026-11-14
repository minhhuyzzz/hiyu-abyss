import subprocess
import json

cmd = "gsheets readonly read 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY \"'Kế Hoạch 150 Bài (TikTok Pipeline)'!A1:P152\""
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
lines = [l.split('\t') for l in res.stdout.strip().split('\n')]
print(f"Total lines in live sheet: {len(lines)}")
headers = lines[0]
print("Headers:", headers)

print("\n--- SAMPLE ROWS (NEW POSTS 101 to 150) ---")
for r_idx in [101, 110, 120, 130, 140, 150]:
    row = lines[r_idx]
    print(f"Row {row[0]:3s} | ID: {row[1]} | Tác giả: {row[4]:20s} | Phôi: {row[14]:8s} | Tiêu đề: {row[2][:40]}...")

# Check any cell validation errors on sample cells in new range
for c in ['I102', 'K102', 'O102', 'P102', 'I150', 'K150', 'O150', 'P150']:
    cmd_insp = f'gsheets readonly inspect-cell 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY "\'Kế Hoạch 150 Bài (TikTok Pipeline)\'!{c}\" --json'
    r_insp = subprocess.run(cmd_insp, shell=True, capture_output=True, text=True)
    d = json.loads(r_insp.stdout)
    dv = "DV: YES" if "dataValidation" in d else "DV: NO"
    val = d.get("formattedValue", "")
    print(f"Cell {c:5s} | {dv:7s} | Val: {val[:30]}")
