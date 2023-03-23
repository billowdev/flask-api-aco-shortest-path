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
            "image": "G1_3e4d03c2-79db-431f-aec9-8faceb4d6817.png",
            "lat": 17.192505969885183, 
            "lng": 104.0936199995255,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
               {
            "bid": "A18",
            "name": "อาคาร 18",
            "desc": "",
            "is_node": 1,
            "image": "default.png",
            "lat": 17.1908002887036, 
            "lng": 104.09268995851393,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
  
       {
            "bid": "C1",
            "name": "สี่แยกเนเซี่ยมเก่า",
            "desc": "",
            "is_node": 1,
            "image": "default.png",
            "lat": 17.18938542032942, 
            "lng":  104.09178738817262,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
         
       {
            "bid": "E9",
            "name": "โรงยิมเนเซี่ยมเก่า",
            "desc": "",
            "is_node": 1,
            "image": "default.png",
            "lat":  17.189841965471373, 
            "lng":  104.09137116697063,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
      
       {
            "bid": "A1",
            "name": "อาคาร 1",
            "desc": "",
            "is_node": 1,
            "image": "default.png",
            "lat": 17.189697124208863, 
            "lng":  104.0900539111374,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },       
        {
            "bid": "A9",
            "name": "อาคาร 9",
            "desc": "",
            "is_node": 1,
            "image": "default.png",
            "lat": 17.19039515336465, 
            "lng":  104.09026018514875,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        
    #        {
    #         "bid": "A7",
    #         "name": "อาคาร 7",
    #         "desc": "",
    #         "is_node": 1,
            # "image": "default.png",
    #         "lat":17.190682083333638, 
    #         "lng":  104.08971485149631,
    #         "created_at": datetime.now(),
    #         "updated_at": datetime.now()
    #     },
    #             {
    #         "bid": "E2",
    #         "name": "ศาลเจ้าปู่หนองหญ้าไซ",
    #         "desc": "",
    #         "is_node": 1,
            # "image": "default.png",
    #         "lat": 17.190546776205434, 
    #         "lng":  104.09121146183305,
    #         "created_at": datetime.now(),
    #         "updated_at": datetime.now()
    #     },
           
    #             {
    #         "bid": "E8",
    #         "name": "สำนักวิทยบริการและเทคโนโลยีสารสนเทศ (ห้องสมุด)",
    #         "desc": "",
    #         "is_node": 1,
            # "image": "default.png",
    #         "lat": 17.190546776205434, 
    #         "lng":  104.09121146183305,
    #         "created_at": datetime.now(),
    #         "updated_at": datetime.now()
    #     },
    #               {
    #         "bid": "E7",
    #         "name": "โรงเรียนวิถีธรรม อนุบาล แห่งมหาวิทยาลัยราชภัฏสกลนคร",
    #         "desc": "",
    #         "is_node": 1,
    # "image": "default.png",
    #         "lat": 17.19065943227838, 
    #         "lng":  104.08929243393098,
    #         "created_at": datetime.now(),
    #         "updated_at": datetime.now()
    #     },
    #    {
    #         "bid": "A6",
    #         "name": "อาคาร 6",
    #         "desc": "",
    #         "is_node": 1,
    # "image": "default.png",
    #         "lat": 17.190996524045243, 
    #         "lng":  104.08854333045862,
    #         "created_at": datetime.now(),
    #         "updated_at": datetime.now()
    #     },
    #        {
    #         "bid": "C7",
    #         "name": "สี่แยกอาคาร 6, อาคาร 7 และอนุบาลวิถีธรรม",
    #         "desc": "",
    #         "is_node": 1,
    # "image": "default.png",
    #         "lat": 17.190931454481092, 
    #         "lng":  104.08893246632512,
    #         "created_at": datetime.now(),
    #         "updated_at": datetime.now()
    #     },
       
      
    ]
    for building in buildings:
        db.session.add(BuildingModel(**building))
    db.session.commit()
