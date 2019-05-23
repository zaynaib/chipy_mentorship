from app import db

#https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
#https://flask-restful.readthedocs.io/en/latest/quickstart.html#resourceful-routing
#http://flask.pocoo.org/docs/1.0/patterns/sqlalchemy/ ***
#https://stackoverflow.com/questions/14789668/separate-sqlalchemy-models-by-file-in-flask ***

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

#print(createSuperhero())