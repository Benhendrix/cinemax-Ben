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