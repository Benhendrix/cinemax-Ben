--SQLite

INSERT INTO films (titel,speelduur,genre,kinderen,omschrijving,imdb)
VALUES ("Spirited Away",125,"Animatie, Familie, Fantasie",1,"Tijdens de verhuizing van haar familie naar een buitenwijk wandelt Chihiro, een 10-jarig meisje, een wereld binnen die geregeerd wordt door heksen en monsters, waar mensen veranderd worden in dieren. Chihiro moet in een groot badhuis werken om te overleven. Zal het haar lukken om terug te keren naar haar eigen wereld?","tt0245429"),
       ("The Lord of the Rings: The Fellowship of the Ring",178,"Avontuur, Fantasie, Actie ",1,"Een eeuwenoude ring, die jaren zoek is geweest, wordt gevonden en komt bij toeval terecht bij de kleine Hobbit Frodo. Als de tovenaar Gandalf erachter komt dat deze ring eigenlijk de Ene Ring is waar de slechte Sauron naar op zoek is, gaat Frodo samen met Gandalf, een Dwerg, een Elf, twee Mensen en drie andere Hobbits op een groots avontuur om deze te vernietigen.","tt0120737"),
       ("Ghost in the Shell",83,"Actie, Animatie, Sciencefiction",0,"Alles speelt zich af in 2029. Het Ministerie van Buitenlandse Zaken heeft de ideale topagent, de 'Puppet Master' gemaakt. Deze is niet menselijk, heeft geen lichaam en kan zichzelf verplaatsen via de elektronische snelweg, het net.","tt0113568"),
       ("The Matrix",136,"Actie, Sciencefiction",0,"De computerhacker Neo komt er achter dat het leven op aarde niets meer is dan een computersimulatie, opgezet door machines om de mensheid in bedwang te houden. Hij wordt door enkele vrijheidsstrijders uit deze 'Matrix' gehaald.","tt0133093"),
       ("Fear and Loathing in Las Vegas",118,"Avontuur, Drama, Komedie",0,"Journalist Raoul Duke en zijn geflipte advocaat Dr. Gonzo reizen af naar Las Vegas om een sportevenement te verslaan. Met het voorschot dat ze hebben gekregen gooien ze hun hele kofferbak vol met allerlei soorten drugs en beginnen ze aan een psychedelische roadtrip, op zoek naar de 'American Dream'.","tt0120669"),
       ("The Godfather",168,"Drama, Misdaad",0,"Don Vito Corleone staat aan het hoofd van een Mafia-familie in New York. Als een gangster van een andere familie besluit drugs te gaan verkopen in heel New York, ontstaan er problemen. Don Vito haat drugs, en laat dit ook blijken.","tt0068646"),
       ("Pulp Fiction",154,"Thriller, Misdaad",0,"Jules en Vincent werken voor de machtige misdadiger Marsellus Wallace. Vincent komt in de problemen als hij Mia, de vrouw van Wallace, een avondje gezelschap moet houden. Ondertussen is Wallace verwikkeld in een deal met de bokser Butch, die Wallace belazert en er met z'n geld vandoor gaat.","tt0110912"),
       ("Howls bewegende kasteel",119,"Fantasie, Animatie, Avontuur",1,"Sophie is achttien en werkt zich te pletter in de hoedenwinkel die haar vader ooit bezat. Op een uitje naar de stad loopt Sophie de mysterieuze tovenaar Howl tegen het lijf.","tt0347149"),
       ("Harry Potter en de Gevangene van Azkaban",141,"Avontuur, Fantasie","Het is Harry's derde jaar op Hogwarts. Een gevaarlijke massamoordenaar, Sirius Black, is ontsnapt uit de Azkaban gevangenis, en iedereen is er van overtuigd dat hij er op uit is om Harry te vermoorden.","tt0304141")
;
INSERT INTO vertoningen (zaal,afspeelmoment,pauze,drie_d,film_id)
VALUES ("Zaal 1","2021-06-07 11:00:00",1,0,1),
       ("Zaal 1","2021-06-07 14:00:00",1,0,1),
       ("Zaal 1","2021-06-07 17:00:00",1,0,1),
       ("Zaal 1","2021-06-07 20:00:00",1,0,2),
       ("Zaal 1","2021-06-07 23:00:00",0,0,2),
       ("Zaal 2","2021-06-07 11:00:00",1,1,3),
       ("Zaal 2","2021-06-07 14:00:00",1,1,3),
       ("Zaal 2","2021-06-07 17:00:00",1,1,3),
       ("Zaal 2","2021-06-07 20:00:00",1,1,4),
       ("Zaal 2","2021-06-07 23:00:00",0,1,4),
       ("Zaal 3","2021-06-07 11:00:00",1,0,4),
       ("Zaal 3","2021-06-07 14:00:00",1,1,5),
       ("Zaal 3","2021-06-07 17:00:00",1,0,5),
       ("Zaal 3","2021-06-07 20:00:00",1,1,5),
       ("Zaal 3","2021-06-07 23:00:00",0,0,6),
       ("Zaal 4","2021-06-07 11:00:00",1,0,6),
       ("Zaal 4","2021-06-07 14:00:00",1,0,7),
       ("Zaal 4","2021-06-07 17:00:00",1,0,7),
       ("Zaal 4","2021-06-07 20:00:00",1,0,8),
       ("Zaal 4","2021-06-07 23:00:00",0,0,8)
       ("Zaal 1","2021-06-08 11:00:00",1,0,9),
       ("Zaal 1","2021-06-08 14:00:00",1,0,9),
       ("Zaal 1","2021-06-08 17:00:00",1,0,9),
       ("Zaal 1","2021-06-08 20:00:00",1,0,1),
       ("Zaal 1","2021-06-08 23:00:00",0,0,2),
       ("Zaal 2","2021-06-08 11:00:00",1,1,2),
       ("Zaal 2","2021-06-08 14:00:00",1,1,3),
       ("Zaal 2","2021-06-08 17:00:00",1,1,4),
       ("Zaal 2","2021-06-08 20:00:00",1,1,5),
       ("Zaal 2","2021-06-08 23:00:00",0,1,6)
;
INSERT INTO tickets (kind,volwassen,totaal,vertoning_id)
VALUES (0,0,0.00,1),
       (0,0,0.00,2),
       (0,0,0.00,3),
       (0,0,0.00,4),
       (0,0,0.00,5),
       (0,0,0.00,6)
;