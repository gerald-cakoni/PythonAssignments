from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.user import User


#FISRT WE GET THE USERS FROM DB THEN WE RETURN TO HTML FILE
@app.route('/')
def index():
    users = User.get_all()
    return render_template("read.html", all_users = users)

# CREATE FORM
@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/create_user', methods=["POST"])
def create_user():
    # TAKE DATA FROM FORM

    data = {
        "firstname": request.form["first_name"],
        "lastname" : request.form["last_name"],
        "email" : request.form["email"]
    }
    #PASS THE DATA TO SAVE CLASSMETHOD

    User.save(data)
    return redirect(url_for('read'))

@app.route('/read')
def read():
    users = User.get_all()
    return render_template("read.html", all_users = users)

# SHOW A SPECIFIC USER
@app.route('/show/<int:id>')
def showUser(id):
    data = {
        'id': id
    }
    user=User.get_user_by_id(data)
    return render_template('show.html', user=user)


@app.route('/delete/<int:id>')
def deleteUser(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/')


@app.route('/edit/<int:id>')
def editUser(id):
    data = {
        'id': id
    }
    user=User.get_user_by_id(data)
    return render_template('edit.html', user=user)

@app.route('/update/<int:id>', methods=['POST'])
def updateUser(id):
    data = {
        'id': id,
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],  
        'email' : request.form['email_address']
    }
    User.update(data)
    return redirect('/show/' + str(id))
