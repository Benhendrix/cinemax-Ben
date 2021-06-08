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

# init() voor colorama te gebruiken
init()
dm = Datamanager()
# Maak de tabel aan met PrettyTabel
table = PrettyTable()
table2 = PrettyTable()
# Funties voor data te verkrijgen, toe te voegen of te verwijderen
def toon_alle_films():
    while True:    
        # Maak de kolom namen aan binnen de tabel
        table.field_names=["id","titel","speelduur","genre","kinderen","imdb"]
        # Haalt de data op met de datamanger
        films = dm.alle_films()
        # Voeg de rijen toe aan de tabel
        for film in films:
            table.add_row([film.id,film.titel,film.speelduur,film.genre,film.kinderen,film.imdb])
        # Print de tabel af
        print("")
        print(colored("LIJST VAN FILMS IN DATABASE","yellow"))
        print(table)
        print("")
        break

def toon_alle_films_alfa():
    while True:
        table.field_names=["id","titel","speelduur","genre","kinderen","imdb"]
        # Haalt de data op maar dan alfabetisch
        films = dm.alle_films_alfa()
        for film in films:
            table.add_row([film.id,film.titel,film.speelduur,film.genre,film.kinderen,film.imdb])
        print("")
        print(colored("LIJST VAN FILMS IN DATABASE ALFABETISCH","yellow"))
        print(table)
        print("")
        break

def voeg_film_toe():
    while True:
        # Geef de atributen in van een instantie van een film klasse
        print("")
        print("="*50)
        print(colored("Je kunt nu een film toevoegen aan de database","yellow"))
        print("="*50)
        print("")
        # Controle of er een titel werdt ingegeven
        while True:  
            titel = input("Geef de titel van de film in: ")
            print("")
            if titel == "":
                print("")
                print("="*50)
                print(colored("GEEN GELDIGE INPUT voor de titel!","red"))
                print(colored("De titel is niet ingevuld!","red"))
                print("="*50)
                print("")
                continue
            else:
                break
        # Controle op het integer getal en of de speelduur leeg is
        while True:
            try:
                speelduur = int(input("Geef het speelduur in minuten in als een getal: "))
                print("")
            except ValueError:
                print("")
                print("="*50)
                print(colored("GEEN GELDIGE INPUT voor het speelduur!","red"))
                print("="*50)
                print("")
                continue
            if speelduur == 0:
                print("")
                print("="*50)
                print(colored("GEEN GELDIGE INPUT voor het speelduur!","red"))
                print(colored("Je hebt 0 minuten ingegeven!","red"))
                print("="*50)
                print("")
                continue
            if speelduur < 30:
                print("")
                print("="*50)
                print(colored("De speelduur is nogal kort, onder de 30 min!","red"))
                bevestiging = input("Ben je zeker van de speelduur J/N: ")
                print("="*50)
                print("")
                if bevestiging.capitalize() == "J":
                    break
                else:
                    continue 
            else:
                break    
        while True:  
            genre = input("Geef een genre of genres in: ")
            print("")
            if genre == "":
                print("")
                print("="*50)
                print(colored("GEEN GELDIGE INPUT voor genre!","red"))
                print(colored("Het genre is niet ingevuld!","red"))
                print("="*50)
                print("")
                continue
            else:
                break
        # Controle op integer getal 
        while True:
            try:
                kinderen = int(input("Geef een 0 voor niet toegelaten voor kinderen of een 1 voor wel toegelaten: "))
                print("")
            except ValueError:
                print("="*50)
                print(colored("GEEN GELDIGE INPUT voor de kinderen!","red"))
                print("="*50)
                print("")
                continue
            if kinderen == 1 or kinderen == 0:
                break
            else:
                print("="*50)
                print(colored("GEEN GELDIGE INPUT voor de kinderen!","red"))
                print("="*50)
                print("")
                continue  
        while True:  
            omschrijving = input("Geef de omschrijving van de film in: ")
            print("")
            if omschrijving == "":
                print("")
                print("="*50)
                print(colored("GEEN GELDIGE INPUT voor omschrijving!","red"))
                print(colored("De omschrijving van de film is niet ingevuld!","red"))
                print("="*50)
                print("")
                continue
            else:
                break
        while True:
            imdb = input("Geef een geldig imdb nummer in: ")
            print("")
            if imdb[0:2] == "tt":
                break
            else:
                print("")
                print("="*50)
                print(colored("GEEN GELDIGE INPUT voor het imdb nummer!","red"))
                print("="*50)
                print("")
                continue
        table2.field_names =["titel","speelduur","genre","kinderen","omschrijving","imdb"]
        table2.add_row([titel,speelduur,genre,kinderen,omschrijving,imdb])
        print(table2)
        print(colored("Ben je zeker of je de film wil toevoegen","yellow"))
        bevestiging = input("J/N: ")
        print("")
        if bevestiging.capitalize() == "J":
            # Instantie van de film maken
            nieuwe_film = Film(titel,speelduur,genre,kinderen,omschrijving,imdb)
            # Film toevoegen aan de database
            dm.film_toevoegen(nieuwe_film)
            print("")
            print("="*50)
            print(colored("De film","blue"),"("+nieuwe_film.titel+")",colored("is toegevoegd aan de database","yellow"))
            print("="*50)
            print("")
            break
        else:
            print("")
            print("="*50)
            print(colored("De film is niet toegevoegd","red"))
            print("="*50)
            print("")
            break

def zoek_film_id():
    keuze_id = input("Geef een id nummer van een film in: ")
    print("")
    while True:
        film_by_id = dm.film_by_id(keuze_id)
        if film_by_id:
            table = PrettyTable()
            table.field_names=["id","titel","speelduur","genre","kinderen","imdb"]
            table.add_row([film_by_id.id,film_by_id.titel,film_by_id.speelduur,film_by_id.genre,film_by_id.kinderen,film_by_id.imdb])
            print("")
            print(table)
            print("")
            break
        else:
            print("")
            print("="*50)
            print(colored("Het id is niet gevonden in de database!","red"))
            print("="*50)
            print("")
            keuze_id = input("Geef een id nummer van een film in: ")
            print("")
            continue
def zoek_film_letters():
    keuze_ingave = input("Geef letters in om te zoeken in de database naar films: ")
    print("")
    films_zoek_op_ingave = dm.zoek_film_op_ingave(keuze_ingave)
    table = PrettyTable()
    table.field_names =["id","titel","speelduur","genre","kinderen","imdb"]

    for film in films_zoek_op_ingave:
        table.add_row([film.id,film.titel,film.speelduur,film.genre,film.kinderen,film.imdb])
    print("")   
    print(table)
    print("")

def film_verwijderen():
    while True:
        # Zoek op id om de film uit de database te verwijderen
        print("")
        print("="*50)
        print(colored("Je kunt nu een film verwijderen van de database","yellow"))
        print("="*50)
        print("")
        keuze_verwijderen = input("Geef een id in om de film te verwijderen: ")
        print("")
        while True:
            film_tonen = dm.film_by_id(keuze_verwijderen)
            if film_tonen:
                    table = PrettyTable()
                    table.field_names=["id","titel","speelduur","genre","kinderen","imdb"]
                    table.add_row([film_tonen.id,film_tonen.titel,film_tonen.speelduur,film_tonen.genre,film_tonen.kinderen,film_tonen.imdb])
                    print("")
                    print(table)
                    print("")
                    break
            else:
                print("")
                print("="*50)
                print(colored("Het id is niet gevonden in de database!","red"))
                print("="*50)
                print("")
                keuze_verwijderen = input("Geef een id in om de film te verwijderen: ")
                print("")
                continue
        bevestiging = input("Ben je zeker of je de film wilt verwijderen J/N: ")
        print("")
        # Vragen aan de admin of hij zeker is voor het toevoegen van de film aan de database hierbij hoort ook dat de instantie wordt aangemaakt binnen de klasse Film
        if bevestiging.capitalize() == "J":
            # Film verwijderen uit de database na bevestiging
            dm.film_verwijderen(keuze_verwijderen)
            print("")
            print("="*50)
            print(colored("De film is verwijdert uit de database","blue"))
            print("="*50)
            print("")
            break
        else:
            # Film niet verwijderen als J of j niet wordt gebruikt
            print("")
            print("="*50)
            print(colored("De film is niet verwijderd","red"))
            print("="*50)
            print("")
            break