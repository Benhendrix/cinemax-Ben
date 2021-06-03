from models.film import Film
from db.datamanager import Datamanager

dm = Datamanager()
print("="*40)
films = dm.alle_films()
for film in films:
    print(film.titel)
print("")
print("="*40)
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
print("Film toevoegen:")
titel = "Jurassic Park"
speelduur = 127
genre =  "Avontuur, Sciencefiction"
kinderen = 0
omschrijving = "Wetenschappers slagen er in om dinosauriërs te klonen uit een druppel dino-bloed afkomstig uit een mug. De ondernemende miljonair John Hammond wil de gekloonde dino's aan het publiek laten zien en bouwt daarvoor een gigantisch thema-park."
imdb = "tt0107290"

nieuwe_film =Film(titel,speelduur,genre,kinderen,omschrijving,imdb) 

dm.film_toevoegen(nieuwe_film)
films = dm.alle_films()
for film in films:
    print(film.titel)
