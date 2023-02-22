# define your seeder function
from src import db
from src.modules.building_module.models import BuildingModel

from datetime import datetime


def seed():
    buildings = [
        {
            "bid": "A7",
            "name": "ตึก 7",
            "desc": "ตึก 7",
            "lat": 17.191058760990806,
            "lng": 104.0894708420397,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "bid": "A9",
            "name": "A9",
            "desc": "ตึก 9",
            "lat": 17.190634027635916,
            "lng": 104.09040683236034,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "bid": "A6",
            "name": "A6",
            "desc": "ตึก 6",
            "lat": 17.190970159860075,
            "lng":  104.08848902422882,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "bid": "C4",
            "name": "C4",
            "desc": "แยกเนเซี่ยม",
            "lat": 17.189400286942945,
            "lng":  104.09174171837972,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "bid": "C5",
            "name": "C5",
            "desc": "ทางสามแยกทางเข้าครุศาสตร์",
            "lat": 17.188738469975437,
            "lng":  104.09137406371342,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "bid": "C1",
            "name": "C1",
            "desc": "หน้าอาคาร 1 ทางเข้าอาคารครุศาสตร์",
            "lat": 17.189578289590823,
            "lng":  104.09041195449454,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
       
    ]
    for building in buildings:
        db.session.add(BuildingModel(**building))
    db.session.commit()
