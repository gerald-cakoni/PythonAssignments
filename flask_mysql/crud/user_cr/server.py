from flask import Flask, render_template, session, redirect, request, url_for
from user import User
app = Flask(__name__)


@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("create.html", all_users = users)


@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "firstname": request.form["first_name"],
        "lastname" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect(url_for('read'))


@app.route('/read')
def read():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

if __name__ == "__main__":
    app.run(debug=True)