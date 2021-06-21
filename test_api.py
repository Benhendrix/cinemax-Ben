from db.datamanager import Datamanager
from models.film import Film
from models.vertoning import Vertoning
from datetime import datetime
# Documentatie: https://pysimplegui.readthedocs.io/en/latest/call%20reference/

dm = Datamanager()
vandaag = datetime.now()

vandaag_uur_str = vandaag.strftime("%H")
vandaag_min_str = vandaag.strftime("%M")
vandaag_uur = int(13)
vandaag_min = int(46)
while True:
    if vandaag_uur <= 10:
        if vandaag_min <= 45:
            uur = "11:00:00"
            break
    if vandaag_uur <= 13:
        if vandaag_min <= 45:
            uur = "14:00:00"
            break
    if vandaag_uur <= 16:
        if vandaag_min <= 45:
            uur = "17:00:00"
            break
    if vandaag_uur <= 19:
        if vandaag_min <= 45:
            uur = "20:00:00"
            break
    if vandaag_uur <= 22:
        if vandaag_min <= 45:
            uur = "23:00:00"
            break
    if vandaag_uur > 23:
        uur = "11:00:00"
    else:
        continue
print(uur)