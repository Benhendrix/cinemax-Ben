from models.film import Film
from db.datamanager import Datamanager
from prettytable import PrettyTable
from colorama import init
from termcolor import colored

init()
dm = Datamanager()
# Menu voor de admin
while True:
 
    print("BEHEER FILMS")
    print(colored("1","yellow",),"Lijst van alle films")
    print(colored("2","yellow",),"Film toevoegen")
    print(colored("3","yellow",),"Film zoeken")
    print(colored("4","yellow",),"Film verwijderen")
    print(colored("0","yellow",),"Terug naar het hoofdmenu")
    keuze = input("Kies een item uit het menu via een cijfer: ")
    print("")
    
    # Toon alle films
    if keuze =="1":
        while True:
            table = PrettyTable()
            table.field_names=["id","titel","speelduur","genre","kinderen","imdb"]
            print("="*40)
            films = dm.alle_films()
            for film in films:
                table.add_row([film.id,film.titel,film.speelduur,film.genre,film.kinderen,film.imdb])
            print(table)
            break
        keuze = input("Duw op een toets om verder te gaan...")
        print("")

    # Voeg een film toe aan de klasse film en aan de database
    if keuze =="2":
        while True:
            # Geef de atributen in van een instantie van een film die word gemaakt
            print("Film toevoegen")
            titel = input("Geef de titel van de film in: ")
            speelduur = input("Geef de speelduur in minuten in als een getal: ")
            genre = input("Geef een genre of genres in gescheiden door komma's: ")
            kinderen = input("Geef een 0 voor niet toegelaten of een 1 voor wel toegelaten: ")
            omschrijving = input("Geef de omschrijving van de film in: ")
            imdb = input("Geef een geldig imdb nummer in: ")

            # Instantie van de film maken
            nieuwe_film = Film(titel,speelduur,genre,kinderen,omschrijving,imdb)

            # Film toevoegen aan de database
            dm.film_toevoegen(nieuwe_film)
            break
        keuze = input("Duw op een toets om verder te gaan...")
        print("")
    if keuze == "3":
        while True:
            print("Zoek een film met het id nummer of met zoeken via letters: ")
            print(colored("1","yellow",),"Zoek op id")
            print(colored("2","yellow",),"Zoek via letter ingave")
            print(colored("0","yellow",),"Terug naar hoofdmenu")
            keuze2 = input("Kies een item via een van de cijfers: ")
            if keuze2 == "0":
                break
            if keuze2 == "1":
                keuze_id = input("Geef een id nummer van een film in: ")
                print("")
                film_by_id = dm.film_by_id(keuze_id)
                if film_by_id:
                    print(f"De film met id {keuze_id} heet: {film_by_id.titel}")
                keuze = input("Duw op een toets om verder te gaan...")
            

            





