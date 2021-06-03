from db.datamanager import Datamanager

dm = Datamanager()
films = dm.alle_films()
for film in films:
    print(film.titel)