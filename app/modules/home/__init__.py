from flask import Blueprint

home_bp = Blueprint('home', __name__, url_prefix='/home', template_folder='.')

from . import home_api
