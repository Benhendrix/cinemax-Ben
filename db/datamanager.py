from models.film import Film
from models.ticket import Ticket
from models.vertoning import Vertoning
from db.database import dbconn
"""
class Datamanager:

    def alle_films(self):
        with dbconn() as cur:
            sql = "SELECT * FROM films"
            cur.execute(sql)
            rijen = cur.fetchall()
            films = []
            for rij in rijen:
                films.append(Film(rij))
            return rijen
"""
class Datamanager:

    def alle_films(self):
        with dbconn() as cur:
            sql = "SELECT * FROM films"
            cur.execute(sql)
            rijen = cur.fetchall()
            """
            films = []
            for rij in rijen:
                films.append(Film.from_dict(rij))
            """
            films = [Film.from_dict(rij)for rij in rijen]

            return films
    
    def film_by_id(self,id):
        with dbconn() as cur:
            sql = "SELECT * FROM films WHERE id = ?"
            cur.execute(sql,[id])
            rij = cur.fetchone()
            """
            films = []
            for rij in rijen:
                films.append(Film.from_dict(rij))
            """
            
            film = Film.from_dict(rij)

            return film
    