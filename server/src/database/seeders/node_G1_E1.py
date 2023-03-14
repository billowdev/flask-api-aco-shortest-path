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
          {
            "bid": "G1L1",
            "name": "โหนดเชื่อม G1L1",
            "desc": "สามแยกโรงแรม ตรงประตู 1",
            "is_node": 0,
            "lat": 17.192329942043273, 
            "lng": 104.09348628794305,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
            {
            "bid": "G1L2",
            "name": "โหนดเชื่อม G1L2",
            "desc": "G1L2",
            "is_node": 0,
            "lat":17.19239965864554, 
            "lng":104.09356088792255,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "bid": "G1L3",
            "name": "โหนดเชื่อม G1L3",
            "desc": "G1L3",
            "is_node": 0,
            "lat":17.192339303302465, 
            "lng":104.09352685948282,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                  
            {
            "bid": "G1L4",
            "name": "โหนดเชื่อม G1L4",
            "desc": "G1L4",
            "is_node": 0,
              "lat":17.192205160723507, 
            "lng":104.0934495591739,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                {
            "bid": "G1L41",
            "name": "โหนดเชื่อม G1L41",
            "desc": "G1L41",
            "is_node": 0,
              "lat":17.19218641444562,
            "lng": 104.09343628774235,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                                {
            "bid": "G1L42",
            "name": "โหนดเชื่อม G1L42",
            "desc": "G1L42",
            "is_node": 0,
              "lat": 17.192176813324867,
            "lng":  104.09343275456074,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                
               
             {
            "bid": "G1L5",
            "name": "โหนดเชื่อม G1L5",
            "desc": "G1L5",
            "is_node": 0,
              "lat":17.192144945154855, 
            "lng":104.09341603156288,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
             {
            "bid": "G1L6",
            "name": "โหนดเชื่อม G1L6",
            "desc": "G1L6",
            "is_node": 0,
              "lat": 17.192072053813625, 
            "lng":104.09337336194189,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
            {
            "bid": "G1L7",
            "name": "โหนดเชื่อม G1L7",
            "desc": "G1L7",
            "is_node": 0,
              "lat":  17.191990494784445, 
            "lng":104.09332642521102,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
           {
            "bid": "G1L8",
            "name": "โหนดเชื่อม G1L8",
            "desc": "G1L8",
            "is_node": 0,
              "lat":  17.19192139730717, 
            "lng":104.09328822535443,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
            {
            "bid": "G1L9",
            "name": "โหนดเชื่อม G1L9",
            "desc": "สามแยกทางเข้าที่จอดรถตรงข้าม หอพระพุธรัชปัญญาบารมี",
            "is_node": 0,
              "lat": 17.19184946066179, 
            "lng":104.09324710018069,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
               {
            "bid": "E1",
            "name": "หอพระพุทธรัชปัญญาบารมี",
            "desc": "หอพระพุทธรัชปัญญาบารมี",
            "is_node": 1,
            "lat": 17.192138651499242, 
            "lng":104.092790389835,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
               
         {
            "bid": "G1E1L01",
            "name": "G1E1L01",
            "desc": "โหนดเชื่อม G1E1L01",
            "is_node": 0,
             "lat": 17.191832217638694, 
            "lng": 104.09323194173122,    
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                                {
            "bid": "G1E1L02",
            "name": "G1E1L02",
            "desc": "โหนดเชื่อม G1E1L02",
            "is_node": 0,
            "lat": 17.191804576414082, 
            "lng":104.09321766475055,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                          {
            "bid": "G1E1L03",
            "name": "G1E1L03",
            "desc": "โหนดเชื่อม G1E1L03",
            "is_node": 0,
            "lat": 17.19176518357731,
            "lng": 104.0931851890825,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "bid": "G1E1L04",
            "name": "G1E1L04",
            "desc": "โหนดเชื่อม G1E1L04",
            "is_node": 0,
            "lat":  17.191702311854886, 
            "lng": 104.09315242756986,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                {
            "bid": "G1E1L05",
            "name": "G1E1L05",
            "desc": "โหนดเชื่อม G1E1L05",
            "is_node": 0,
            "lat":  17.191600890270553, 
            "lng": 104.09309293181127,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                        {
            "bid": "G1E1L06",
            "name": "G1E1L06",
            "desc": "โหนดเชื่อม G1E1L06",
            "is_node": 0,
            "lat":  17.191487969075066, 
            "lng": 104.09302472514737,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
               {
            "bid": "G1E1L07",
            "name": "LINK G1E1L07",
            "desc": "โหนดเชื่อม G1E1L07",
            "is_node": 0,
            "lat":   17.19138678546207, 
            "lng": 104.09296904400135,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                  
                 {
            "bid": "G1E1L08",
            "name": "LINK G1E1L08",
            "desc": "โหนดเชื่อม G1E1L08",
            "is_node": 0,
            "lat":   17.191392722051607, 
            "lng": 104.09297122443695,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                  
        {
            "bid": "G1E1L09",
            "name": "LINK G1E1L09",
            "desc": "โหนดเชื่อม G1E1L09",
            "is_node": 0,
            "lat":   17.191303362818008, 
            "lng": 104.0929208376387,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                {
            "bid": "G1E1L10",
            "name": "LINK G1E1L10",
            "desc": "โหนดเชื่อม G1E1L10",
            "is_node": 0,
            "lat":  17.191193350140953, 
            "lng": 104.09285436772541,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                   {
            "bid": "G1E1L11",
            "name": "LINK G1E1L11",
            "desc": "โหนดเชื่อม G1E1L11",
            "is_node": 0,
            "lat": 17.191226020458423, 
            "lng": 104.09287381374162,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                   {
            "bid": "G1E1L12",
            "name": "LINK G1E1L12",
            "desc": "โหนดเชื่อม G1E1L12",
            "is_node": 0,
            "lat": 17.191093743178683, 
            "lng": 104.09279492022006,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
  {
            "bid": "G1E1L13",
            "name": "LINK G1E1L13",
            "desc": "โหนดเชื่อม G1E1L13",
            "is_node": 0,
            "lat": 17.19102026439513, 
            "lng": 104.09275263166732,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
     {
            "bid": "G1E1L14",
            "name": "LINK G1E1L14",
            "desc": "โหนดเชื่อม G1E1L14",
            "is_node": 0,
            "lat": 17.19095823188803, 
            "lng": 104.0927150539265,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
     
          {
            "bid": "G1E1L15",
            "name": "LINK G1E1L15",
            "desc": "โหนดเชื่อม G1E1L15",
            "is_node": 0,
            "lat":  17.19091247881427, 
            "lng": 104.0926907907248,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
                                                                                                    

       
    ]
    for building in buildings:
        db.session.add(BuildingModel(**building))
    db.session.commit()
