import json
import subprocess
import os

with open('scripts/verified_artworks_download_list.json', 'r', encoding='utf-8') as f:
    artworks = json.load(f)

test_dir = 'assets/templates/fresh_cache_151'
os.makedirs(test_dir, exist_ok=True)

for art in artworks[:3]:
    fn = art['safe_filename']
    url = art['url']
    dest = os.path.join(test_dir, fn)
    title = art['title']
    size = art['size_kb']
    print(f"Downloading {title} ({size} KB)...")
    cmd = ['curl.exe', '-s', '-A', 'HiyuAbyssResearchBot/1.0 (https://hiyuabyss.com; research@hiyuabyss.com)', url, '-o', dest]
    res = subprocess.run(cmd)
    if os.path.exists(dest):
        actual_kb = os.path.getsize(dest) // 1024
        print(f"   Saved {fn} ({actual_kb} KB)")
