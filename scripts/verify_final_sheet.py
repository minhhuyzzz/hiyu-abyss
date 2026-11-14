import subprocess
import json

cells = ['I2', 'I5', 'I10', 'I20', 'K2', 'K5', 'K10', 'K20', 'O2', 'O5', 'O10', 'O20', 'P2', 'P5', 'P10', 'P20']
for c in cells:
    cmd = f'gsheets readonly inspect-cell 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY "\'Kế Hoạch 100 Bài (TikTok Pipeline)\'!{c}" --json'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    d = json.loads(res.stdout)
    dv = 'DV: YES' if 'dataValidation' in d else 'DV: NO'
    val = d.get('formattedValue', '')
    print(f"{c:4s} | {dv} | {val[:35]}")
