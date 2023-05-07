# By Andy Nguyen
# Ninja Gold Assignment - Create a simple game to test your understanding of flask, and implement the functionality below.
# For this assignment, you're going to create a mini-game that helps a ninja make some money! When you start the game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or LOSE up to 50 golds. Your job is to create a web app that allows this ninja to earn gold and to display past activities of this ninja.

from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if 'total_gold' not in session:
        session['total_gold'] = 0
        print("Total Gold = 0")
        session['activities'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():

    if request.form['building'] == 'farm':
        session['message'] = ''
        number = random.randrange(10,21)
        time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        session['total_gold'] += number
        print(f"Gold increased by {number}.")
        print(f"Total Gold = {session['total_gold']}")
        session['activities'].append(f"<div class='won'>Earned {number} gold from the farm! ({time})</div>")
        # print(session['activities'])
        
        for i in range(len(session['activities'])-1, -1, -1):
            session['message'] += session['activities'][i]
            # print(session['message'])


    elif request.form['building'] == 'cave':
        session['message'] = ''
        number = random.randrange(5,11)
        time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        session['total_gold'] += number      
        print(f"Gold increased by {number}.")
        print(f"Total Gold = {session['total_gold']}")
        session['activities'].append(f"<div class='won'>Earned {number} gold from the cave! ({time})</div>")
        # print(session['activities'])
        
        for i in range(len(session['activities'])-1, -1, -1):
            session['message'] += session['activities'][i]
            # print(session['message'])
    
    elif request.form['building'] == 'house':
        session['message'] = ''
        number = random.randrange(2,6)
        time = datetime.now().strftime("%Y/%m/%d %I:%M %p")        
        session['total_gold'] += number
        print(f"Gold increased by {number}.")
        print(f"Total Gold = {session['total_gold']}")
        session['activities'].append(f"<div class='won'>Earned {number} gold from the house! ({time})</div>")
        # print(session['activities'])
        
        for i in range(len(session['activities'])-1, -1, -1):
            session['message'] += session['activities'][i]
            # print(session['message'])
    
    elif request.form['building'] == 'casino':
        if session['total_gold'] > 0:
            session['message'] = ''
            number = random.randrange(-50,51)
            time = datetime.now().strftime("%Y/%m/%d %I:%M %p")        
            session['total_gold'] += number        
            if number > 0:
                print(f"Gold increased by {number}.")
                session['activities'].append(f"<div class='won'>Earned {number} gold from the casino! ({time})</div>")
            if number < 0:
                print(f"Gold decreased by {abs(number)}.")
                session['activities'].append(f"<div class='lost'>Entered a casino and lost {abs(number)} gold....Ouch! ({time})</div>")
            print(f"Total Gold = {session['total_gold']}")
            # print(session['activities'])

            for i in range(len(session['activities'])-1, -1, -1):
                session['message'] += session['activities'][i]
                # print(session['message'])
        
        elif session['total_gold'] <= 0:
            session['message'] = ''
            session['activities'].append(f"<div>You have no gold to gamble. Please come back to the casino when you have more money.</div>")
            print(f"Total Gold = {session['total_gold']}")
            print("You have no gold to gamble. Please come back to the casino when you have more money.")

            for i in range(len(session['activities'])-1, -1, -1):
                session['message'] += session['activities'][i]
                # print(session['message'])

    return redirect('/')

@app.route('/reset')
def reset():
    print("Current game is ending. Gold count will reset to 0.")
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

