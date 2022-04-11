import sys
sys.path.insert(1, '/users/podda/anaconda3/lib/site-packages')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = '952525frbgrrgirg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////users/podda/flask_blog/flaskblog/final.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flaskblog import routes