from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField
from wtforms.validators import DataRequired,ValidationError,Length
from flask_babel import _, lazy_gettext as _l
from app.models import User
from flask_login import current_user


class EditProfileForm(FlaskForm):
	username=StringField(_l('Username'),validators=[DataRequired()])
	about_me=TextAreaField(_l('About Me'),validators=[Length(min=0,max=150)])
	submit=SubmitField(_l('Update Info'))

	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user and user.username!=current_user.username:
			raise ValidationError(_('Username is taken. Please choose a different one'))

class EmptyForm(FlaskForm):
	submit=SubmitField("Submit")
		
class PostForm(FlaskForm):
	post=TextAreaField(_l('Share your thoughts'),validators=[DataRequired(),Length(min=1,max=600)])
	submit=SubmitField(_l('Post'))	

class SearchForm(FlaskForm):
	q = StringField(_l('Search'), validators=[DataRequired()])
	def __init__(self, *args, **kwargs):
		if 'formdata' not in kwargs:
			kwargs['formdata'] = request.args
		if 'csrf_enabled' not in kwargs:
			kwargs['csrf_enabled'] = False
		super(SearchForm, self).__init__(*args, **kwargs)

class MessageForm(FlaskForm):
	message=TextAreaField(_l('Messagea'),validators=[DataRequired(),Length(min=0,max=150)])
	submit=SubmitField(_l('Send'))