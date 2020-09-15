import sys
import os
sys.path.append(os.path.join(os.getcwd(),'..'))
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests
from flask_babel import _
from flask import current_app

def translate(text,source_language,dest_language):
	url=current_app.config['IBMAPI_URL']
	authenticator = IAMAuthenticator(current_app.config['IBMAPI_KEY'])
	language_translator = LanguageTranslatorV3(
		version='2018-05-01',
		authenticator=authenticator)
	language_translator.set_service_url(url)
	r = language_translator.translate(
    text=text, model_id=source_language+'-'+dest_language).get_result()
	r=r['translations'][0]['translation']
	return r