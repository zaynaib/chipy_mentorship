from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

##import the config instance in or flask app
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import routes, models

if __name__ == '__main__':
    app.debug=True

