from datetime import datetime
from sys import version
import PySimpleGUI as gui
from db.datamanager import Datamanager
from models.film import Film
from models.vertoning import Vertoning
# Documentatie: https://pysimplegui.readthedocs.io/en/latest/call%20reference/

dm = Datamanager()
uur ="20:00:00"
films = dm.films_vandaag_uur(uur)


gui.theme('DarkTeal10')

layout_titel = [gui.Text("Welkom bij Cinemax.",size=(20, 1),font= "Helvetica 32")]

layout_listbox = [
    gui.Column([
        [gui.Text("Kies een film")],
        [gui.Listbox(films, size=(25, 5), key="-films-", enable_events=True)]
    ]),
    gui.Column([
        [gui.Text("Kies een vertoning")],
        [gui.Listbox(values=[], size=(25, 5), key="-vertoningen-", enable_events=True)]
    ])
]

layout_beschrijving = [
    gui.Column([
    [gui.Text("Titel:",size=(15, 1)),gui.Text("",size=(40,1),key="-titel-")],
    [gui.Text("Kinderen:",size=(15, 1)),gui.Text("",size=(40,1),key="-kinderen-")],
    [gui.Text("Genres:",size=(15, 1)),gui.Text("",size=(40,1),key="-genres-")],
    [gui.Text("Speelduur:",size=(15, 1)),gui.Text("",size=(40,1),key="-speelduur-")],
    [gui.Text("Omschrijving:",size=(15, 5)),gui.Text("",size=(40,5),key="-omschrijving-")]
    ]),
    gui.Column([
    [gui.Text("Zaal:",size=(15, 1)),gui.Text("",size=(40,1),key="-zaal-")],
    [gui.Text("afspeelmoment:",size=(15, 1)),gui.Text("",size=(40,1),key="-afspeelmoment-")],
    [gui.Text("Pauze:",size=(15, 1)),gui.Text("",size=(40,1),key="-pauze-")],
    [gui.Text("3D:",size=(15, 1)),gui.Text("",size=(40,1),key="-3D-")]         
    ])
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
        vertoningen = dm.vertoningen_filmId_uur(geselecteerde_film,uur)

        window["-vertoningen-"].update(values=vertoningen)
     
    if event =="-films-":
        film = values["-films-"][0]

        window["-titel-"].update(value=film.titel_str)
        window["-kinderen-"].update(value=film.kinderen_str)
        window["-genres-"].update(value=film.genre_str)
        window["-speelduur-"].update(value=film.speelduur_str)
        window["-omschrijving-"].update(value=film.omschrijving_str)

    if event == "-vertoningen-":
        vertoning = values["-vertoningen-"][0]

        window["-zaal-"].update(value=vertoning.zaal_str)
        window["-afspeelmoment-"].update(value=vertoning.afspeelmoment_uur)
        window["-pauze-"].update(value=vertoning.pauze_str)
        window["-3D-"].update(value=vertoning.dried_str)

 
window.close()