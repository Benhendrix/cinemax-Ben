
class Vertoning:
    def __init__(self,zaal,afspeelmoment,pauze,drie_d,film_id,id=None):
        self.zaal = zaal
        self.afspeelmoment = afspeelmoment
        self.pauze = pauze
        self.drie_d = drie_d
        self.film_id = film_id
        self._id = id
    # ID eigenschap
    @property
    def id(self):
        return self._id
    
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
    