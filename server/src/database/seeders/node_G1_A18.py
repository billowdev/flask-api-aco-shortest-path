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
                                   {
            "bid": "G1A18L2",
            "name": "LINK G1A18L2",
            "desc": "โหนดเชื่อม G1A18L2",
            "is_node": 0,
            "lat":   17.190624181142397, 
            "lng": 104.09249030034253,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },     
         {
            "bid": "G1A18L3",
            "name": "LINK G1A18L3",
            "desc": "โหนดเชื่อม G1A18L3",
            "is_node": 0,
            "lat":   17.19017844824752, 
            "lng": 104.09222526318611,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },          
             {
            "bid": "A18",
            "name": "อาคาร 18 สนามกีฬาราชพฤกษ์",
            "desc": "อาคาร 18 หรือ สนามกีฬาราชพฤกษ์ มหาวิทยาลัยราชภัฏสกลนคร",
            "is_node": 1,
            "lat":  17.190810571090672, 
            "lng": 104.0926771469646,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
       
    ]
    for building in buildings:
        db.session.add(BuildingModel(**building))
    db.session.commit()
