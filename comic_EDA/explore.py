import os

from flask import Flask , render_template , request
from flask_restful import Resource, Api

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "comics.db"))


app = Flask(__name__)

#database configurations
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

#tracks sql light modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


#restful api configuration
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)