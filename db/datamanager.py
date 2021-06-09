from models.film import Film
from models.ticket import Ticket
from models.vertoning import Vertoning
from db.database import dbconn
import datetime
from datetime import datetime

class Datamanager:
    # Methodes voor Films
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
                film = Film.from_dict(rij)
                return film
            else:
                return None

    def film_by_titel(self, titel):
        with dbconn() as cur:
            sql = "SELECT * FROM films WHERE titel = ?"
            cur.execute(sql, [titel])
            rij = cur.fetchone()

            if rij:
                film = Film.from_dict(rij)
                return film
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
            
    def zoek_film_op_titel(self, zoekterm):
        with dbconn() as cur:
            ingave = f"%{zoekterm}%"
            sql = "SELECT * FROM films WHERE titel LIKE ?"
            cur.execute(sql, [ingave])
            rijen = cur.fetchall()

            films = [Film.from_dict(rij) for rij in rijen]
            return films
    # Methodes voor vertoningen
    def alle_vertoningen(self):
        with dbconn() as cur:
            sql = "SELECT * FROM vertoningen"
            cur.execute(sql)
            rijen = cur.fetchall()

            vertoningen =[Vertoning.from_dict(rij)for rij in rijen]

            return vertoningen
    
    def alle_vertoningen_datum(self):
        with dbconn() as cur:
            sql = "SELECT * FROM vertoningen ORDER BY afspeelmoment ASC"
            cur.execute(sql)
            rijen = cur.fetchall()
            
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen
    
    def vertoningen_vandaag(self,zoekterm):
        with dbconn() as cur:
            ingave = f"%{zoekterm}%"
            sql = "SELECT * FROM vertoningen WHERE afspeelmoment LIKE ?"
            cur.execute(sql,[ingave])
            rijen = cur.fetchall()

            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen
    
    def vertoning_toevoegen(self,vertoning):
        with dbconn() as cur:
            sql = "INSERT INTO vertoningen (zaal,afspeelmoment,pauze,drie_d,film_id) VALUES (?, ?, ?, ?, ?)"
            cur.execute(sql, [vertoning.zaal,vertoning.afspeelmoment,vertoning.pauze,vertoning.drie_d,vertoning.film_id])
    
    def vertoning_verwijderen(self, id):
        with dbconn() as cur:
            if id:
                sql = "DELETE FROM vertoningen WHERE id = ?"
                cur.execute(sql, [id])
            else:
                raise ValueError
    
    def tickets_vorige_week():
        with dbconn() as cur:
            pass
            