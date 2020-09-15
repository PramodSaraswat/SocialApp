from flask import Blueprint

bp=Blueprint('error',__name__)

from app.errors import handlers