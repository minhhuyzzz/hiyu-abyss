import subprocess

cmd = "gsheets readonly read 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY \"'Kế Hoạch 100 Bài (TikTok Pipeline)'!A1:P101\""
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
lines = [l.split('\t') for l in res.stdout.strip().split('\n')]
print(f"Total lines returned: {len(lines)}")
if not lines or not lines[0]:
    print("No data")
    exit(0)

headers = lines[0]
for idx, h in enumerate(headers):
    col_letter = chr(65 + idx)
    print(f"Col {col_letter}: {h}")

# Check Col I, K, O across all rows
col_I_idx = 8   # Col I
col_K_idx = 10  # Col K
col_O_idx = 14  # Col O

print("\n--- SAMPLE ROWS (1 to 15) ---")
for r_idx in range(1, min(16, len(lines))):
    row = lines[r_idx]
    val_I = row[col_I_idx] if len(row) > col_I_idx else "MISSING"
    val_K = row[col_K_idx] if len(row) > col_K_idx else "MISSING"
    val_O = row[col_O_idx] if len(row) > col_O_idx else "MISSING"
    fmt = row[6] if len(row) > 6 else ""
    print(f"Row {r_idx:02d} ({fmt}):")
    print(f"  Col I ({headers[col_I_idx]}): {val_I[:50]}")
    print(f"  Col K ({headers[col_K_idx]}): {val_K[:50]}")
    print(f"  Col O ({headers[col_O_idx]}): {val_O}")

print("\n--- CHECKING ANOMALIES IN COL I, K, O ACROSS ALL 100 ROWS ---")
for r_idx in range(1, len(lines)):
    row = lines[r_idx]
    val_I = row[col_I_idx] if len(row) > col_I_idx else ""
    val_K = row[col_K_idx] if len(row) > col_K_idx else ""
    val_O = row[col_O_idx] if len(row) > col_O_idx else ""
    fmt = row[6] if len(row) > 6 else ""
    
    # Check if Col I is empty
    if not val_I:
        print(f"Row {r_idx}: Col I is EMPTY")
    # Check if Col K is empty
    if not val_K:
        print(f"Row {r_idx}: Col K is EMPTY")
    # Check if Col O is empty
    if not val_O:
        print(f"Row {r_idx}: Col O is EMPTY")
