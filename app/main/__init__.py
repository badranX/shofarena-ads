from flask import Blueprint

main_blueprint = Blueprint('main_blueprint',__name__)

from . import views