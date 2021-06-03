
class Film:
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
    
    @classmethod
    def from_dict(cls,dict):
        titel = dict["titel"]
        speelduur = dict["speelduur"]
        genre = dict["genre"]
        kinderen = dict["kinderen"]
        omschrijving = dict["omschrijving"]
        imdb = dict["imdb"]
        id =dict["id"]

        return cls(titel,speelduur,genre,kinderen,omschrijving,imdb,id)
        
    
