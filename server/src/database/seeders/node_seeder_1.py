# define your seeder function
from src import db
from src.modules.building_module.models import BuildingModel

from datetime import datetime


def seed():
    buildings = [ 
   
        # {
        #     "bid": "A0",
        #     "name": "A0",
        #     "desc": "ทางสามแยกทางเข้าครุศาสตร์",
        #     "is_node": 1,
        #     "lat": 17.188738469975437,
        #     "lng":  104.09137406371342,
        #     "created_at": datetime.now(),
        #     "updated_at": datetime.now()
        # },
       
    ]
    for building in buildings:
        db.session.add(BuildingModel(**building))
    db.session.commit()
