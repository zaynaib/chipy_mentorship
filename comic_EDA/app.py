import os

from flask import Flask , render_template , request, jsonify
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



class Marvel(db.Model):
    align = db.Column(db.String(128))
    alive = db.Column(db.String(128))
    appearances = db.Column(db.Float)
    sex = db.Column(db.String(128))
    year = db.Column(db.Float)
    name = db.Column(db.String(120), index=True, unique=True)
    page_id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Marvel {} ,{} >'.format(self.page_id,self.name) 



def createSuperhero():
    heroes = Marvel.query.all()
    heroData = {}
    heroName = []
    heroId = []
    
    for hero in heroes:
        heroId.append(hero.page_id)
        heroName.append(hero.name)
    heroData = dict(zip(heroId,heroName))
    return heroData

superheroDict = createSuperhero()


print(superheroDict)
'''

#restful api configuration
api = Api(app)

class MarvelApi(Resource): 
    def get(self,db):
        return {'courses': db.fetchone()}

class HelloWorld(Resource):
    def get(self):
        return{'hello':'world'}

api.add_resource(HelloWorld,'/')
api.add_resource(MarvelApi,'/mav')



@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
'''