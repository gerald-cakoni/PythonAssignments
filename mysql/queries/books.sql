USE books;
############################################################################################
# CREATE 5 USERS
INSERT INTO users (first_name, last_name) VALUES ("Jane", "Amsden"), ("Emily", "Dixon"), ("Theodore", "Dostoevsky"), ("William", "Shapiro"), ("Lao", "Xiu");

############################################################################################
# CREATE 5 BOOKS
INSERT INTO books (title, num_of_pages) VALUES ("C Sharp", "100"), ("Java", "120"), ("Python", "130"), ("PHP", "90"), ("Ruby", "120");

############################################################################################
# CHANGE THE NAME OF C SHARP TO C#
SET SQL_SAFE_UPDATES = 0;
UPDATE books SET title = "C#"
WHERE title="C Sharp";

############################################################################################
# CHANGE THE FIST NAME OF THE 4TH USER TO BILL
UPDATE users
SET first_name="Bill"
WHERE id=4; 

############################################################################################
# Have the first user favorite the first 2 books
INSERT INTO favorites (user_id, book_id) VALUES (1,1), (1,2);

############################################################################################
# Have the second user favorite the first 3 books
INSERT INTO favorites (user_id, book_id) VALUES (2,1), (2,2),(2,3);

############################################################################################
# Have the third user favorite the first 4 books
INSERT INTO favorites (user_id, book_id) VALUES (3,1), (3,2),(3,3), (3,4);

############################################################################################
# Have the fourth user favorite all the books
INSERT INTO favorites (user_id, book_id) VALUES (4,1), (4,2),(4,3), (4,4),(4,5);

############################################################################################
# Retrieve all the users who favorited the 3rd book
SELECT first_name, last_name FROM users
LEFT JOIN favorites ON users.id=favorites.user_id
WHERE book_id=3;

############################################################################################
DELETE FROM favorites
WHERE book_id=3 AND user_id = 1; 

############################################################################################
# Have the 5th user favorite the 2nd book
INSERT INTO favorites (user_id, book_id) VALUES (5,2);

############################################################################################
# Find all the books that the 3rd user favorited
select title AS "Favourite Book", user_id from books
LEFT JOIN favorites ON books.id=favorites.book_id
WHERE favorites.user_id = 3 ;

############################################################################################
# Find all the books that the 3rd user favorited
select * from users
LEFT JOIN favorites ON users.id=favorites.user_id
WHERE book_id = 5 ;

SELECT first_name, last_name from users
JOIN favorites on users.id = favorites.user_id
WHERE favorites.book_id = 5;