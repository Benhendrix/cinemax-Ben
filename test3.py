from datetime import datetime
from db.datamanager import Datamanager
dm = Datamanager()
vandaag = datetime.now()
str_vandaag= f"{vandaag.strftime('%Y')}-{vandaag.strftime('%M')}-{vandaag.strftime('%d')}"
tickets_vorige_week = dm.tickets_vorige_week(str_vandaag)
for ticket in tickets_vorige_week:
    print(ticket)