from flask_app import app
from flask_app.models.user import User
from flask_app.models.band import Band

from flask import render_template, redirect, session, request, flash

@app.route('/add/band')
def addBand():
    if 'user_id' in session:
        data = {
            'user_id': session['user_id']
        }
        loggedUser = User.get_user_by_id(data)
        return render_template('addBand.html', loggedUser = loggedUser)
    return redirect('/')

@app.route('/create/band', methods = ['POST'])
def createBand():
    if 'user_id' in session:
        if not Band.validate_band(request.form):
            return redirect(request.referrer)
        data = {
            'name': request.form['name'],
            'genre': request.form['genre'],
            'city': request.form['city'],
            'user_id': session['user_id']
        }
        Band.save(data)
        return redirect('/dashboard')
    return redirect('/')

@app.route('/edit/band/<int:id>')
def editPost(id):
    if 'user_id' in session:
        data = {
            'user_id': session['user_id'],
            'band_id': id
        }
        loggedUser = User.get_user_by_id(data)
        band = Band.get_band_by_id(data)
        if loggedUser['id'] == band['user_id']:
            return render_template('editBand.html', loggedUser = loggedUser, band= band)
        return redirect('/dashboard')
    return redirect('/')


@app.route('/update/band/<int:id>', methods = ['POST'])
def updateBand(id):
    if 'user_id' in session:
        data1 = {
            'user_id': session['user_id'],
            'band_id': id
        }
        loggedUser = User.get_user_by_id(data1)
        band = Band.get_band_by_id(data1)
        if loggedUser['id'] == band['user_id']:
            if not Band.validate_band(request.form):
                return redirect(request.referrer)
            data = {
                'name': request.form['name'],
                'genre': request.form['genre'],
                'city': request.form['city'],
                'band_id': id
            }
            Band.update(data)
            return redirect('/')

        return redirect('/dashboard')
    return redirect('/')

@app.route('/delete/band/<int:id>')
def deleteBand(id):
    if 'user_id' in session:
        data = {
            'user_id': session['user_id'],
            'band_id': id
        }
        loggedUser = User.get_user_by_id(data)
        band = Band.get_band_by_id(data)
        if loggedUser['id'] == band['user_id']:
            Band.deleteAllJoinUsers(data)
            Band.delete(data)
            return redirect(request.referrer)

        return redirect('/dashboard')
    return redirect('/')

@app.route('/join/<int:id>')
def joinMember(id):
    if 'user_id' in session:
        data = {
            'user_id': session['user_id'],
            'band_id': id
        }
        
        joinedBands = User.get_user_joined_bands(data)
        if id not in joinedBands:
            Band.join(data)
            return redirect(request.referrer)
        return redirect(request.referrer)
    return redirect('/')

@app.route('/quit/<int:id>')
def unlikePost(id):
    if 'user_id' in session:
        data = {
            'user_id': session['user_id'],
            'band_id': id
        }
        Band.quit(data)
        return redirect(request.referrer)
    return redirect('/')
