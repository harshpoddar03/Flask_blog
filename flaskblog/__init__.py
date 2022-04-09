import sys
sys.path.insert(1, '/users/podda/anaconda3/lib/site-packages')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '952525frbgrrgirg'
app.config['SQLALCHEMY_DATABASES_URI'] = 'sqlite:///site.db'
datab = SQLAlchemy(app)

from flaskblog import routes