import urllib.request
import urllib.parse
import json
import os
import time

HEADERS = {
    'User-Agent': 'HiyuAbyssResearchBot/1.0 (https://hiyuabyss.com; research@hiyuabyss.com)'
}

CANDIDATES = [
    # Italian Renaissance & Baroque
    ('Leonardo da Vinci', 'Ginevra de Benci', 'National Gallery of Art, Washington', '1474-1478', 'Leonardo da Vinci Ginevra de Benci'),
    ('Leonardo da Vinci', 'St. John the Baptist', 'Louvre Museum, Paris', '1513-1516', 'Leonardo da Vinci St John the Baptist'),
    ('Michelangelo', 'The Torment of Saint Anthony', 'Kimbell Art Museum', '1487-1488', 'Michelangelo Torment of Saint Anthony'),
    ('Raphael', 'Portrait of Baldassare Castiglione', 'Louvre Museum, Paris', '1514-1515', 'Raphael Portrait of Baldassare Castiglione'),
    ('Raphael', 'Madonna of the Meadow', 'Kunsthistorisches Museum, Vienna', '1506', 'Raphael Madonna of the Meadow'),
    ('Titian', 'Equestrian Portrait of Charles V', 'Prado Museum, Madrid', '1548', 'Titian Equestrian Portrait of Charles V'),
    ('Titian', 'The Entombment of Christ', 'Prado Museum, Madrid', '1559', 'Titian Entombment of Christ Prado'),
    ('Tintoretto', 'The Miracle of the Slave', 'Gallerie dell Accademia, Venice', '1548', 'Tintoretto Miracle of the Slave'),
    ('Tintoretto', 'The Origin of the Milky Way', 'National Gallery, London', '1575', 'Tintoretto Origin of the Milky Way'),
    ('Paolo Veronese', 'The Wedding at Cana', 'Louvre Museum, Paris', '1562-1563', 'Paolo Veronese Wedding at Cana'),
    ('Paolo Veronese', 'The Feast in the House of Levi', 'Gallerie dell Accademia, Venice', '1573', 'Paolo Veronese Feast in the House of Levi'),
    ('Caravaggio', 'Boy with a Basket of Fruit', 'Galleria Borghese, Rome', '1593', 'Caravaggio Boy with a Basket of Fruit'),
    ('Caravaggio', 'The Incredulity of Saint Thomas', 'Sanssouci, Potsdam', '1601-1602', 'Caravaggio Incredulity of Saint Thomas'),
    ('Artemisia Gentileschi', 'Self-Portrait as the Allegory of Painting', 'Royal Collection, UK', '1638-1639', 'Artemisia Gentileschi Self-Portrait Allegory of Painting'),
    ('Annibale Carracci', 'The Bean Eater', 'Galleria Colonna, Rome', '1584-1585', 'Annibale Carracci Bean Eater'),
    ('Annibale Carracci', 'The Flight into Egypt', 'Doria Pamphilj Gallery, Rome', '1603', 'Annibale Carracci Flight into Egypt'),
    ('Guido Reni', 'Saint Michael the Archangel', 'Santa Maria della Concezione dei Cappuccini, Rome', '1636', 'Guido Reni Saint Michael Archangel'),
    ('Guido Reni', 'Atalanta and Hippomenes', 'Prado Museum, Madrid', '1618-1619', 'Guido Reni Atalanta and Hippomenes'),
    ('Guercino', 'Et in Arcadia ego', 'Galleria Nazionale d Arte Antica, Rome', '1618-1622', 'Guercino Et in Arcadia ego'),
    ('Sandro Botticelli', 'Primavera', 'Uffizi Gallery, Florence', '1480', 'Botticelli Primavera'),
    ('Sandro Botticelli', 'Pallas and the Centaur', 'Uffizi Gallery, Florence', '1482', 'Botticelli Pallas and the Centaur'),
    ('Parmigianino', 'Self-portrait in a Convex Mirror', 'Kunsthistorisches Museum, Vienna', '1524', 'Parmigianino Self-portrait in a Convex Mirror'),
    ('Bronzino', 'Venus, Cupid, Folly and Time', 'National Gallery, London', '1545', 'Bronzino Venus Cupid Folly and Time'),
    ('Canaletto', 'The Stonemason Yard', 'National Gallery, London', '1725', 'Canaletto Stonemason Yard'),
    ('Tiepolo', 'The Banquet of Cleopatra', 'National Gallery of Victoria, Melbourne', '1744', 'Tiepolo Banquet of Cleopatra'),
    
    # Dutch Golden Age & Flemish
    ('Rembrandt', 'The Storm on the Sea of Galilee', 'Isabella Stewart Gardner Museum', '1633', 'Rembrandt Storm on the Sea of Galilee'),
    ('Rembrandt', 'Belshazzar Feast', 'National Gallery, London', '1635', 'Rembrandt Belshazzar Feast'),
    ('Rembrandt', 'The Blinding of Samson', 'Stadel Museum, Frankfurt', '1636', 'Rembrandt Blinding of Samson'),
    ('Rembrandt', 'The Return of the Prodigal Son', 'Hermitage Museum, Saint Petersburg', '1669', 'Rembrandt Return of the Prodigal Son'),
    ('Rembrandt', 'Danae', 'Hermitage Museum, Saint Petersburg', '1636', 'Rembrandt Danae Hermitage'),
    ('Rembrandt', 'Syndics of the Drapers Guild', 'Rijksmuseum, Amsterdam', '1662', 'Rembrandt Syndics of the Drapers Guild'),
    ('Johannes Vermeer', 'The Milkmaid', 'Rijksmuseum, Amsterdam', '1658-1659', 'Johannes Vermeer Milkmaid'),
    ('Johannes Vermeer', 'View of Delft', 'Mauritshuis, The Hague', '1660-1661', 'Johannes Vermeer View of Delft'),
    ('Johannes Vermeer', 'The Little Street', 'Rijksmuseum, Amsterdam', '1657-1658', 'Johannes Vermeer Little Street'),
    ('Johannes Vermeer', 'The Music Lesson', 'Royal Collection, UK', '1662-1665', 'Johannes Vermeer Music Lesson'),
    ('Johannes Vermeer', 'The Geographer', 'Stadel Museum, Frankfurt', '1668-1669', 'Johannes Vermeer Geographer'),
    ('Frans Hals', 'Malle Babbe', 'Gemaldegalerie, Berlin', '1633-1635', 'Frans Hals Malle Babbe'),
    ('Frans Hals', 'Gypsy Girl', 'Louvre Museum, Paris', '1628-1630', 'Frans Hals Gypsy Girl'),
    ('Frans Hals', 'Banquet of Officers of St George', 'Frans Hals Museum, Haarlem', '1616', 'Frans Hals Banquet Officers St George'),
    ('Jan Steen', 'The Feast of Saint Nicholas', 'Rijksmuseum, Amsterdam', '1665-1668', 'Jan Steen Feast of Saint Nicholas'),
    ('Jan Steen', 'The Dissolute Household', 'Apsley House, London', '1663-1664', 'Jan Steen Dissolute Household'),
    ('Pieter de Hooch', 'A Boy Bringing Bread', 'Wallace Collection, London', '1663', 'Pieter de Hooch Boy Bringing Bread'),
    ('Pieter de Hooch', 'Courtyard of a House in Delft', 'National Gallery, London', '1658', 'Pieter de Hooch Courtyard House Delft'),
    ('Jacob van Ruisdael', 'The Windmill at Wijk bij Duurstede', 'Rijksmuseum, Amsterdam', '1670', 'Jacob van Ruisdael Windmill Wijk'),
    ('Jacob van Ruisdael', 'The Jewish Cemetery', 'Gemaldegalerie Alte Meister, Dresden', '1655-1657', 'Jacob van Ruisdael Jewish Cemetery'),
    ('Meindert Hobbema', 'The Avenue at Middelharnis', 'National Gallery, London', '1689', 'Meindert Hobbema Avenue at Middelharnis'),
    ('Aelbert Cuyp', 'The Maas at Dordrecht', 'National Gallery of Art, Washington', '1650', 'Aelbert Cuyp Maas at Dordrecht'),
    ('Peter Paul Rubens', 'The Descent from the Cross', 'Cathedral of Our Lady, Antwerp', '1612-1614', 'Rubens Descent from the Cross Antwerp'),
    ('Peter Paul Rubens', 'The Garden of Love', 'Prado Museum, Madrid', '1633', 'Rubens Garden of Love Prado'),
    ('Peter Paul Rubens', 'The Judgment of Paris', 'National Gallery, London', '1636', 'Rubens Judgment of Paris London'),
    ('Peter Paul Rubens', 'Samson and Delilah', 'National Gallery, London', '1609-1610', 'Rubens Samson and Delilah'),
    ('Anthony van Dyck', 'Equestrian Portrait of Charles I', 'National Gallery, London', '1637-1638', 'Anthony van Dyck Equestrian Portrait Charles I'),
    ('Anthony van Dyck', 'Cupid and Psyche', 'Royal Collection, UK', '1638-1640', 'Anthony van Dyck Cupid and Psyche'),
    ('Anthony van Dyck', 'Self-Portrait with a Sunflower', 'Private Collection', '1633', 'Anthony van Dyck Self-Portrait Sunflower'),
    ('Pieter Bruegel the Elder', 'The Fall of the Rebel Angels', 'Royal Museums of Fine Arts of Belgium', '1562', 'Pieter Bruegel Fall of the Rebel Angels'),
    ('Pieter Bruegel the Elder', 'The Peasant Wedding', 'Kunsthistorisches Museum, Vienna', '1567', 'Pieter Bruegel Peasant Wedding'),
    ('Pieter Bruegel the Elder', 'Children Games', 'Kunsthistorisches Museum, Vienna', '1560', 'Pieter Bruegel Children Games'),
    ('Pieter Bruegel the Elder', 'The Netherlandish Proverbs', 'Gemaldegalerie, Berlin', '1559', 'Pieter Bruegel Netherlandish Proverbs'),
    ('Hieronymus Bosch', 'The Haywain Triptych', 'Prado Museum, Madrid', '1516', 'Hieronymus Bosch Haywain Triptych'),
    ('Hieronymus Bosch', 'Ship of Fools', 'Louvre Museum, Paris', '1490-1500', 'Hieronymus Bosch Ship of Fools'),
    ('Rogier van der Weyden', 'The Descent from the Cross', 'Prado Museum, Madrid', '1435', 'Rogier van der Weyden Descent Cross'),
    ('Jan van Eyck', 'The Arnolfini Portrait', 'National Gallery, London', '1434', 'Jan van Eyck Arnolfini Portrait'),
    ('Jan van Eyck', 'Madonna of Chancellor Rolin', 'Louvre Museum, Paris', '1435', 'Jan van Eyck Chancellor Rolin'),
    ('Judith Leyster', 'The Proposition', 'Mauritshuis, The Hague', '1631', 'Judith Leyster Proposition'),
    ('Judith Leyster', 'Self-Portrait', 'National Gallery of Art, Washington', '1630', 'Judith Leyster Self-Portrait'),
    ('Gerrit Dou', 'The Astronomer', 'National Gallery, London', '1650', 'Gerrit Dou Astronomer'),
    ('Hendrick Avercamp', 'Winter Landscape with Ice Skaters', 'Rijksmuseum, Amsterdam', '1608', 'Hendrick Avercamp Winter Landscape Ice Skaters'),
    ('Willem Claesz Heda', 'Still Life with Gilded Cup', 'Rijksmuseum, Amsterdam', '1635', 'Willem Claesz Heda Still Life Gilded Cup'),

    # Spanish Masterworks
    ('Diego Velázquez', 'The Triumph of Bacchus', 'Prado Museum, Madrid', '1628-1629', 'Diego Velazquez Triumph of Bacchus'),
    ('Diego Velázquez', 'The Surrender of Breda', 'Prado Museum, Madrid', '1634-1635', 'Diego Velazquez Surrender of Breda'),
    ('Diego Velázquez', 'Apollo in the Forge of Vulcan', 'Prado Museum, Madrid', '1630', 'Diego Velazquez Apollo Forge Vulcan'),
    ('Diego Velázquez', 'Portrait of Innocent X', 'Doria Pamphilj Gallery, Rome', '1650', 'Diego Velazquez Portrait Innocent X'),
    ('Diego Velázquez', 'The Spinners', 'Prado Museum, Madrid', '1657', 'Diego Velazquez Spinners Prado'),
    ('Francisco Goya', 'The Third of May 1808', 'Prado Museum, Madrid', '1814', 'Francisco Goya Third of May 1808'),
    ('Francisco Goya', 'The Parasol', 'Prado Museum, Madrid', '1777', 'Francisco Goya Parasol Prado'),
    ('Francisco Goya', 'Witches Flight', 'Prado Museum, Madrid', '1798', 'Francisco Goya Witches Flight'),
    ('Francisco Goya', 'Duel with Cudgels', 'Prado Museum, Madrid', '1820-1823', 'Francisco Goya Duel with Cudgels'),
    ('El Greco', 'The Burial of the Count of Orgaz', 'Santo Tome, Toledo', '1586-1588', 'El Greco Burial of the Count of Orgaz'),
    ('El Greco', 'View of Toledo', 'Metropolitan Museum of Art, New York', '1596-1600', 'El Greco View of Toledo'),
    ('El Greco', 'The Disrobing of Christ', 'Toledo Cathedral', '1577-1579', 'El Greco Disrobing of Christ'),
    ('Bartolomé Esteban Murillo', 'The Young Beggar', 'Louvre Museum, Paris', '1645-1650', 'Murillo Young Beggar Louvre'),
    ('Bartolomé Esteban Murillo', 'Two Women at a Window', 'National Gallery of Art, Washington', '1655-1660', 'Murillo Two Women at a Window'),
    ('Jusepe de Ribera', 'The Clubfoot', 'Louvre Museum, Paris', '1642', 'Jusepe de Ribera Clubfoot'),
    ('Francisco de Zurbarán', 'Saint Serapion', 'Wadsworth Atheneum, Hartford', '1628', 'Francisco de Zurbaran Saint Serapion'),

    # French Classical, Rococo & Neoclassical
    ('Nicolas Poussin', 'Landscape with the Funeral of Phocion', 'National Museum Cardiff', '1648', 'Nicolas Poussin Funeral of Phocion'),
    ('Nicolas Poussin', 'The Abduction of the Sabine Women', 'Louvre Museum, Paris', '1637-1638', 'Nicolas Poussin Abduction Sabine Women'),
    ('Claude Lorrain', 'Seaport with the Embarkation of Queen of Sheba', 'National Gallery, London', '1648', 'Claude Lorrain Embarkation Queen of Sheba'),
    ('Claude Lorrain', 'Pastoral Landscape', 'Louvre Museum, Paris', '1638', 'Claude Lorrain Pastoral Landscape'),
    ('Georges de La Tour', 'Joseph the Carpenter', 'Louvre Museum, Paris', '1642', 'Georges de La Tour Joseph the Carpenter'),
    ('Georges de La Tour', 'The Penitent Magdalene', 'Metropolitan Museum of Art, New York', '1640', 'Georges de La Tour Penitent Magdalene'),
    ('Jean-Antoine Watteau', 'The Embarkation for Cythera', 'Louvre Museum, Paris', '1717', 'Watteau Embarkation for Cythera'),
    ('Jean-Antoine Watteau', 'Pierrot', 'Louvre Museum, Paris', '1718-1719', 'Watteau Pierrot Louvre'),
    ('François Boucher', 'The Toilette of Venus', 'Metropolitan Museum of Art, New York', '1751', 'Boucher Toilette of Venus Met'),
    ('François Boucher', 'Diana Leaving the Bath', 'Louvre Museum, Paris', '1742', 'Boucher Diana Leaving the Bath'),
    ('Jean-Honoré Fragonard', 'The Swing', 'Wallace Collection, London', '1767', 'Fragonard The Swing Wallace'),
    ('Jean-Honoré Fragonard', 'The Reader', 'National Gallery of Art, Washington', '1770-1772', 'Fragonard The Reader'),
    ('Jean-Baptiste-Siméon Chardin', 'The Ray', 'Louvre Museum, Paris', '1728', 'Chardin The Ray Louvre'),
    ('Jean-Baptiste-Siméon Chardin', 'The Soap Bubble', 'National Gallery of Art, Washington', '1733-1734', 'Chardin Soap Bubble'),
    ('Jacques-Louis David', 'The Death of Marat', 'Royal Museums of Fine Arts of Belgium', '1793', 'Jacques-Louis David Death of Marat'),
    ('Jacques-Louis David', 'Oath of the Horatii', 'Louvre Museum, Paris', '1784', 'Jacques-Louis David Oath of the Horatii'),
    ('Jacques-Louis David', 'The Death of Socrates', 'Metropolitan Museum of Art, New York', '1787', 'Jacques-Louis David Death of Socrates'),
    ('Jacques-Louis David', 'Napoleon Crossing the Alps', 'Chateau de Malmaison', '1801', 'Jacques-Louis David Napoleon Crossing Alps'),
    ('Jean-Auguste-Dominique Ingres', 'The Valpinçon Bather', 'Louvre Museum, Paris', '1808', 'Ingres Valpincon Bather'),
    ('Jean-Auguste-Dominique Ingres', 'Jupiter and Thetis', 'Musee Granet, Aix-en-Provence', '1811', 'Ingres Jupiter and Thetis'),
    ('Jean-Auguste-Dominique Ingres', 'The Turkish Bath', 'Louvre Museum, Paris', '1862', 'Ingres Turkish Bath Louvre'),

    # Romanticism & Realism
    ('Eugène Delacroix', 'Liberty Leading the People', 'Louvre Museum, Paris', '1830', 'Delacroix Liberty Leading the People'),
    ('Eugène Delacroix', 'The Massacre at Chios', 'Louvre Museum, Paris', '1824', 'Delacroix Massacre at Chios'),
    ('Eugène Delacroix', 'The Death of Sardanapalus', 'Louvre Museum, Paris', '1827', 'Delacroix Death of Sardanapalus'),
    ('Théodore Géricault', 'The Raft of the Medusa', 'Louvre Museum, Paris', '1818-1819', 'Gericault Raft of the Medusa'),
    ('Gustave Courbet', 'A Burial at Ornans', 'Musee d Orsay, Paris', '1849-1850', 'Gustave Courbet Burial at Ornans'),
    ('Gustave Courbet', 'The Painters Studio', 'Musee d Orsay, Paris', '1855', 'Gustave Courbet Painters Studio'),
    ('Gustave Courbet', 'The Desperate Man', 'Private Collection', '1843-1845', 'Gustave Courbet Desperate Man'),
    ('Jean-François Millet', 'The Angelus', 'Musee d Orsay, Paris', '1857-1859', 'Jean-Francois Millet Angelus'),
    ('Jean-François Millet', 'The Gleaners', 'Musee d Orsay, Paris', '1857', 'Jean-Francois Millet Gleaners'),
    ('Jean-François Millet', 'The Sower', 'Museum of Fine Arts, Boston', '1850', 'Jean-Francois Millet Sower Boston'),
    ('Camille Corot', 'Souvenir de Mortefontaine', 'Louvre Museum, Paris', '1864', 'Camille Corot Souvenir de Mortefontaine'),
    ('Camille Corot', 'Bridge at Narni', 'Louvre Museum, Paris', '1826', 'Camille Corot Bridge at Narni'),
    ('Honoré Daumier', 'The Third-Class Carriage', 'Metropolitan Museum of Art, New York', '1862-1864', 'Honore Daumier Third-Class Carriage'),
    ('Honoré Daumier', 'Don Quixote', 'Neue Pinakothek, Munich', '1868', 'Honore Daumier Don Quixote'),
    ('Caspar David Friedrich', 'The Sea of Ice', 'Kunsthalle Hamburg', '1823-1824', 'Caspar David Friedrich Sea of Ice'),
    ('Arnold Böcklin', 'Isle of the Dead', 'Kunstmuseum Basel', '1880', 'Arnold Bocklin Isle of the Dead'),
    ('Henry Fuseli', 'The Nightmare', 'Detroit Institute of Arts', '1781', 'Henry Fuseli Nightmare'),
    ('William Blake', 'The Ancient of Days', 'British Museum, London', '1794', 'William Blake Ancient of Days'),

    # British Masterworks & Pre-Raphaelite
    ('J.M.W. Turner', 'The Fighting Temeraire', 'National Gallery, London', '1839', 'JMW Turner Fighting Temeraire'),
    ('J.M.W. Turner', 'Rain, Steam and Speed', 'National Gallery, London', '1844', 'JMW Turner Rain Steam Speed'),
    ('J.M.W. Turner', 'The Slave Ship', 'Museum of Fine Arts, Boston', '1840', 'JMW Turner Slave Ship'),
    ('John Constable', 'The Hay Wain', 'National Gallery, London', '1821', 'John Constable Hay Wain'),
    ('John Constable', 'Salisbury Cathedral from the Bishops Grounds', 'Victoria and Albert Museum, London', '1823', 'John Constable Salisbury Cathedral Bishops'),
    ('Thomas Gainsborough', 'The Blue Boy', 'Huntington Library, San Marino', '1770', 'Thomas Gainsborough Blue Boy'),
    ('Thomas Gainsborough', 'Mr and Mrs Andrews', 'National Gallery, London', '1750', 'Thomas Gainsborough Mr and Mrs Andrews'),
    ('William Hogarth', 'Marriage A-la-Mode The Tête à Tête', 'National Gallery, London', '1743', 'William Hogarth Marriage A-la-Mode'),
    ('George Stubbs', 'Whistlejacket', 'National Gallery, London', '1762', 'George Stubbs Whistlejacket'),
    ('John William Waterhouse', 'The Lady of Shalott', 'Tate Britain, London', '1888', 'John William Waterhouse Lady of Shalott'),
    ('John William Waterhouse', 'Hylas and the Nymphs', 'Manchester Art Gallery', '1896', 'John William Waterhouse Hylas Nymphs'),
    ('John William Waterhouse', 'Miranda The Tempest', 'Art Gallery of Ontario', '1916', 'John William Waterhouse Miranda Tempest'),
    ('Dante Gabriel Rossetti', 'Beata Beatrix', 'Tate Britain, London', '1864-1870', 'Dante Gabriel Rossetti Beata Beatrix'),
    ('Dante Gabriel Rossetti', 'Lady Lilith', 'Delaware Art Museum', '1866-1868', 'Dante Gabriel Rossetti Lady Lilith'),
    ('John Everett Millais', 'Ophelia', 'Tate Britain, London', '1851-1852', 'John Everett Millais Ophelia'),
    ('John Everett Millais', 'The Blind Girl', 'Birmingham Museum and Art Gallery', '1856', 'John Everett Millais Blind Girl'),
    ('Edward Burne-Jones', 'The Beguiling of Merlin', 'Lady Lever Art Gallery, Port Sunlight', '1874', 'Edward Burne-Jones Beguiling Merlin'),
    ('Ford Madox Brown', 'Work', 'Manchester Art Gallery', '1852-1865', 'Ford Madox Brown Work'),
    ('William Holman Hunt', 'The Light of the World', 'Keble College, Oxford', '1853-1854', 'William Holman Hunt Light of the World'),

    # Impressionism & Post-Impressionism
    ('Édouard Manet', 'Le Dejeuner sur l herbe', 'Musee d Orsay, Paris', '1863', 'Edouard Manet Le Dejeuner sur l herbe'),
    ('Édouard Manet', 'Olympia', 'Musee d Orsay, Paris', '1863', 'Edouard Manet Olympia'),
    ('Édouard Manet', 'A Bar at the Folies-Bergere', 'Courtauld Gallery, London', '1882', 'Edouard Manet Bar at the Folies-Bergere'),
    ('Claude Monet', 'Impression, Sunrise', 'Musee Marmottan Monet, Paris', '1872', 'Claude Monet Impression Sunrise'),
    ('Claude Monet', 'Woman with a Parasol', 'National Gallery of Art, Washington', '1875', 'Claude Monet Woman with a Parasol'),
    ('Claude Monet', 'The Rue Montorgueil in Paris', 'Musee d Orsay, Paris', '1878', 'Claude Monet Rue Montorgueil Paris'),
    ('Pierre-Auguste Renoir', 'Bal du moulin de la Galette', 'Musee d Orsay, Paris', '1876', 'Renoir Bal du moulin de la Galette'),
    ('Pierre-Auguste Renoir', 'Luncheon of the Boating Party', 'The Phillips Collection, Washington', '1881', 'Renoir Luncheon of the Boating Party'),
    ('Pierre-Auguste Renoir', 'The Large Bathers', 'Philadelphia Museum of Art', '1884-1887', 'Renoir Large Bathers Philadelphia'),
    ('Edgar Degas', 'L Absinthe', 'Musee d Orsay, Paris', '1876', 'Edgar Degas L Absinthe'),
    ('Edgar Degas', 'The Dance Class', 'Musee d Orsay, Paris', '1874', 'Edgar Degas Dance Class Musee d Orsay'),
    ('Edgar Degas', 'The Bellelli Family', 'Musee d Orsay, Paris', '1858-1867', 'Edgar Degas Bellelli Family'),
    ('Camille Pissarro', 'Boulevard Montmartre, Spring', 'Private Collection', '1897', 'Camille Pissarro Boulevard Montmartre Spring'),
    ('Alfred Sisley', 'Flood at Port-Marly', 'Musee d Orsay, Paris', '1876', 'Alfred Sisley Flood at Port-Marly'),
    ('Berthe Morisot', 'The Cradle', 'Musee d Orsay, Paris', '1872', 'Berthe Morisot Cradle'),
    ('Mary Cassatt', 'Little Girl in a Blue Armchair', 'National Gallery of Art, Washington', '1878', 'Mary Cassatt Little Girl Blue Armchair'),
    ('Mary Cassatt', 'The Child Bath', 'Art Institute of Chicago', '1893', 'Mary Cassatt The Child Bath'),
    ('Gustave Caillebotte', 'Paris Street Rainy Day', 'Art Institute of Chicago', '1877', 'Gustave Caillebotte Paris Street Rainy Day'),
    ('Gustave Caillebotte', 'The Floor Scrapers', 'Musee d Orsay, Paris', '1875', 'Gustave Caillebotte Floor Scrapers'),
    ('Vincent van Gogh', 'Starry Night Over the Rhone', 'Musee d Orsay, Paris', '1888', 'Vincent van Gogh Starry Night Over the Rhone'),
    ('Vincent van Gogh', 'Wheatfield with Crows', 'Van Gogh Museum, Amsterdam', '1890', 'Vincent van Gogh Wheatfield with Crows'),
    ('Vincent van Gogh', 'The Bedroom', 'Van Gogh Museum, Amsterdam', '1888', 'Vincent van Gogh Bedroom in Arles'),
    ('Paul Cézanne', 'The Large Bathers', 'Philadelphia Museum of Art', '1898-1905', 'Paul Cezanne Large Bathers'),
    ('Paul Cézanne', 'The Card Players', 'Musee d Orsay, Paris', '1894-1895', 'Paul Cezanne Card Players Musee d Orsay'),
    ('Paul Gauguin', 'Where Do We Come From', 'Museum of Fine Arts, Boston', '1897-1898', 'Paul Gauguin Where Do We Come From'),
    ('Paul Gauguin', 'The Yellow Christ', 'Albright-Knox Art Gallery, Buffalo', '1889', 'Paul Gauguin Yellow Christ'),
    ('Georges Seurat', 'A Sunday on La Grande Jatte', 'Art Institute of Chicago', '1884-1886', 'Georges Seurat Sunday on La Grande Jatte'),
    ('Georges Seurat', 'The Circus', 'Musee d Orsay, Paris', '1891', 'Georges Seurat Circus Musee d Orsay'),
    ('Paul Signac', 'The Port of Saint-Tropez', 'Musee de l Annonciade, Saint-Tropez', '1901', 'Paul Signac Port of Saint-Tropez'),
    ('Henri de Toulouse-Lautrec', 'At the Moulin Rouge', 'Art Institute of Chicago', '1892-1895', 'Toulouse-Lautrec At the Moulin Rouge'),
    ('Henri Rousseau', 'The Sleeping Gypsy', 'Museum of Modern Art, New York', '1897', 'Henri Rousseau The Sleeping Gypsy'),
    ('Henri Rousseau', 'The Dream', 'Museum of Modern Art, New York', '1910', 'Henri Rousseau The Dream MoMA'),
    ('Odilon Redon', 'The Cyclops', 'Kroller-Muller Museum, Otterlo', '1914', 'Odilon Redon Cyclops'),

    # American Masters & Realism
    ('Thomas Cole', 'The Course of Empire Destruction', 'New-York Historical Society', '1836', 'Thomas Cole Course of Empire Destruction'),
    ('Frederic Edwin Church', 'The Heart of the Andes', 'Metropolitan Museum of Art, New York', '1859', 'Frederic Edwin Church Heart of the Andes'),
    ('Albert Bierstadt', 'Among the Sierra Nevada Mountains', 'Smithsonian American Art Museum', '1868', 'Albert Bierstadt Among the Sierra Nevada'),
    ('Asher Brown Durand', 'Kindred Spirits', 'Crystal Bridges Museum of American Art', '1849', 'Asher Brown Durand Kindred Spirits'),
    ('Winslow Homer', 'The Gulf Stream', 'Metropolitan Museum of Art, New York', '1899', 'Winslow Homer Gulf Stream Met'),
    ('Winslow Homer', 'Fox Hunt', 'Pennsylvania Academy of the Fine Arts', '1893', 'Winslow Homer Fox Hunt'),
    ('Thomas Eakins', 'The Gross Clinic', 'Philadelphia Museum of Art', '1875', 'Thomas Eakins Gross Clinic'),
    ('Thomas Eakins', 'Max Schmitt in a Single Scull', 'Metropolitan Museum of Art, New York', '1871', 'Thomas Eakins Max Schmitt Single Scull'),
    ('John Singer Sargent', 'Carnation, Lily, Lily, Rose', 'Tate Britain, London', '1885-1886', 'John Singer Sargent Carnation Lily Lily Rose'),
    ('John Singer Sargent', 'The Daughters of Edward Darley Boit', 'Museum of Fine Arts, Boston', '1882', 'John Singer Sargent Daughters Edward Darley Boit'),
    ('James McNeill Whistler', 'Symphony in White No 1', 'National Gallery of Art, Washington', '1862', 'Whistler Symphony in White No 1'),
    ('Grant Wood', 'American Gothic', 'Art Institute of Chicago', '1930', 'Grant Wood American Gothic'),

    # Russian & Northern Masters
    ('Ilya Repin', 'Barge Haulers on the Volga', 'State Russian Museum, Saint Petersburg', '1870-1873', 'Ilya Repin Barge Haulers Volga'),
    ('Ilya Repin', 'Reply of the Zaporozhian Cossacks', 'State Russian Museum, Saint Petersburg', '1880-1891', 'Ilya Repin Zaporozhian Cossacks'),
    ('Ivan Shishkin', 'Morning in a Pine Forest', 'Tretyakov Gallery, Moscow', '1889', 'Ivan Shishkin Morning in a Pine Forest'),
    ('Arkhip Kuindzhi', 'Moonlit Night on the Dnieper', 'State Russian Museum, Saint Petersburg', '1880', 'Arkhip Kuindzhi Moonlit Night Dnieper'),
    ('Isaac Levitan', 'Golden Autumn', 'Tretyakov Gallery, Moscow', '1895', 'Isaac Levitan Golden Autumn'),
    ('Viktor Vasnetsov', 'Bogatyrs', 'Tretyakov Gallery, Moscow', '1898', 'Viktor Vasnetsov Bogatyrs'),
    ('Edvard Munch', 'The Sick Child', 'National Gallery, Oslo', '1885-1886', 'Edvard Munch Sick Child'),
    ('Peder Severin Krøyer', 'Summer Evening on Skagen Southern Beach', 'Skagens Museum', '1893', 'Peder Severin Kroyer Summer Evening Skagen')
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
    print(f"Total curated candidates: {len(CANDIDATES)}")
    out_file = "scripts/verified_artworks_download_list.json"
    
    verified_list = []
    if os.path.exists(out_file):
        try:
            with open(out_file, "r", encoding="utf-8") as f:
                verified_list = json.load(f)
        except Exception:
            verified_list = []
            
    already_done = set(item['title'] for item in verified_list)
    print(f"Already verified: {len(already_done)}")
    
    needed = 160 - len(verified_list)
    if needed <= 0:
        print("Already have at least 160 verified artworks!")
        return
        
    for idx, (artist, title, museum, year, query) in enumerate(CANDIDATES):
        if len(verified_list) >= 160:
            break
        if title in already_done:
            continue
            
        url, sz = search_wikimedia(query)
        if url and sz > 200000:
            verified_list.append({
                "artist": artist,
                "title": title,
                "museum": museum,
                "year": year,
                "url": url,
                "size_kb": sz // 1024,
                "safe_filename": f"fresh_art_{len(verified_list)+1:03d}_{title.lower().replace(' ', '_')[:25]}.jpg"
            })
            print(f"[{len(verified_list)}/160] FOUND: {title} by {artist} ({sz//1024} KB)")
        else:
            print(f"[-] SKIPPED: {title} by {artist}")
            
        time.sleep(0.15) # respectful delay
        
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(verified_list, f, ensure_ascii=False, indent=2)
    print(f"Successfully saved {len(verified_list)} verified artworks to {out_file}!")

if __name__ == "__main__":
    main()
