from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database

    #CREATE A BOOK IN DB
    @classmethod
    def save_book(cls, data ):
        query = "INSERT INTO books ( title , num_of_pages, created_at, updated_at ) VALUES ( %(title)s , %(num_of_pages)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('books_authors').query_db( query, data )

    # GET ALL BOOKS
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_authors').query_db(query)
        # Create an empty list to append our instances of friends
        books = []
        # Iterate over the db results and create instances of friends with cls.
        for book in results:
            books.append( cls(book) )
        return books
    
    # GET A SPECIFIC BOOK
    @classmethod
    def get_book_by_id(cls, data):
        query = "SELECT * FROM books WHERE users.id = %(id)s;"
        results = connectToMySQL('books_authors').query_db(query, data)
        if results:
            return results[0]
        return False
    
    @classmethod
    def get_book_by_id_favourites(cls,data):
        query = "SELECT * FROM books LEFT JOIN favourites ON books.id = favourites.book_id LEFT JOIN authors ON authors.id = favourites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_authors').query_db(query,data)

        book = cls(results[0])

        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.favorites.append(author.Author(data))
        return book

    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favourites WHERE author_id = %(id)s );"
        results = connectToMySQL('books_authors').query_db(query,data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books