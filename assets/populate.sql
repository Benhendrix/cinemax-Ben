--SQLite

INSERT INTO films (titel,speelduur,genre,kinderen,omschrijving,imdb)
VALUES ("Spirited Away",125,"Animatie, Familie, Fantasie",1,"Tijdens de verhuizing van haar familie naar een buitenwijk wandelt Chihiro, een 10-jarig meisje, een wereld binnen die geregeerd wordt door heksen en monsters, waar mensen veranderd worden in dieren. Chihiro moet in een groot badhuis werken om te overleven. Zal het haar lukken om terug te keren naar haar eigen wereld?","tt0245429"),
       ("The Lord of the Rings: The Fellowship of the Ring",178,"Avontuur, Fantasie, Actie ",1,"Een eeuwenoude ring, die jaren zoek is geweest, wordt gevonden en komt bij toeval terecht bij de kleine Hobbit Frodo. Als de tovenaar Gandalf erachter komt dat deze ring eigenlijk de Ene Ring is waar de slechte Sauron naar op zoek is, gaat Frodo samen met Gandalf, een Dwerg, een Elf, twee Mensen en drie andere Hobbits op een groots avontuur om deze te vernietigen.","tt0120737"),
       ("Ghost in the Shell",83,"Actie, Animatie, Sciencefiction",0,"Alles speelt zich af in 2029. Het Ministerie van Buitenlandse Zaken heeft de ideale topagent, de 'Puppet Master' gemaakt. Deze is niet menselijk, heeft geen lichaam en kan zichzelf verplaatsen via de elektronische snelweg, het net.","tt0113568"),
       ("The Matrix",136,"Actie, Sciencefiction",0,"De computerhacker Neo komt er achter dat het leven op aarde niets meer is dan een computersimulatie, opgezet door machines om de mensheid in bedwang te houden. Hij wordt door enkele vrijheidsstrijders uit deze 'Matrix' gehaald.","tt0133093")
;
INSERT INTO vertoningen (zaal,afspeelmoment,pauze,drie_d,film_id)
VALUES ("Zaal 1","11:00:00",1,0,1),
       ("Zaal 2","14:00:00",1,0,1),
       ("Zaal 3","17:00:00",1,0,1),
       ("Zaal 4","11:00:00",1,1,2),
       ("Zaal 5","14:00:00",1,0,2),
       ("Zaal 6","17:00:00",1,1,2),
       ("Zaal 7","11:00:00",0,0,3),
       ("Zaal 8","14:00:00",0,0,3),
       ("Zaal 9","17:00:00",0,0,3),
       ("Zaal 1","11:00:00",1,0,4),
       ("Zaal 2","14:00:00",1,1,4),
       ("Zaal 3","17:00:00",1,0,4)
;
INSERT INTO tickets (kind,volwassen,totaal,vertoning_id)
VALUES (1,1,0.00,1),
       (1,1,0.00,2),
       (1,1,0.00,3)
;