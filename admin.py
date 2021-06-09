from ansimarkup import ansiprint as print
from utils.terminalutils import clear_terminal, toon_menu
from adminapp.adminbeheerfilms import beheer_films
from adminapp.adminbeheervertoningen import beheer_vertoningen
menu_items = [
    "BEHEER FILMS",
    "BEHEER VERTONINGEN",
    "BEHEER TICKETS"   
]

while True:
    clear_terminal()
    print("<white,blue>  CINEMAX  </white,blue>")
    keuze = toon_menu(menu_items, "Afsluiten")

    if keuze == 0:
        break
    
    if keuze == 1:
        beheer_films()

    if keuze == 2:
        beheer_vertoningen()

    if keuze == 3:
        pass