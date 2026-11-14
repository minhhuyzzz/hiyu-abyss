import subprocess
import json

cols = [chr(65+i) for i in range(16)] # A to P
print("Checking data validation on row 2 for each column:")
for col in cols:
    cell = f"{col}2"
    cmd = f'gsheets readonly inspect-cell 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY "\'Kế Hoạch 100 Bài (TikTok Pipeline)\'!{cell}" --json'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    try:
        data = json.loads(res.stdout)
        dv = data.get("dataValidation")
        if dv:
            vals = [v.get("userEnteredValue") for v in dv.get("condition", {}).get("values", [])]
            print(f"Col {col} ({cell}): HAS DATA VALIDATION! Values: {vals}")
        else:
            print(f"Col {col} ({cell}): No data validation (Clean)")
    except Exception as e:
        print(f"Col {col}: parse error")
