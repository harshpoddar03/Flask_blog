import sys
sys.path.insert(1, '/users/podda/anaconda3/lib/site-packages')
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired





class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    content= TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('Post')