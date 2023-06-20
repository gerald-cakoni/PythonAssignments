from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # GET ALL AUTHORS
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_authors').query_db(query)
        # Create an empty list to append our instances of friends
        authors = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            authors.append( cls(user) )
        return authors
    
    # GET A SPECIFIC AUTHOR
    @classmethod
    def get_author_by_id(cls, data):
        query = "SELECT * FROM authors WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_authors').query_db(query, data)
        if results:
            return results[0]
        return False
    
    #CREATE IN THE DB
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO authors ( name, created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('books_authors').query_db( query, data )

    # SELECT FROM THEOSE WHO ARE NOT FAVORITED YET
    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL('books_authors').query_db(query,data)
        for row in results:
            authors.append(cls(row))
        return authors

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favourites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_authors').query_db(query,data)


    #DELETE FROM DB
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM authors WHERE authors.id = %(id)s;"
        return connectToMySQL('books_authors').query_db(query, data)  

    #UPDATE THE EXISTING AUTHOR
    @classmethod
    def update(cls, data):
        query = "UPDATE authors SET authors.name = %(name)s WHERE authors.id = %(id)s;"
        return connectToMySQL('books_authors').query_db(query, data)  
