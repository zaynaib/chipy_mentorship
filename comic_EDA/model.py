from explore import db
#https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
#https://flask-restful.readthedocs.io/en/latest/quickstart.html#resourceful-routing

class Marvel(db.Model):
    align = db.Column(db.String(128))
    alive = db.Column(db.String(128))
    appearances = db.Column(db.Float)
    sex = db.Column(db.String(128))
    year = db.Column(db.Float)
    name = db.Column(db.String(120), index=True, unique=True)
    page_id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Marvel {}>'.format(self.name) 
    
    def createSuperheroDict(self):
        #create a dictionary object
        #loop through all the marvel queries 
        #put them into the dictionary object
        character_id = self.page_id
        character_name = self.name
        return {character_id : character_name}

    

print(Marvel.query.all())