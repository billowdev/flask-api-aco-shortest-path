from flask import Blueprint

building_bp = Blueprint('buildings', __name__, url_prefix='/buildings')

# import views to register them with the blueprint
from . import views
