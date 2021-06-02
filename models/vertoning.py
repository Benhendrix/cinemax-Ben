class vertoning:
    def __init__(self,zaal,afspeelmoment,pauze,drieD,filmID,id=None):
        self.zaal = zaal
        self.afspeelmoment = afspeelmoment
        self.pauze = pauze
        self.drieD = drieD
        self.filmID = filmID
        self._id = id
    
    @property
    def id(self):
        return self._id