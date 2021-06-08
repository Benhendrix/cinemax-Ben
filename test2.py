# Imports
import datetime
from datetime import datetime
import prettytable
from models.film import Film
from models.ticket import Ticket
from models.vertoning import Vertoning
from db.datamanager import Datamanager
from prettytable import PrettyTable
from colorama import init
from termcolor import colored
from adminapp.adminbeheermenus import duw_toets,toon_hoofdmenu,toon_film_menu,film_zoekmenu
from adminapp.adminbeheerfilms import film_verwijderen,toon_alle_films,toon_alle_films_alfa, voeg_film_toe, zoek_film_id, zoek_film_letters
# init() voor colorama te gebruiken
init()
# Variabele aangemaakt voor de datamanager
dm = Datamanager()
# Menu voor de admin
while True:
    toon_hoofdmenu()
    keuze = input("Kies een item uit het menu via een cijfer: ")
    print("")
    if keuze == "0":
        break
    if keuze == "1":
        while True:
            toon_film_menu()
            keuze = input("Kies een item uit het menu via een cijfer: ")
            print("")
            if keuze == "0":
                break

            if keuze == "1":
                toon_alle_films()
                duw_toets()
                continue

            if keuze == "2":
                toon_alle_films_alfa()
                duw_toets()
                continue

            if keuze == "3":
                voeg_film_toe()
                duw_toets()
                continue

            if keuze == "4":
                while True:
                    film_zoekmenu()
                    keuze = input("Kies een item uit het menu via een cijfer: ")
                    print("")
                    if keuze == "0":
                        break
                    if keuze == "1":
                        zoek_film_id()
                        duw_toets()
                        continue
                    if keuze == "2":
                        zoek_film_letters()
                        duw_toets()
                        continue

            if keuze == "5":
                film_verwijderen()
                duw_toets()
                continue
            


            