import subprocess

cmd = "gsheets readonly read 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY \"'Kế Hoạch 100 Bài (TikTok Pipeline)'!A1:P101\""
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
lines = [l.split('\t') for l in res.stdout.strip().split('\n')]
headers = lines[0]

print("=== CHECKING ALL 100 ROWS FOR COL I, K, O ===")
for r_idx in range(1, len(lines)):
    row = lines[r_idx]
    stt = row[0]
    post_id = row[1]
    title = row[2]
    fmt = row[6]
    s1 = row[7]
    s2 = row[8]
    s3 = row[9]
    full = row[10]
    theme = row[11]
    time_slot = row[12]
    date = row[13]
    phoianh = row[14]
    status = row[15] if len(row) > 15 else ""

    # Check potential issues in I (s2)
    # If Carousel 2 or 3, is s2 empty or '-'?
    if fmt in ["Carousel 2 trang", "Carousel 3 trang"] and (not s2 or s2 == "-"):
        print(f"ERROR Col I in Row {stt} ({post_id}): {fmt} but s2 is '{s2}'")

    # Check potential issues in K (full text)
    if not full or len(full) < 15:
        print(f"ERROR Col K in Row {stt} ({post_id}): full text too short or empty: '{full}'")

    # Check potential issues in O (phôi ảnh)
    if not phoianh:
        print(f"ERROR Col O in Row {stt} ({post_id}): phoianh is empty")
