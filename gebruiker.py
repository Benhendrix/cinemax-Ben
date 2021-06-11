import PySimpleGUI as gui 
import requests
from test_image import get_img_data
class Gebruiker:
    class Gebruiker:
        def __init__(self, voornaam, naam, email, adres, avatar_url):
            self.voornaam = voornaam
            self.naam = naam
            self.email = email
            self.adres = adres
            self.avatar_url = avatar_url
        
        @property
        def volledige_naam(self):
            return f"{self.voornaam} {self.naam}"

        @property
        def straat(self):
            return f"{self.adres['street']['name']} {self.adres['street']['number']}"

        @property
        def plaats(self):
            return f"{self.adres['postcode']} {self.adres['city']}"

        @property
        def avatar(self):
            return get_img_data(self.avatar_url, first=True, local=False)

        def __str__(self):
            return f"{self.voornaam} {self.naam}"

        @classmethod
        def fromDict(cls, dict):

            return cls(
                dict["name"]["first"],
                dict["name"]["last"],
                dict["email"],
                dict["location"],
                dict["picture"]["large"]
            )
        @classmethod
        def from_api_dict(cls, dict):
            adres = {
                "straat": {
                    "naam": dict["location"]["street"]["name"],
                    "nummer": dict["location"]["street"]["number"]
                },
                "postcode": dict["location"]["postcode"],
                "stad": dict["location"]["city"]
            }
            return cls(
                dict["name"]["first"],
                dict["name"]["last"],
                dict["email"], 
                adres,
                dict["picture"]["large"]
            )


