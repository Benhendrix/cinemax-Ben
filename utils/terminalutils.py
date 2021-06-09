from ansimarkup import ansiprint as print
import os

def clear_terminal():
    os.system("cls" if os.name in ("nt", "dos") else "clear")

def print_instructie(tekst):
    print(f"<green>{tekst}</green>")

def print_waarschuwing(tekst):
    print(f"<yellow>{tekst}</yellow>")

def print_fout(tekst):
    print(f"<red>{tekst}</red>")

def invoer_getal(bereik):
    while True:
        invoer = input()
        try:
            invoer = int(invoer)
        except ValueError:
            print_fout("Invoer is geen getal.")
        else:
            if invoer not in bereik:
                print_fout("Getal niet in geldig bereik.")
            else:
                return invoer


def toon_menu(items, laatste_item="Terug naar vorig menu"):
    for index, item in enumerate(items):
        print(f"<green>{index + 1}.</green> {item}")
    
    print(f"<green>0.</green> {laatste_item}")

    print_instructie("Kies een item uit het menu via het cijfer.")
    keuze = invoer_getal(range(len(items) + 1))
    return keuze

