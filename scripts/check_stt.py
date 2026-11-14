import subprocess
cmd = "gsheets readonly read 1kimL2BCQ602wNIKTj0sqgFoPW9gRjiUKtV3YvIES1JY \"'Kế Hoạch 100 Bài (TikTok Pipeline)'!A1:B15\""
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
for l in res.stdout.strip().split('\n'):
    print(repr(l))
