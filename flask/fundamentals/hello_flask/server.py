from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
  return "Dojo!"


@app.route('/say/<string:name>')
def say_hello(name):
   return f"Hi {name}!"


@app.route('/repeat/<int:repeated>/<string:expression>')
def repeat(repeated, expression):
   return f"{repeated*expression}"


@app.route('/repeat1/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output


@app.errorhandler(Exception)
def error404(error):
   return "<h1>Sorry! No response. Try again.</h1>", 404


if __name__=="__main__":
    app.run(debug=True)


