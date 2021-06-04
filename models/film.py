
from typing import ValuesView


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

    # Het maken van de instanties van de films.
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
        
    
