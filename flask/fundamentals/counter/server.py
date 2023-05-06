from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    session['count']+=1 
    if 'countall' not in session:
        session['countall']=0
    session['countall']+=1
    return render_template("index.html", count= session['count'], countall=session['countall'])

  

@app.route('/addtwo')
def addtwo():
    session['count']+=1
    session['countall']+=1
    return redirect('/')


@app.route('/reset')
def reset():
    # session.pop('count')
    session['count']=0
    return redirect('/')

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')


@app.route('/addextra', methods=['POST'])
def addextra():
    session['count'] =session['count'] + int(request.form['number']) -1
    session['countall'] =session['countall'] + int(request.form['number']) -1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)



