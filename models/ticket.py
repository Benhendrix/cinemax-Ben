from models.vertoning import Vertoning
class Ticket:
    def __init__(self,kind,volwassen,totaal,vertoning_id,id=None):
        self.kind = kind
        self.volwassen = volwassen
        self.totaal = totaal
        self.vertoning_id = vertoning_id
        self._id = id
    
    @property
    def id(self):
        return self._id

    @property
    def kind_prijs(self):
        return f"5.00 €"

    @property
    def volwassen_prijs(self):
        return f"7.00 €"

    @property
    def totaal_prijs(self):
        prijskind = 5
        prijsvolwassen = 7
        self.totaal = self.kind * prijskind + self.volwassen * prijsvolwassen
        return f"{self.totaal}"
    # Het maken van de instanties van de films.
    @classmethod
    def from_dict(cls,dict):
        kind = dict["kind"]
        volwassen = dict["volwassen"]
        totaal = dict["totaal"]
        vertoning_id = dict["vertoning_id"]
        id = dict["id"]

        return cls(kind,volwassen,totaal,vertoning_id,id)