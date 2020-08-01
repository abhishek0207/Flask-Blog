  
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('username', 
    validators=[DataRequired(), Length(min=2, max=20) ])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirmpassword = PasswordField('confirm password', 
    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, please chose a different one!')
    def validate_email(self, email):
        emailID = User.query.filter_by(email=email.data).first()
        if emailID:
            raise ValidationError('That email is registered, please chose a different email!')

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('username', 
    validators=[DataRequired(), Length(min=2, max=20) ])
    email = StringField('email', validators=[DataRequired(), Email()])
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update Account')

    def validate_username(self, username):
        if username.data!=current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken, please chose a different one!')
    def validate_email(self, email):
        if email.data!=current_user.email:
            emailID = User.query.filter_by(email=email.data).first()
            if emailID:
                raise ValidationError('That email is registered, please chose a different email!')
class RequestResetForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('There is no account with that email. You must register First!!')
class ResetPasswordForm(FlaskForm):
    password = PasswordField('password', validators=[DataRequired()])
    confirmpassword = PasswordField('confirm password', 
    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')