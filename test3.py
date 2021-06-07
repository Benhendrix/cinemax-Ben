from models.film import Film
from models.ticket import Ticket
from models.vertoning import Vertoning
from db.database import dbconn

class Datamanager:
    def alle_films(self):
        with dbconn() as cur:
            sql = "SELECT * FROM films"
            cur.execute(sql)
            rijen = cur.fetchall()
            
            films = [Film.from_dict(rij) for rij in rijen]

            return films
            
    def alle_films_alfa(self):
        with dbconn() as cur:
            sql = "SELECT * FROM films ORDER BY titel ASC"
            cur.execute(sql)
            rijen = cur.fetchall()
            
            films = [Film.from_dict(rij) for rij in rijen]

            return films

    def film_by_id(self, id):
        with dbconn() as cur:
            sql = "SELECT * FROM films WHERE id = ?"
            cur.execute(sql, [id])
            rij = cur.fetchone()

            if rij:
                auteur = Film.from_dict(rij)
                return auteur
            else:
                return None

    def film_toevoegen(self, film):
        with dbconn() as cur:
            sql = "INSERT INTO films (titel,speelduur,genre,kinderen,omschrijving,imdb) VALUES (?, ?, ?, ?, ?, ?)"
            cur.execute(sql, [film.titel,film.speelduur,film.genre,film.kinderen,film.omschrijving,film.imdb])

    def film_verwijderen(self, id):
        with dbconn() as cur:
            if id:
                sql = "DELETE FROM films WHERE id = ?"
                cur.execute(sql, [id])
            else:
                raise ValueError
    
    def zoek_film_op_ingave(self, zoekterm):
        with dbconn() as cur:
            ingave = f"%{zoekterm}%"
            sql = "SELECT * FROM films WHERE titel LIKE ? OR genre LIKE ? OR omschrijving LIKE ?"
            cur.execute(sql, [ingave,ingave,ingave])
            rijen = cur.fetchall()

            films = [Film.from_dict(rij) for rij in rijen]

            return films
    
    def alle_vertoningen(self):
        with dbconn() as cur:
            sql = "SELECT * FROM vertoningen"
            cur.execute(sql)
            rijen = cur.fetchall()

            vertoningen =[Vertoning.from_dict(rij)for rij in rijen]

            return vertoningen