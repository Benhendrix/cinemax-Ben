
DROP TABLE IF EXISTS vertoningen
DROP TABLE IF EXISTS films
DROP TABLE IF EXISTS tickets

CREATE TABLE IF NOT EXISTS vertoningen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    zaal TEXT NOT NULL,
    afspeelmoment BLOB NOT NULL,
    pauze INTEGER NOT NULL?
    3d INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS films (
    id INTEGER PRIMARY KEY  AUTOINCREMENT?
    titel TEXT NOT NULL,
    speelduur BLOB NOT NULL,
    genre TEXT NOT NULL,
    kinderen INTEGER NOT NULL,
    omschrijving TEXT NOT NULL,
    imdb TEXT NOT NULL,
    vertoning_film_id INTEGER,
    FOREIGN KEY (vertoning_film_id) REFERENCES vertoningen(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titel TEXT NOT NULL,
    kind INTEGER NOT NULL,
    volwassen INTEGER NOT NULL,
    totaal FLOAT NOT NULL,
    vertoning_ticket_id INTEGER,
    FOREIGN KEY (vertoning_ticket_id) REFERENCES vertoningen(id) ON DELETE CASCADE
);