from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojo_survey;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    # GET A SPECIFIC USER
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM dojo_survey WHERE dojo_survey.id = %(id)s;"
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        if results:
            return results[0]
        return False
    
    #CREATE
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojo_survey ( name , location , language , comment, created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(language)s ,%(comment)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_survey_schema').query_db( query, data )
    
    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['name']) < 3:
            flash("Name must be at least 3 characters.", "firstNameRegister")
            is_valid = False
        if not user.get('location'):
              flash("You must select a location.", "locationRegister")
              is_valid = False
        if not user.get('language'):
             flash("You must select a language.", "languageRegister")
             is_valid = False
        if len(user['comment']) < 3:
            flash("Comment must be at least 3 characters.", "commentRegister")
            is_valid = False

        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False


        return is_valid