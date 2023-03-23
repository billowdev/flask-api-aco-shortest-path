# define your seeder function
from src import db
from src.modules.building_module.models import BuildingModel

from datetime import datetime


def seed():
    buildings = [ 
    
    #   {
    #         "bid": "A18C1L1",
    #         "name": "LINK A18C1L1",
    #         "desc": "โหนดเชื่อม A18C1L1",
    #         "is_node": 0,
    #         "image": "",
    #         "lat":  17.192294512504006, 
    #         "lng": 104.09349868442199, 
    #         "created_at": datetime.now(),
    #         "updated_at": datetime.now()
    #     },         

           
    ]
    for building in buildings:
        db.session.add(BuildingModel(**building))
    db.session.commit()
