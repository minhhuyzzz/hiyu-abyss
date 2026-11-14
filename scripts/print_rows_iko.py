import subprocess

cmd = "gsheets readonly read 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY \"'Kế Hoạch 100 Bài (TikTok Pipeline)'!A1:P31\""
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
lines = [l.split('\t') for l in res.stdout.strip().split('\n')]
headers = lines[0]

for idx in [8, 10, 14]:
    print(f"\n--- Column {chr(65+idx)}: {headers[idx]} ---")
    for r in range(1, 16):
        row = lines[r]
        print(f"R{row[0]:02s} [{row[6]}]: {row[idx]}")
