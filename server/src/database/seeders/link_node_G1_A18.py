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
            "image": "",
            "lat":  17.192294512504006, 
            "lng": 104.09349868442199, 
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },         
           {
            "bid": "G1A18L2",
            "name": "LINK G1A18L2",
            "desc": "โหนดเชื่อม G1A18L2",
            "is_node": 0,
            "image": "",
            "lat":  17.191841833253346, 
            "lng": 104.09323681201225, 
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },   
                   {
            "bid": "G1A18L3",
            "name": "LINK G1A18L3",
            "desc": "โหนดเชื่อม G1A18L3",
            "is_node": 0,
            "image": "",
            "lat":  17.191276843888947, 
            "lng": 104.09290456892681, 
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }, 
                        {
            "bid": "G1A18L4",
            "name": "LINK G1A18L4",
            "desc": "โหนดเชื่อม G1A18L4",
            "is_node": 0,
            "image": "",
            "lat":  17.19082658366511, 
            "lng":104.09264055339503, 
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }, 
           
    ]
    for building in buildings:
        db.session.add(BuildingModel(**building))
    db.session.commit()
