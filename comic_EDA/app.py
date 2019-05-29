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
        return '<Marvel {} ,{},{} >'.format(self.page_id,self.name,self.sex) 


#split up function into more modular parts

def queryAllHeroes():
    hero_data = Marvel.query.all()
    return hero_data


#endpoint find name with page id
def createSuperhero():
    heroes = queryAllHeroes()
    heroData = {}
    heroName = []
    heroId = []
    
    for hero in heroes:
        heroId.append(hero.page_id)
        heroName.append(hero.name)
    heroData = dict(zip(heroId,heroName))
    return heroData

#I want to get character bio by page id
def superHeroInfo():
    heroes = queryAllHeroes()
    information = []
    for hero in heroes:
        hero_info = {'id':hero.page_id,'name':hero.name,'status':hero.alive,'sex':hero.sex,'appearances':hero.appearances,'year':hero.year}
        information.append(hero_info)

    return information

superheroDict = createSuperhero()

#print(superHeroInfo())

#print(superheroDict)
print(superheroDict[695217])
#print(superheroDict[526248])


#restful api configuration
api = Api(app)


#resources
class TodoSimple(Resource):
    def get(self, super_id):
        return {super_id: superheroDict[super_id]}

class allHero(Resource):
    def get(self):
        return superHeroInfo()

class Hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}


# Route

api.add_resource(Hello, '/Hello')
api.add_resource(TodoSimple, '/superhero/<int:super_id>')
api.add_resource(allHero, '/superhero/')





@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)






