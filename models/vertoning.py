class Vertoning:
    def __init__(self,zaal,afspeelmoment,pauze,drie_d,film_id,id=None):
        self.zaal = zaal
        self.afspeelmoment = afspeelmoment
        self.pauze = pauze
        self.drie_d = drie_d
        self.film_id = film_id
        self._id = id
    
    @property
    def id(self):
        return self._id
    
    