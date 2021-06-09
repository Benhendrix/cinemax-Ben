import prettytable
from models.vertoning import Vertoning
from db.datamanager import Datamanager
from prettytable import PrettyTable
from colorama import init
from termcolor import colored
import datetime
from datetime import datetime
from adminapp.adminbeheermenus import duw_toets
# Voor colorama te gebruiken
init()
# Var voor de datamanger
dm = Datamanager()
# Voor de tabel te maken
def beheer_vertoningen():
    
    table1 = PrettyTable()
    while True:
        table1.field_names = ["id","zaal","afspeelmoment","pauze","drie_d","film_id"]
        vertoningen = dm.alle_vertoningen()
        for vertoning in vertoningen:
            table1.add_row([vertoning.id,vertoning.zaal,vertoning.afspeelmoment,vertoning.pauze,vertoning.drie_d,vertoning.film_id])
        print("")  
        print(colored("LIJST VAN VERTONINGEN IN DATABASE","yellow"))
        print(table1)
        print("")
        break

    table2 =PrettyTable()
    while True:
        table2.field_names = ["id","zaal","afspeelmoment","pauze","drie_d","film_id"]
        datum_vandaag = datetime.now()
        str_vandaag = datum_vandaag.strftime("%Y-%m-%d")
        vertoningen_vandaag = dm.vertoningen_vandaag(str_vandaag)
        for vertoning in vertoningen_vandaag:
            table2.add_row([vertoning.id,vertoning.zaal,vertoning.afspeelmoment,vertoning.pauze,vertoning.drie_d,vertoning.film_id])
        print("")
        print(colored("LIJST VAN VERTONINGEN IN DATABASE VAN VANDAAG","yellow"))
        print(table2)
        print("")
        break

    table3 = PrettyTable()
    # Vertoning toevoegen
    while True:
        # Geef de atributen in van een instantie van een Vertoning klasse
        print("")
        print("="*50)
        print(colored("Je kunt nu een vertoning toevoegen aan de database","yellow"))
        print("="*50)
        print("")
        # Controle of de zaal is ingegeven
        while True: 
            try: 
                zaalnummer = int(input("Geef de zaalnummer in waar de vertoning wordt afgespeeld, er zijn 5 zalen: "))
                print("")
            except ValueError:
                print("="*50)
                print(colored("GEEN GELDIGE INPUT voor de zaalnummer!","red"))
                print("="*50)
                print("")
                continue
            # Als er ooit zalen bijkomen of weggaan moet deze int(5) veranderd worden!
            if zaalnummer <= 5:
                break
            else:
                print("")
                print("="*50)
                print(colored("GEEN GELDIGE INPUT voor de zaal!","red"))
                print(colored("Gelieve de zaalnummer in te geven, er zijn maar 5 zalen!","red"))
                print("="*50)
                print("")
                continue
        zaal = f"Zaal {str(zaalnummer)}"
        # Controle of de datum correct is
        while True:
            print(colored("Geef nu het jaar, de maand en de tijd in voor het afspeelmoment.","yellow"))
            print("")
            while True:
                jaar = input("Geef het jaar in bv 2020: ")
                print("")
                if jaar == "":
                    print(colored("Geen jaar ingegeven!","red"))
                    print("")
                    continue
                if len(jaar) != 4:
                    print(colored("Geef het jaar correct in!","red"))
                    print("")
                    continue
                else:
                    break
            while True :
                maand = input("Geef de maand in cijfers bv 08: ")
                print("")
                if maand == "":
                    print(colored("Geen maand ingegeven!","red"))
                    print("")
                    continue
                if len(maand) != 2:
                    print(colored("Geef de maand correct in!","red"))
                    print("")
                    continue
                else:
                    break
            while True :
                dag = input("Geef de dag in cijfers bv 04: ")
                print("")
                if dag == "":
                    print(colored("Geen dag ingegeven!","red"))
                    print("")
                    continue
                if len(dag) != 2:
                    print(colored("Geef de dag correct in!","red"))
                    print("")
                    continue
                else:
                    break
            while True:
                tijd = input("Geef het tijdstip in wanneer de vetoning afspeelt (HH:MM:SS): ")
                print("")
                if tijd == "":
                    print(colored("Geen tijd ingegeven!","red"))
                    print("")
                    continue
                if len(tijd) != 8:
                    print(colored("Geef de tijd correct in (HH:MM:SS)!","red"))
                    print("")
                    continue
                if tijd[2] != ":":
                    print(colored("Geef de tijd gescheiden door het (:) teken","red"))
                    print("")
                    continue
                if tijd[5] != ":":
                    print(colored("Geef de tijd gescheiden door het (:) teken","red"))
                    print("")
                    continue
                else:
                    break
            break
        # Samenstellen van de datum en tijd voor afspeelmoment
        afspeelmoment = f"{jaar}-{maand}-{dag} {tijd}"
        # Controle of er een pauze is
        while True:
            pauze = input("Geef in of er een pauze is of niet (J/N): ")
            print("")
            if pauze == "":
                print("")
                print("="*50)
                print(colored("GEEN GELDIGE INPUT voor de pauze!","red"))                      
                print("="*50)
                print("")
                continue
            if pauze.capitalize == "J":
                pauze = 1
                break
            else:
                pauze = 0
                break
        # Controle of er 3D is of niet
        while True:
            drie_d = input("Geef in of de vertoning in 3D is (J/N): ")
            print("")
            if drie_d == "":
                print("")
                print("="*50)
                print(colored("GEEN GELDIGE INPUT voor de pauze!","red"))                      
                print("="*50)
                print("")
                continue
            if drie_d.capitalize == "J":
                drie_d = 1
                break
            else:
                drie_d = 0
                break 
        while True:
            keuze_titel = input("Geef de titel van de film in: ") 
            vertoning_film_titel =dm.film_by_titel(keuze_titel) 
            if vertoning_film_titel:
                print("")
                print("="*50)
                print(colored("De titel is gevonden in de database!","blue"))
                print("="*50)
                print("")
                film_id = vertoning_film_titel.id
                table3.field_names =["zaal","afspeelmoment","pauze","drie_d","film_id"] 
                table3.add_row([zaal,afspeelmoment,pauze,drie_d,film_id]) 
                print(table3)
                break
            else:
                print("")
                print("="*50)
                print(colored("De titel is niet gevonden in de database!","red"))
                print("="*50)
                print("")
                continue
        bevestiging = input("Ben je zeker of je de vertoning wilt toevoegen J/N: ")
        print("")
        if bevestiging.capitalize() == "J":
            # Instantie van de vertoning maken
            nieuwe_vertoning = Vertoning(zaal,afspeelmoment,pauze,drie_d,film_id)
            # vertoning toevoegen aan de database
            dm.vertoning_toevoegen(nieuwe_vertoning)
            print("")
            print("="*50)
            print(colored("De vertoning is toegevoegt aan de database","blue"))
            print("="*50)
            print("")
            break
        else:
            print("")
            print("="*50)
            print(colored("De vertoning is niet toegevoegd","red"))
            print("="*50)
            print("")
            break

