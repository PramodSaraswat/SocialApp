import os
basedir=os.path.abspath(os.path.dirname(__file__))



class Config(object):
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'cc3dae2cd67d2fb6e'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  or 'sqlite:///'+os.path.join(basedir,'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER='smtp.gmail.com'
	MAIL_PORT=465
	MAIL_USE_SSL=True
	MAIL_USERNAME=os.environ.get('EMAIL_USER') or None
	MAIL_PASSWORD=os.environ.get('EMAIL_PASS') or None
	LANGUAGES=['en','hi','es',]
	ADMINS=os.environ.get('ADMINS') or None
	POSTS_PER_PAGE=25
	IBMAPI_KEY=os.environ.get('API_KEY')
	IBMAPI_URL=os.environ.get('API_URL') or None
	ELASTICSEARCH_URL=os.environ.get('ELASTICSEARCH_URL') or None
	LOG_TO_STDOUT=os.environ.get('LOG_TO_STDOUT')