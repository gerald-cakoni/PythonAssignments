from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('user_login_schema').query_db(query)
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
        results = connectToMySQL('user_login_schema').query_db(query, data)
        if results:
            return results[0]
        return False
    
        # GET A SPECIFIC USER
    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE users.email = %(email)s;"
        results = connectToMySQL('user_login_schema').query_db(query, data)
        if results:
            return cls(results[0])
        return False

    #CREATE
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at ) VALUES ( %(first_name)s ,  %(last_name)s,  %(email)s,  %(password)s,  NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('user_login_schema').query_db( query, data )
    
        #CREATE
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM users WHERE users.id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('user_login_schema').query_db( query, data )

    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "emailRegister")
            is_valid = False 
        if len(user['first_name']) < 2:
            flash("Name must be at least 2 characters.", "firstnameRegister")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.", "lastNameRegister")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.", "passwordRegister")
            is_valid = False
        return is_valid