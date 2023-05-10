# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the user table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('user_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    # GET A SPECIFIC USER
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        results = connectToMySQL('user_schema').query_db(query, data)
        if results:
            return results[0]
        return False
    
    #CREATE
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(firstname)s , %(lastname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('user_schema').query_db( query, data )

    #DELETE 
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE users.id = %(id)s;"
        return connectToMySQL('user_schema').query_db(query, data)  

    #UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET users.first_name = %(first_name)s, users.last_name=%(last_name)s, users.email=%(email)s WHERE users.id = %(id)s;"
        return connectToMySQL('user_schema').query_db(query, data)  
    
    