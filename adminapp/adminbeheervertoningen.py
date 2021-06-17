import prettytable
import os
from models.vertoning import Vertoning
from db.datamanager import Datamanager
from prettytable import PrettyTable
from ansimarkup import ansiprint as print
import datetime
from datetime import datetime
from utils.terminalutils import clear_terminal, print_fout, print_instructie, print_waarschuwing, toon_menu

def beheer_vertoningen():
    dm = Datamanager()

    menu_items =[
        "Lijst van alle vertoningen",
        "Lijst van alle vertoningen op datum",
        "Lijst van alle vertoningen van vandaag",
        "Vertoning toevoegen",
        "Vertoning verwijderen",
    ]

    while True:
        clear_terminal()
        print_instructie("BEHEER VERTONINGEN")
        keuze = toon_menu(menu_items)

        if keuze == 0:
            break

        if keuze == 1:
            while True:
                table = PrettyTable()
                table.field_names = ["id","zaal","afspeelmoment","pauze","drie_d","film_id"]
                vertoningen = dm.alle_vertoningen()
                for vertoning in vertoningen:
                    table.add_row([vertoning.id,vertoning.zaal,vertoning.afspeelmoment,vertoning.pauze,vertoning.drie_d,vertoning.film_id])
                print("")  
                print_instructie("LIJST VAN VERTONINGEN IN DATABASE")
                print(table)
                print("")
                break
            print("<i>Druk op enter om verder te gaan</i>")
            input() 
        if keuze == 2:
            while True:
                table = PrettyTable()
                table.field_names = ["id","zaal","afspeelmoment","pauze","drie_d","film_id"]
                vertoningen = dm.alle_vertoningen_datum()
                for vertoning in vertoningen:
                    table.add_row([vertoning.id,vertoning.zaal,vertoning.afspeelmoment,vertoning.pauze,vertoning.drie_d,vertoning.film_id])
                print("")  
                print_instructie("LIJST VAN VERTONINGEN IN DATABASE OP DATUM")
                print(table)
                print("")
                break
            print("<i>Druk op enter om verder te gaan</i>")
            input() 
        if keuze == 3:
            while True:
                table =PrettyTable()
                table.field_names = ["id","zaal","afspeelmoment","pauze","drie_d","film_id"]
                vertoningen_vandaag = dm.vertoningen_vandaag()
                for vertoning in vertoningen_vandaag:
                    table.add_row([vertoning.id,vertoning.zaal,vertoning.afspeelmoment,vertoning.pauze,vertoning.drie_d,vertoning.film_id])
                print("")
                print_instructie("LIJST VAN VERTONINGEN IN DATABASE VAN VANDAAG")
                print(table)
                print("")
                break
            print("<i>Druk op enter om verder te gaan</i>")
            input() 
        if keuze == 4:
            # Vertoning toevoegen
            while True:
                table = PrettyTable()
                # Geef de atributen in van een instantie van een Vertoning klasse
                print("")
                print("="*50)
                print_waarschuwing("Je kunt nu een vertoning toevoegen aan de database")
                print("="*50)
                print("")
                # Controle of de zaal is ingegeven
                while True: 
                    try: 
                        zaalnummer = int(input("Geef de zaalnummer in waar de vertoning wordt afgespeeld, er zijn 5 zalen: "))
                        print("")
                    except ValueError:
                        print("="*50)
                        print_fout("GEEN GELDIGE INPUT voor de zaalnummer!")
                        print("="*50)
                        print("")
                        continue
                    # Als er ooit zalen bijkomen of weggaan moet deze int(5) veranderd worden!
                    if zaalnummer <= 5:
                        break
                    else:
                        print("")
                        print("="*50)
                        print_fout("GEEN GELDIGE INPUT voor de zaal!")
                        print_fout("Gelieve de zaalnummer in te geven, er zijn maar 5 zalen!")
                        print("="*50)
                        print("")
                        continue
                zaal = f"Zaal {str(zaalnummer)}"
                # Controle of de datum correct is
                while True:
                    print_waarschuwing("Geef nu het jaar, de maand en de tijd in voor het afspeelmoment.")
                    print("")
                    while True:
                        jaar = input("Geef het jaar in bv 2020: ")
                        print("")
                        if jaar == "":
                            print_fout("Geen jaar ingegeven!")
                            print("")
                            continue
                        if len(jaar) != 4:
                            print_fout("Geef het jaar correct in!")
                            print("")
                            continue
                        else:
                            break
                    while True :
                        maand = input("Geef de maand in cijfers bv 08: ")
                        print("")
                        if maand == "":
                            print_fout("Geen maand ingegeven!")
                            print("")
                            continue
                        if len(maand) != 2:
                            print_fout("Geef de maand correct in!")
                            print("")
                            continue
                        else:
                            break
                    while True :
                        dag = input("Geef de dag in cijfers bv 04: ")
                        print("")
                        if dag == "":
                            print_fout("Geen dag ingegeven!")
                            print("")
                            continue
                        if len(dag) != 2:
                            print_fout("Geef de dag correct in!")
                            print("")
                            continue
                        else:
                            break
                    while True:
                        tijd = input("Geef het tijdstip in wanneer de vetoning afspeelt (HH:MM:SS): ")
                        print("")
                        if tijd == "":
                            print_fout("Geen tijd ingegeven!")
                            print("")
                            continue
                        if len(tijd) != 8:
                            print_fout("Geef de tijd correct in (HH:MM:SS)!")
                            print("")
                            continue
                        if tijd[2] != ":":
                            print_fout("Geef de tijd gescheiden door het (:) teken")
                            print("")
                            continue
                        if tijd[5] != ":":
                            print_fout("Geef de tijd gescheiden door het (:) teken","red")
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
                    if pauze.capitalize() == "J":
                        pauze = 1
                        break
                    if pauze.capitalize() =="N":
                        pauze = 0
                        break
                    else:
                        print("Gelieve J of N te gebruiken voor je keuze")
                        continue
                # Controle of er 3D is of niet
                while True:
                    drie_d = input("Geef in of de vertoning in 3D is (J/N): ")
                    print("")
                    if drie_d.capitalize() == "j":
                        drie_d = 1
                        break
                    if drie_d.capitalize() =="N":
                        drie_d = 0
                        break
                    else:
                        print("Gelieve J of N te gebruiken voor je keuze")
                        continue
                while True:
                    keuze_titel = input("Geef de titel van de film in: ") 
                    vertoning_film_titel =dm.film_by_titel(keuze_titel)
                    if vertoning_film_titel:
                        print("")
                        print("="*50)
                        print_instructie("De titel is gevonden in de database!")
                        print("="*50)
                        print("")
                        film_id = vertoning_film_titel.id
                        table.field_names =["zaal","afspeelmoment","pauze","drie_d","film_id"] 
                        table.add_row([zaal,afspeelmoment,pauze,drie_d,film_id]) 
                        print(table)
                        print("")
                        break
                    else:
                        print("")
                        print("="*50)
                        print_fout("De titel is niet gevonden in de database!")
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
                    print_instructie("De vertoning is toegevoegt aan de database")
                    print("="*50)
                    print("")
                    break
                else:
                    print("")
                    print("="*50)
                    print_fout("De vertoning is niet toegevoegd")
                    print("="*50)
                    print("")
                    break
            print("<i>Druk op enter om verder te gaan</i>")
            input() 
        if keuze == 5:
            while True:
                # Zoek op id om de vertoning uit de database te verwijderen
                print("")
                print("="*50)
                print_instructie("Je kunt nu een vertoning verwijderen uit de database")
                print("="*50)
                print("")
                while True:
                    keuze_verwijderen = input("Geef een id in om de vertoning te verwijderen: ")
                    vertoning_tonen = dm.vertoning_by_id(keuze_verwijderen)
                    if vertoning_tonen:
                        table = PrettyTable()
                        table.field_names=["id","zaal","afspeelmoment","pauze","drie_d","film_id"]
                        table.add_row([vertoning_tonen.id,vertoning_tonen.zaal,vertoning_tonen.afspeelmoment,vertoning_tonen.pauze,vertoning_tonen.drie_d,vertoning_tonen.film_id])
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
                print_waarschuwing("Ben je zeker of je de vertoning wil toevoegen")
                bevestiging = input("J/N: ")
                # Vragen aan de admin of hij zeker is voor het toevoegen van de vertoning aan de database hierbij hoort ook dat de instantie wordt aangemaakt binnen de klasse Film
                if bevestiging.capitalize() == "J":
                    # Vertoning verwijderen uit de database na bevestiging
                    dm.vertoning_verwijderen(keuze_verwijderen)
                    print("")
                    print("="*50)
                    print_instructie("De vertoning is verwijdert uit de database")
                    print("="*50)
                    print("")
                    break
                else:
                    # Vertoning niet verwijderen als J of j niet wordt gebruikt
                    print("")
                    print("="*50)
                    print_fout("De vertoning is niet verwijderd")
                    print("")
                    break
            print("<i>Druk op enter om verder te gaan</i>")
            input() 
        
