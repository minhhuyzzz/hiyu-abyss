import urllib.request
import urllib.parse
import json

queries = [
    ("theme_61", "Henriette Ronner-Knip The Globetrotters"),
    ("theme_62", "Henriette Ronner-Knip Kittens"),
    ("theme_63", "Henriette Ronner-Knip"),
    ("theme_64", "Beatrix Potter Tailor of Gloucester"),
    ("theme_65", "Beatrix Potter Peter Rabbit"),
    ("theme_66", "Arthur Rackham Wind in the Willows"),
    ("theme_67", "Carl Spitzweg Der Bucherwurm"),
    ("theme_68", "Johannes Vermeer The Astronomer"),
    ("theme_69", "Winslow Homer Fresh Air"),
    ("theme_70", "Carl Larsson Lisbeth"),
    ("theme_71", "Johannes Vermeer Girl reading a letter"),
    ("theme_72", "Jean-Simeon Chardin House of Cards"),
    ("theme_73", "Claude Monet Giverny irises"),
    ("theme_74", "Claude Monet Nympheas 1906"),
    ("theme_75", "John Singer Sargent Carnation Lily Lily Rose"),
    ("theme_76", "John Singer Sargent Breakfast in the Loggia"),
    ("theme_77", "Gustav Klimt Bauerngarten"),
    ("theme_78", "John Singer Sargent Grand Canal Venice"),
    ("theme_79", "Mary Cassatt The Cup of Tea"),
    ("theme_80", "Carl Larsson Blomsterfonstret"),
    ("theme_81", "Carl Larsson Lathornet"),
    ("theme_82", "Johannes Vermeer The Milkmaid"),
    ("theme_83", "Claude Monet Le Dejeuner 1868"),
    ("theme_84", "Jean-Simeon Chardin Maitresse d'ecole"),
    ("theme_85", "Winslow Homer The Blue Boat"),
    ("theme_86", "Carl Larsson Frukost under stora bjorken"),
    ("theme_87", "Berthe Morisot Dans la salle a manger"),
    ("theme_88", "Pierre-Auguste Renoir Two Sisters"),
    ("theme_89", "Claude Lorrain Landscape with Cattle and Figures"),
    ("theme_90", "Carl Spitzweg Der Briefbote")
]

results = {}
for theme_id, q in queries:
    url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(q)}&format=json&srlimit=5"
    req = urllib.request.Request(url, headers={"User-Agent": "HiyuAbyssBot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            search_items = data.get("query", {}).get("search", [])
            results[theme_id] = [item["title"] for item in search_items if item["title"].startswith("File:")]
    except Exception as e:
        results[theme_id] = [str(e)]

for tid, files in results.items():
    print(f"{tid}:")
    for f in files[:2]:
        print(f"   {f}")

with open("scripts/wikimedia_search_charming.json", "w", encoding="utf-8") as out_f:
    json.dump(results, out_f, indent=2, ensure_ascii=False)
