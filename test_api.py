from datetime import datetime
from models.vertoning import Vertoning
from db.datamanager import Datamanager
from prettytable import PrettyTable
from models.film import Film
import PySimpleGUI as gui

dm = Datamanager()

uur ="20:00:00"
films = dm.films_vandaag_uur(uur)
list1 = []
list2 = []

for film in films:
    list1.append(dm.vertoningen_filmId_uur(film,uur))
for vertoningen in list1:
    for items in vertoningen:

        print(items,"1vertoning")


