from flask import Blueprint

login_bp = Blueprint('login', __name__, url_prefix='/login', template_folder='.')

from . import login_api
