from datetime import datetime
from tkinter.constants import DISABLED
from models.ticket import Ticket
from sys import version
import PySimpleGUI as gui
from db.datamanager import Datamanager
from models.film import Film
from models.vertoning import Vertoning
# Documentatie: https://pysimplegui.readthedocs.io/en/latest/call%20reference/

dm = Datamanager()
vandaag = datetime.now()
vandaag_uur_str = vandaag.strftime("%H")
vandaag_min_str = vandaag.strftime("%M")
vandaag_uur = int(vandaag_uur_str)
vandaag_min = int(vandaag_min_str)
# Invullen van het uur.
while True:
    if vandaag_uur <= 10:
        uur = "11:00:00"
        break
    if vandaag_uur <= 13:
        uur = "14:00:00"
        break
    if vandaag_uur <= 16:
        uur = "17:00:00"
        break
    if vandaag_uur <= 19:
        uur = "20:00:00"
        break
    if vandaag_uur <= 22:
        uur = "23:00:00"
        break
    if vandaag_uur > 23:
        uur = "11:00:00"
    else:
        continue
films = dm.films_vandaag_uur(uur)
# Gui thema
gui.theme('DarkTeal10')

# Layout's
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
        [gui.Text("Omschrijving:",size=(15, 10)),gui.Text("",size=(40,10),key="-omschrijving-")]
    ]),
    gui.Column([
        [gui.Text("Zaal:",size=(15, 1)),gui.Text("",size=(40,1),key="-zaal-")],
        [gui.Text("afspeelmoment:",size=(15, 1)),gui.Text("",size=(40,1),key="-afspeelmoment-")],
        [gui.Text("Pauze:",size=(15, 1)),gui.Text("",size=(40,1),key="-pauze-")],
        [gui.Text("3D:",size=(15, 1)),gui.Text("",size=(40,1),key="-3D-")]         
    ])
]

layout_ticket_beschrijving = [
    gui.Column([]),
    gui.Column([
        [gui.Text("Prijs per kind:",size=(30, 1)),gui.Text("5.00 €",size=(15,1),key="-kind-")],
        [gui.Text("Prijs per volwassenen:",size=(30, 1)),gui.Text("7.00 € ",size=(15,1),key="-volwassen-")],
        [gui.Text("Geef het aantal tickets voor de kinderen in:",size=(30, None)),gui.Spin(values=[i for i in range(999)],initial_value=0,disabled=False,key="-kindtotaal-", size=(4, None),enable_events=True)],
        [gui.Text("Geef het aantal tickets voor de volwassenen in:",size=(30, None)),gui.Spin(values=[i for i in range(999)],initial_value=0,key="-volwassentotaal-", size=(4, None),enable_events=True)],
        [gui.Text("Toon totaal bedrag",size=(30,1)),gui.Text("", size=(30, None), key="-totaal-", font="bold")]
    ]),
        [gui.Button("Aankoop doen?",disabled=True, key="-b_aankoop-"),gui.Text("", size=(37, None), key="-aankoop-", font="bold")]
]

layout = [
    layout_titel,
    layout_listbox,
    layout_beschrijving,
    layout_ticket_beschrijving
]

window = gui.Window("CINEMAX", layout, size=(1500, 900),font= "Helvetica 14", element_justification="c")

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event == 'Cancel':
        break
    
    if event == "-films-":
        geselecteerde_film = values["-films-"][0]
        vertoningen = dm.vertoningen_filmId_uur(geselecteerde_film,uur)

        window["-vertoningen-"].update(values=vertoningen)
        # Aantal terug op 0 zetten.
        window["-totaal-"].update(value="0.00 €")
        window["-volwassentotaal-"].update(value=0)
        window["-b_aankoop-"].update(disabled=True)
        # Tickets toelaten of niet voor kinderen.
        film = values["-films-"][0]
        if film.kinderen == 0:
            window["-kindtotaal-"].update(disabled=True)
            window["-kindtotaal-"].update(value=0)
        if film.kinderen == 1:
            window["-kindtotaal-"].update(disabled=False)

    if event =="-films-":
        
        film = values["-films-"][0]
        window["-titel-"].update(value=film.titel_str)
        window["-kinderen-"].update(value=film.kinderen_str)
        window["-genres-"].update(value=film.genre_str)
        window["-speelduur-"].update(value=film.speelduur_str)
        window["-omschrijving-"].update(value=film.omschrijving_str)
        window["-aankoop-"].update(value=f"{film.titel}")

    if event == "-vertoningen-":
  
        vertoning = values["-vertoningen-"][0]
        window["-zaal-"].update(value=vertoning.zaal_str)
        window["-afspeelmoment-"].update(value=vertoning.afspeelmoment_uur)
        window["-pauze-"].update(value=vertoning.pauze_str)
        window["-3D-"].update(value=vertoning.dried_str)
        window["-aankoop-"].update(value=f"{film.titel}, {vertoning.zaal}, {vertoning.afspeelmoment_uur}")
    
    if event == "-kindtotaal-" or event == "-volwassentotaal-":
        kindtotaal = values.get("-kindtotaal-") or ""
        if kindtotaal == "":
            kindtotaal = 0
        volwasssentotaal = values.get("-volwassentotaal-") or ""
        if volwasssentotaal == "":
            volwasssentotaal = 0

        totaalprijs = int(kindtotaal)*5.00 + int(volwasssentotaal)*7.00
        totaalprijs_flt = format(totaalprijs,".2f")
    
        window["-totaal-"].update(value=f"{totaalprijs_flt} €")
        window["-aankoop-"].update(value=f"{film.titel}, {vertoning.zaal}, {vertoning.afspeelmoment_uur}, {totaalprijs_flt} €")
        if totaalprijs == 0:
            window["-b_aankoop-"].update(disabled=True)
        else:
            window["-b_aankoop-"].update(disabled=False)
 
window.close()