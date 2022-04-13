
from ast import Sub
import sys

from nbformat import ValidationError
sys.path.insert(1, '/users/podda/anaconda3/lib/site-packages')
from wsgiref.validate import validator
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField , FileAllowed
from wtforms import StringField , PasswordField , SubmitField , BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length , Email , EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max =20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different username')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different email')



class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember =BooleanField('Remember Me')
    submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max =20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    picture = FileField('Update Profile Picture', validators = [FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')
    
    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different username')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different email')


class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    content= TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('Post')




class RequestResetForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. Create an account first')



class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('ResetPassword')