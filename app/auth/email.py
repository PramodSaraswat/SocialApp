from flask import render_template
from app.email import send_email
from flask_babel import _


def send_password_reset_email(user):
	token=user.get_reset_password_token()
	send_email(_('[SocialApp] Reset Your Password'),sender='noreply@demo.com',
		recipients=[user.email],
		text_body=render_template('email/reset_password.txt',user=user, token=token),
		html_body=render_template('email/reset_password.html',user=user, token=token))