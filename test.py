from models.film import Film
from models.vertoning import Vertoning
from db.datamanager import Datamanager

dm = Datamanager()
"""
# Tonen van alle films
print("="*40)
films = dm.alle_films()
for film in films:
    print(film.titel)
print("")
print("="*40)

# Toon een film met gebruik van het id.
film2 = dm.film_by_id(2)
if film2:
    print(f"De film met id {film2.id} heet {film2.titel}")
print("")
print("="*40)
film4 = dm.film_by_id(4)
if film2:
    print(f"De film met id {film4.id} heet {film4.titel}")
print("")
print("="*40)

# Variabelen gemaakt voor nieuwe instantie van een film te maken
print("Film toevoegen:")
titel = "Jurassic Park"
speelduur = 127
genre =  "Avontuur, Sciencefiction"
kinderen = 0
omschrijving = "Wetenschappers slagen er in om dinosauriërs te klonen uit een druppel dino-bloed afkomstig uit een mug. De ondernemende miljonair John Hammond wil de gekloonde dino's aan het publiek laten zien en bouwt daarvoor een gigantisch thema-park."
imdb = "tt0107290"
nieuwe_film =Film(titel,speelduur,genre,kinderen,omschrijving,imdb) 

# Film toevoegen aan de db.
dm.film_toevoegen(nieuwe_film)

# Controle of de film is toegevoegt
films = dm.alle_films()
for film in films:
    print(film.titel)

# Verwijder film met id 3
dm.film_verwijderen(6)
# Controle of de film is verwijderd
films = dm.alle_films()
for film in films:
    print(film.titel)
"""
# Tonen van alle vertoningen
print("="*40)
vertoningen = dm.alle_vertoningen()
for vertoning in vertoningen:
    print(vertoning.id,vertoning.zaal,vertoning.afspeelmoment,vertoning.pauze,vertoning.drie_d,vertoning.film_id)
print("="*40)
# Tonen van alle vertoningen volgens datum
print("="*40)
vertoningen = dm.alle_vertoningen_datum()
for vertoning in vertoningen:
    print(vertoning.id,vertoning.zaal,vertoning.afspeelmoment,vertoning.pauze,vertoning.drie_d,vertoning.film_id)
print("="*40)
