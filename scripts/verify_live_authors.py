import subprocess

cmd = "gsheets readonly read 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY \"'Kế Hoạch 100 Bài (TikTok Pipeline)'!A1:F101\""
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
lines = [l.split('\t') for l in res.stdout.strip().split('\n')]
headers = lines[0]
print("Header Col E:", headers[4])

print("\n--- SAMPLE LIVE AUTHORS FROM GOOGLE SHEET ---")
for r in [1, 2, 4, 6, 8, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100]:
    row = lines[r]
    print(f"Row {row[0]:3s} | ID: {row[1]} | Nguồn: {row[4]:22s} | Tiêu đề: {row[2][:45]}...")

hiyu_in_live = sum(1 for row in lines[1:] if len(row) > 4 and "@hiyuabyss" in row[4])
print(f"\n[✓] Tổng số '@hiyuabyss' còn sót lại trên Google Sheet: {hiyu_in_live}")
