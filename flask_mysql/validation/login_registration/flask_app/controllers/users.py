from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("register.html")

@app.route('/create_user/user', methods=["POST"])
def create_user():
    if User.get_user_by_email(request.form):
        flash("This email aleready exist", "emailexists")
        return redirect('/')
    if not User.validate_user(request.form):
        return redirect('/')
    # else no errors: 
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # TAKE DATA FROM FORM FORM
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password": pw_hash
    }

    #PASS THE DATA TO SAVE CLASSMETHOD
    print(data)
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect(url_for('success'))

#Name of route should be the same as name of function
@app.route('/success')
def success():
    users = User.get_all()
    return render_template("info.html", users = users)

@app.route('/login_page')
def login_page():
    users = User.get_all()
    return render_template("login.html", users = users)


@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"],
            "password" : request.form['password'] }
    user_in_db = User.get_user_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/success")

@app.route('/delete/<int:id>/')
def delete(id):
    data = {
        'id' : id
    }
    User.delete(data)
    return redirect('/success')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login_page')