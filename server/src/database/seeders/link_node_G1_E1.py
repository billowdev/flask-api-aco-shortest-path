# define your seeder function
from src import db
from src.modules.building_module.models import BuildingModel

from datetime import datetime


def seed():
    buildings = [ 
        {
            "bid": "G1",
            "name": "ประตู 1",
            "desc": "ประตู 1 มหาวิทยาลัยราชภัฏสกลนคร",
            "is_node": 1,
            "lat": 17.19256404202556,
            "lng": 104.09360793646384,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                                                              

       
    ]
    for building in buildings:
        db.session.add(BuildingModel(**building))
    db.session.commit()
