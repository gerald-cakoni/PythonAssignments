USE dojos_and_ninjas_schdema;

# CREATE 3 NEW DOJOS
INSERT INTO dojos (name) VALUES ("First Dojo"),("Second Dojo"),("Third Dojo");

# DELETE 3 DOJOS YOU JUST CREATED
DELETE FROM dojos
WHERE id=1 OR id=2 OR id=3;

# CREATE 3 MORE DOJOS
INSERT INTO dojos (name) VALUES ("Fourth Dojo"),("Fifth Dojo"),("Sixth  Dojo");

# CREATE 3 NINJAS THAT BELONG TO THE FIRST DOJO
INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (4, "Gerald", "Cakoni", 23),(4, "Anida", "Cakoni", 25),(4, "Gani", "Cakoni", 63);

# CREATE 3 NINJAS THAT BELONG TO THE SECOND DOJO
INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (5, "Guido", "Guidi", 23), (5, "Monty", "Monti", 22), (5, "Romy", "York", 24);

# CREATE 3 NINJAS THAT BELONG TO THE THIRD DOJO
INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (6, "Gerald 2", "Cakoni 2", 19),(6, "Guido 2", "Guidi 2", 27),(6, "Monty 2", "Monti 2", 28);

#RETRIEVE ALL THE NINJAS FROM THE FIRST DOJO
SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id=4;

#RETRIEVE ALL THE NINJAS FROM THE LAST DOJO
SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id=6;

#RETRIEVE THE LAST NINJA'S DOJO
SELECT * FROM dojos
WHERE dojos.id=6;