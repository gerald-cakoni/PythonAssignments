from flask_app import app

from flask_app.controllers import burgers
from flask_app.controllers import restaurants

if __name__ == "__main__":
 app.run(debug=True)