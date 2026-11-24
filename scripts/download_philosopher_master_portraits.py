import urllib.request
import urllib.parse
import json
import os
import time

CACHE_DIR = "assets/templates/raw_cache"
os.makedirs(CACHE_DIR, exist_ok=True)
USER_AGENT = "HiyuAbyssResearchBot/2.1 (https://hiyuabyss.com; contact: research@hiyuabyss.com)"

PORTRAIT_QUERIES = [
    ("marcus_aurelius_delacroix.jpg", "Delacroix Dernieres paroles de l'empereur Marc-Aurele"),
    ("marcus_aurelius_bust.jpg", "Marcus Aurelius bust Glyptothek Munich"),
    ("seneca_sanchez.jpg", "Manuel Dominguez Sanchez El suicidio de Seneca Prado"),
    ("seneca_rubens.jpg", "Peter Paul Rubens Dying Seneca Munich"),
    ("schopenhauer_lunteschutz.jpg", "Jules Lunteschutz Bildnis Arthur Schopenhauer"),
    ("schopenhauer_portrait.jpg", "Arthur Schopenhauer 1859 portrait"),
    ("nietzsche_munch.jpg", "Edvard Munch Friedrich Nietzsche 1906"),
    ("nietzsche_olde.jpg", "Hans Olde Friedrich Nietzsche"),
    ("epictetus_burghers.jpg", "Epictetus frontispiece Burghers 1715"),
    ("laozi_zhang_lu.jpg", "Zhang Lu Laozi Riding an Ox"),
    ("machiavelli_santi_di_tito.jpg", "Santi di Tito Ritratto di Niccolo Machiavelli"),
    ("franklin_duplessis.jpg", "Joseph Duplessis Benjamin Franklin MET"),
    ("franklin_martin.jpg", "David Martin Benjamin Franklin 1767"),
    ("aristotle_rembrandt.jpg", "Rembrandt Aristotle with a Bust of Homer MET"),
    ("carl_jung_study.jpg", "Carl Gustav Jung Bollingen"),
    ("viktor_frankl_portrait.jpg", "Viktor Frankl portrait"),
    ("erich_fromm_portrait.jpg", "Erich Fromm 1974 portrait"),
    ("thomas_cole_empire.jpg", "Thomas Cole Course of Empire Desolation"),
    ("bierstadt_mountains.jpg", "Albert Bierstadt Among the Sierra Nevada Mountains"),
    ("church_andes.jpg", "Frederic Edwin Church The Heart of the Andes"),
    ("turner_temeraire.jpg", "J.M.W. Turner The Fighting Temeraire"),
    ("monet_waterlilies.jpg", "Claude Monet Water Lilies 1916"),
    ("vermeer_geographer.jpg", "Johannes Vermeer The Geographer"),
    ("rembrandt_night_watch.jpg", "Rembrandt van Rijn Night Watch"),
    ("daumier_third_class.jpg", "Honore Daumier The Third-Class Carriage MET"),
    ("hammershoi_interior.jpg", "Vilhelm Hammershoi Interior Strandgade 30"),
    ("sargent_fiske_warren.jpg", "John Singer Sargent Mrs. Fiske Warren"),
    ("sorolla_beach.jpg", "Joaquin Sorolla Walk on the Beach 1909"),
    ("renoir_boating_party.jpg", "Pierre-Auguste Renoir Luncheon of the Boating Party"),
    ("pissarro_boulevard.jpg", "Camille Pissarro Boulevard Montmartre Spring Morning"),
    ("corot_bridge_narni.jpg", "Jean-Baptiste-Camille Corot The Bridge at Narni Louvre"),
    ("millet_gleaners.jpg", "Jean-Francois Millet The Gleaners Musee d'Orsay"),
    ("cezanne_mont_sainte.jpg", "Paul Cezanne Mont Sainte-Victoire Barnes"),
    ("degas_dance_class.jpg", "Edgar Degas The Dance Class MET"),
    ("morisot_cradle.jpg", "Berthe Morisot The Cradle Musee d'Orsay"),
    ("cassatt_cup_of_tea.jpg", "Mary Cassatt The Cup of Tea MET"),
    ("homer_breezing_up.jpg", "Winslow Homer Breezing Up National Gallery"),
    ("whistler_nocturne.jpg", "James Abbott McNeill Whistler Nocturne Blue and Gold"),
    ("redon_cyclops.jpg", "Odilon Redon The Cyclops Kroller-Muller"),
    ("gainsborough_blue_boy.jpg", "Thomas Gainsborough The Blue Boy Huntington"),
    ("constable_hay_wain.jpg", "John Constable The Hay Wain National Gallery"),
    ("friedrich_monk_by_the_sea.jpg", "Caspar David Friedrich The Monk by the Sea Alte Nationalgalerie"),
    ("friedrich_chalk_cliffs.jpg", "Caspar David Friedrich Chalk Cliffs on Rugen"),
    ("inness_autumn_oaks.jpg", "George Inness Autumn Oaks MET"),
    ("durand_kindred_spirits.jpg", "Asher Brown Durand Kindred Spirits Crystal Bridges"),
    ("kensett_lake_george.jpg", "John Frederick Kensett Lake George MET"),
    ("gifford_twilight_catskills.jpg", "Sanford Robinson Gifford Twilight in the Catskills"),
    ("cole_oxbow.jpg", "Thomas Cole The Oxbow MET"),
    ("heade_marsh.jpg", "Martin Johnson Heade Sunlight and Shadow The Newburyport Marshes"),
    ("lane_boston_harbor.jpg", "Fitz Henry Lane Boston Harbor")
]

def search_and_download(filename, query):
    save_path = os.path.join(CACHE_DIR, filename)
    if os.path.exists(save_path) and os.path.getsize(save_path) > 40000:
        print(f"Already exists: {filename}")
        return True
    try:
        search_url = "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=" + urllib.parse.quote(query) + "&srnamespace=6&format=json&srlimit=3"
        req = urllib.request.Request(search_url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode())
            items = data.get("query", {}).get("search", [])
            file_titles = [it["title"] for it in items if it["title"].startswith("File:") and not it["title"].lower().endswith((".svg", ".pdf", ".tif", ".ogg", ".webm"))]
            if not file_titles:
                print(f"No file found for: {query}")
                return False
            chosen = file_titles[0]
            info_url = "https://commons.wikimedia.org/w/api.php?action=query&format=json&titles=" + urllib.parse.quote(chosen) + "&prop=imageinfo&iiprop=url&iiurlwidth=2560"
            info_req = urllib.request.Request(info_url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(info_req, timeout=12) as info_resp:
                info_data = json.loads(info_resp.read().decode())
                page = list(info_data.get("query", {}).get("pages", {}).values())[0]
                img_info = page.get("imageinfo", [{}])[0]
                url = img_info.get("thumburl") or img_info.get("url")
                if not url:
                    return False
                img_req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(img_req, timeout=25) as img_resp:
                    content = img_resp.read()
                    if len(content) > 30000:
                        with open(save_path, "wb") as f:
                            f.write(content)
                        print(f"Downloaded: {filename} ({len(content)//1024} KB)")
                        return True
    except Exception as e:
        print(f"Error {filename}: {e}")
    return False

def main():
    print("=== DOWNLOADING MASTER ARTWORKS & PHILOSOPHER PORTRAITS ===")
    success = 0
    for fn, q in PORTRAIT_QUERIES:
        if search_and_download(fn, q):
            success += 1
        time.sleep(0.3)
    print(f"Finished: {success}/{len(PORTRAIT_QUERIES)} masterworks ready.")

if __name__ == '__main__':
    main()
