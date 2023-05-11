from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojo_email;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_email_schema').query_db(query)
        # Create an empty list to append our instances of friends
        emails = []
        # Iterate over the db results and create instances of friends with cls.
        for email in results:
            emails.append( cls(email) )
        return emails
    
    # GET A SPECIFIC USER
    @classmethod
    def get_email_by_id(cls, data):
        query = "SELECT * FROM dojo_email WHERE dojo_email.id = %(id)s;"
        results = connectToMySQL('dojo_email_schema').query_db(query, data)
        if results:
            return results[0]
        return False
    
        # GET A SPECIFIC USER
    @classmethod
    def get_email_by_name(cls, data):
        query = "SELECT * FROM dojo_email WHERE dojo_email.name = %(name)s;"
        results = connectToMySQL('dojo_email_schema').query_db(query, data)
        if results:
            return results[0]
        return False

    #CREATE
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojo_email ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_email_schema').query_db( query, data )
    

        #CREATE
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM dojo_email WHERE dojo_email.id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_email_schema').query_db( query, data )

    @staticmethod
    def validate_email(email):
        is_valid = True # we assume this is true
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(email['name']): 
            flash("Invalid email address!")
            is_valid = False 
        return is_valid