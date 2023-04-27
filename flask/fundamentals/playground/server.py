from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/play/<int:x>/<col>')                           
def hello_world(x, col):
    return render_template('index.html', x=x, col=col)  
    
if __name__=="__main__":
    app.run(debug=True)

