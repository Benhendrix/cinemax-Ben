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
    
    def films_vandaag_uur(self,uur):
        with dbconn() as cur:
            ingave = f"%{uur}%"
            sql = "SELECT films.*,vertoningen.* FROM films INNER JOIN vertoningen ON films.id = vertoningen.film_id AND date(vertoningen.afspeelmoment) = date('now') AND vertoningen.afspeelmoment LIKE ?"
            cur.execute(sql,[ingave])
            rijen = cur.fetchall()

            films = [Film.from_dict(rij) for rij in rijen]
            return films

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
    
    def vertoningen_vandaag(self):
        with dbconn() as cur:
            sql = "SELECT * FROM vertoningen WHERE date(afspeelmoment) == date('now')"
            cur.execute(sql)
            rijen = cur.fetchall()

            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen
    
    def vertoning_toevoegen(self,vertoning):
        with dbconn() as cur:
            sql = "INSERT INTO vertoningen (zaal,afspeelmoment,pauze,drie_d,film_id) VALUES (?, ?, ?, ?, ?)"
            cur.execute(sql, [vertoning.zaal,vertoning.afspeelmoment,vertoning.pauze,vertoning.drie_d,vertoning.film_id])
    
    def vertoning_by_id(self, id):
        with dbconn() as cur:
            sql = "SELECT * FROM vertoningen WHERE id = ?"
            cur.execute(sql, [id])
            rij = cur.fetchone()

            if rij:
                vertoning = Vertoning.from_dict(rij)
                return vertoning
            else:
                return None

    def vertoning_verwijderen(self, id):
        with dbconn() as cur:
            if id:
                sql = "DELETE FROM vertoningen WHERE id = ?"
                cur.execute(sql, [id])
            else:
                raise ValueError

    def vertoningen_vandaag_uur(self,vertoning,uur):
        with dbconn() as cur:
            ingave = f"%{uur}%"
            sql = "SELECT * FROM vertoningen WHERE vertoningen.zaal = ? AND date(vertoningen.afspeelmoment) = date('now') AND vertoningen.afspeelmoment LIKE ?"
            cur.execute(sql,[vertoning,ingave])
            rijen = cur.fetchall()

            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen
    
    def vertoningen_filmId_uur(self,film,uur):
        with dbconn() as cur:
            ingave = f"%{uur}%"
            sql = "SELECT * FROM vertoningen INNER JOIN films ON vertoningen.film_id = films.id WHERE films.id = ? AND date(vertoningen.afspeelmoment) = date('now') AND vertoningen.afspeelmoment LIKE ? "
            cur.execute(sql, [film.id,ingave])
            rijen = cur.fetchall()

            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen

    # Methodes voor tickets
    def tickets_vorige_week(self,id):
        with dbconn() as cur:
            sql = "SELECT tickets.id,tickets.kind,tickets.totaal,tickets.vertoning_id,vertoningen.id,vertoningen.afspeelmoment FROM tickets INNER JOIN vertoningen ON tickets.vertoning_id = vertoning.id WHERE WEEK id = ? = WEEK(NOW()) - 1"
            cur.execute(sql, [id])
            rij = cur.fetchone()

            if rij:
                ticket = Ticket.from_dict(rij)
                return ticket
            else:
                return None

    def alle_tickets(self):
        with dbconn() as cur:
            sql = "SELECT * FROM tickets"
            cur.execute(sql)
            rijen = cur.fetchall()
            
            tickets = [Ticket.from_dict(rij) for rij in rijen]

            return tickets
    
    def ticket_toevoegen(self, ticket):
        with dbconn() as cur:
            sql = "INSERT INTO tickets (kind,volwassen,totaal,vertoning_id) VALUES (?, ?, ?, ?)"
            cur.execute(sql, [ticket.kind,ticket.volwassen,ticket.totaal,ticket.vertoning_id])