import sqlite3
from db.datamanager import Datamanager
from prettytable import PrettyTable

dm = Datamanager()

table = PrettyTable()
table.field_names=["id","titel","speelduur","genre","kinderen","imdb"]
# Tonen van alle films
print("="*40)
films = dm.alle_films()
for film in films:
    table.add_row([film.id,film.titel,film.speelduur,film.genre,film.kinderen,film.imdb])

print(table)
print("")
print("="*40)