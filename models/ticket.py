class ticket:
    def __init__(self,kind,volwassen,totaal,vertoningID,id=None):
        self.kind = kind
        self.volwassen = volwassen
        self.totaal = totaal
        self.vertoningID = vertoningID
        self._id = id
    
    @property
    def id(self):
        return self._id