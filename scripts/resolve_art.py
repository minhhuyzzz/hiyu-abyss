import urllib.request
import urllib.parse
import json
import time

searches = [
    ("Carl Spitzweg Bucherwurm", "theme_67"),
    ("Vermeer Milkmaid", "theme_82"),
    ("Vermeer Girl reading letter", "theme_71"),
    ("Monet Garden Giverny", "theme_73"),
    ("Carl Larsson Blomsterfonstret", "theme_80"),
    ("Carl Larsson Lisbeth", "theme_70"),
    ("Carl Larsson Frukost stora bjorken", "theme_86"),
    ("Henriette Ronner-Knip cats", "theme_61"),
    ("Henriette Ronner-Knip kittens", "theme_62"),
    ("Henriette Ronner-Knip", "theme_63"),
    ("Beatrix Potter mice", "theme_64"),
    ("Beatrix Potter Peter Rabbit", "theme_65"),
    ("Arthur Rackham", "theme_66"),
    ("Chardin House of Cards", "theme_72"),
    ("Sargent Breakfast Loggia", "theme_76"),
    ("Sargent Grand Canal Venice", "theme_78"),
    ("Klimt Bauerngarten", "theme_77"),
    ("Mary Cassatt Cup of Tea", "theme_79"),
    ("Carl Larsson Cosy Corner", "theme_81"),
    ("Monet Le Dejeuner 1868", "theme_83"),
    ("Chardin Maitresse d'ecole", "theme_84"),
    ("Winslow Homer Blue Boat", "theme_85"),
    ("Berthe Morisot salle a manger", "theme_87"),
    ("Winslow Homer Fresh Air", "theme_69"),
    ("Claude Lorrain sunset landscape", "theme_89"),
    ("Spitzweg Briefbote", "theme_90")
]

results = {}
for q, tid in searches:
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&prop=imageinfo&iiprop=url&iiurlwidth=1920&format=json&gsrlimit=3"
    req = urllib.request.Request(url, headers={"User-Agent": "HiyuAbyssBot/1.0 (contact: admin@hiyuabyss.local)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            pages = data.get("query", {}).get("pages", {})
            for pid, p in pages.items():
                title = p.get("title")
                info = p.get("imageinfo", [{}])[0]
                url_img = info.get("thumburl") or info.get("url")
                if title and url_img:
                    results[tid] = (title, url_img)
                    print(f"FOUND {tid} ({q}): {title}")
                    break
    except Exception as e:
        print(f"Error for {tid}: {e}")
    time.sleep(1.0)

print(f"\nTotal found: {len(results)} / {len(searches)}")
with open("scripts/resolved_charming_art.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
