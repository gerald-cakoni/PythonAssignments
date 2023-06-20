from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.book import Book
from flask_app.models.author import Author


@app.route('/add_book')
def add_book():
    return render_template("books.html")

@app.route('/create_book', methods=["POST"])
def create_book():
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"]
    }
    Book.save_book(data)
    return redirect(url_for('display_books'))

@app.route('/display_books')
def display_books():
    all_books = Book.get_all_books()
    return render_template("books.html", all_books=all_books)


# SHOW A SPECIFIC AUTHOR
@app.route('/show/<int:id>')
def showBooks(id):
    data = {
        'id': id
    }
    book = Book.get_books_by_id()
    all_author=Author.get_author(data)
    return render_template('book_show.html', all_author=all_author, book=book, unfavorited_books=Book.unfavorited_books(data))


@app.route('/join/author',methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")
