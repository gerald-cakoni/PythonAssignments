from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Band:
    db_name = 'bands'
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.genre = data['genre']
        self.city = data['city']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_band_by_id(cls, data):
        query = "SELECT * FROM bands WHERE bands.id = %(band_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return False

    #READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM bands LEFT JOIN users ON bands.user_id = users.id;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of users
        bands = []
        if results:
        # Iterate over the db results and create instances of friends with cls.
            for band in results:
                bands.append(band)
            return bands
        return bands
    
    @classmethod
    def get_all_createdBands(cls, data):
        query = "SELECT * FROM bands WHERE bands.user_id = %(user_id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db_name).query_db(query, data)
        # Create an empty list to append our instances of users
        bands = []
        if results:
        # Iterate over the db results and create instances of friends with cls.
            for band in results:
                bands.append(band)
            return bands
        return bands
    #CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO bands (name, genre, city ,user_id) VALUES ( %(name)s, %(genre)s, %(city)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)  
    
    #UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE bands SET name = %(name)s, genre = %(genre)s, city = %(city)s WHERE bands.id = %(band_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)  
    
    #DELETE
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM bands WHERE bands.id = %(band_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
        #DELETE
    @classmethod
    def deleteAllJoinUsers(cls, data):
        query = "DELETE FROM members WHERE members.band_id = %(bands_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    #add like
    @classmethod
    def join(cls, data):
        query = "INSERT INTO members (band_id, user_id) VALUES ( %(band_id)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)  
    
    @classmethod
    def quit(cls, data):
        query = "DELETE FROM members WHERE band_id = %(band_id)s and user_id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)


    @staticmethod
    def validate_band(band):
        is_valid = True
        if len(band['name']) <2:
            flash('Band name should be more than 2 characters!', 'nameBand')
            is_valid= False
        if len(band['genre']) <2:
            flash('Band genre should be more than 2 characters!', 'genreBand')
            is_valid= False
        if len(band['city']) <2:
            flash('Band city should be more than 2 characters!', 'cityBand')
            is_valid= False
        return is_valid
        