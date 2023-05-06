from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    return redirect('/results')

@app.route('/results')
def process():
    return render_template("info.html", name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

if __name__ == "__main__":
    app.run(debug=True)