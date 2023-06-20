from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post

from flask import render_template, redirect, session, request, flash

from .env import UPLOAD_FOLDER
from .env import ALLOWED_EXTENSIONS

from werkzeug.utils import secure_filename
from datetime import datetime   
import os

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
# The limit is 3 MB

#Check if the format is right
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@app.route('/add/post')
def addPost():
    if 'user_id' in session:
        data = {
            'user_id': session['user_id']
        }
        loggedUser = User.get_user_by_id(data)
        return render_template('addPost.html', loggedUser = loggedUser)
    return redirect('/')

@app.route('/create/post', methods = ['POST'])
def createPost():
    if 'user_id' in session:
        if not Post.validate_post(request.form):
            return redirect(request.referrer)
        
###############################################################################
        # 1  Check is image exist / is uploadedn
        if not request.files['image']:
            flash('Post image is required!', 'postImage')
            return redirect(request.referrer)
        image = request.files['image']
        # IMAGE
        # 2  Controll if it is in the correct format 
        if not allowed_file(image.filename):
            flash('Post image showld be in png, jpg. jpeg format!', 'postImage')
            return redirect(request.referrer)
  
        # 3  ADD Timestamp to use as name to avaid same names on uploaded files

        if image and allowed_file(image.filename):
            filename1 = secure_filename(image.filename)
            time = datetime.now().strftime("%d%m%Y%S%f")
            time += filename1
            filename1=time
            image.save(os.path.join(app.config['UPLOAD_FOLDER'],filename1))
        
        # 4 - Save it in the db at data 
        data = {
            'title': request.form['title'],
            'content': request.form['content'],
            # 4 
            'user_id': session['user_id'],
            'image' : filename1
        }
        Post.save(data)
        return redirect('/dashboard')
    return redirect('/')

###########################################################################
# To use it
#@app.route('downloadPDF/<path: filename>')
#def downloadPDF(filename):
    return send_file(app.root_path+'static/UPLOADED_FOLDER/'+filename, as_attachment = True)



###########################################################################

@app.route('/edit/post/<int:id>')
def editPost(id):
    if 'user_id' in session:
        data = {
            'user_id': session['user_id'],
            'post_id': id
        }
        loggedUser = User.get_user_by_id(data)
        post = Post.get_post_by_id(data)
        if loggedUser['id'] == post['user_id']:
            return render_template('editPost.html', loggedUser = loggedUser, post= post)
        return redirect('/dashboard')
    return redirect('/')

@app.route('/post/<int:id>')
def viewPost(id):
    if 'user_id' in session:
        data = {
            'user_id': session['user_id'],
            'post_id': id
        }
        loggedUser = User.get_user_by_id(data)

        post = Post.get_post_by_id(data)
        likesNr = Post.get_post_likers(data)

        return render_template('showOne.html', loggedUser = loggedUser, post= post, likesNr= likesNr)
    return redirect('/')

@app.route('/edit/post/<int:id>', methods = ['POST'])
def updatePost(id):
    if 'user_id' in session:
        data1 = {
            'user_id': session['user_id'],
            'post_id': id
        }
        loggedUser = User.get_user_by_id(data1)
        post = Post.get_post_by_id(data1)
        if loggedUser['id'] == post['user_id']:
            if not Post.validate_post(request.form):
                return redirect(request.referrer)
            data = {
                'title': request.form['title'],
                'content': request.form['content'],
                'post_id': id
            }
            Post.update(data)
            return redirect(request.referrer)

        return redirect('/dashboard')
    return redirect('/')

@app.route('/delete/post/<int:id>')
def deletePost(id):
    if 'user_id' in session:
        data = {
            'user_id': session['user_id'],
            'post_id': id
        }
        loggedUser = User.get_user_by_id(data)
        post = Post.get_post_by_id(data)
        if loggedUser['id'] == post['user_id']:
            Post.deleteAllLikes(data)
            Post.delete(data)
            return redirect(request.referrer)

        return redirect('/dashboard')
    return redirect('/')

@app.route('/like/<int:id>')
def likePost(id):
    if 'user_id' in session:
        data = {
            'user_id': session['user_id'],
            'post_id': id
        }
        
        likedPost = User.get_user_liked_posts(data)
        if id not in likedPost:
            Post.addLike(data)
            return redirect(request.referrer)

        return redirect(request.referrer)
    return redirect('/')

@app.route('/unlike/<int:id>')
def unlikePost(id):
    if 'user_id' in session:
        data = {
            'user_id': session['user_id'],
            'post_id': id
        }
        Post.unLike(data)
        return redirect(request.referrer)
    return redirect('/')
