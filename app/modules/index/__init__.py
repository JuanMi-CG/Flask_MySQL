from flask import Blueprint

index_bp = Blueprint('index', __name__, url_prefix='/index', template_folder='')

from . import index_api
