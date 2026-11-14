import subprocess
import json

cells = ['I1', 'I2', 'I3', 'I4', 'K1', 'K2', 'K3', 'K4', 'O1', 'O2', 'O3', 'O4']
for cell in cells:
    cmd = f'gsheets readonly inspect-cell 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY "\'Kế Hoạch 100 Bài (TikTok Pipeline)\'!{cell}" --json'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    try:
        data = json.loads(res.stdout)
        print(f"=== CELL {cell} ===")
        print("Value:", data.get("formattedValue") or data.get("effectiveValue"))
        print("Format:", data.get("effectiveFormat", {}).get("wrapStrategy"))
    except Exception as e:
        print(f"Cell {cell} raw:", res.stdout[:200])
