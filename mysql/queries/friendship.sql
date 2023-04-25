INSERT INTO users (first_name, last_name) VALUES ("Amy", "Giver"), ("Eli", "Byers"),("Marky", "Mark"),("Kermit", "The Frog"),("Marky", "Mark"), ("Big", "Bird");

INSERT INTO friendships (user_id, friend_id) VALUES (1,2), (1,4), (1,6), (2,1), (2,3), (2,5), (3,2), (3,5), (4,3), (5,1), (5,6), (6,2), (6,3);


# Display the relationships create as shown in the above image
SELECT users.first_name, users.last_name, friend.first_name AS friend_first_name,  friend.last_name AS friend_last_name  FROM users 
JOIN friendships ON users.id = friendships.user_id 
LEFT JOIN users AS friend ON friend.id = friendships.friend_id;

# Return all users who are friends with the first user, make sure their names are displayed in results.
SELECT users.first_name, users.last_name, friend.first_name AS friend_first_name,  friend.last_name AS friend_last_name  FROM users 
JOIN friendships ON users.id = friendships.user_id 
LEFT JOIN users AS friend ON friend.id = friendships.friend_id
WHERE user_id = 1;

# Return the count of all friendships
SELECT count(*) FROM friendships;

# Find out who has the most friends and return the count of their friends.
SELECT users.first_name, users.last_name, count(user_id) FROM users
JOIN friendships ON users.id = friendships.user_id
GROUP BY user_id
ORDER BY count(user_id) DESC
LIMIT 1;


# Return all users who are friends with the first user, make sure their names are displayed in results.
SELECT users.first_name, users.last_name, friend.first_name AS friend_first_name,  friend.last_name AS friend_last_name  FROM users 
JOIN friendships ON users.id = friendships.user_id 
LEFT JOIN users AS friend ON friend.id = friendships.friend_id
WHERE user_id = 3
ORDER BY friend.first_name;

