from flaskblog import datab
from datetime import datetime


class User(datab.Model):
    id = datab.Column(datab.Integer,primary_key=True)
    username = datab.Column(datab.String(20), unique=True,nullable=False)
    email = datab.Column(datab.String(120), unique=True,nullable=False)
    image_file= datab.Column(datab.String(20),nullable=False,default='default.jpg')
    password = datab.Column(datab.String(60),nullable=False)
    posts = datab.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email},'{self.image_file}')"


class Post(datab.Model):
    id = datab.Column(datab.Integer,primary_key=True)
    title = datab.Column(datab.String(100),nullable=False)
    date_posted = datab.Column(datab.DateTime,nullable=False,default=datetime.utcnow)
    content = datab.Column(datab.Text,nullable=False)
    user_id = datab.Column(datab.Integer,datab.ForeignKey('user.id'),nullable=False)



    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"