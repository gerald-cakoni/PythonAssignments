USE user_schema;

# CREATE 3 NEW USERS
INSERT INTO users (first_name, last_name, email) VALUES ("Klea", "Manushi", "kleamanushi@gmail.com");
INSERT INTO users (first_name, last_name, email) VALUES ("Gerald", "Cakoni", "cakonigerald");
INSERT INTO users (first_name, last_name, email) VALUES ("Endi", "Mimini", "endimimini@gmail.com");

#RETRIEVE ALL THE USERS
SELECT * FROM users;

# RETRIEVE THE FIRST USER USING THEIR EMAIL
SELECT * FROM users
WHERE email = "kleamanushi@gmail.com";

# RETRIEVE THE LAST USER USING THEIR ID
SELECT * FROM users
WHERE id=4;

# CHANGE THE THIRD USER LAST NAME TO PANCAKES
UPDATE users SET last_name = "Pancakes"
WHERE id=3;

# DELETE USER WITH id=2
DELETE FROM users
WHERE id=2;

# GET ALL THE USERS SORTED BY THEIR FIRST NAME
 SELECT * FROM users
 ORDER BY first_name;
 
 
 # BONUS: GET ALL THE USERS SORTED BY THEIR FIRST NAME IN DESCENDING
 SELECT * FROM users
 ORDER BY first_name DESC;

