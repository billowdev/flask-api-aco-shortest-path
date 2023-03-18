# define your seeder function
from src import db
from src.modules.building_module.models import BuildingModel

from datetime import datetime


def seed():
    buildings = [ 
    
      {
            "bid": "G1A18L1",
            "name": "LINK G1A18L1",
            "desc": "โหนดเชื่อม G1A18L1",
            "is_node": 0,
            "lat":  17.190834855122393, 
            "lng": 104.09264319733927, 
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },         
        
    ]
    for building in buildings:
        db.session.add(BuildingModel(**building))
    db.session.commit()
