import requests
import json


ENDPOINT = "https://api.themoviedb.org/3/movie/"

api_key= "?api_key=56b70a17fca0d6f0cb706ca6e6882234"

keuze_film_int = "400"

resource = keuze_film_int+api_key

data = requests.get(ENDPOINT + resource).json()
x =json.dumps(data,indent=4)
print(type(x))
