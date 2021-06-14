
class Film:
    def __init__(self,titel,speelduur,genre,kinderen,omschrijving,imdb,id=None):
        self.titel = titel
        self.speelduur = speelduur
        self.genre = genre
        self.kinderen = kinderen
        self.omschrijving = omschrijving
        self.imdb = imdb
        self._id = id

    # ID eigenschap
    @property
    def id(self):
        return self._id 

    # Controle of het IMDB nummer met "tt" begint.
    @property
    def imdb(self):
        return self._imdb

    @imdb.setter
    def imdb(self,imdb):
        if imdb[0:2] == "tt":
            self._imdb = imdb
        else:
            raise ValueError


    # Dundermethodes 
    def __str__(self):
        return self.titel
    @property
    def titel_str(self):
        return self.titel
    @property
    def speelduur_str(self):
        if self.speelduur >= 120:
            min = self.speelduur - 120
            return f"2u {min}min"
        if self.speelduur >= 60:
            min = self.speelduur - 60
            return f"1u {min}min"

    @property
    def genre_str(self):
        return f"{self.genre}"
    @property
    def kinderen_str(self):
        if self.kinderen == 0:
            return f"Kinderen zijn niet toegelaten!"
        else:
            return f"Kinderen zijn toegelaten."
    @property
    def omschrijving_str(self):
        return f"{self.omschrijving}"


    # Het maken van de instanties van de films.
    @classmethod
    def from_dict(cls,dict):
        titel = dict["titel"]
        speelduur = dict["speelduur"]
        genre = dict["genre"]
        kinderen = dict["kinderen"]
        omschrijving = dict["omschrijving"]
        imdb = dict["imdb"]
        id = dict["id"]

        return cls(titel,speelduur,genre,kinderen,omschrijving,imdb,id)
        
    
