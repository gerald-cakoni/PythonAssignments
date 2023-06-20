from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post

from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
import random
import math
import smtplib

from .env import ADMINEMAIL
from .env import PASSWORD  
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return redirect('/logout')


@app.route('/registerPage')
def registerPage():
    if 'user_id' in session:
        return redirect('/')
    return render_template('register.html')


@app.route('/register', methods = ['POST'])
def register():
    if 'user_id' in session:
        return redirect('/')
    
    if User.get_user_by_email(request.form):
        flash('This email already exists', 'emailRegister')
        return redirect(request.referrer)

    if not User.validate_user(request.form):
        flash('You have some errors! Fix them to sign Up', 'registrationFailed')
        return redirect(request.referrer)

#################################################
# Gjenerojme nje kod verifikimi
    string = '0123456789'
    vCode = ''
    length = len(string)
    for i in range(6):
        vCode += string[math.floor(random.random() * length)]
    verification_code = vCode

###################################################
    # line- i know for sure that my validate_user was true. User had all the required info
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password']),
        'isVerified': 0,
        'verification_code': verification_code
    }
    User.save(data)
    LOGIN = ADMINEMAIL
    TOADDRS  = user['email']
    SENDER = ADMINEMAIL
    SUBJECT = 'Verify Your Email'
    msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
        % ((SENDER), "".join(TOADDRS), SUBJECT) )
    msg += f'Use this verification code to activate your account: {verification_code}'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(LOGIN, PASSWORD)
    server.sendmail(SENDER, TOADDRS, msg)
    server.quit()



    user = User.get_user_by_email(data)
    session['user_id'] = user['id']
    return redirect('/verify/email')

###############################################################
@app.route('/verify/email')
def verifyEmail():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'user_id': session['user_id']
    }
    user = User.get_user_by_id(data)
    if user['isVerified'] == 1:
        return redirect('/dashboard')
    return render_template('verifyEmail.html', loggedUser = user)


@app.route('/activate/account', methods = ['POST'])
def activateAccount():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'user_id': session['user_id']
    }
    user = User.get_user_by_id(data)
    if user['isVerified'] == 1:
        return redirect('/dashboard')
    return render_template('verifyEmail.html', loggedUser = user)
    print('(/////////////////////////////////////////////////////////////)')
    print(verification_code)
    if not request.form('verification_code'):
        flash('Verification Code is required', 'wrongCode')
        return redirect(request.referrer)
    
    if request.form('verification_code') != user['verification_code'] :
        string = '0123456789'
        vCode = ''
        length = len(string)
        for i in range(8):
            vCode += string[math.floor(random.random() * length)]
        verification_code = vCode


        dataUpdate ={
        'verification_code' : verification_code ,
        'user_id': session['user_id']
        }
        User.updateVerificationCode(dataUpdate)

        LOGIN = ADMINEMAIL
        TOADDRS  = user['email']
        SENDER = ADMINEMAIL
        SUBJECT = 'Verify Your Email'
        msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
            % ((SENDER), "".join(TOADDRS), SUBJECT) )
        msg += f'Use this verification code to activate your account: {verificationCode}'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.login(LOGIN, PASSWORD)
        server.sendmail(SENDER, TOADDRS, msg)
        server.quit()

        flash('Verification Code is wrong we just send you a new one', 'wrongCode')
        return redirect(request.referrer)
    User.activateAccount(data)
    return redirect('/dashboard')
    

    return render_template('verifyEmail.html', loggedUser = user)

################################################################
@app.route('/loginPage')
def loginPage():
    if 'user_id' in session:
        return redirect('/')
    return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login():
    if 'user_id' in session:
        return redirect('/')
    if not User.get_user_by_email(request.form):
        flash('This email doesnt appear to be in our system! Try another one!', 'emailLogin')
        return redirect(request.referrer)
    
    user = User.get_user_by_email(request.form)
    if user:
        if not bcrypt.check_password_hash(user['password'], request.form['password']):
            flash('Wrong Password', 'passwordLogin')
            return redirect(request.referrer)
    
    session['user_id'] = user['id']
    return redirect('/verify/email')


    
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    data = {
        'user_id': session['user_id']
    }
    loggedUser = User.get_user_by_id(data)
    ###############################################
    # Check is verified before letting to pass
    if loggedUser['isVerified'] == 0:
        return redirect('/verify/email')
    ###############################################
    posts = Post.get_all()
    loggedUserLikedPost = User.get_user_liked_posts(data)
    return render_template('dashboard.html', posts = posts, loggedUser=loggedUser, likedPost = loggedUserLikedPost)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/loginPage')