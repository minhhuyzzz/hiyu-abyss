import subprocess

cmd = "gsheets readonly read 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY \"'Kế Hoạch 100 Bài (TikTok Pipeline)'!A1:P101\""
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
lines = [l.split('\t') for l in res.stdout.strip().split('\n')]
headers = lines[0]
print("All Headers:")
for i, h in enumerate(headers):
    print(f"  {chr(65+i)}: {h}")

for idx in [8, 10, 14]:
    col_letter = chr(65 + idx)
    col_name = headers[idx]
    print(f"\n================ COLUMN {col_letter}: {col_name} ================")
    vals = []
    for r in range(1, len(lines)):
        val = lines[r][idx] if len(lines[r]) > idx else "MISSING"
        vals.append(val)
    
    empty_cnt = sum(1 for v in vals if not v or v == "-")
    print(f"Total rows: {len(vals)}, '-' or empty: {empty_cnt}")
    print("Sample rows:")
    for r in range(1, 16):
        val = lines[r][idx] if len(lines[r]) > idx else "MISSING"
        fmt = lines[r][6] if len(lines[r]) > 6 else ""
        print(f"  Row {r:02d} [{fmt}]: {val}")
