from models.film import Film
class Vertoning:
    def __init__(self,zaal,afspeelmoment,pauze,drie_d,film_id,id=None):
        self.zaal = zaal
        self.afspeelmoment = afspeelmoment
        self.pauze = pauze
        self.drie_d = drie_d
        self.film_id = film_id
        self._id = id
    
    # Dundermethodes
    def __str__(self):
        return f"{self.zaal}, {self.afspeelmoment[11:19]}"
    # ID eigenschap
    @property
    def id(self):
        return self._id
        
    # Datum eigenschap, moet een lengte van 19 hebben
    @property
    def afspeelmoment(self):
        return self._afspeelmoment

    @afspeelmoment.setter
    def afspeelmoment(self,afspeelmoment):
        if len(afspeelmoment) == 19:
            self._afspeelmoment = afspeelmoment
        else:
            raise ValueError
    # Atributen eigenschappen
    @property
    def afspeelmoment_uur(self):
        return f"{self.afspeelmoment[11:19]}"
    @property
    def pauze_str(self):
        if self.pauze == 0:
            return f"Er is geen pauze tijdens deze voorstelling."
        else:
            return f"Er is een pauze van 15 minuten tijdens de voorstelling."

    
    
    # Voor de datum te krijgen van een vertoning
    @classmethod
    def get_datum(cls):
        return cls.afspeelmoment

    # Het maken van de instanties van de vertoningen.
    @classmethod
    def from_dict(cls,dict):
        zaal = dict["zaal"]
        afspeelmoment = dict["afspeelmoment"]
        pauze = dict["pauze"]
        drie_d = dict["drie_d"]
        film_id = dict["film_id"]
        id = dict["id"]

        return cls(zaal,afspeelmoment,pauze,drie_d,film_id,id)
    