USE friendship_schema;

#CREATE
INSERT INTO friends (first_name, last_name) VALUES ("Gerald 4", "Cakoni");

# READ
SELECT * FROM friends;
SELECT first_name, last_name FROM friends;

# UPDATE
UPDATE friends SET first_name = "Gerald 2"
WHERE id = 3;

# DELETE

DELETE FROM friends
WHERE  id=2 OR id=3;