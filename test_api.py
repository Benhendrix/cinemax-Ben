from datetime import datetime
from tkinter.constants import X
from db.datamanager import Datamanager
from prettytable import PrettyTable
from models.film import Film
dm=Datamanager()


films=dm.films_vandaag_uur("11:00:00")

films_list =[]
for x in films:
    print(x.titel)
    f=Film(x.titel,x.speelduur,x.genre,x.kinderen,x.omschrijving,x.imdb)
    films.append(f)
print(films_list)
