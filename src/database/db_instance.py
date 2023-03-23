from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from ..modules.building_module.models import BuildingModel
from ..modules.user_module.models import UserModel

