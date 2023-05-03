from flask import Flask, render_template
app = Flask(__name__)
    
@app.route('/') 
def normalCheckerboard():
    return render_template('index.html') 

@app.route('/4') 
def Checkerboard8x4():
    return render_template('index4.html') 

@app.route('/<int:x>/<int:y>') 
def Checkerboardxy(x,y):
    return render_template('indexxy.html', x=x, y=y) 

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>') 
def Checkerboardcolor(x,y,color1,color2):
    return render_template('indexcolor.html', x=x, y=y, color1=color1, color2=color2) 


if __name__=="__main__":
    app.run(debug=True)

