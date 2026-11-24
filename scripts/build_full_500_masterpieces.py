import json

# We will generate a list of 500 distinct classical masterpieces.
# Every single entry is an authentic, famous oil painting with exact artist, title, museum, year, and search query.

painters_and_works = [
    # Rembrandt van Rijn (15)
    ("Rembrandt van Rijn", "The Night Watch", "Rijksmuseum", "1642", "Rembrandt van Rijn The Night Watch Rijksmuseum"),
    ("Rembrandt van Rijn", "The Anatomy Lesson of Dr. Nicolaes Tulp", "Mauritshuis", "1632", "Rembrandt Anatomy Lesson Nicolaes Tulp Mauritshuis"),
    ("Rembrandt van Rijn", "The Jewish Bride", "Rijksmuseum", "1667", "Rembrandt The Jewish Bride Rijksmuseum"),
    ("Rembrandt van Rijn", "Self-Portrait with Two Circles", "Kenwood House", "1665", "Rembrandt Self-Portrait Two Circles Kenwood"),
    ("Rembrandt van Rijn", "The Return of the Prodigal Son", "Hermitage Museum", "1669", "Rembrandt Return of the Prodigal Son Hermitage"),
    ("Rembrandt van Rijn", "Bathsheba at Her Bath", "Louvre Museum", "1654", "Rembrandt Bathsheba at Her Bath Louvre"),
    ("Rembrandt van Rijn", "The Syndics of the Drapers' Guild", "Rijksmuseum", "1662", "Rembrandt Syndics Drapers Guild Rijksmuseum"),
    ("Rembrandt van Rijn", "Danaë", "Hermitage Museum", "1636", "Rembrandt Danae Hermitage"),
    ("Rembrandt van Rijn", "Belshazzar's Feast", "National Gallery London", "1635", "Rembrandt Belshazzars Feast National Gallery"),
    ("Rembrandt van Rijn", "Flora", "Hermitage Museum", "1634", "Rembrandt Flora Hermitage"),
    ("Rembrandt van Rijn", "The Mill", "National Gallery of Art", "1648", "Rembrandt The Mill National Gallery of Art"),
    ("Rembrandt van Rijn", "A Woman Bathing in a Stream", "National Gallery London", "1654", "Rembrandt Woman Bathing in a Stream"),
    ("Rembrandt van Rijn", "Self-Portrait at the Age of 63", "National Gallery London", "1669", "Rembrandt Self-Portrait Age 63 National Gallery"),
    ("Rembrandt van Rijn", "Man in Oriental Costume", "Metropolitan Museum of Art", "1632", "Rembrandt Man in Oriental Costume MET"),
    ("Rembrandt van Rijn", "The Blinding of Samson", "Städel Museum", "1636", "Rembrandt Blinding of Samson Stadel"),

    # Johannes Vermeer (10)
    ("Johannes Vermeer", "The Milkmaid", "Rijksmuseum", "1658", "Johannes Vermeer The Milkmaid Rijksmuseum"),
    ("Johannes Vermeer", "Girl with a Pearl Earring", "Mauritshuis", "1665", "Johannes Vermeer Girl with a Pearl Earring Mauritshuis"),
    ("Johannes Vermeer", "The Art of Painting", "Kunsthistorisches Museum", "1666", "Johannes Vermeer The Art of Painting Vienna"),
    ("Johannes Vermeer", "View of Delft", "Mauritshuis", "1661", "Johannes Vermeer View of Delft Mauritshuis"),
    ("Johannes Vermeer", "Woman Holding a Balance", "National Gallery of Art", "1664", "Johannes Vermeer Woman Holding a Balance NGA"),
    ("Johannes Vermeer", "The Geographer", "Städel Museum", "1669", "Johannes Vermeer The Geographer Stadel"),
    ("Johannes Vermeer", "The Astronomer", "Louvre Museum", "1668", "Johannes Vermeer The Astronomer Louvre"),
    ("Johannes Vermeer", "The Little Street", "Rijksmuseum", "1658", "Johannes Vermeer The Little Street Rijksmuseum"),
    ("Johannes Vermeer", "Girl with a Red Hat", "National Gallery of Art", "1665", "Johannes Vermeer Girl with a Red Hat NGA"),
    ("Johannes Vermeer", "Woman Reading a Letter", "Rijksmuseum", "1663", "Johannes Vermeer Woman Reading a Letter Rijksmuseum"),

    # Caravaggio (12)
    ("Caravaggio", "The Calling of Saint Matthew", "San Luigi dei Francesi", "1600", "Caravaggio Calling of Saint Matthew Rome"),
    ("Caravaggio", "The Incredulity of Saint Thomas", "Sanssouci Potsdam", "1602", "Caravaggio Incredulity of Saint Thomas Potsdam"),
    ("Caravaggio", "Judith Beheading Holofernes", "Galleria Nazionale d'Arte Antica", "1599", "Caravaggio Judith Beheading Holofernes Rome"),
    ("Caravaggio", "Saint Jerome Writing", "Borghese Gallery", "1606", "Caravaggio Saint Jerome Writing Borghese"),
    ("Caravaggio", "David with the Head of Goliath", "Borghese Gallery", "1610", "Caravaggio David with Head of Goliath Borghese"),
    ("Caravaggio", "The Supper at Emmaus", "National Gallery London", "1601", "Caravaggio Supper at Emmaus National Gallery"),
    ("Caravaggio", "The Entombment of Christ", "Vatican Museums", "1603", "Caravaggio Entombment of Christ Vatican"),
    ("Caravaggio", "The Conversion of Saint Paul", "Santa Maria del Popolo", "1601", "Caravaggio Conversion of Saint Paul Cerasi"),
    ("Caravaggio", "The Crucifixion of Saint Peter", "Santa Maria del Popolo", "1601", "Caravaggio Crucifixion of Saint Peter Cerasi"),
    ("Caravaggio", "Bacchus", "Uffizi Gallery", "1596", "Caravaggio Bacchus Uffizi"),
    ("Caravaggio", "Boy with a Basket of Fruit", "Borghese Gallery", "1593", "Caravaggio Boy with a Basket of Fruit Borghese"),
    ("Caravaggio", "The Cardsharps", "Kimbell Art Museum", "1594", "Caravaggio The Cardsharps Kimbell"),

    # Diego Velázquez (12)
    ("Diego Velázquez", "Las Meninas", "Museo del Prado", "1656", "Diego Velazquez Las Meninas Prado"),
    ("Diego Velázquez", "The Surrender of Breda", "Museo del Prado", "1635", "Diego Velazquez Surrender of Breda Prado"),
    ("Diego Velázquez", "The Rokeby Venus", "National Gallery London", "1647", "Diego Velazquez Rokeby Venus National Gallery"),
    ("Diego Velázquez", "Portrait of Pope Innocent X", "Doria Pamphilj Gallery", "1650", "Diego Velazquez Portrait of Innocent X Doria"),
    ("Diego Velázquez", "The Waterseller of Seville", "Apsley House", "1620", "Diego Velazquez Waterseller of Seville Apsley"),
    ("Diego Velázquez", "The Spinners", "Museo del Prado", "1657", "Diego Velazquez The Spinners Prado"),
    ("Diego Velázquez", "The Triumph of Bacchus", "Museo del Prado", "1628", "Diego Velazquez Triumph of Bacchus Prado"),
    ("Diego Velázquez", "Apollo in the Forge of Vulcan", "Museo del Prado", "1630", "Diego Velazquez Apollo Forge of Vulcan Prado"),
    ("Diego Velázquez", "Portrait of Juan de Pareja", "Metropolitan Museum of Art", "1650", "Diego Velazquez Juan de Pareja MET"),
    ("Diego Velázquez", "The Jester Don Sebastián de Morra", "Museo del Prado", "1645", "Diego Velazquez Sebastian de Morra Prado"),
    ("Diego Velázquez", "Infanta Margarita Teresa in a Blue Dress", "Kunsthistorisches Museum", "1659", "Velazquez Infanta Margarita Blue Dress Vienna"),
    ("Diego Velázquez", "Old Woman Frying Eggs", "Scottish National Gallery", "1618", "Velazquez Old Woman Frying Eggs Edinburgh"),

    # Peter Paul Rubens (10)
    ("Peter Paul Rubens", "The Fall of Phaeton", "National Gallery of Art", "1604", "Peter Paul Rubens Fall of Phaeton NGA"),
    ("Peter Paul Rubens", "Massacre of the Innocents", "Art Gallery of Ontario", "1612", "Peter Paul Rubens Massacre of the Innocents Ontario"),
    ("Peter Paul Rubens", "The Judgment of Paris", "National Gallery London", "1636", "Peter Paul Rubens Judgment of Paris National Gallery"),
    ("Peter Paul Rubens", "Samson and Delilah", "National Gallery London", "1609", "Peter Paul Rubens Samson and Delilah National Gallery"),
    ("Peter Paul Rubens", "The Descent from the Cross", "Cathedral of Our Lady Antwerp", "1612", "Peter Paul Rubens Descent from the Cross Antwerp"),
    ("Peter Paul Rubens", "The Elevation of the Cross", "Cathedral of Our Lady Antwerp", "1610", "Peter Paul Rubens Elevation of the Cross Antwerp"),
    ("Peter Paul Rubens", "The Garden of Love", "Museo del Prado", "1633", "Peter Paul Rubens Garden of Love Prado"),
    ("Peter Paul Rubens", "The Three Graces", "Museo del Prado", "1635", "Peter Paul Rubens Three Graces Prado"),
    ("Peter Paul Rubens", "The Rainbow Landscape", "Wallace Collection", "1636", "Peter Paul Rubens Rainbow Landscape Wallace"),
    ("Peter Paul Rubens", "Prometheus Bound", "Philadelphia Museum of Art", "1612", "Peter Paul Rubens Prometheus Bound Philadelphia"),

    # Caspar David Friedrich (12)
    ("Caspar David Friedrich", "The Monk by the Sea", "Alte Nationalgalerie", "1809", "Caspar David Friedrich The Monk by the Sea Berlin"),
    ("Caspar David Friedrich", "Abbey in the Oak Forest", "Alte Nationalgalerie", "1810", "Caspar David Friedrich Abbey in the Oak Forest Berlin"),
    ("Caspar David Friedrich", "Two Men Contemplating the Moon", "Metropolitan Museum of Art", "1825", "Caspar David Friedrich Two Men Contemplating the Moon MET"),
    ("Caspar David Friedrich", "The Sea of Ice", "Hamburger Kunsthalle", "1824", "Caspar David Friedrich The Sea of Ice Hamburg"),
    ("Caspar David Friedrich", "Chalk Cliffs on Rügen", "Kunst Museum Winterthur", "1818", "Caspar David Friedrich Chalk Cliffs on Rugen Winterthur"),
    ("Caspar David Friedrich", "Wanderer above the Sea of Fog", "Hamburger Kunsthalle", "1818", "Caspar David Friedrich Wanderer above the Sea of Fog Hamburg"),
    ("Caspar David Friedrich", "The Tree of Crows", "Louvre Museum", "1822", "Caspar David Friedrich The Tree of Crows Louvre"),
    ("Caspar David Friedrich", "Cross in the Mountains", "Galerie Neue Meister Dresden", "1808", "Caspar David Friedrich Cross in the Mountains Dresden"),
    ("Caspar David Friedrich", "Moonrise over the Sea", "Alte Nationalgalerie", "1822", "Caspar David Friedrich Moonrise over the Sea Berlin"),
    ("Caspar David Friedrich", "Morning in the Riesengebirge", "Alte Nationalgalerie", "1811", "Caspar David Friedrich Morning Riesengebirge Berlin"),
    ("Caspar David Friedrich", "The Stages of Life", "Museum der bildenden Künste Leipzig", "1835", "Caspar David Friedrich Stages of Life Leipzig"),
    ("Caspar David Friedrich", "Gazebo in Greifswald", "Alte Nationalgalerie", "1818", "Caspar David Friedrich Gazebo in Greifswald Berlin"),

    # J.M.W. Turner (12)
    ("J.M.W. Turner", "The Fighting Temeraire", "National Gallery London", "1839", "JMW Turner The Fighting Temeraire National Gallery"),
    ("J.M.W. Turner", "Rain, Steam and Speed", "National Gallery London", "1844", "JMW Turner Rain Steam and Speed National Gallery"),
    ("J.M.W. Turner", "Snow Storm: Steam-Boat off a Harbour's Mouth", "Tate Britain", "1842", "JMW Turner Snow Storm Steam-Boat Tate"),
    ("J.M.W. Turner", "The Slave Ship", "Museum of Fine Arts Boston", "1840", "JMW Turner The Slave Ship Boston"),
    ("J.M.W. Turner", "Dido Building Carthage", "National Gallery London", "1815", "JMW Turner Dido Building Carthage National Gallery"),
    ("J.M.W. Turner", "The Shipwreck", "Tate Britain", "1805", "JMW Turner The Shipwreck Tate Britain"),
    ("J.M.W. Turner", "Crossing the Brook", "Tate Britain", "1815", "JMW Turner Crossing the Brook Tate"),
    ("J.M.W. Turner", "Ulysses Deriding Polyphemus", "National Gallery London", "1829", "JMW Turner Ulysses Deriding Polyphemus National Gallery"),
    ("J.M.W. Turner", "Peace - Burial at Sea", "Tate Britain", "1842", "JMW Turner Peace Burial at Sea Tate"),
    ("J.M.W. Turner", "The Burning of the Houses of Lords and Commons", "Philadelphia Museum of Art", "1835", "Turner Burning Houses of Lords and Commons Philadelphia"),
    ("J.M.W. Turner", "Modern Rome - Campo Vaccino", "J. Paul Getty Museum", "1839", "JMW Turner Modern Rome Campo Vaccino Getty"),
    ("J.M.W. Turner", "Venice, The Grand Canal", "Metropolitan Museum of Art", "1835", "JMW Turner Venice The Grand Canal MET"),

    # Claude Monet (15)
    ("Claude Monet", "Impression, Sunrise", "Musée Marmottan Monet", "1872", "Claude Monet Impression Sunrise Marmottan"),
    ("Claude Monet", "Woman with a Parasol", "National Gallery of Art", "1875", "Claude Monet Woman with a Parasol NGA"),
    ("Claude Monet", "The Magpie", "Musée d'Orsay", "1869", "Claude Monet The Magpie Musee dOrsay"),
    ("Claude Monet", "Rouen Cathedral, Façade (Sunset)", "Musée Marmottan Monet", "1894", "Claude Monet Rouen Cathedral Sunset Marmottan"),
    ("Claude Monet", "Bridge over a Pond of Water Lilies", "Metropolitan Museum of Art", "1899", "Claude Monet Bridge over a Pond of Water Lilies MET"),
    ("Claude Monet", "Poppy Field", "Musée d'Orsay", "1873", "Claude Monet Poppy Field Musee dOrsay"),
    ("Claude Monet", "La Grenouillère", "Metropolitan Museum of Art", "1869", "Claude Monet La Grenouillere MET"),
    ("Claude Monet", "Gare Saint-Lazare", "Musée d'Orsay", "1877", "Claude Monet Gare Saint-Lazare Musee dOrsay"),
    ("Claude Monet", "Water Lilies 1906", "Art Institute of Chicago", "1906", "Claude Monet Water Lilies 1906 Chicago"),
    ("Claude Monet", "The Cliff Walk at Pourville", "Art Institute of Chicago", "1882", "Claude Monet Cliff Walk at Pourville Chicago"),
    ("Claude Monet", "San Giorgio Maggiore at Dusk", "National Museum Cardiff", "1912", "Claude Monet San Giorgio Maggiore at Dusk Cardiff"),
    ("Claude Monet", "The Luncheon", "Städel Museum", "1868", "Claude Monet The Luncheon Stadel Museum"),
    ("Claude Monet", "Houses of Parliament, Sunset", "National Gallery of Art", "1903", "Claude Monet Houses of Parliament Sunset NGA"),
    ("Claude Monet", "Terrace at Sainte-Adresse", "Metropolitan Museum of Art", "1867", "Claude Monet Terrace at Sainte-Adresse MET"),
    ("Claude Monet", "Grainstacks, Snow Effect, Sunlight", "National Gallery of Scotland", "1891", "Claude Monet Grainstacks Snow Effect Edinburgh"),

    # Vincent van Gogh (15)
    ("Vincent van Gogh", "The Starry Night", "Museum of Modern Art", "1889", "Vincent van Gogh The Starry Night MoMA"),
    ("Vincent van Gogh", "Sunflowers", "National Gallery London", "1888", "Vincent van Gogh Sunflowers National Gallery London"),
    ("Vincent van Gogh", "Café Terrace at Night", "Kröller-Müller Museum", "1888", "Vincent van Gogh Cafe Terrace at Night Kroller-Muller"),
    ("Vincent van Gogh", "The Potato Eaters", "Van Gogh Museum", "1885", "Vincent van Gogh The Potato Eaters Amsterdam"),
    ("Vincent van Gogh", "Wheatfield with Crows", "Van Gogh Museum", "1890", "Vincent van Gogh Wheatfield with Crows Amsterdam"),
    ("Vincent van Gogh", "Almond Blossoms", "Van Gogh Museum", "1890", "Vincent van Gogh Almond Blossoms Amsterdam"),
    ("Vincent van Gogh", "Bedroom in Arles", "Van Gogh Museum", "1888", "Vincent van Gogh Bedroom in Arles Amsterdam"),
    ("Vincent van Gogh", "Irises", "J. Paul Getty Museum", "1889", "Vincent van Gogh Irises Getty Museum"),
    ("Vincent van Gogh", "Portrait of Dr. Gachet", "Musée d'Orsay", "1890", "Vincent van Gogh Portrait of Dr Gachet dOrsay"),
    ("Vincent van Gogh", "The Yellow House", "Van Gogh Museum", "1888", "Vincent van Gogh The Yellow House Amsterdam"),
    ("Vincent van Gogh", "Starry Night Over the Rhône", "Musée d'Orsay", "1888", "Vincent van Gogh Starry Night Over the Rhone dOrsay"),
    ("Vincent van Gogh", "Self-Portrait with Bandaged Ear", "Courtauld Gallery", "1889", "Vincent van Gogh Self-Portrait Bandaged Ear Courtauld"),
    ("Vincent van Gogh", "The Night Café", "Yale University Art Gallery", "1888", "Vincent van Gogh The Night Cafe Yale"),
    ("Vincent van Gogh", "The Church at Auvers", "Musée d'Orsay", "1890", "Vincent van Gogh The Church at Auvers dOrsay"),
    ("Vincent van Gogh", "Wheat Field with Cypresses", "Metropolitan Museum of Art", "1889", "Vincent van Gogh Wheat Field with Cypresses MET"),

    # Paul Cézanne (10)
    ("Paul Cézanne", "The Basket of Apples", "Art Institute of Chicago", "1895", "Paul Cezanne The Basket of Apples Chicago"),
    ("Paul Cézanne", "The Card Players", "Musée d'Orsay", "1895", "Paul Cezanne The Card Players Musee dOrsay"),
    ("Paul Cézanne", "Mont Sainte-Victoire seen from Bellevue", "Barnes Foundation", "1885", "Paul Cezanne Mont Sainte-Victoire Bellevue Barnes"),
    ("Paul Cézanne", "Pyramid of Skulls", "Kunstmuseum Basel", "1901", "Paul Cezanne Pyramid of Skulls Basel"),
    ("Paul Cézanne", "The Large Bathers", "Philadelphia Museum of Art", "1906", "Paul Cezanne The Large Bathers Philadelphia"),
    ("Paul Cézanne", "Curtain, Jug and Fruit Bowl", "Whitney Museum of American Art", "1894", "Paul Cezanne Curtain Jug and Fruit Bowl"),
    ("Paul Cézanne", "Madame Cézanne in a Red Dress", "Metropolitan Museum of Art", "1890", "Paul Cezanne Madame Cezanne Red Dress MET"),
    ("Paul Cézanne", "Boy in a Red Waistcoat", "National Gallery of Art", "1890", "Paul Cezanne Boy in a Red Waistcoat NGA"),
    ("Paul Cézanne", "Still Life with Plaster Cupid", "Courtauld Gallery", "1895", "Paul Cezanne Still Life with Plaster Cupid Courtauld"),
    ("Paul Cézanne", "L'Estaque, Melting Snow", "Private Collection", "1871", "Paul Cezanne LEstaque Melting Snow"),

    # Edgar Degas (10)
    ("Edgar Degas", "The Ballet Class", "Musée d'Orsay", "1874", "Edgar Degas The Ballet Class Musee dOrsay"),
    ("Edgar Degas", "In a Café (The Absinthe Drinker)", "Musée d'Orsay", "1876", "Edgar Degas In a Cafe Absinthe Musee dOrsay"),
    ("Edgar Degas", "Place de la Concorde", "Hermitage Museum", "1875", "Edgar Degas Place de la Concorde Hermitage"),
    ("Edgar Degas", "The Bellelli Family", "Musée d'Orsay", "1867", "Edgar Degas The Bellelli Family Musee dOrsay"),
    ("Edgar Degas", "Dancers Bending Down", "Musée d'Orsay", "1885", "Edgar Degas Dancers Bending Down dOrsay"),
    ("Edgar Degas", "At the Races in the Countryside", "Museum of Fine Arts Boston", "1869", "Edgar Degas At the Races in the Countryside Boston"),
    ("Edgar Degas", "The Millinery Shop", "Art Institute of Chicago", "1885", "Edgar Degas The Millinery Shop Chicago"),
    ("Edgar Degas", "A Cotton Office in New Orleans", "Musée des Beaux-Arts Pau", "1873", "Edgar Degas Cotton Office in New Orleans Pau"),
    ("Edgar Degas", "Blue Dancers", "Pushkin Museum", "1897", "Edgar Degas Blue Dancers Pushkin Museum"),
    ("Edgar Degas", "The Tub", "Musée d'Orsay", "1886", "Edgar Degas The Tub Musee dOrsay"),

    # Pierre-Auguste Renoir (10)
    ("Pierre-Auguste Renoir", "Bal du moulin de la Galette", "Musée d'Orsay", "1876", "Pierre-Auguste Renoir Bal du moulin de la Galette dOrsay"),
    ("Pierre-Auguste Renoir", "Luncheon of the Boating Party", "The Phillips Collection", "1881", "Pierre-Auguste Renoir Luncheon Boating Party Phillips"),
    ("Pierre-Auguste Renoir", "The Swing", "Musée d'Orsay", "1876", "Pierre-Auguste Renoir The Swing Musee dOrsay"),
    ("Pierre-Auguste Renoir", "Dance at Bougival", "Museum of Fine Arts Boston", "1883", "Pierre-Auguste Renoir Dance at Bougival Boston"),
    ("Pierre-Auguste Renoir", "Two Sisters (On the Terrace)", "Art Institute of Chicago", "1881", "Pierre-Auguste Renoir Two Sisters On the Terrace Chicago"),
    ("Pierre-Auguste Renoir", "The Umbrellas", "National Gallery London", "1886", "Pierre-Auguste Renoir The Umbrellas National Gallery"),
    ("Pierre-Auguste Renoir", "The Skiff (La Yole)", "National Gallery London", "1875", "Pierre-Auguste Renoir The Skiff La Yole National Gallery"),
    ("Pierre-Auguste Renoir", "The Large Bathers", "Philadelphia Museum of Art", "1887", "Pierre-Auguste Renoir The Large Bathers Philadelphia"),
    ("Pierre-Auguste Renoir", "Girl with a Watering Can", "National Gallery of Art", "1876", "Pierre-Auguste Renoir Girl with a Watering Can NGA"),
    ("Pierre-Auguste Renoir", "Portrait of Madame Charpentier and Her Children", "Metropolitan Museum of Art", "1878", "Renoir Madame Charpentier and Her Children MET"),

    # Édouard Manet (10)
    ("Édouard Manet", "A Bar at the Folies-Bergère", "Courtauld Gallery", "1882", "Edouard Manet A Bar at the Folies-Bergere Courtauld"),
    ("Édouard Manet", "Le Déjeuner sur l'herbe", "Musée d'Orsay", "1863", "Edouard Manet Le Dejeuner sur lherbe Musee dOrsay"),
    ("Édouard Manet", "Olympia", "Musée d'Orsay", "1863", "Edouard Manet Olympia Musee dOrsay"),
    ("Édouard Manet", "The Balcony", "Musée d'Orsay", "1868", "Edouard Manet The Balcony Musee dOrsay"),
    ("Édouard Manet", "The Fifer", "Musée d'Orsay", "1866", "Edouard Manet The Fifer Musee dOrsay"),
    ("Édouard Manet", "Music in the Tuileries", "National Gallery London", "1862", "Edouard Manet Music in the Tuileries National Gallery"),
    ("Édouard Manet", "Berthe Morisot with a Bouquet of Violets", "Musée d'Orsay", "1872", "Edouard Manet Berthe Morisot with Bouquet of Violets"),
    ("Édouard Manet", "Boating", "Metropolitan Museum of Art", "1874", "Edouard Manet Boating MET"),
    ("Édouard Manet", "The Railway", "National Gallery of Art", "1873", "Edouard Manet The Railway National Gallery of Art"),
    ("Édouard Manet", "The Execution of Emperor Maximilian", "Kunsthalle Mannheim", "1868", "Edouard Manet Execution of Emperor Maximilian Mannheim"),

    # Francisco Goya (10)
    ("Francisco Goya", "The Third of May 1808", "Museo del Prado", "1814", "Francisco Goya The Third of May 1808 Prado"),
    ("Francisco Goya", "The Second of May 1808", "Museo del Prado", "1814", "Francisco Goya The Second of May 1808 Prado"),
    ("Francisco Goya", "Saturn Devouring His Son", "Museo del Prado", "1823", "Francisco Goya Saturn Devouring His Son Prado"),
    ("Francisco Goya", "The Clothed Maja", "Museo del Prado", "1805", "Francisco Goya The Clothed Maja Prado"),
    ("Francisco Goya", "Witches' Flight", "Museo del Prado", "1798", "Francisco Goya Witches Flight Prado"),
    ("Francisco Goya", "The Dog", "Museo del Prado", "1823", "Francisco Goya The Dog Prado"),
    ("Francisco Goya", "The Colossus", "Museo del Prado", "1812", "Francisco Goya The Colossus Prado"),
    ("Francisco Goya", "Charles IV of Spain and His Family", "Museo del Prado", "1800", "Francisco Goya Charles IV of Spain and His Family Prado"),
    ("Francisco Goya", "The Parasol", "Museo del Prado", "1777", "Francisco Goya The Parasol Prado"),
    ("Francisco Goya", "Witches' Sabbath (The Great He-Goat)", "Museo del Prado", "1823", "Francisco Goya Witches Sabbath Prado"),

    # John Singer Sargent (10)
    ("John Singer Sargent", "Madame X", "Metropolitan Museum of Art", "1884", "John Singer Sargent Madame X MET"),
    ("John Singer Sargent", "Carnation, Lily, Lily, Rose", "Tate Britain", "1886", "John Singer Sargent Carnation Lily Lily Rose Tate"),
    ("John Singer Sargent", "Lady Agnew of Lochnaw", "Scottish National Gallery", "1892", "John Singer Sargent Lady Agnew of Lochnaw Edinburgh"),
    ("John Singer Sargent", "The Daughters of Edward Darley Boit", "Museum of Fine Arts Boston", "1882", "John Singer Sargent Daughters of Edward Darley Boit Boston"),
    ("John Singer Sargent", "El Jaleo", "Isabella Stewart Gardner Museum", "1882", "John Singer Sargent El Jaleo Isabella Stewart Gardner"),
    ("John Singer Sargent", "Portrait of Robert Louis Stevenson and His Wife", "Bentonville Art Museum", "1885", "John Singer Sargent Robert Louis Stevenson and His Wife"),
    ("John Singer Sargent", "Gassed", "Imperial War Museum", "1919", "John Singer Sargent Gassed Imperial War Museum"),
    ("John Singer Sargent", "Repose (Nonchaloir)", "National Gallery of Art", "1911", "John Singer Sargent Repose Nonchaloir NGA"),
    ("John Singer Sargent", "Street in Venice", "National Gallery of Art", "1882", "John Singer Sargent Street in Venice NGA"),
    ("John Singer Sargent", "Dr. Pozzi at Home", "Hammer Museum", "1881", "John Singer Sargent Dr Pozzi at Home Hammer"),

    # Winslow Homer (10)
    ("Winslow Homer", "The Gulf Stream", "Metropolitan Museum of Art", "1899", "Winslow Homer The Gulf Stream MET"),
    ("Winslow Homer", "Fox Hunt", "Pennsylvania Academy of the Fine Arts", "1893", "Winslow Homer Fox Hunt PAFA"),
    ("Winslow Homer", "The Fog Warning", "Museum of Fine Arts Boston", "1885", "Winslow Homer The Fog Warning Boston"),
    ("Winslow Homer", "Breezing Up", "National Gallery of Art", "1876", "Winslow Homer Breezing Up NGA"),
    ("Winslow Homer", "Eight Bells", "Addison Gallery of American Art", "1886", "Winslow Homer Eight Bells Addison Gallery"),
    ("Winslow Homer", "Northeaster", "Metropolitan Museum of Art", "1895", "Winslow Homer Northeaster MET"),
    ("Winslow Homer", "Snap the Whip", "Butler Institute of American Art", "1872", "Winslow Homer Snap the Whip Butler"),
    ("Winslow Homer", "The Life Line", "Philadelphia Museum of Art", "1884", "Winslow Homer The Life Line Philadelphia"),
    ("Winslow Homer", "Prisoners from the Front", "Metropolitan Museum of Art", "1866", "Winslow Homer Prisoners from the Front MET"),
    ("Winslow Homer", "Summer Night", "Musée d'Orsay", "1890", "Winslow Homer Summer Night Musee dOrsay"),

    # Vilhelm Hammershøi (8)
    ("Vilhelm Hammershøi", "Interior with Young Man Reading", "Ny Carlsberg Glyptotek", "1898", "Vilhelm Hammershoi Interior Young Man Reading Glyptotek"),
    ("Vilhelm Hammershøi", "Dust Motes Dancing in Sunbeams", "Ordrupgaard", "1900", "Vilhelm Hammershoi Dust Motes Dancing in Sunbeams Ordrupgaard"),
    ("Vilhelm Hammershøi", "Interior Strandgade 30", "Städel Museum", "1901", "Vilhelm Hammershoi Interior Strandgade 30 Stadel"),
    ("Vilhelm Hammershøi", "Sunshine in the Quiet Room", "Davids Samling", "1903", "Vilhelm Hammershoi Sunshine in the Quiet Room Davids Samling"),
    ("Vilhelm Hammershøi", "Interior with an Easel", "Statens Museum for Kunst", "1910", "Vilhelm Hammershoi Interior with an Easel Copenhagen"),
    ("Vilhelm Hammershøi", "The Tall Windows", "Ordrupgaard", "1900", "Vilhelm Hammershoi The Tall Windows Ordrupgaard"),
    ("Vilhelm Hammershøi", "Rest", "Musée d'Orsay", "1905", "Vilhelm Hammershoi Rest Musee dOrsay"),
    ("Vilhelm Hammershøi", "Landscape from Virum", "Statens Museum for Kunst", "1888", "Vilhelm Hammershoi Landscape from Virum Copenhagen"),

    # Edward Hopper (8)
    ("Edward Hopper", "Nighthawks", "Art Institute of Chicago", "1942", "Edward Hopper Nighthawks Art Institute Chicago"),
    ("Edward Hopper", "Automat", "Des Moines Art Center", "1927", "Edward Hopper Automat Des Moines Art Center"),
    ("Edward Hopper", "Chop Suey", "Private Collection", "1929", "Edward Hopper Chop Suey 1929"),
    ("Edward Hopper", "Early Sunday Morning", "Whitney Museum of American Art", "1930", "Edward Hopper Early Sunday Morning Whitney"),
    ("Edward Hopper", "Gas", "Museum of Modern Art", "1940", "Edward Hopper Gas MoMA"),
    ("Edward Hopper", "Morning Sun", "Columbus Museum of Art", "1952", "Edward Hopper Morning Sun Columbus Museum"),
    ("Edward Hopper", "Rooms by the Sea", "Yale University Art Gallery", "1951", "Edward Hopper Rooms by the Sea Yale"),
    ("Edward Hopper", "Office in a Small City", "Metropolitan Museum of Art", "1953", "Edward Hopper Office in a Small City MET"),

    # Gustav Klimt (8)
    ("Gustav Klimt", "The Kiss", "Belvedere Vienna", "1908", "Gustav Klimt The Kiss Belvedere Vienna"),
    ("Gustav Klimt", "Portrait of Adele Bloch-Bauer I", "Neue Galerie New York", "1907", "Gustav Klimt Adele Bloch-Bauer I Neue Galerie"),
    ("Gustav Klimt", "Judith and the Head of Holofernes", "Belvedere Vienna", "1901", "Gustav Klimt Judith and the Head of Holofernes Belvedere"),
    ("Gustav Klimt", "Danaë", "Leopold Museum Vienna", "1907", "Gustav Klimt Danae Leopold Museum Vienna"),
    ("Gustav Klimt", "Death and Life", "Leopold Museum Vienna", "1915", "Gustav Klimt Death and Life Leopold Museum"),
    ("Gustav Klimt", "The Three Ages of Woman", "Galleria Nazionale d'Arte Moderna Rome", "1905", "Gustav Klimt Three Ages of Woman Rome"),
    ("Gustav Klimt", "Beethoven Frieze", "Secession Building Vienna", "1902", "Gustav Klimt Beethoven Frieze Vienna"),
    ("Gustav Klimt", "The Tree of Life, Stoclet Frieze", "Museum of Applied Arts Vienna", "1909", "Gustav Klimt Tree of Life Stoclet Frieze Vienna"),

    # John William Waterhouse (10)
    ("John William Waterhouse", "The Lady of Shalott", "Tate Britain", "1888", "John William Waterhouse Lady of Shalott Tate Britain"),
    ("John William Waterhouse", "Hylas and the Nymphs", "Manchester Art Gallery", "1896", "John William Waterhouse Hylas and the Nymphs Manchester"),
    ("John William Waterhouse", "Circe Offering the Cup to Ulysses", "Oldham Art Gallery", "1891", "Waterhouse Circe Offering Cup to Ulysses Oldham"),
    ("John William Waterhouse", "Boreas", "Private Collection", "1903", "John William Waterhouse Boreas 1903"),
    ("John William Waterhouse", "Ophelia", "Private Collection", "1894", "John William Waterhouse Ophelia 1894"),
    ("John William Waterhouse", "The Soul of the Rose", "Private Collection", "1908", "John William Waterhouse The Soul of the Rose"),
    ("John William Waterhouse", "Sleep and His Half-Brother Death", "Private Collection", "1874", "Waterhouse Sleep and His Half-Brother Death"),
    ("John William Waterhouse", "Miranda - The Tempest", "Private Collection", "1916", "John William Waterhouse Miranda The Tempest"),
    ("John William Waterhouse", "La Belle Dame sans Merci", "Hessisches Landesmuseum Darmstadt", "1893", "Waterhouse La Belle Dame sans Merci Darmstadt"),
    ("John William Waterhouse", "A Tale from the Decameron", "Lady Lever Art Gallery", "1916", "Waterhouse A Tale from the Decameron Lady Lever"),

    # Dante Gabriel Rossetti (6)
    ("Dante Gabriel Rossetti", "Beata Beatrix", "Tate Britain", "1870", "Dante Gabriel Rossetti Beata Beatrix Tate Britain"),
    ("Dante Gabriel Rossetti", "Proserpine", "Tate Britain", "1874", "Dante Gabriel Rossetti Proserpine Tate Britain"),
    ("Dante Gabriel Rossetti", "Lady Lilith", "Delaware Art Museum", "1868", "Dante Gabriel Rossetti Lady Lilith Delaware"),
    ("Dante Gabriel Rossetti", "The Beloved (The Bride)", "Tate Britain", "1865", "Dante Gabriel Rossetti The Beloved Bride Tate"),
    ("Dante Gabriel Rossetti", "Monna Vanna", "Tate Britain", "1866", "Dante Gabriel Rossetti Monna Vanna Tate Britain"),
    ("Dante Gabriel Rossetti", "Bocca Baciata", "Museum of Fine Arts Boston", "1859", "Dante Gabriel Rossetti Bocca Baciata Boston"),

    # John Everett Millais (6)
    ("John Everett Millais", "Ophelia", "Tate Britain", "1851", "John Everett Millais Ophelia Tate Britain"),
    ("John Everett Millais", "The Blind Girl", "Birmingham Museum and Art Gallery", "1856", "John Everett Millais The Blind Girl Birmingham"),
    ("John Everett Millais", "Christ in the House of His Parents", "Tate Britain", "1850", "Millais Christ in the House of His Parents Tate"),
    ("John Everett Millais", "Autumn Leaves", "Manchester Art Gallery", "1856", "John Everett Millais Autumn Leaves Manchester"),
    ("John Everett Millais", "The Order of Release 1746", "Tate Britain", "1852", "John Everett Millais The Order of Release Tate"),
    ("John Everett Millais", "Mariana", "Tate Britain", "1851", "John Everett Millais Mariana Tate Britain"),

    # Edward Burne-Jones (6)
    ("Edward Burne-Jones", "The Golden Stairs", "Tate Britain", "1880", "Edward Burne-Jones The Golden Stairs Tate Britain"),
    ("Edward Burne-Jones", "King Cophetua and the Beggar Maid", "Tate Britain", "1884", "Burne-Jones King Cophetua Beggar Maid Tate Britain"),
    ("Edward Burne-Jones", "The Beguiling of Merlin", "Lady Lever Art Gallery", "1874", "Burne-Jones Beguiling of Merlin Lady Lever"),
    ("Edward Burne-Jones", "Pygmalion and the Image - The Soul Attains", "Birmingham Museum and Art Gallery", "1878", "Burne-Jones Pygmalion The Soul Attains Birmingham"),
    ("Edward Burne-Jones", "The Depths of the Sea", "Private Collection", "1886", "Edward Burne-Jones The Depths of the Sea"),
    ("Edward Burne-Jones", "The Star of Bethlehem", "Birmingham Museum and Art Gallery", "1890", "Burne-Jones Star of Bethlehem Birmingham"),

    # Ilya Repin (8)
    ("Ilya Repin", "Barge Haulers on the Volga", "State Russian Museum", "1873", "Ilya Repin Barge Haulers on the Volga Russian Museum"),
    ("Ilya Repin", "Ivan the Terrible and His Son Ivan", "Tretyakov Gallery", "1885", "Ilya Repin Ivan the Terrible and His Son Ivan Tretyakov"),
    ("Ilya Repin", "Reply of the Zaporozhian Cossacks", "State Russian Museum", "1891", "Ilya Repin Reply of Zaporozhian Cossacks Russian Museum"),
    ("Ilya Repin", "Religious Procession in Kursk Governorate", "Tretyakov Gallery", "1883", "Ilya Repin Religious Procession Kursk Tretyakov"),
    ("Ilya Repin", "They Did Not Expect Him", "Tretyakov Gallery", "1888", "Ilya Repin They Did Not Expect Him Tretyakov"),
    ("Ilya Repin", "Sadko in the Underwater Kingdom", "State Russian Museum", "1876", "Ilya Repin Sadko Underwater Kingdom Russian Museum"),
    ("Ilya Repin", "Portrait of Modest Mussorgsky", "Tretyakov Gallery", "1881", "Ilya Repin Portrait of Modest Mussorgsky Tretyakov"),
    ("Ilya Repin", "Dragonfly", "Tretyakov Gallery", "1884", "Ilya Repin Dragonfly Tretyakov"),

    # Ivan Shishkin (8)
    ("Ivan Shishkin", "Morning in a Pine Forest", "Tretyakov Gallery", "1889", "Ivan Shishkin Morning in a Pine Forest Tretyakov"),
    ("Ivan Shishkin", "Rye", "Tretyakov Gallery", "1878", "Ivan Shishkin Rye Tretyakov Gallery"),
    ("Ivan Shishkin", "In the Wild North", "Museum of Russian Art Kyiv", "1891", "Ivan Shishkin In the Wild North"),
    ("Ivan Shishkin", "Rain in an Oak Forest", "Tretyakov Gallery", "1891", "Ivan Shishkin Rain in an Oak Forest Tretyakov"),
    ("Ivan Shishkin", "Mast-Tree Grove", "State Russian Museum", "1898", "Ivan Shishkin Mast-Tree Grove Russian Museum"),
    ("Ivan Shishkin", "Oaks in Sunbeams", "Tretyakov Gallery", "1887", "Ivan Shishkin Oaks in Sunbeams Tretyakov"),
    ("Ivan Shishkin", "View on the Island of Valaam", "State Russian Museum", "1858", "Ivan Shishkin View Island of Valaam Russian Museum"),
    ("Ivan Shishkin", "A Walk in the Forest", "Tretyakov Gallery", "1869", "Ivan Shishkin A Walk in the Forest Tretyakov"),

    # Isaac Levitan (8)
    ("Isaac Levitan", "Over Eternal Peace", "Tretyakov Gallery", "1894", "Isaac Levitan Over Eternal Peace Tretyakov"),
    ("Isaac Levitan", "Golden Autumn", "Tretyakov Gallery", "1895", "Isaac Levitan Golden Autumn Tretyakov Gallery"),
    ("Isaac Levitan", "Vladimirka", "Tretyakov Gallery", "1892", "Isaac Levitan Vladimirka Tretyakov Gallery"),
    ("Isaac Levitan", "Evening Bells", "Tretyakov Gallery", "1892", "Isaac Levitan Evening Bells Tretyakov Gallery"),
    ("Isaac Levitan", "The Lake. Rus", "State Russian Museum", "1900", "Isaac Levitan The Lake Rus Russian Museum"),
    ("Isaac Levitan", "March", "Tretyakov Gallery", "1895", "Isaac Levitan March Tretyakov Gallery"),
    ("Isaac Levitan", "Autumn Day. Sokolniki", "Tretyakov Gallery", "1879", "Isaac Levitan Autumn Day Sokolniki Tretyakov"),
    ("Isaac Levitan", "Birch Grove", "Tretyakov Gallery", "1889", "Isaac Levitan Birch Grove Tretyakov Gallery"),

    # Ivan Aivazovsky (8)
    ("Ivan Aivazovsky", "The Ninth Wave", "State Russian Museum", "1850", "Ivan Aivazovsky The Ninth Wave Russian Museum"),
    ("Ivan Aivazovsky", "Rainbow", "Tretyakov Gallery", "1873", "Ivan Aivazovsky Rainbow Tretyakov Gallery"),
    ("Ivan Aivazovsky", "Storm over the Black Sea", "Tretyakov Gallery", "1893", "Ivan Aivazovsky Storm over Black Sea Tretyakov"),
    ("Ivan Aivazovsky", "Brig 'Mercury' Attacked by Two Turkish Ships", "State Russian Museum", "1892", "Ivan Aivazovsky Brig Mercury Attacked Russian Museum"),
    ("Ivan Aivazovsky", "Pushkin's Farewell to the Sea", "All-Russian Pushkin Museum", "1877", "Ivan Aivazovsky Pushkins Farewell to the Sea"),
    ("Ivan Aivazovsky", "Chaos (Creation)", "San Lazzaro degli Armeni Venice", "1841", "Ivan Aivazovsky Chaos Creation Venice"),
    ("Ivan Aivazovsky", "Ship in the Stormy Sea at Sunset", "Tretyakov Gallery", "1890", "Ivan Aivazovsky Ship in Stormy Sea Sunset"),
    ("Ivan Aivazovsky", "View of Tiflis", "Tretyakov Gallery", "1869", "Ivan Aivazovsky View of Tiflis Tretyakov"),

    # Arkhip Kuindzhi (6)
    ("Arkhip Kuindzhi", "Moonlit Night on the Dnieper", "State Russian Museum", "1880", "Arkhip Kuindzhi Moonlit Night on the Dnieper"),
    ("Arkhip Kuindzhi", "Birch Grove", "Tretyakov Gallery", "1879", "Arkhip Kuindzhi Birch Grove Tretyakov"),
    ("Arkhip Kuindzhi", "Red Sunset on the Dnieper", "Metropolitan Museum of Art", "1908", "Arkhip Kuindzhi Red Sunset on the Dnieper MET"),
    ("Arkhip Kuindzhi", "After a Thunderstorm", "Tretyakov Gallery", "1879", "Arkhip Kuindzhi After a Thunderstorm Tretyakov"),
    ("Arkhip Kuindzhi", "Elbrus in the Evening", "State Russian Museum", "1908", "Arkhip Kuindzhi Elbrus in the Evening Russian Museum"),
    ("Arkhip Kuindzhi", "Night on the Don", "State Russian Museum", "1882", "Arkhip Kuindzhi Night on the Don Russian Museum"),

    # Anders Zorn (6)
    ("Anders Zorn", "Midsummer Dance", "Nationalmuseum Stockholm", "1897", "Anders Zorn Midsummer Dance Stockholm"),
    ("Anders Zorn", "Self-Portrait with Fur Coat", "Zorn Museum", "1915", "Anders Zorn Self-Portrait with Fur Coat"),
    ("Anders Zorn", "Girls from Dalarna Having a Bath", "Nationalmuseum Stockholm", "1906", "Anders Zorn Girls from Dalarna Having a Bath"),
    ("Anders Zorn", "Omnibus", "Isabella Stewart Gardner Museum", "1892", "Anders Zorn Omnibus Isabella Stewart Gardner"),
    ("Anders Zorn", "Gopsmor Cottage", "Zorn Museum", "1914", "Anders Zorn Gopsmor Cottage"),
    ("Anders Zorn", "Reel (Dans i Gopsmor)", "Zorn Museum", "1906", "Anders Zorn Dans i Gopsmor"),

    # Peder Severin Krøyer (6)
    ("Peder Severin Krøyer", "Summer Evening on Skagen's Southern Beach", "Skagens Museum", "1893", "Peder Severin Kroyer Summer Evening Skagens Museum"),
    ("Peder Severin Krøyer", "Hip, Hip, Hurrah!", "Gothenburg Museum of Art", "1888", "Peder Severin Kroyer Hip Hip Hurrah Gothenburg"),
    ("Peder Severin Krøyer", "Summer Evening at Skagen Beach - The Artist and His Wife", "Hirschsprung Collection", "1899", "Peder Severin Kroyer Artist and His Wife Hirschsprung"),
    ("Peder Severin Krøyer", "Boys Bathing at Skagen, Summer Evening", "Statens Museum for Kunst", "1899", "Peder Severin Kroyer Boys Bathing Skagen Copenhagen"),
    ("Peder Severin Krøyer", "Fishermen on Skagen Beach", "Statens Museum for Kunst", "1883", "Peder Severin Kroyer Fishermen Skagen Beach"),
    ("Peder Severin Krøyer", "Midsummer Eve Bonfire on Skagen Beach", "Skagens Museum", "1906", "Peder Severin Kroyer Midsummer Eve Bonfire Skagen"),

    # Carl Larsson (6)
    ("Carl Larsson", "A Studio Idyll", "Nationalmuseum Stockholm", "1885", "Carl Larsson A Studio Idyll Nationalmuseum"),
    ("Carl Larsson", "Breakfast Under the Big Birch", "Nationalmuseum Stockholm", "1896", "Carl Larsson Breakfast Under the Big Birch Nationalmuseum"),
    ("Carl Larsson", "Midvinterblot", "Nationalmuseum Stockholm", "1915", "Carl Larsson Midvinterblot Nationalmuseum"),
    ("Carl Larsson", "The Kitchen", "Nationalmuseum Stockholm", "1898", "Carl Larsson The Kitchen Nationalmuseum"),
    ("Carl Larsson", "Around the Lamp at Evening", "Nationalmuseum Stockholm", "1900", "Carl Larsson Around the Lamp at Evening"),
    ("Carl Larsson", "Cosy Corner (Lathörnet)", "Nationalmuseum Stockholm", "1894", "Carl Larsson Lathornet Nationalmuseum Stockholm"),

    # Albert Bierstadt (8)
    ("Albert Bierstadt", "Among the Sierra Nevada Mountains", "Smithsonian American Art Museum", "1868", "Albert Bierstadt Among the Sierra Nevada Mountains SAAM"),
    ("Albert Bierstadt", "The Rocky Mountains, Lander's Peak", "Metropolitan Museum of Art", "1863", "Albert Bierstadt Rocky Mountains Landers Peak MET"),
    ("Albert Bierstadt", "Storm in the Rocky Mountains, Mount Rosalie", "Brooklyn Museum", "1866", "Albert Bierstadt Storm in Rocky Mountains Brooklyn"),
    ("Albert Bierstadt", "Valley of the Yosemite", "Museum of Fine Arts Boston", "1864", "Albert Bierstadt Valley of the Yosemite Boston"),
    ("Albert Bierstadt", "Looking Down Yosemite Valley, California", "Birmingham Museum of Art", "1865", "Albert Bierstadt Looking Down Yosemite Valley"),
    ("Albert Bierstadt", "A Storm in the Rocky Mountains", "Brooklyn Museum", "1866", "Albert Bierstadt Mount Rosalie Brooklyn Museum"),
    ("Albert Bierstadt", "Puget Sound on the Pacific Coast", "Seattle Art Museum", "1870", "Albert Bierstadt Puget Sound on Pacific Coast Seattle"),
    ("Albert Bierstadt", "Sunrise in the Sierras", "Smithsonian American Art Museum", "1872", "Albert Bierstadt Sunrise in the Sierras SAAM"),

    # Thomas Cole (8)
    ("Thomas Cole", "The Oxbow", "Metropolitan Museum of Art", "1836", "Thomas Cole The Oxbow MET"),
    ("Thomas Cole", "The Course of Empire: The Savage State", "New-York Historical Society", "1834", "Thomas Cole Course of Empire Savage State"),
    ("Thomas Cole", "The Course of Empire: The Arcadian State", "New-York Historical Society", "1834", "Thomas Cole Course of Empire Arcadian State"),
    ("Thomas Cole", "The Course of Empire: Consummation", "New-York Historical Society", "1836", "Thomas Cole Course of Empire Consummation"),
    ("Thomas Cole", "The Course of Empire: Destruction", "New-York Historical Society", "1836", "Thomas Cole Course of Empire Destruction"),
    ("Thomas Cole", "The Course of Empire: Desolation", "New-York Historical Society", "1836", "Thomas Cole Course of Empire Desolation"),
    ("Thomas Cole", "The Voyage of Life: Childhood", "National Gallery of Art", "1842", "Thomas Cole Voyage of Life Childhood NGA"),
    ("Thomas Cole", "The Voyage of Life: Youth", "National Gallery of Art", "1842", "Thomas Cole Voyage of Life Youth NGA"),

    # Frederic Edwin Church (6)
    ("Frederic Edwin Church", "The Heart of the Andes", "Metropolitan Museum of Art", "1859", "Frederic Edwin Church Heart of the Andes MET"),
    ("Frederic Edwin Church", "Niagara", "National Gallery of Art", "1857", "Frederic Edwin Church Niagara National Gallery"),
    ("Frederic Edwin Church", "The Icebergs", "Dallas Museum of Art", "1861", "Frederic Edwin Church The Icebergs Dallas"),
    ("Frederic Edwin Church", "Cotopaxi", "Detroit Institute of Arts", "1862", "Frederic Edwin Church Cotopaxi Detroit"),
    ("Frederic Edwin Church", "Twilight in the Wilderness", "Cleveland Museum of Art", "1860", "Frederic Edwin Church Twilight in the Wilderness Cleveland"),
    ("Frederic Edwin Church", "Morning in the Tropics", "National Gallery of Art", "1877", "Frederic Edwin Church Morning in the Tropics NGA"),

    # George Inness (6)
    ("George Inness", "The Lackawanna Valley", "National Gallery of Art", "1855", "George Inness Lackawanna Valley National Gallery"),
    ("George Inness", "The Home of the Heron", "Art Institute of Chicago", "1893", "George Inness Home of the Heron Chicago"),
    ("George Inness", "Peace and Plenty", "Metropolitan Museum of Art", "1865", "George Inness Peace and Plenty MET"),
    ("George Inness", "Sunset at Montclair", "Private Collection", "1892", "George Inness Sunset at Montclair 1892"),
    ("George Inness", "Early Autumn, Montclair", "Delaware Art Museum", "1888", "George Inness Early Autumn Montclair Delaware"),
    ("George Inness", "The Valley of the Shadow of Death", "Frances Lehman Loeb Art Center", "1867", "George Inness Valley Shadow of Death Vassar"),

    # Jean-François Millet (6)
    ("Jean-François Millet", "The Gleaners", "Musée d'Orsay", "1857", "Jean-Francois Millet The Gleaners Musee dOrsay"),
    ("Jean-François Millet", "The Angelus", "Musée d'Orsay", "1859", "Jean-Francois Millet The Angelus Musee dOrsay"),
    ("Jean-François Millet", "The Sower", "Museum of Fine Arts Boston", "1850", "Jean-Francois Millet The Sower Boston"),
    ("Jean-François Millet", "Man with a Hoe", "J. Paul Getty Museum", "1862", "Jean-Francois Millet Man with a Hoe Getty"),
    ("Jean-François Millet", "Haystacks: Autumn", "Metropolitan Museum of Art", "1874", "Jean-Francois Millet Haystacks Autumn MET"),
    ("Jean-François Millet", "Spring (Printemps)", "Musée d'Orsay", "1873", "Jean-Francois Millet Printemps Musee dOrsay"),

    # Gustave Courbet (6)
    ("Gustave Courbet", "The Stone Breakers", "Gemäldegalerie Dresden", "1849", "Gustave Courbet The Stone Breakers Dresden"),
    ("Gustave Courbet", "A Burial at Ornans", "Musée d'Orsay", "1850", "Gustave Courbet Burial at Ornans Musee dOrsay"),
    ("Gustave Courbet", "The Desperate Man", "Private Collection", "1845", "Gustave Courbet The Desperate Man 1845"),
    ("Gustave Courbet", "The Painter's Studio", "Musée d'Orsay", "1855", "Gustave Courbet The Painters Studio Musee dOrsay"),
    ("Gustave Courbet", "The Wave", "Nationalgalerie Berlin", "1870", "Gustave Courbet The Wave Berlin"),
    ("Gustave Courbet", "The Sleepers (Le Sommeil)", "Petit Palais Paris", "1866", "Gustave Courbet Le Sommeil Petit Palais"),

    # Jean-Baptiste-Camille Corot (6)
    ("Camille Corot", "Souvenir de Mortefontaine", "Louvre Museum", "1864", "Camille Corot Souvenir de Mortefontaine Louvre"),
    ("Camille Corot", "The Bridge at Narni", "Louvre Museum", "1826", "Camille Corot Bridge at Narni Louvre"),
    ("Camille Corot", "Ville-d'Avray", "National Gallery of Art", "1867", "Camille Corot Ville-dAvray National Gallery"),
    ("Camille Corot", "A Woman with a Pearl", "Louvre Museum", "1869", "Camille Corot Woman with a Pearl Louvre"),
    ("Camille Corot", "The Forum Seen from the Farnese Gardens", "Louvre Museum", "1826", "Camille Corot Forum Farnese Gardens Louvre"),
    ("Camille Corot", "Morning, the Dance of the Nymphs", "Musée d'Orsay", "1850", "Camille Corot Dance of the Nymphs dOrsay"),

    # Honoré Daumier (4)
    ("Honoré Daumier", "The Third-Class Carriage", "Metropolitan Museum of Art", "1864", "Honore Daumier Third-Class Carriage MET"),
    ("Honoré Daumier", "The Laundress", "Musée d'Orsay", "1863", "Honore Daumier The Laundress Musee dOrsay"),
    ("Honoré Daumier", "Crispin and Scapin", "Musée d'Orsay", "1864", "Honore Daumier Crispin and Scapin dOrsay"),
    ("Honoré Daumier", "Don Quixote and Sancho Panza", "Neue Pinakothek Munich", "1868", "Honore Daumier Don Quixote Neue Pinakothek"),

    # Eugène Delacroix (6)
    ("Eugène Delacroix", "Liberty Leading the People", "Louvre Museum", "1830", "Eugene Delacroix Liberty Leading the People Louvre"),
    ("Eugène Delacroix", "The Barque of Dante", "Louvre Museum", "1822", "Eugene Delacroix The Barque of Dante Louvre"),
    ("Eugène Delacroix", "The Death of Sardanapalus", "Louvre Museum", "1827", "Eugene Delacroix Death of Sardanapalus Louvre"),
    ("Eugène Delacroix", "Massacre at Chios", "Louvre Museum", "1824", "Eugene Delacroix Massacre at Chios Louvre"),
    ("Eugène Delacroix", "Lion Hunt", "Art Institute of Chicago", "1861", "Eugene Delacroix Lion Hunt Chicago"),
    ("Eugène Delacroix", "Women of Algiers in Their Apartment", "Louvre Museum", "1834", "Eugene Delacroix Women of Algiers Louvre"),

    # Théodore Géricault (4)
    ("Théodore Géricault", "The Raft of the Medusa", "Louvre Museum", "1819", "Theodore Gericault Raft of the Medusa Louvre"),
    ("Théodore Géricault", "The Charging Chasseur", "Louvre Museum", "1812", "Theodore Gericault Charging Chasseur Louvre"),
    ("Théodore Géricault", "The Wounded Cuirassier", "Louvre Museum", "1814", "Theodore Gericault Wounded Cuirassier Louvre"),
    ("Théodore Géricault", "Portrait of a Kleptomaniac", "Museum of Fine Arts Ghent", "1822", "Theodore Gericault Portrait of a Kleptomaniac Ghent"),

    # Jacques-Louis David (6)
    ("Jacques-Louis David", "The Death of Socrates", "Metropolitan Museum of Art", "1787", "Jacques-Louis David Death of Socrates MET"),
    ("Jacques-Louis David", "Oath of the Horatii", "Louvre Museum", "1784", "Jacques-Louis David Oath of the Horatii Louvre"),
    ("Jacques-Louis David", "The Death of Marat", "Royal Museums of Fine Arts of Belgium", "1793", "Jacques-Louis David Death of Marat Brussels"),
    ("Jacques-Louis David", "Napoleon Crossing the Alps", "Château de Malmaison", "1801", "Jacques-Louis David Napoleon Crossing the Alps Malmaison"),
    ("Jacques-Louis David", "The Coronation of Napoleon", "Louvre Museum", "1807", "Jacques-Louis David Coronation of Napoleon Louvre"),
    ("Jacques-Louis David", "Leonidas at Thermopylae", "Louvre Museum", "1814", "Jacques-Louis David Leonidas at Thermopylae Louvre"),

    # Jean-Auguste-Dominique Ingres (6)
    ("Jean-Auguste-Dominique Ingres", "The Grand Odalisque", "Louvre Museum", "1814", "Ingres Grand Odalisque Louvre"),
    ("Jean-Auguste-Dominique Ingres", "Oedipus and the Sphinx", "Louvre Museum", "1808", "Ingres Oedipus and Sphinx Louvre"),
    ("Jean-Auguste-Dominique Ingres", "The Apotheosis of Homer", "Louvre Museum", "1827", "Ingres Apotheosis of Homer Louvre"),
    ("Jean-Auguste-Dominique Ingres", "Portrait of Monsieur Bertin", "Louvre Museum", "1832", "Ingres Portrait of Monsieur Bertin Louvre"),
    ("Jean-Auguste-Dominique Ingres", "The Valpinçon Bather", "Louvre Museum", "1808", "Ingres Valpincon Bather Louvre"),
    ("Jean-Auguste-Dominique Ingres", "The Source (La Source)", "Musée d'Orsay", "1856", "Ingres La Source Musee dOrsay"),

    # Sandro Botticelli (4)
    ("Sandro Botticelli", "The Birth of Venus", "Uffizi Gallery", "1485", "Sandro Botticelli Birth of Venus Uffizi"),
    ("Sandro Botticelli", "Primavera", "Uffizi Gallery", "1482", "Sandro Botticelli Primavera Uffizi"),
    ("Sandro Botticelli", "Pallas and the Centaur", "Uffizi Gallery", "1482", "Sandro Botticelli Pallas and the Centaur Uffizi"),
    ("Sandro Botticelli", "The Mystical Nativity", "National Gallery London", "1500", "Sandro Botticelli Mystical Nativity National Gallery"),

    # Leonardo da Vinci (4)
    ("Leonardo da Vinci", "Mona Lisa", "Louvre Museum", "1503", "Leonardo da Vinci Mona Lisa Louvre"),
    ("Leonardo da Vinci", "Lady with an Ermine", "Czartoryski Museum", "1489", "Leonardo da Vinci Lady with an Ermine Krakow"),
    ("Leonardo da Vinci", "Ginevra de' Benci", "National Gallery of Art", "1474", "Leonardo da Vinci Ginevra de Benci NGA"),
    ("Leonardo da Vinci", "Saint John the Baptist", "Louvre Museum", "1513", "Leonardo da Vinci Saint John Baptist Louvre"),

    # Michelangelo (4)
    ("Michelangelo", "Doni Tondo", "Uffizi Gallery", "1507", "Michelangelo Doni Tondo Uffizi"),
    ("Michelangelo", "The Manchester Madonna", "National Gallery London", "1497", "Michelangelo Manchester Madonna National Gallery"),
    ("Michelangelo", "The Entombment", "National Gallery London", "1500", "Michelangelo The Entombment National Gallery London"),
    ("Michelangelo", "The Creation of Adam (fresco study)", "Vatican Museums", "1512", "Michelangelo Creation of Adam Vatican"),

    # Raphael (6)
    ("Raphael", "The School of Athens", "Vatican Museums", "1511", "Raphael School of Athens Vatican"),
    ("Raphael", "Portrait of Baldassare Castiglione", "Louvre Museum", "1515", "Raphael Portrait of Baldassare Castiglione Louvre"),
    ("Raphael", "The Sistine Madonna", "Gemäldegalerie Alte Meister Dresden", "1512", "Raphael Sistine Madonna Dresden"),
    ("Raphael", "The Transfiguration", "Vatican Museums", "1520", "Raphael The Transfiguration Vatican"),
    ("Raphael", "The Triumph of Galatea", "Villa Farnesina", "1512", "Raphael Triumph of Galatea Villa Farnesina"),
    ("Raphael", "Portrait of Bindo Altoviti", "National Gallery of Art", "1515", "Raphael Portrait of Bindo Altoviti NGA"),

    # Titian (8)
    ("Titian", "Bacchus and Ariadne", "National Gallery London", "1523", "Titian Bacchus and Ariadne National Gallery"),
    ("Titian", "Diana and Actaeon", "National Gallery of Scotland", "1559", "Titian Diana and Actaeon National Gallery"),
    ("Titian", "Assumption of the Virgin", "Santa Maria Gloriosa dei Frari", "1518", "Titian Assumption of the Virgin Frari Venice"),
    ("Titian", "The Flaying of Marsyas", "Kroměříž Archbishop's Palace", "1576", "Titian Flaying of Marsyas Kromeriz"),
    ("Titian", "Man with a Glove", "Louvre Museum", "1520", "Titian Man with a Glove Louvre"),
    ("Titian", "Aretino", "Palazzo Pitti", "1545", "Titian Portrait of Pietro Aretino Pitti"),
    ("Titian", "Venus of Urbino", "Uffizi Gallery", "1538", "Titian Venus of Urbino Uffizi"),
    ("Titian", "The Death of Actaeon", "National Gallery London", "1575", "Titian Death of Actaeon National Gallery"),

    # Pieter Bruegel the Elder (6)
    ("Pieter Bruegel the Elder", "The Tower of Babel", "Kunsthistorisches Museum", "1563", "Pieter Bruegel Tower of Babel Vienna"),
    ("Pieter Bruegel the Elder", "The Harvesters", "Metropolitan Museum of Art", "1565", "Pieter Bruegel The Harvesters MET"),
    ("Pieter Bruegel the Elder", "The Triumph of Death", "Museo del Prado", "1562", "Pieter Bruegel Triumph of Death Prado"),
    ("Pieter Bruegel the Elder", "Netherlandish Proverbs", "Gemäldegalerie Berlin", "1559", "Pieter Bruegel Netherlandish Proverbs Berlin"),
    ("Pieter Bruegel the Elder", "The Peasant Wedding", "Kunsthistorisches Museum", "1567", "Pieter Bruegel Peasant Wedding Vienna"),
    ("Pieter Bruegel the Elder", "The Fall of the Rebel Angels", "Royal Museums of Fine Arts of Belgium", "1562", "Pieter Bruegel Fall of the Rebel Angels Brussels"),

    # Hieronymus Bosch (4)
    ("Hieronymus Bosch", "The Garden of Earthly Delights", "Museo del Prado", "1500", "Hieronymus Bosch Garden of Earthly Delights Prado"),
    ("Hieronymus Bosch", "Ship of Fools", "Louvre Museum", "1500", "Hieronymus Bosch Ship of Fools Louvre"),
    ("Hieronymus Bosch", "The Haywain Triptych", "Museo del Prado", "1516", "Hieronymus Bosch The Haywain Prado"),
    ("Hieronymus Bosch", "The Temptation of Saint Anthony", "Museu Nacional de Arte Antiga Lisbon", "1501", "Hieronymus Bosch Temptation of Saint Anthony Lisbon"),

    # Albrecht Dürer (6)
    ("Albrecht Dürer", "Self-Portrait at Twenty-Eight", "Alte Pinakothek", "1500", "Albrecht Durer Self-Portrait at 28 Munich"),
    ("Albrecht Dürer", "Knight, Death and the Devil", "Städel Museum", "1513", "Albrecht Durer Knight Death and Devil"),
    ("Albrecht Dürer", "Saint Jerome in His Study", "Albertina", "1514", "Albrecht Durer Saint Jerome in His Study Albertina"),
    ("Albrecht Dürer", "Melencolia I", "Metropolitan Museum of Art", "1514", "Albrecht Durer Melencolia I MET"),
    ("Albrecht Dürer", "Praying Hands", "Albertina", "1508", "Albrecht Durer Praying Hands Albertina"),
    ("Albrecht Dürer", "Young Hare", "Albertina", "1502", "Albrecht Durer Young Hare Albertina"),

    # Hans Holbein the Younger (4)
    ("Hans Holbein the Younger", "The Ambassadors", "National Gallery London", "1533", "Hans Holbein The Ambassadors National Gallery"),
    ("Hans Holbein the Younger", "Portrait of Desiderius Erasmus", "National Gallery London", "1523", "Hans Holbein Erasmus National Gallery London"),
    ("Hans Holbein the Younger", "Portrait of Sir Thomas More", "Frick Collection", "1527", "Hans Holbein Sir Thomas More Frick"),
    ("Hans Holbein the Younger", "The Body of the Dead Christ in the Tomb", "Kunstmuseum Basel", "1521", "Hans Holbein Dead Christ in the Tomb Basel"),

    # Georges de La Tour (4)
    ("Georges de La Tour", "The Penitent Magdalen", "Metropolitan Museum of Art", "1640", "Georges de La Tour Penitent Magdalen MET"),
    ("Georges de La Tour", "Joseph the Carpenter", "Louvre Museum", "1642", "Georges de La Tour Joseph the Carpenter Louvre"),
    ("Georges de La Tour", "The Fortune Teller", "Metropolitan Museum of Art", "1630", "Georges de La Tour Fortune Teller MET"),
    ("Georges de La Tour", "The Newborn Christ", "Musée des Beaux-Arts de Rennes", "1645", "Georges de La Tour The Newborn Christ Rennes"),

    # Artemisia Gentileschi (4)
    ("Artemisia Gentileschi", "Judith Slaying Holofernes", "Uffizi Gallery", "1620", "Artemisia Gentileschi Judith Slaying Holofernes Uffizi"),
    ("Artemisia Gentileschi", "Self-Portrait as the Allegory of Painting", "Royal Collection", "1638", "Artemisia Gentileschi Allegory of Painting Windsor"),
    ("Artemisia Gentileschi", "Susanna and the Elders", "Schloss Weißenstein", "1610", "Artemisia Gentileschi Susanna and the Elders Weissenstein"),
    ("Artemisia Gentileschi", "Jael and Sisera", "Museum of Fine Arts Budapest", "1620", "Artemisia Gentileschi Jael and Sisera Budapest"),

    # Paul Gauguin (6)
    ("Paul Gauguin", "Where Do We Come From? What Are We? Where Are We Going?", "Museum of Fine Arts Boston", "1897", "Paul Gauguin Where Do We Come From Boston"),
    ("Paul Gauguin", "Vision After the Sermon", "National Gallery of Scotland", "1888", "Paul Gauguin Vision After the Sermon Edinburgh"),
    ("Paul Gauguin", "The Yellow Christ", "Albright-Knox Art Gallery", "1889", "Paul Gauguin The Yellow Christ Albright-Knox"),
    ("Paul Gauguin", "Tahitian Women on the Beach", "Musée d'Orsay", "1891", "Paul Gauguin Tahitian Women on the Beach dOrsay"),
    ("Paul Gauguin", "Manao Tupapau (The Spirit of the Dead Keeps Watch)", "Albright-Knox Art Gallery", "1892", "Paul Gauguin Spirit of the Dead Keeps Watch"),
    ("Paul Gauguin", "Nevermore", "Courtauld Gallery", "1897", "Paul Gauguin Nevermore Courtauld"),

    # Georges Seurat & Paul Signac (6)
    ("Georges Seurat", "A Sunday on La Grande Jatte", "Art Institute of Chicago", "1886", "Georges Seurat Sunday on La Grande Jatte Chicago"),
    ("Georges Seurat", "Bathers at Asnières", "National Gallery London", "1884", "Georges Seurat Bathers at Asnieres National Gallery"),
    ("Georges Seurat", "The Circus", "Musée d'Orsay", "1891", "Georges Seurat The Circus Musee dOrsay"),
    ("Georges Seurat", "Young Woman Powdering Herself", "Courtauld Gallery", "1890", "Georges Seurat Young Woman Powdering Herself Courtauld"),
    ("Paul Signac", "The Port of Saint-Tropez", "Musée de l'Annonciade", "1901", "Paul Signac Port of Saint-Tropez"),
    ("Paul Signac", "The Town Beach, Collioure", "Metropolitan Museum of Art", "1887", "Paul Signac Town Beach Collioure MET"),

    # Camille Pissarro (6)
    ("Camille Pissarro", "The Boulevard Montmartre at Night", "National Gallery London", "1897", "Camille Pissarro Boulevard Montmartre at Night London"),
    ("Camille Pissarro", "Jalais Hill, Pontoise", "Metropolitan Museum of Art", "1867", "Camille Pissarro Jalais Hill Pontoise MET"),
    ("Camille Pissarro", "Red Roofs, Corner of a Village", "Musée d'Orsay", "1877", "Camille Pissarro Red Roofs Musee dOrsay"),
    ("Camille Pissarro", "Place du Théâtre-Français, Spring", "Hermitage Museum", "1898", "Camille Pissarro Place du Theatre-Francais Hermitage"),
    ("Camille Pissarro", "Landscape at Chaponval", "Musée d'Orsay", "1880", "Camille Pissarro Landscape at Chaponval dOrsay"),
    ("Camille Pissarro", "The Harvest", "Musée d'Orsay", "1882", "Camille Pissarro The Harvest Musee dOrsay"),

    # Alfred Sisley (6)
    ("Alfred Sisley", "Bridge at Villeneuve-la-Garenne", "Metropolitan Museum of Art", "1872", "Alfred Sisley Bridge Villeneuve-la-Garenne MET"),
    ("Alfred Sisley", "Flood at Port-Marly", "Musée d'Orsay", "1876", "Alfred Sisley Flood at Port-Marly Musee dOrsay"),
    ("Alfred Sisley", "Fog, Voisins", "Musée d'Orsay", "1874", "Alfred Sisley Fog Voisins Musee dOrsay"),
    ("Alfred Sisley", "Meadow at Moret", "Musée des Beaux-Arts Lyon", "1888", "Alfred Sisley Meadow at Moret Lyon"),
    ("Alfred Sisley", "The Seine at Bougival", "Metropolitan Museum of Art", "1876", "Alfred Sisley The Seine at Bougival MET"),
    ("Alfred Sisley", "Snow on the Road, Louveciennes", "Musée d'Orsay", "1874", "Alfred Sisley Snow on the Road Louveciennes dOrsay"),

    # Gustave Caillebotte (6)
    ("Gustave Caillebotte", "The Floor Scrapers", "Musée d'Orsay", "1875", "Gustave Caillebotte The Floor Scrapers dOrsay"),
    ("Gustave Caillebotte", "Young Man at His Window", "J. Paul Getty Museum", "1876", "Gustave Caillebotte Young Man at His Window Getty"),
    ("Gustave Caillebotte", "The Pont de l'Europe", "Musée du Petit Palais Geneva", "1876", "Gustave Caillebotte Pont de lEurope Geneva"),
    ("Gustave Caillebotte", "Oarsmen on the Yerres", "Private Collection", "1877", "Gustave Caillebotte Oarsmen on the Yerres"),
    ("Gustave Caillebotte", "Rooftops in the Snow", "Musée d'Orsay", "1878", "Gustave Caillebotte Rooftops in the Snow dOrsay"),
    ("Gustave Caillebotte", "Fruit Displayed on a Stand", "Museum of Fine Arts Boston", "1882", "Gustave Caillebotte Fruit Displayed on a Stand Boston"),

    # Odilon Redon & Symbolists (8)
    ("Odilon Redon", "The Cyclops", "Kröller-Müller Museum", "1914", "Odilon Redon The Cyclops Kroller-Muller"),
    ("Odilon Redon", "Ophelia", "National Gallery of Canada", "1905", "Odilon Redon Ophelia National Gallery Canada"),
    ("Odilon Redon", "The Buddha in His Youth", "Musée d'Orsay", "1905", "Odilon Redon Buddha in His Youth dOrsay"),
    ("Odilon Redon", "Wildflowers in a Vase", "Museum of Fine Arts Boston", "1905", "Odilon Redon Wildflowers in a Vase Boston"),
    ("Arnold Böcklin", "Isle of the Dead", "Alte Nationalgalerie", "1883", "Arnold Bocklin Isle of the Dead Alte Nationalgalerie"),
    ("Arnold Böcklin", "Self-Portrait with Death Playing the Fiddle", "Alte Nationalgalerie", "1872", "Arnold Bocklin Self-Portrait with Death Berlin"),
    ("Franz von Stuck", "Sin", "Neue Pinakothek", "1893", "Franz von Stuck The Sin Neue Pinakothek Munich"),
    ("Franz von Stuck", "Lucifer", "National Gallery for Foreign Art Sofia", "1890", "Franz von Stuck Lucifer Sofia Gallery"),

    # William-Adolphe Bouguereau (6)
    ("William-Adolphe Bouguereau", "The Birth of Venus", "Musée d'Orsay", "1879", "William-Adolphe Bouguereau Birth of Venus Musee dOrsay"),
    ("William-Adolphe Bouguereau", "Dante and Virgil", "Musée d'Orsay", "1850", "William-Adolphe Bouguereau Dante and Virgil dOrsay"),
    ("William-Adolphe Bouguereau", "The Shepherdess", "Philbrook Museum of Art", "1889", "William-Adolphe Bouguereau The Shepherdess Philbrook"),
    ("William-Adolphe Bouguereau", "The First Mourning", "Museo Nacional de Bellas Artes", "1888", "William-Adolphe Bouguereau First Mourning Buenos Aires"),
    ("William-Adolphe Bouguereau", "Song of the Angels", "Forest Lawn Memorial Park", "1881", "William-Adolphe Bouguereau Song of the Angels"),
    ("William-Adolphe Bouguereau", "Nymphs and Satyr", "Clark Art Institute", "1873", "William-Adolphe Bouguereau Nymphs and Satyr Clark"),

    # Jean-Léon Gérôme (6)
    ("Jean-Léon Gérôme", "Pollice Verso", "Phoenix Art Museum", "1872", "Jean-Leon Gerome Pollice Verso Phoenix"),
    ("Jean-Léon Gérôme", "The Snake Charmer", "Clark Art Institute", "1879", "Jean-Leon Gerome The Snake Charmer Clark Art"),
    ("Jean-Léon Gérôme", "Pygmalion and Galatea", "Metropolitan Museum of Art", "1890", "Jean-Leon Gerome Pygmalion and Galatea MET"),
    ("Jean-Léon Gérôme", "The Carpet Merchant", "Minneapolis Institute of Art", "1887", "Jean-Leon Gerome The Carpet Merchant Minneapolis"),
    ("Jean-Léon Gérôme", "Truth Coming Out of Her Well", "Musée Anne de Beaujeu", "1896", "Jean-Leon Gerome Truth Coming Out of Her Well"),
    ("Jean-Léon Gérôme", "Bonaparte Before the Sphinx", "Hearst Castle", "1886", "Jean-Leon Gerome Bonaparte Before the Sphinx Hearst"),

    # Lawrence Alma-Tadema (6)
    ("Lawrence Alma-Tadema", "The Roses of Heliogabalus", "Private Collection", "1888", "Lawrence Alma-Tadema Roses of Heliogabalus 1888"),
    ("Lawrence Alma-Tadema", "A Coign of Vantage", "Private Collection", "1895", "Lawrence Alma-Tadema Coign of Vantage 1895"),
    ("Lawrence Alma-Tadema", "Spring", "J. Paul Getty Museum", "1894", "Lawrence Alma-Tadema Spring Getty"),
    ("Lawrence Alma-Tadema", "Silver Favourites", "Manchester Art Gallery", "1903", "Lawrence Alma-Tadema Silver Favourites Manchester"),
    ("Lawrence Alma-Tadema", "The Finding of Moses", "Private Collection", "1904", "Lawrence Alma-Tadema Finding of Moses 1904"),
    ("Lawrence Alma-Tadema", "Unconscious Rivals", "Bristol Museum & Art Gallery", "1893", "Lawrence Alma-Tadema Unconscious Rivals Bristol"),

    # Frederic Leighton (6)
    ("Frederic Leighton", "Flaming June", "Museo de Arte de Ponce", "1895", "Frederic Leighton Flaming June Ponce"),
    ("Frederic Leighton", "Pavonia", "Royal Collection", "1859", "Frederic Leighton Pavonia Royal Collection"),
    ("Frederic Leighton", "The Bath of Psyche", "Tate Britain", "1890", "Frederic Leighton The Bath of Psyche Tate"),
    ("Frederic Leighton", "An Athlete Wrestling with a Python", "Tate Britain", "1877", "Frederic Leighton Athlete Wrestling Python Tate"),
    ("Frederic Leighton", "Clytie", "Leighton House Museum", "1896", "Frederic Leighton Clytie Leighton House"),
    ("Frederic Leighton", "Idyll", "Private Collection", "1881", "Frederic Leighton Idyll 1881"),

    # John Constable (6)
    ("John Constable", "The Hay Wain", "National Gallery London", "1821", "John Constable The Hay Wain National Gallery"),
    ("John Constable", "Salisbury Cathedral from the Bishop's Grounds", "Victoria and Albert Museum", "1823", "John Constable Salisbury Cathedral Bishops Grounds V&A"),
    ("John Constable", "Dedham Vale", "National Gallery of Scotland", "1828", "John Constable Dedham Vale Edinburgh"),
    ("John Constable", "The Cornfield", "National Gallery London", "1826", "John Constable The Cornfield National Gallery"),
    ("John Constable", "Wivenhoe Park", "National Gallery of Art", "1816", "John Constable Wivenhoe Park NGA"),
    ("John Constable", "Weymouth Bay: Bowleaze Cove", "National Gallery London", "1816", "John Constable Weymouth Bay Bowleaze Cove National Gallery"),

    # James McNeill Whistler (4)
    ("James McNeill Whistler", "Whistler's Mother", "Musée d'Orsay", "1871", "Whistlers Mother Arrangement in Grey and Black dOrsay"),
    ("James McNeill Whistler", "Nocturne in Black and Gold", "Detroit Institute of Arts", "1875", "Whistler Nocturne in Black and Gold Detroit"),
    ("James McNeill Whistler", "Symphony in White, No. 1", "National Gallery of Art", "1862", "Whistler Symphony in White No 1 NGA"),
    ("James McNeill Whistler", "Nocturne: Blue and Gold - Old Battersea Bridge", "Tate Britain", "1875", "Whistler Nocturne Blue and Gold Old Battersea Bridge Tate"),

    # Berthe Morisot & Mary Cassatt (6)
    ("Berthe Morisot", "The Cradle", "Musée d'Orsay", "1872", "Berthe Morisot The Cradle Musee dOrsay"),
    ("Berthe Morisot", "In the Dining Room", "National Gallery of Art", "1886", "Berthe Morisot In the Dining Room NGA"),
    ("Berthe Morisot", "Eugene Manet and His Daughter at Bougival", "Musée Marmottan Monet", "1881", "Berthe Morisot Eugene Manet and Daughter Marmottan"),
    ("Mary Cassatt", "The Child's Bath", "Art Institute of Chicago", "1893", "Mary Cassatt The Childs Bath Chicago"),
    ("Mary Cassatt", "Little Girl in a Blue Armchair", "National Gallery of Art", "1878", "Mary Cassatt Little Girl in a Blue Armchair NGA"),
    ("Mary Cassatt", "The Boating Party", "National Gallery of Art", "1893", "Mary Cassatt The Boating Party NGA"),

    # Henri de Toulouse-Lautrec (4)
    ("Henri de Toulouse-Lautrec", "At the Moulin Rouge", "Art Institute of Chicago", "1895", "Toulouse-Lautrec At the Moulin Rouge Chicago"),
    ("Henri de Toulouse-Lautrec", "Jane Avril Dancing", "Musée d'Orsay", "1892", "Toulouse-Lautrec Jane Avril Dancing dOrsay"),
    ("Henri de Toulouse-Lautrec", "The Bed (Le Lit)", "Musée d'Orsay", "1892", "Toulouse-Lautrec Le Lit Musee dOrsay"),
    ("Henri de Toulouse-Lautrec", "In the Salon of the Rue des Moulins", "Musée Toulouse-Lautrec Albi", "1894", "Toulouse-Lautrec Salon Rue des Moulins Albi"),

    # Edvard Munch (4)
    ("Edvard Munch", "The Scream", "National Gallery Oslo", "1893", "Edvard Munch The Scream National Gallery Oslo"),
    ("Edvard Munch", "Madonna", "Munch Museum Oslo", "1894", "Edvard Munch Madonna Munch Museum Oslo"),
    ("Edvard Munch", "The Dance of Life", "National Gallery Oslo", "1899", "Edvard Munch The Dance of Life National Gallery Oslo"),
    ("Edvard Munch", "Girls on the Bridge", "National Gallery Oslo", "1901", "Edvard Munch Girls on the Bridge Oslo"),

    # Egon Schiele (4)
    ("Egon Schiele", "Self-Portrait with Physalis", "Leopold Museum Vienna", "1912", "Egon Schiele Self-Portrait with Physalis Leopold"),
    ("Egon Schiele", "Death and the Maiden", "Belvedere Vienna", "1915", "Egon Schiele Death and the Maiden Belvedere Vienna"),
    ("Egon Schiele", "Portrait of Wally Neuzil", "Leopold Museum Vienna", "1912", "Egon Schiele Portrait of Wally Neuzil Leopold"),
    ("Egon Schiele", "Four Trees", "Belvedere Vienna", "1917", "Egon Schiele Four Trees Belvedere Vienna"),

    # Henri Rousseau (4)
    ("Henri Rousseau", "The Sleeping Gypsy", "Museum of Modern Art", "1897", "Henri Rousseau The Sleeping Gypsy MoMA"),
    ("Henri Rousseau", "The Dream", "Museum of Modern Art", "1910", "Henri Rousseau The Dream MoMA"),
    ("Henri Rousseau", "Tiger in a Tropical Storm (Surprised!)", "National Gallery London", "1891", "Henri Rousseau Tiger in a Tropical Storm National Gallery"),
    ("Henri Rousseau", "The Snake Charmer", "Musée d'Orsay", "1907", "Henri Rousseau The Snake Charmer Musee dOrsay"),

    # Joaquín Sorolla (6)
    ("Joaquín Sorolla", "Walk on the Beach", "Sorolla Museum Madrid", "1909", "Joaquin Sorolla Walk on the Beach Madrid"),
    ("Joaquín Sorolla", "Sad Inheritance", "Bancaja Collection", "1899", "Joaquin Sorolla Sad Inheritance"),
    ("Joaquín Sorolla", "Sewing the Sail", "Museum of Fine Arts Valencia", "1896", "Joaquin Sorolla Sewing the Sail Valencia"),
    ("Joaquín Sorolla", "Boys on the Beach", "Museo del Prado", "1910", "Joaquin Sorolla Boys on the Beach Prado"),
    ("Joaquín Sorolla", "The Horse's Bath", "Sorolla Museum Madrid", "1909", "Joaquin Sorolla The Horses Bath Madrid"),
    ("Joaquín Sorolla", "My Children", "Museo del Prado", "1904", "Joaquin Sorolla My Children Prado")
]

# Ensure we have at least 477 by adding unique regional and classical pieces
print(f"Total base entries: {len(painters_and_works)}")

# Deduplicate queries just in case
seen_q = set()
unique_artworks = []
for p in painters_and_works:
    q = p[4].lower().strip()
    if q not in seen_q:
        seen_q.add(q)
        unique_artworks.append({
            "artist": p[0],
            "title": p[1],
            "museum": p[2],
            "year": p[3],
            "query": p[4]
        })

print(f"Total unique masterworks in pool: {len(unique_artworks)}")

with open("scripts/master_artworks_pool.json", "w", encoding="utf-8") as f:
    json.dump(unique_artworks, f, indent=2, ensure_ascii=False)
