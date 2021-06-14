from tkinter.constants import HORIZONTAL
import PySimpleGUI as gui
from db.datamanager import Datamanager
from models.film import Film
from models.vertoning import Vertoning
# Documentatie: https://pysimplegui.readthedocs.io/en/latest/call%20reference/

dm = Datamanager()
films = dm.alle_films()
vertoningen = dm.alle_vertoningen()

kolom_layout =[
    [gui.Text("Titel:", size=(15, 2)), gui.Text("", size=(30, 2), key="-titel-")],
    [gui.Text("Speelduur", size=(15, 1)), gui.Text("", size=(30, 1), key="-speelduur-")],
    [gui.Text("Kinderen", size=(15, 1)), gui.Text("", size=(30, 1), key="-kinderen-")],
    [gui.Text("Genre:", size=(15, 1)), gui.Text("", size=(30, 1), key="-genre-")],
    [gui.Text("Omschrijving:", size=(15, 10)), gui.Text("", size=(30, 10), key="-omschrijving-")],
]
kolom_layout2 =[

]
layout = [
    [gui.Text("Welkom bij Cinemax.",size=(20, 2),font= "Helvetica 16")],
    [gui.Listbox(films, size=(20, 20),pad=((0, 0), (0, 0)), key="-FILMS-", enable_events=True), gui.Column(kolom_layout, vertical_alignment="top")]
]


window = gui.Window("CINEMAX", layout, size=(1280, 740),font= "Helvetica 16", element_justification="c")

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event == 'Cancel' or event == "Sluiten":
        break
    if event == "-FILMS-":
        film = values["-FILMS-"][0]
        window["-titel-"].update(value=film.titel_str)
        window["-speelduur-"].update(value=film.speelduur_str)
        window["-kinderen-"].update(value=film.kinderen_str)
        window["-genre-"].update(value=film.genre_str)
        window["-omschrijving-"].update(value=film.omschrijving_str)


window.close()