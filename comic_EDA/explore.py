import os

import pandas as pd
import numpy as np

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

database_file = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

#Import csv data 

dc_path = 'dc-wikia-data.csv'
marvel_path = 'marvel-wikia-data.csv'

dc_data = pd.read_csv(dc_path)
marvel_data= pd.read_csv(marvel_path)

marvel_data.head()