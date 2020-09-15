from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,EqualTo,Email,ValidationError,Length
from flask_babel import _, lazy_gettext as _l
from app.models import User

class LoginForm(FlaskForm):
	username=StringField(_l('Username'),validators=[DataRequired()])
	password=PasswordField(_l('Password'),validators=[DataRequired()])
	remember_me=BooleanField(_l('Remember Me'))
	submit=SubmitField(_l('Sign In'))


class RegistrationForm(FlaskForm):
	username=StringField(_l('Username'), validators=[DataRequired()])
	email=StringField(_l('Email'),validators=[DataRequired(),Email()])
	password=PasswordField(_l('Password'), validators=[DataRequired()])
	confirm_password=PasswordField(_l('Confirm Password'), validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField(_l('Sign Up'))

	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError(_('This Email is taken. Please choose a different one'))

	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError(_('Username is taken. Please choose a different one'))
class ResetPasswordRequestForm(FlaskForm):
	email=StringField(_l('Email'),validators=[DataRequired(),Email()])
	submit=SubmitField(_l('Request Password Reset'))

class ResetPasswordForm(FlaskForm):
	password=PasswordField(_l('Password'), validators=[DataRequired()])
	confirm_password=PasswordField(_l('Confirm Password'), validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField(_l('Request Password Reset'))