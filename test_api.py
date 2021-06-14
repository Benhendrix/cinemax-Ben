import PySimpleGUI as gui
from db.datamanager import Datamanager
from models.film import Film
from models.vertoning import Vertoning
# Documentatie: https://pysimplegui.readthedocs.io/en/latest/call%20reference/

dm = Datamanager()
films = dm.alle_films()
vertoningen = dm.alle_vertoningen()

print(films)