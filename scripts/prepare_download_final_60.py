import urllib.request
import urllib.parse
import json
import os
import time

HEADERS = {
    'User-Agent': 'HiyuAbyssResearchBot/1.0 (https://hiyuabyss.com; research@hiyuabyss.com)'
}

EXTRA_CANDIDATES = [
    ('Albrecht Dürer', 'Feast of the Rosary', 'National Gallery Prague', '1506', 'Durer Feast of the Rosary'),
    ('Albrecht Dürer', 'Self-Portrait at 28', 'Alte Pinakothek, Munich', '1500', 'Durer Self-Portrait Alte Pinakothek'),
    ('Lucas Cranach the Elder', 'The Judgment of Paris', 'Metropolitan Museum of Art', '1528', 'Lucas Cranach Judgment of Paris Met'),
    ('Hans Holbein the Younger', 'The Ambassadors', 'National Gallery, London', '1533', 'Holbein The Ambassadors National Gallery'),
    ('Hans Holbein the Younger', 'Portrait of Henry VIII', 'Galleria Nazionale d Arte Antica', '1540', 'Holbein Portrait Henry VIII Rome'),
    ('Lorenzo Lotto', 'Portrait of a Young Man', 'Uffizi Gallery, Florence', '1505', 'Lorenzo Lotto Portrait Young Man Uffizi'),
    ('Bronzino', 'Portrait of Eleonora of Toledo', 'Uffizi Gallery, Florence', '1545', 'Bronzino Eleonora of Toledo Uffizi'),
    ('Pieter Brueghel the Younger', 'The Village Lawyer', 'Museum of Fine Arts, Ghent', '1621', 'Brueghel Village Lawyer'),
    ('Hendrick Avercamp', 'A Scene on the Ice near a Town', 'National Gallery, London', '1615', 'Avercamp Scene on the Ice National Gallery'),
    ('Rachel Ruysch', 'Flowers in a Glass Vase', 'Mauritshuis, The Hague', '1700', 'Rachel Ruysch Flowers Glass Vase Mauritshuis'),
    ('Willem Kalf', 'Still Life with a Chinese Bowl', 'Gemaldegalerie, Berlin', '1662', 'Willem Kalf Still Life Chinese Bowl Berlin'),
    ('Nicolaes Maes', 'The Eavesdropper', 'Dordrechts Museum', '1657', 'Nicolaes Maes Eavesdropper'),
    ('Francesco Guardi', 'View of the Venetian Lagoon', 'Wallace Collection, London', '1770', 'Guardi Venetian Lagoon Wallace'),
    ('Joshua Reynolds', 'The Age of Innocence', 'Tate Britain, London', '1788', 'Joshua Reynolds Age of Innocence'),
    ('Joshua Reynolds', 'Sarah Siddons as the Tragic Muse', 'Huntington Library', '1784', 'Reynolds Sarah Siddons Tragic Muse'),
    ('George Stubbs', 'Whistlejacket', 'National Gallery, London', '1762', 'George Stubbs Whistlejacket'),
    ('Henry Fuseli', 'The Nightmare', 'Detroit Institute of Arts', '1781', 'Henry Fuseli Nightmare Detroit'),
    ('John Martin', 'The Great Day of His Wrath', 'Tate Britain, London', '1851-1853', 'John Martin Great Day of His Wrath'),
    ('Caspar David Friedrich', 'Chalk Cliffs on Rugen', 'Museum Oskar Reinhart', '1818', 'Friedrich Chalk Cliffs on Rugen'),
    ('Caspar David Friedrich', 'The Abbey in the Oakwood', 'Alte Nationalgalerie, Berlin', '1809-1810', 'Friedrich Abbey in the Oakwood'),
    ('Carl Blechen', 'The Forest Path', 'Alte Nationalgalerie, Berlin', '1835', 'Carl Blechen Forest Path'),
    ('Thomas Cole', 'The Voyage of Life Youth', 'National Gallery of Art, Washington', '1842', 'Thomas Cole Voyage of Life Youth'),
    ('Frederic Edwin Church', 'Niagara', 'National Gallery of Art, Washington', '1857', 'Frederic Edwin Church Niagara'),
    ('Frederic Edwin Church', 'Twilight in the Wilderness', 'Cleveland Museum of Art', '1860', 'Frederic Edwin Church Twilight Wilderness'),
    ('Albert Bierstadt', 'The Rocky Mountains, Lander Peak', 'Metropolitan Museum of Art', '1863', 'Albert Bierstadt Rocky Mountains Lander Peak'),
    ('Albert Bierstadt', 'Storm in the Mountains', 'Museum of Fine Arts, Boston', '1870', 'Albert Bierstadt Storm in the Mountains'),
    ('Martin Johnson Heade', 'Approaching Thunder Storm', 'Metropolitan Museum of Art', '1859', 'Martin Johnson Heade Approaching Thunder Storm'),
    ('Sanford Robinson Gifford', 'A Gorge in the Mountains', 'Metropolitan Museum of Art', '1862', 'Gifford Gorge in the Mountains'),
    ('John Frederick Kensett', 'Eatons Neck, Long Island', 'Metropolitan Museum of Art', '1872', 'Kensett Eatons Neck Long Island'),
    ('George Inness', 'The Lackawanna Valley', 'National Gallery of Art, Washington', '1855', 'George Inness Lackawanna Valley'),
    ('Winslow Homer', 'Snap the Whip', 'Butler Institute of American Art', '1872', 'Winslow Homer Snap the Whip'),
    ('Winslow Homer', 'The Life Line', 'Philadelphia Museum of Art', '1884', 'Winslow Homer Life Line Philadelphia'),
    ('Thomas Eakins', 'The Champion Single Sculls', 'Metropolitan Museum of Art', '1871', 'Thomas Eakins Champion Single Sculls'),
    ('Childe Hassam', 'The Avenue in the Rain', 'White House Collection', '1917', 'Childe Hassam Avenue in the Rain'),
    ('Childe Hassam', 'Boston Common at Twilight', 'Museum of Fine Arts, Boston', '1885-1886', 'Childe Hassam Boston Common Twilight'),
    ('Mary Cassatt', 'Mother and Child', 'Metropolitan Museum of Art', '1890', 'Mary Cassatt Mother and Child Met'),
    ('John Singer Sargent', 'Lady Agnew of Lochnaw', 'Scottish National Gallery', '1892', 'Sargent Lady Agnew of Lochnaw'),
    ('John Singer Sargent', 'The Daughters of Edward Darley Boit', 'Museum of Fine Arts, Boston', '1882', 'Sargent Daughters Edward Darley Boit'),
    ('James Tissot', 'The Shop Girl', 'Art Gallery of Ontario', '1883-1885', 'James Tissot Shop Girl'),
    ('Arthur Hughes', 'April Love', 'Tate Britain, London', '1855-1856', 'Arthur Hughes April Love Tate'),
    ('Ford Madox Brown', 'The Last of England', 'Birmingham Museum and Art Gallery', '1855', 'Ford Madox Brown Last of England'),
    ('William Holman Hunt', 'The Awakening Conscience', 'Tate Britain, London', '1853', 'William Holman Hunt Awakening Conscience'),
    ('Gustave Moreau', 'The Apparition', 'Musee d Orsay, Paris', '1876', 'Gustave Moreau Apparition Musee d Orsay'),
    ('Puvis de Chavannes', 'The Poor Fisherman', 'Musee d Orsay, Paris', '1881', 'Puvis de Chavannes Poor Fisherman'),
    ('Arnold Böcklin', 'Self-Portrait with Death Playing the Fiddle', 'Alte Nationalgalerie, Berlin', '1872', 'Bocklin Self-Portrait Death Fiddle'),
    ('Fernand Khnopff', 'The Caress', 'Royal Museums of Fine Arts of Belgium', '1896', 'Fernand Khnopff The Caress'),
    ('Franz von Stuck', 'The Sin', 'Neue Pinakothek, Munich', '1893', 'Franz von Stuck The Sin'),
    ('Gustav Klimt', 'Judith and the Head of Holofernes', 'Belvedere, Vienna', '1901', 'Gustav Klimt Judith Head Holofernes'),
    ('Gustav Klimt', 'Death and Life', 'Leopold Museum, Vienna', '1915', 'Gustav Klimt Death and Life Leopold'),
    ('Egon Schiele', 'Self-Portrait with Chinese Lantern Plant', 'Leopold Museum, Vienna', '1912', 'Egon Schiele Self-Portrait Chinese Lantern Plant'),
    ('Edvard Munch', 'Madonna', 'Munch Museum, Oslo', '1894-1895', 'Edvard Munch Madonna Munch Museum'),
    ('Edvard Munch', 'Vampire', 'Munch Museum, Oslo', '1893-1895', 'Edvard Munch Vampire Munch Museum'),
    ('Henri de Toulouse-Lautrec', 'Jane Avril', 'Museum of Modern Art, New York', '1893', 'Toulouse-Lautrec Jane Avril'),
    ('Pierre Bonnard', 'The Dining Room in the Country', 'Minneapolis Institute of Art', '1913', 'Pierre Bonnard Dining Room in the Country'),
    ('Édouard Vuillard', 'The Seamstress', 'Metropolitan Museum of Art', '1893', 'Vuillard The Seamstress Met'),
    ('Felix Vallotton', 'The Ball', 'Musee d Orsay, Paris', '1899', 'Felix Vallotton The Ball Orsay'),
    ('Odilon Redon', 'Buddha', 'Musee d Orsay, Paris', '1904', 'Odilon Redon Buddha Orsay'),
    ('Vasily Surikov', 'Boyarynya Morozova', 'Tretyakov Gallery, Moscow', '1887', 'Vasily Surikov Boyarynya Morozova'),
    ('Viktor Vasnetsov', 'Alyonushka', 'Tretyakov Gallery, Moscow', '1881', 'Viktor Vasnetsov Alyonushka'),
    ('Arkhip Kuindzhi', 'After a Rain', 'Tretyakov Gallery, Moscow', '1879', 'Arkhip Kuindzhi After a Rain'),
    ('Isaac Levitan', 'Over Eternal Peace', 'Tretyakov Gallery, Moscow', '1894', 'Isaac Levitan Over Eternal Peace'),
    ('Mikhail Vrubel', 'The Demon Seated', 'Tretyakov Gallery, Moscow', '1890', 'Mikhail Vrubel Demon Seated'),
    ('Valentin Serov', 'Girl with Peaches', 'Tretyakov Gallery, Moscow', '1887', 'Valentin Serov Girl with Peaches'),
    ('Konstantin Korovin', 'In the Boat', 'Tretyakov Gallery, Moscow', '1888', 'Konstantin Korovin In the Boat'),
    ('Anders Zorn', 'Midsummer Dance', 'Nationalmuseum, Stockholm', '1897', 'Anders Zorn Midsummer Dance'),
    ('Carl Larsson', 'A Studio Idyll', 'Nationalmuseum, Stockholm', '1885', 'Carl Larsson Studio Idyll'),
    ('Vilhelm Hammershøi', 'Interior with Young Man Reading', 'Hirschsprung Collection', '1898', 'Hammershoi Interior with Young Man Reading')
]

def search_wikimedia(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrlimit=3&prop=imageinfo&iiprop=url|size&gsrsearch={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            data = json.loads(res.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            best_url = None
            max_size = 0
            for pid, pdata in pages.items():
                if 'imageinfo' in pdata and len(pdata['imageinfo']) > 0:
                    info = pdata['imageinfo'][0]
                    u = info.get('url', '')
                    sz = info.get('size', 0)
                    if sz > 200000 and ('.jpg' in u.lower() or '.jpeg' in u.lower()):
                        if sz > max_size:
                            max_size = sz
                            best_url = u.split('?')[0]
            return best_url, max_size
    except Exception as e:
        return None, 0

def main():
    out_file = "scripts/final_verified_artworks.json"
    verified_list = []
    
    print(f"Searching Wikimedia for {len(EXTRA_CANDIDATES)} candidates...")
    for idx, (artist, title, museum, year, query) in enumerate(EXTRA_CANDIDATES):
        if len(verified_list) >= 70:
            break
        url, sz = search_wikimedia(query)
        if url and sz > 200000:
            verified_list.append({
                "artist": artist,
                "title": title,
                "museum": museum,
                "year": year,
                "url": url,
                "size_kb": sz // 1024,
                "safe_filename": f"final_art_{len(verified_list)+1:03d}_{title.lower().replace(' ', '_')[:25]}.jpg"
            })
            print(f"[{len(verified_list)}/70] FOUND: {title} by {artist} ({sz//1024} KB)")
        else:
            print(f"[-] SKIPPED: {title} by {artist}")
        time.sleep(0.12)
        
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(verified_list, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(verified_list)} verified artworks to {out_file}!")

if __name__ == "__main__":
    main()
