-- SQLite

DROP TABLE IF EXISTS films;
DROP TABLE IF EXISTS vertoningen;
DROP TABLE IF EXISTS tickets;

CREATE TABLE IF NOT EXISTS films (
    id INTEGER PRIMARY KEY  AUTOINCREMENT,
    titel TEXT NOT NULL,
    speelduur INTEGER NOT NULL,
    genre TEXT NOT NULL,
    kinderen INTEGER NOT NULL,
    omschrijving TEXT NOT NULL,
    imdb TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS vertoningen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    zaal TEXT NOT NULL,
    afspeelmoment TEXT NOT NULL,
    pauze INTEGER NOT NULL,
    drie_d INTEGER NOT NULL,
    film_id INTEGER,
    FOREIGN KEY (film_id) REFERENCES films (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kind INTEGER NOT NULL,
    volwassen INTEGER NOT NULL,
    totaal REAL NOT NULL,
    vertoning_id INTEGER,
    FOREIGN KEY (vertoning_id) REFERENCES vertoningen(id) ON DELETE SET NULL
);