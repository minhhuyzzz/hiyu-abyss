import subprocess
import json

cmd = "gsheets readonly inspect-cell 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY \"'Kế Hoạch 100 Bài (TikTok Pipeline)'!I2\" --json"
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print("Inspect I2:", res.stdout[:500])

cmd2 = "gsheets readonly inspect-cell 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY \"'Kế Hoạch 100 Bài (TikTok Pipeline)'!K2\" --json"
res2 = subprocess.run(cmd2, shell=True, capture_output=True, text=True)
print("Inspect K2:", res2.stdout[:500])

cmd3 = "gsheets readonly inspect-cell 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY \"'Kế Hoạch 100 Bài (TikTok Pipeline)'!O2\" --json"
res3 = subprocess.run(cmd3, shell=True, capture_output=True, text=True)
print("Inspect O2:", res3.stdout[:500])
