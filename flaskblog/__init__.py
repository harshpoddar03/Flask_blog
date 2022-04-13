import os
import sys
sys.path.insert(1, '/users/podda/anaconda3/lib/site-packages')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail



app = Flask(__name__)
app.config['SECRET_KEY'] = '952525frbgrrgirg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////users/podda/flask_blog/flaskblog/final.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'harsh.poddar1605@gmail.com'
app.config['MAIL_PASSWORD'] = 'Harshcooldude@1605'

mail=Mail(app)


from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main


app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)