from datetime import datetime
from tkinter.constants import HORIZONTAL
import PySimpleGUI as gui
from db.datamanager import Datamanager
from models.film import Film
from models.vertoning import Vertoning
# Documentatie: https://pysimplegui.readthedocs.io/en/latest/call%20reference/

dm = Datamanager()
films = dm.films_vandaag_uur("11:00:00")

gui.theme('DarkTeal10')

layout_titel = [gui.Text("Welkom bij Cinemax.",size=(20, 1),font= "Helvetica 32")]

layout_listbox = [
    gui.Column([
        [gui.Text("Kies een films")],
        [gui.Listbox(films, size=(25, 10), key="-films-", enable_events=True)]
    ]),
    gui.Column([
        [gui.Text("Kies een vertoning")],
        [gui.Listbox(values=[], size=(25, 10), key="-vertoningen-")]
    ])
]

layout_beschrijving = [
    [gui.Text("Titel:",size=(15, 1)),gui.Text("",size=(40,1),key="-titel-")],
    [gui.Text("Kinderen:",size=(15, 1)),gui.Text("",size=(40,1),key="-kinderen-")],
    [gui.Text("Genres:",size=(15, 1)),gui.Text("",size=(40,1),key="-genres-")],
    [gui.Text("Speelduur:",size=(15, 1)),gui.Text("",size=(40,1),key="-speelduur-")],
    [gui.Text("Omschrijving:",size=(15, 5)),gui.Text("",size=(40,5),key="-omschrijving-")]

]


layout = [
    layout_titel,
    layout_listbox,
    layout_beschrijving
]

window = gui.Window("CINEMAX", layout, size=(1400, 800),font= "Helvetica 16", element_justification="c")

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED:
        break
    if event == "-films-":
        geselecteerde_film = values["-films-"][0]
        vertoningen = dm.vertoningen_by_filmId(geselecteerde_film,"11:00:00")
        window["-vertoningen-"].update(values=vertoningen)
    if event =="-films-":
        film = values["-films-"][0]

        window["-titel-"].update(value=film.titel_str)
        window["-kinderen-"].update(value=film.kinderen_str)
        window["-genres-"].update(value=film.genre_str)
        window["-speelduur-"].update(value=film.speelduur_str)
        window["-omschrijving-"].update(value=film.omschrijving_str)

window.close()