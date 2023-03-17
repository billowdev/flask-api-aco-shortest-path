
    
    
    
    
    # define your seeder function
from src import db
from src.modules.building_module.models import BuildingModel

from datetime import datetime


def seed():
    buildings = [ 
                     
       {
            "bid": "C1",
            "name": "แยกโรงยิมเนเซี่ยมเก่า",
            "desc": "แยกโรงยิมเนเซี่ยมเก่า ใกล้คณะวิทยาการจัดการ หรืออาคาร 4",
            "is_node": 1,
            "lat":17.18940353583393, 
            "lng":104.09178602815216,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },     
          
      {
            "bid": "E9L1",
            "name": "บันไดทางเข้าโรงยิมเนเซี่ยมเก่า",
            "desc": "บันไดทางเข้าโรงยิมเนเซี่ยมเก่า",
            "is_node": 0,
            "lat": 17.189616933256058, 
            "lng": 104.09144210756546,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },  
                 
         {
            "bid": "E9",
            "name": "โรงยิมเนเซี่ยมเก่า",
            "desc": "โรงยิมเนเซี่ยมเก่า",
            "is_node": 1,
            "lat": 17.189883812372376, 
            "lng": 104.09138741224955,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
         
            {
            "bid": "C1E9L1",
            "name": "โหนดเชื่อม C1E9L1 เส้นทางจากสี่แยกโรงยิมเนเซี่ยมเก่า",
            "desc": "เส้นทางจาก สี่แยกโรงยิมเนเซี่ยมเก่าหรือทางข้างโรงยิมเนเซี่ยมเก่า",
            "is_node": 0,
            "lat": 17.189656567713783, 
            "lng": 104.09129441419039,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }, 
        {
            "bid": "C1E9L2",
            "name": "C1E9L2 เส้นทางจากสี่แยกโรงยิมเนเซี่ยมเก่าใกล้ทางเข้าอาคาร 1",
            "desc": "โหนดเชื่อม C1E9L2 เส้นทางจากสี่แยกโรงยิมเนเซี่ยมเก่าใกล้ทางเข้าอาคาร 1",
            "is_node": 0,
            "lat": 17.189889931927706, 
            "lng": 104.09080261756962,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }, 
         {
            "bid": "A1C1L1",
            "name": "A1C1L1 ทางหน้าอาคาร 1",
            "desc": "โหนดเชื่อม A1C1L1 ทางหน้าอาคาร 1",
            "is_node": 0,
            "lat":   17.190128206716498, 
            "lng": 104.09035942065883,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }, 
            {
            "bid": "A1G1L1",
            "name": "A1G1L1 ปากทางเข้าอาคาร 1",
            "desc": "โหนดเชื่อม ปากทางเข้าอาคาร 1",
            "is_node": 0,
            "lat":  17.18995657452885, 
            "lng": 104.09057742792508,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },                                       
                                                 
        {
            "bid": "A1G1L2",
            "name": "A1G1L2 ทางเข้าอาคาร 1 หน้าอาคาร",
            "desc": "โหนดเชื่อม ทางเข้าอาคาร 1",
            "is_node": 0,
            "lat":   17.189667025651538, 
            "lng": 104.09025935888026,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }, 
             {
            "bid": "A1G2L1",
            "name": "A1G2L1 ทางออกอาคาร 1 ปากทาง",
            "desc": "โหนดเชื่อม A1G2L1 ทางออกอาคาร 1 ปากทาง",
            "is_node": 0,
            "lat":  17.19017517708049, 
            "lng": 104.0901563607132,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }, 
                 {
            "bid": "A1G2L2",
            "name": "A1G2L2 ทางออกอาคาร 1 โค้ง",
            "desc": "โหนดเชื่อม A1G2L2 ทางออกอาคาร 1 โค้ง",
            "is_node": 0,
            "lat":   17.190001227826556, 
            "lng": 104.0899834971026,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }, 
              {
            "bid": "A1G2L3",
            "name": "A1G2L3 ทางออกอาคาร 1 หน้าอาคาร",
            "desc": "โหนดเชื่อม A1G2L3 ทางออกอาคาร 1 หน้าอาคาร",
            "is_node": 0,
            "lat":   17.189799139263698, 
            "lng": 104.08993668015496,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }, 
         {
            "bid": "A1",
            "name": "อาคาร 1",
            "desc": "อาคาร 1",
            "is_node": 1,
            "lat": 17.1896467231417,
            "lng": 104.09003305133994,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        #  =============================================
        {
            "bid": "A7",
            "name": "ตึก 7",
            "desc": "ตึก 7",
            "is_node": 1,
            "lat": 17.191058760990806,
            "lng": 104.0894708420397,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "bid": "A9",
            "name": "A9",
            "desc": "ตึก 9",
                        "is_node": 1,

            "lat": 17.190634027635916,
            "lng": 104.09040683236034,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "bid": "A6",
            "name": "A6",
            "desc": "ตึก 6",
            "is_node": 1,
            "lat": 17.190970159860075,
            "lng":  104.08848902422882,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "bid": "C4",
            "name": "C4",
            "desc": "แยกเนเซี่ยม",
                        "is_node": 1,

            "lat": 17.189400286942945,
            "lng":  104.09174171837972,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "bid": "C5",
            "name": "C5",
            "desc": "ทางสามแยกทางเข้าครุศาสตร์",
            "is_node": 1,
            "lat": 17.188738469975437,
            "lng":  104.09137406371342,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
    ]
    for building in buildings:
        db.session.add(BuildingModel(**building))
    db.session.commit()
