# define your seeder function
from src import db
from src.modules.building_module.models import BuildingModel

from datetime import datetime


def seed():
    buildings = [ 
          {
            "bid": "G1",
            "name": "ประตู 1",
            "desc": "",
            "is_node": 1,
            "lat": 17.192579386157856, 
            "lng": 104.0936108516875,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
  
       {
            "bid": "C1",
            "name": "สี่แยกเนเซี่ยมเก่า",
            "desc": "",
            "is_node": 1,
            "lat": 17.189393571433737,
            "lng":  104.09175530354463,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
       
       {
            "bid": "A1",
            "name": "อาคาร 1",
            "desc": "",
            "is_node": 1,
            "lat": 17.18973683143573, 
            "lng":  104.09010693513467,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
       
        {
            "bid": "A9",
            "name": "อาคาร 9",
            "desc": "",
            "is_node": 1,
            "lat": 17.19022292488029, 
            "lng":  104.09052137384434,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
            {
            "bid": "A1C1",
            "name": "A1C1",
            "desc": "",
            "is_node": 1,
            "lat":  17.189986936192767,
            "lng":   104.09063367402148,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        
       
        
           {
            "bid": "A7",
            "name": "อาคาร 7",
            "desc": "",
            "is_node": 1,
            "lat":17.190703061822163, 
            "lng":  104.08971200774761,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
       
    ]
    for building in buildings:
        db.session.add(BuildingModel(**building))
    db.session.commit()
