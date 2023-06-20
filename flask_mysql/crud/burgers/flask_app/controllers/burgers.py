from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.burger import Burger
from flask_app.models.restaurant import Restaurant




@app.route('/restaurant12',methods=['POST'])
def addRestaurant():
        # if there are errors:
    # We call the staticmethod on Burger model to validate

    data = {
        "name":request.form['name'],
    }
    Restaurant.save(data)
    return redirect(url_for('restaurant1'))


@app.route('/restaurant1')
def displayRestaurant():
        # if there are errors:
    # We call the staticmethod on Burger model to validate

    return render_template('results.html',all_restaurants=Restaurant.get_all())

