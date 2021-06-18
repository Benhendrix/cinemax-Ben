from datetime import datetime
from models.vertoning import Vertoning
from db.datamanager import Datamanager
from prettytable import PrettyTable
from models.film import Film
import PySimpleGUI as gui

dm = Datamanager()

uur ="20:00:00"
vertoningen = dm.vertoningen_vandaag_uur("11:00:00")

for items in vertoningen:
    print(items.zaal_str)
  