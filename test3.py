from colorama import init
from termcolor import colored
# init() voor colorama te gebruiken
init()
# Menu's
def duw_toets():
    print(colored("Duw op een toets om verder te gaan...","yellow"))      
    input()
    
def toon_hoofdmenu():
    print("")
    print("="*50)
    print(colored("----------CINEMAX----------","blue"))
    print(colored("ADMIN MENU","yellow"))
    print(colored("1","yellow",),"BEHEER FILMS")
    print(colored("2","yellow",),"BEHEER VERTONINGEN")
    print(colored("3","yellow",),"BEHEER TICKETS")
    print(colored("0","yellow",),"AFSLUITEN")
    print("="*50)
    print("")

def toon_film_menu():
    print("")
    print("="*50)
    print(colored("BEHEER FILMS","yellow"))
    print(colored("1","yellow",),"Lijst van alle films")
    print(colored("2","yellow",),"Lijst van alle films op alfabetische volgorde")
    print(colored("3","yellow",),"Film toevoegen")
    print(colored("4","yellow",),"Film zoeken")
    print(colored("5","yellow",),"Film verwijderen")
    print(colored("0","yellow",),"Terug naar het hoofdmenu")
    print("="*50)
    print("")

def film_zoekmenu():
    print("")
    print("="*50)
    print("Zoek een film via het",colored("id","yellow"),"nummer of met zoeken via de",colored("letters","yellow"),": ")
    print(colored("1","yellow",),"Zoek op id")
    print(colored("2","yellow",),"Zoek via letter ingave")
    print(colored("0","yellow",),"Terug naar hoofdmenu")
    print("="*50)
    print("")

def toon_vertoning_menu():
    print("")
    print("="*50)
    print(colored("BEHEER VERTONINGEN","yellow"))
    print(colored("1","yellow",),"Lijst van alle vertoningen in de database")
    print(colored("2","yellow",),"Lijst van alle vertoningen van vandaag")
    print(colored("3","yellow",),"Vertoning toevoegen")
    print(colored("4","yellow",),"Vertoning verwijderen")
    print(colored("0","yellow",),"Terug naar het hoofdmenu")
    print("="*50)
    print("")