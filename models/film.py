class film:
    def __init__(self,titel,speelduur,genre,kinderen,omschrijving,imdb,id=None):
        self.titel = titel
        self.speelduur = speelduur
        self.genre = genre
        self.kinderen = kinderen
        self.omschrijving = omschrijving
        self.imdb = imdb
        self._id = id
        
    @property
    def id(self):
        return self._id 
      
    
