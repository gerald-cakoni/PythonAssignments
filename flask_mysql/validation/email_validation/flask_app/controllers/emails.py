from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.email import Email


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_email', methods=["POST"])
def create_email():

    if Email.get_email_by_name(request.form):
        flash("This email aleready exist")
        return redirect('/')
    if not Email.validate_email(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors: 

    # TAKE DATA FROM FORM FORM
    data = {
        "name": request.form["name"],
    }
    #PASS THE DATA TO SAVE CLASSMETHOD
    print(data)
    Email.save(data)
    return redirect(url_for('success'))

#Name of route should be the same as name of function
@app.route('/success')
def success():
    emails = Email.get_all()
    return render_template("info.html", emails = emails)

@app.route('/delete/<int:id>/')
def delete(id):
    data = {
        'id' : id
    }
    Email.delete(data)
    return redirect('/success')