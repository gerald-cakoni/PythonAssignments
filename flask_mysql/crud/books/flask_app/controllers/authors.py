from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/')
def index():
    return render_template("authors.html")

@app.route('/create_author', methods=["POST"])
def create_author():
    data = {
        "name": request.form["name"],
    }
    Author.save(data)
    return redirect(url_for('display_author'))

@app.route('/display_author')
def display_author():
    all_authors = Author.get_all()
    return render_template("authors.html", all_authors=all_authors)



# SHOW A SPECIFIC AUTHOR
@app.route('/show/<int:id>')
def showAuthor(id):
    data = {
        'id': id
    }
    all_books = Book.get_all_books()
    author=Author.get_author_by_id(data)
    return render_template('author_show.html', author=author, all_books=all_books, unfavorited_books=Book.unfavorited_books(data))


@app.route('/join/book',methods=['POST'])
def join_book():
    data = {
        'book_id': request.form['book_id'],
        'author_id': request.form['author_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")