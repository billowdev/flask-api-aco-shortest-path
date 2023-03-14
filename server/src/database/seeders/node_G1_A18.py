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
                {
            "bid": "A18L01",
            "name": "LINK A18L01",
            "desc": "โหนดเชื่อม A18L01",
            "is_node": 1,
            "lat":  17.190828466728988, 
            "lng": 104.09264026440133,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                    {
            "bid": "A18L02",
            "name": "LINK A18L02",
            "desc": "โหนดเชื่อม A18L02",
            "is_node": 1,
            "lat":  17.190794067977038, 
            "lng":104.09261946061027,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                       {
            "bid": "A18L03",
            "name": "LINK A18L03",
            "desc": "โหนดเชื่อม A18L03",
            "is_node": 1,
            "lat":  17.19070385932756, 
            "lng":104.09256572910839,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
           {
            "bid": "A18L04",
            "name": "LINK A18L04",
            "desc": "โหนดเชื่อม A18L04",
            "is_node": 1,
            "lat":  17.190642999261538, 
            "lng":104.09253204896639,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
              {
            "bid": "A18L05",
            "name": "LINK A18L05",
            "desc": "โหนดเชื่อม A18L05",
            "is_node": 1,
            "lat":  17.19055935031709, 
            "lng": 104.0924798101123,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                {
            "bid": "A18L06",
            "name": "LINK A18L06",
            "desc": "โหนดเชื่อม A18L06",
            "is_node": 1,
            "lat":  17.190449952237493,
            "lng":  104.09241682192359,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                    {
            "bid": "A18L07",
            "name": "LINK A18L07",
            "desc": "โหนดเชื่อม A18L07",
            "is_node": 1,
            "lat":  17.190283336315566, 
            "lng":  104.09231786926254,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
               {
            "bid": "A18L08",
            "name": "LINK A18L08",
            "desc": "โหนดเชื่อม A18L08",
            "is_node": 1,
            "lat":  17.190104135778697, 
            "lng":  104.09221359958588,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
             {
            "bid": "A18L09",
            "name": "LINK A18L09",
            "desc": "โหนดเชื่อม A18L09",
            "is_node": 1,
            "lat":  17.19014324569629, 
            "lng": 104.09223558517257,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
    ]
    for building in buildings:
        db.session.add(BuildingModel(**building))
    db.session.commit()
