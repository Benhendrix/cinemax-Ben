
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
    
    # Het maken van de instanties van de films.
    @classmethod
    def from_dict(cls,dict):
        kind = dict["kind"]
        volwassen = dict["volwassen"]
        totaal = dict["totaal"]
        vertoning_id = dict["vertoning_id"]
        id = dict["id"]

        return cls(kind,volwassen,vertoning_id,totaal,id)