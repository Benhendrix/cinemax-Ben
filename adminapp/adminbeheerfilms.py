import prettytable
import os
from models.film import Film
from db.datamanager import Datamanager
from prettytable import PrettyTable
from ansimarkup import ansiprint as print
import os
from utils.terminalutils import clear_terminal, invoer_getal, print_fout, print_instructie, print_waarschuwing, toon_menu

def beheer_films():
    dm = Datamanager()

    menu_items =[
        "Lijst van alle films",
        "Lijst van alle films op alfabetische volgorde",
        "Film toevoegen",
        "Film zoeken",
        "Film verwijderen",
    ]

    while True:
        clear_terminal()
        print_instructie("BEHEER FILMS")
        keuze = toon_menu(menu_items)
        
        if keuze == 0:
            break
        
        if keuze == 1:
            while True:  
                table = PrettyTable()  
                # Maak de kolom namen aan binnen de tabel
                table.field_names=["id","titel","speelduur","genre","kinderen","imdb"]
                # Haalt de data op met de datamanger
                films = dm.alle_films()
                # Voeg de rijen toe aan de tabel
                for film in films:
                    table.add_row([film.id,film.titel,film.speelduur,film.genre,film.kinderen,film.imdb])
                # Print de tabel af
                print("")
                print_instructie("LIJST VAN FILMS IN DATABASE")
                print(table)
                print("")
                break
            print("<i>Druk op enter om verder te gaan</i>")
            input()

        if keuze == 2:
            while True:
                table = PrettyTable()
                table.field_names=["id","titel","speelduur","genre","kinderen","imdb"]
                # Haalt de data op maar dan alfabetisch
                films = dm.alle_films_alfa()
                for film in films:
                    table.add_row([film.id,film.titel,film.speelduur,film.genre,film.kinderen,film.imdb])
                print("")
                print_instructie("LIJST VAN FILMS IN DATABASE ALFABETISCH")
                print(table)
                print("")
                break
            print("<i>Druk op enter om verder te gaan</i>")
            input()  

        if keuze == 3:
            while True:
                table = PrettyTable()
                # Geef de atributen in van een instantie van een film klasse
                print("")
                print("="*50)
                print_waarschuwing("Je kunt nu een film toevoegen aan de database")
                print("="*50)
                print("")
                # Controle of er een titel werdt ingegeven
                while True:  
                    titel = input("Geef de titel van de film in: ")
                    print("")
                    if titel == "":
                        print("")
                        print("="*50)
                        print_fout("GEEN GELDIGE INPUT voor de titel!")
                        print_fout("De titel is niet ingevuld!")
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
                        print_fout("GEEN GELDIGE INPUT voor het speelduur!")
                        print("="*50)
                        print("")
                        continue
                    if speelduur == 0:
                        print("")
                        print("="*50)
                        print_fout("GEEN GELDIGE INPUT voor het speelduur!")
                        print_fout("Je hebt 0 minuten ingegeven!")
                        print("="*50)
                        print("")
                        continue
                    if speelduur < 30:
                        print("")
                        print("="*50)
                        print_waarschuwing("De speelduur is nogal kort, onder de 30 min!")
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
                        print_fout("GEEN GELDIGE INPUT voor genre!")
                        print_fout("Het genre is niet ingevuld!")
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
                        print_fout("GEEN GELDIGE INPUT voor de kinderenn geef een getal in!")
                        print("="*50)
                        print("")
                        continue
                    if kinderen == 1 or kinderen == 0:
                        break
                    else:
                        print("="*50)
                        print_fout("GEEN GELDIGE INPUT voor de kinderen!")
                        print("="*50)
                        print("")
                        continue
                while True:  
                    omschrijving = input("Geef de omschrijving van de film in: ")
                    print("")
                    if omschrijving == "":
                        print("")
                        print("="*50)
                        print_fout("GEEN GELDIGE INPUT voor omschrijving!")
                        print_fout("De omschrijving van de film is niet ingevuld!")
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
                        print_fout("GEEN GELDIGE INPUT voor het imdb nummer!")
                        print("="*50)
                        print("")
                        continue
                table.field_names =["titel","speelduur","genre","kinderen","omschrijving","imdb"]
                table.add_row([titel,speelduur,genre,kinderen,omschrijving,imdb])
                print(table)
                print("")
                print_waarschuwing("Ben je zeker of je de film wil toevoegen")
                bevestiging = input("J/N: ")
                print("")
                if bevestiging.capitalize() == "J":
                    # Instantie van de film maken
                    nieuwe_film = Film(titel,speelduur,genre,kinderen,omschrijving,imdb)
                    # Film toevoegen aan de database
                    dm.film_toevoegen(nieuwe_film)
                    print("")
                    print("="*50)
                    print_instructie("De film is aan de database toegevoegd")
                    print("="*50)
                    print("")
                    break
                else:
                    print("")
                    print("="*50)
                    print_fout("De film is niet aan de database toegevoegd")
                    print("="*50)
                    print("")
                    break
            print("<i>Druk op enter om verder te gaan</i>")
            input() 

        if keuze == 4:
            menu_items2 = [
                "Zoek op id",
                "Zoek op letteringave"
            ]

            while True:
                clear_terminal()
                print_instructie("FILM ZOEKEN")
                keuze = toon_menu(menu_items2)
                print("")
                if keuze == 0:
                    break

                if keuze ==1:
                    while True:
                        keuze_id = input("Geef een id nummer van een film in: ")
                        print("")
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
                            print_fout("Het id is niet gevonden in de database!")
                            print("="*50)
                            print("")
                            print("")
                            continue
                    print("<i>Druk op enter om verder te gaan</i>")
                    input() 

                if keuze ==2:
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
                    print("<i>Druk op enter om verder te gaan</i>")
                    input() 
                    
        if keuze == 5:
            while True:
                # Zoek op id om de film uit de database te verwijderen
                print("")
                print("="*50)
                print_waarschuwing("Je kunt nu een film verwijderen van de database")
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
                        print_fout("Het id is niet gevonden in de database!")
                        print("="*50)
                        print("")
                        keuze_verwijderen = input("Geef een id in om de film te verwijderen: ")
                        print("")
                        continue
                print_waarschuwing("Ben je zeker of je de film wil toevoegen")
                bevestiging = input("J/N: ")
                # Vragen aan de admin of hij zeker is voor het toevoegen van de film aan de database hierbij hoort ook dat de instantie wordt aangemaakt binnen de klasse Film
                if bevestiging.capitalize() == "J":
                    # Film verwijderen uit de database na bevestiging
                    dm.film_verwijderen(keuze_verwijderen)
                    print("")
                    print("="*50)
                    print_instructie("De film is verwijdert uit de database")
                    print("="*50)
                    print("")
                    break
                else:
                    # Film niet verwijderen als J of j niet wordt gebruikt
                    print("")
                    print("="*50)
                    print_fout("De film is niet verwijderd")
                    print("")
                    break
            print("<i>Druk op enter om verder te gaan</i>")
            input()