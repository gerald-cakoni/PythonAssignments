from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    if not User.validate_user(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors: 

    # TAKE DATA FROM FORM FORM
    data = {
        "name": request.form["name"],
        "location" : request.form["location"],
        "language" : request.form["language"],
        "comment": request.form["comment"]
    }
    #PASS THE DATA TO SAVE CLASSMETHOD
    print(data)
    User.save(data)
    return redirect(url_for('read'))

@app.route('/read')
def read():
    users = User.get_all()
    return render_template("info.html", all_users = users)