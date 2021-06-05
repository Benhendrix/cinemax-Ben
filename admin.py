# Imports
import prettytable
from models.film import Film
from models.ticket import Ticket
from models.vertoning import Vertoning
from db.datamanager import Datamanager
from prettytable import PrettyTable
from colorama import init
from termcolor import colored

# init() voor colorama te gebruiken
init()

# Variabele aangemaakt voor de datamanager
dm = Datamanager()

# Menu voor de admin
while True:
    print("")
    print("="*40)
    print(colored("ADMIN MENU","yellow"))
    print(colored("1","yellow",),"BEHEER FILMS")
    print(colored("2","yellow",),"BEHEER VERTONINGEN")
    print(colored("3","yellow",),"BEHEER TICKETS")
    print("="*40)
    print("")
    keuze = input("Kies een item uit het menu via een cijfer: ")
    print("")
    # Het beheer van de films 
    if keuze == "1":
        while True:
            print("")
            print("="*40)
            print(colored("BEHEER FILMS","yellow"))
            print(colored("1","yellow",),"Lijst van alle films")
            print(colored("2","yellow",),"Lijst van alle films op alfabetische volgorde")
            print(colored("3","yellow",),"Film toevoegen")
            print(colored("4","yellow",),"Film zoeken")
            print(colored("5","yellow",),"Film verwijderen")
            print(colored("0","yellow",),"Terug naar het hoofdmenu")
            print("="*40)
            print("")
            keuze = input("Kies een item uit het menu via een cijfer: ")
            print("")
            # Terug na vorig menu gaan
            if keuze == "0":
                break
            # Toon alle films aan de admin
            if keuze =="1":
                while True:
                    table = PrettyTable()
                    table.field_names=["id","titel","speelduur","genre","kinderen","imdb"]
                    print("="*40)
                    films = dm.alle_films()
                    for film in films:
                        table.add_row([film.id,film.titel,film.speelduur,film.genre,film.kinderen,film.imdb])
                    print(colored("LIJST VAN FILMS IN DATABASE","yellow"))
                    print(table)
                    break
                keuze = input("Duw op een toets om verder te gaan...")
                print("")
            # Toon alle films aan de admin
            if keuze =="2":
                while True:
                    table = PrettyTable()
                    table.field_names=["id","titel","speelduur","genre","kinderen","imdb"]
                    print("="*40)
                    films = dm.alle_films_alfa()
                    for film in films:
                        table.add_row([film.id,film.titel,film.speelduur,film.genre,film.kinderen,film.imdb])
                    print(colored("LIJST VAN FILMS IN DATABASE ALFABETISCH","yellow"))
                    print(table)
                    break
                keuze = input("Duw op een toets om verder te gaan...")
                print("")
            # Voeg een film toe aan de database
            if keuze =="3":
                while True:
                    # Geef de atributen in om een instantie te makken binnen Film en om aan de database toe te voegen
                    print(colored("Je kunt nu een film toevoegen aan de database","yellow"))
                    print("")
                    titel = input("Geef de titel van de film in: ")
                    try:
                        speelduur = int(input("Geef de speelduur in minuten in als een getal: "))
                    except ValueError:
                        print(colored("GEEN GELDIGE INPUT","red"))
                        print(colored("Terug naar film toevoegen!!!","red"))
                        print("")
                        continue

                    genre = input("Geef een genre of genres in gescheiden door komma's: ")
                    kinderen = int(input("Geef een 0 voor niet toegelaten voor kinderen of een 1 voor wel toegelaten: "))
                    omschrijving = input("Geef de omschrijving van de film in: ")
                    imdb = input("Geef een geldig imdb nummer in: ")
                    print("")
                    bevestiging = input("Ben je zeker of je de film wil toevoegen J/N: ")
                    print("")
                    # Vragen aan de admin of hij zeker is voor het toevoegen van de film aan de database hierbij hoort ook dat de instantie wordt aangemaakt binnen de klasse Film
                    if bevestiging.capitalize() == "J":
                        # Instantie van de film maken
                        nieuwe_film = Film(titel,speelduur,genre,kinderen,omschrijving,imdb)
                        # Film toevoegen aan de database
                        dm.film_toevoegen(nieuwe_film)
                        print(colored("De film","yellow"),"("+nieuwe_film.titel+")",colored("is toegevoegd aan de database","yellow"))
                        print("")
                        break
                    else:
                        print(colored("De film is niet toegevoegd","yellow"))
                        print("")
                        break
                keuze = input("Duw op een toets om verder te gaan...")
                print("")
            # Zoek een film op op id of via letteringave
            if keuze == "4":
                while True:
                    print("")
                    print("="*40)
                    print("Zoek een film via het",colored("id","yellow"),"nummer of met zoeken via de",colored("letters","yellow"),": ")
                    print(colored("1","yellow",),"Zoek op id")
                    print(colored("2","yellow",),"Zoek via letter ingave")
                    print(colored("0","yellow",),"Terug naar hoofdmenu")
                    print("="*40)
                    print("")
                    keuze = input("Kies een item via een van de cijfers: ")
                    print("")
                    if keuze == "0":
                        break
                    # Zoeken op het id van de film
                    if keuze == "1":
                        keuze_id = input("Geef een id nummer van een film in: ")
                        print("")
                        film_by_id = dm.film_by_id(keuze_id)

                        if film_by_id:
                            table2 = PrettyTable()
                            table2.field_names=["id","titel","speelduur","genre","kinderen","imdb"]
                            table2.add_row([film_by_id.id,film_by_id.titel,film_by_id.speelduur,film_by_id.genre,film_by_id.kinderen,film_by_id.imdb])
                            print(table2)
                        keuze = input("Duw op een toets om verder te gaan...")
                        print("")
                    # Zoeken op letteringave 
                    if keuze == "2":
                        keuze_ingave = input("Geef letters in om te zoeken in de database naar films: ")
                        print("")
                        films_zoek_op_ingave = dm.zoek_film_op_ingave(keuze_ingave)
                        table3 = PrettyTable()
                        table3.field_names =["id","titel","speelduur","genre","kinderen","imdb"]
                        for film in films_zoek_op_ingave:
                            table3.add_row([film.id,film.titel,film.speelduur,film.genre,film.kinderen,film.imdb])
                        print(table3)
                        print("")
                        keuze = input("Duw op een toets om verder te gaan...")
           