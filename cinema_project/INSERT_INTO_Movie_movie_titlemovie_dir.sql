
INSERT INTO Moviecategory(id, category_name) VALUES(1,"Horror");
INSERT INTO Moviecategory(id, category_name) VALUES(2,"Comedy");
INSERT INTO Moviecategory(id, category_name) VALUES(3,"Action");

INSERT INTO ticket_price(id, ticket_price, ticket_category_name) VALUES(1,13.59,"Adult");
INSERT INTO ticket_price(id, ticket_price, ticket_category_name) VALUES(2,10.59,"Senior");
INSERT INTO ticket_price(id, ticket_price, ticket_category_name) VALUES(3,9.59,"Child");

INSERT INTO showroom(id, total_seats) VALUES(1,48);

INSERT INTO Movie (id, movie_title, movie_director_name, movie_cast_name, movie_producer_name, movie_synopsis, movie_status, 
movie_picture, movie_video, category_ID)
VALUES(1, "Moonfall",	"Rolan Emmerich", "Halle Berry, Patrick Wilson, John Bradley, Michael Peña, Charlie Plummer, Kelly Yu, Donald Sutherland", 
"Roland Emmerich", "It follows two former astronauts alongside a conspiracy theorist who discover the hidden truth about Earth's moon when it leaves its orbit.",
"PG-13",
"moonfall.jpg",
"https://youtu.be/ivIwdQBlS10", 1);

INSERT INTO Movie (id, movie_title, movie_director_name, movie_cast_name, movie_producer_name, movie_synopsis, movie_status, 
movie_picture, movie_video, category_ID)
VALUES(2, "Jackass Forever Comedy",	"Jeff Tremaine", "Johnny Knoxville, Steve-o, Chris Pontius, Dave England, Wee Man, Danger Ehren, Preston Lacy", 
"Jeff Tremaine", 
"Celebrate the joy of a perfectly executed shot to the groin as Johnny Knoxville, Steve-O and the rest of the gang return for another round of hilarious, wildly absurd and often dangerous displays of stunts and comedy.",
"R",
"ja_forever.jpeg",
"https://youtu.be/p74bzf-beGc", 2);
																


INSERT INTO Movie (id, movie_title, movie_director_name, movie_cast_name, movie_producer_name, movie_synopsis, movie_status, 
movie_picture, movie_video, category_ID)
VALUES(3, "Marry Me",	
"Kat Coiro", 
"Jennifer LopezOwen , Wilson, Maluma, John Bradley, Chloe Coleman, Sarah Silverman", 
"Elaine Goldsmith-Thomas, Jennifer Lopez, Benny Medina, John Roger", 
"Music superstars Kat Valdez and Bastian are getting married before a global audience of fans. But when Kat learns, seconds before her vows, that Bastian has been unfaithful, she instead decides to marry Charlie, a stranger in the crowd.",
"PG-13",
"marry_me.jpg",
"https://youtu.be/Ebv9_rNb5Ig", 3);


INSERT INTO Movie (id, movie_title, movie_director_name, movie_cast_name, movie_producer_name, movie_synopsis, movie_status, 
movie_picture, movie_video, category_ID)
VALUES(4, "Death on the Nile",	
"Kenneth Branagh", 
"Tom Bateman, Annette Bening, Kenneth Branagh, Russell Brand, Ali Fazal, Dawn French, Gal Gadot, Armie Hammer, Rose Leslie, Emma Mackey, Sophie Okonedo, Jennifer Saunders
Letitia Wright",
"Ridley Scott, Kenneth Branagh, Judy Hofflund, Kevin J. Walsh", 
"Belgian sleuth Hercule Poirot's Egyptian vacation aboard a glamorous river steamer turns into a terrifying search for a murderer when a picture-perfect couple's idyllic honeymoon is tragically cut short.",
"PG-13",
"deathotn.jpg",
"https://youtu.be/dZRqB0JLizw", 1);


INSERT INTO Movie (id, movie_title, movie_director_name, movie_cast_name, movie_producer_name, movie_synopsis, movie_status, 
movie_picture, movie_video, category_ID)
VALUES(5, "Nope",	
"Jordan Peele", 
"Daniel Kaluuya, Keke Palmer, Steven Yeun", 
"Jordan Peele, Ian Cooper", 
"Caretakers at a California horse ranch encounter a mysterious force that affects human and animal behaviour.",
"N/A",
"nope.jpg",
"https://youtu.be/In8fuzj3gck", 2);


