import urllib.request
import urllib.parse
import json
import time

test_titles = [
    "File:Carl Spitzweg - Der Bücherwurm (Exemplar aus der Sammlung Georg Schäfer).jpg",
    "File:Johannes Vermeer - The Astronomer - WGA24685.jpg",
    "File:Johannes Vermeer - Girl reading a letter at an open window - Google Art Project.jpg",
    "File:The Milkmaid by Johannes Vermeer.jpg",
    "File:Claude Monet - The Artist's Garden at Giverny.jpg",
    "File:Claude Monet - Water Lilies - Google Art Project.jpg",
    "File:John Singer Sargent - Carnation, Lily, Lily, Rose - Google Art Project.jpg",
    "File:John Singer Sargent - Breakfast in the Loggia.jpg",
    "File:Gustav Klimt - Bauerngarten (Blumengarten) - Google Art Project.jpg",
    "File:Pierre-Auguste Renoir - Two Sisters (On the Terrace) - Google Art Project.jpg",
    "File:Winslow Homer - The Blue Boat.jpg",
    "File:Carl Larsson - Frukost under stora björken (1896).jpg",
    "File:Carl Larsson - Blomsterfönstret (1894).jpg",
    "File:Jean Siméon Chardin - The House of Cards - National Gallery London.jpg",
    "File:Mary Stevenson Cassatt - The Cup of Tea - 1922.604 - Metropolitan Museum of Art.jpg"
]

url = "https://commons.wikimedia.org/w/api.php?action=query&format=json&titles=" + urllib.parse.quote('|'.join(test_titles)) + "&prop=imageinfo&iiprop=url|size&iiurlwidth=1920"
req = urllib.request.Request(url, headers={"User-Agent": "HiyuAbyssBot/1.0 (contact: admin@hiyuabyss.local)"})

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode())
        pages = data.get("query", {}).get("pages", {})
        print(f"Total resolved pages: {len(pages)}")
        for pid, p in pages.items():
            title = p.get("title", "")
            info = p.get("imageinfo", [{}])[0]
            thumb = info.get("thumburl") or info.get("url")
            print(f"{title}: {thumb is not None} -> {thumb[:70] if thumb else 'MISSING'}")
except Exception as e:
    print("Error:", e)
