from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'message' not in session:
        session["message"]=""
    if 'number' not in session:
        import random
        session['number']=random.randint(1,100)
    return render_template("index.html", message=session['message'] )

@app.route('/guess', methods=['POST'])
def guess():
    guess=int(request.form['number'])
    if guess== session['number']:
        session['message']= f" {session['number']} was the number"
    if guess > session['number']:
        session['message']= 'Too high!'
    elif guess< session['number']:
        session['message']= 'Too low!'
    return redirect('/')
 
@app.route('/reset')
def reset():
    session['number']
    session.pop("number")
    session.pop("message")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)