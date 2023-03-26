# define your seeder function
from src import db
from src.modules.building_module.models import BuildingModel

def seed():
    buildings = [ 
             {
            "bid": "G1",
            "desc": "",
            "id": 1,
            "image": "G1_3e4d03c2-79db-431f-aec9-8faceb4d6817.png",
            "is_node": True,
            "lat": "17.192505969885183",
            "lng": "104.093619999525500",
            "name": "ประตู 1"
        },
        {
            "bid": "A18",
            "desc": "",
            "id": 2,
            "image": "default.png",
            "is_node": True,
            "lat": "17.190800288703600",
            "lng": "104.092689958513930",
            "name": "อาคาร 18"
        },
        {
            "bid": "C1",
            "desc": "",
            "id": 3,
            "image": "default.png",
            "is_node": True,
            "lat": "17.189385420329420",
            "lng": "104.091787388172620",
            "name": "สี่แยกเนเซี่ยมเก่า"
        },
        {
            "bid": "E9",
            "desc": "",
            "id": 4,
            "image": "default.png",
            "is_node": True,
            "lat": "17.189841965471373",
            "lng": "104.091371166970630",
            "name": "โรงยิมเนเซี่ยมเก่า"
        },
        {
            "bid": "A1",
            "desc": "",
            "id": 5,
            "image": "default.png",
            "is_node": True,
            "lat": "17.189697124208863",
            "lng": "104.090053911137400",
            "name": "อาคาร 1"
        },
        {
            "bid": "A9",
            "desc": "",
            "id": 6,
            "image": "default.png",
            "is_node": True,
            "lat": "17.190395153364650",
            "lng": "104.090260185148750",
            "name": "อาคาร 9"
        },
        {
            "bid": "E7",
            "desc": "โรงเรียนวิถีธรรม แห่งมหาวิทยาลัยราชภัฏสกลนครอนุบาล",
            "id": 55,
            "image": "default.png",
            "is_node": True,
            "lat": "17.190645991242697",
            "lng": "104.089289445378870",
            "name": "โรงเรียนวิถีธรรม แห่งมหาวิทยาลัยราชภัฏสกลนครอนุบาล"
        },
        {
            "bid": "A7E7L1",
            "desc": "A7E7L1",
            "id": 56,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190543252097413",
            "lng": "104.089643955230730",
            "name": "A7E7L1"
        },
        {
            "bid": "A7",
            "desc": "",
            "id": 10,
            "image": "default.png",
            "is_node": True,
            "lat": "17.190723612065913",
            "lng": "104.089666404964920",
            "name": "อาคาร 7"
        },
        {
            "bid": "G1A18L1",
            "desc": "LINK G1A18L1",
            "id": 13,
            "image": "default.png",
            "is_node": False,
            "lat": "17.192234419868488",
            "lng": "104.093436621084350",
            "name": "LINK G1A18L1"
        },
        {
            "bid": "G1A18L2",
            "desc": "G1A18L2",
            "id": 14,
            "image": "default.png",
            "is_node": False,
            "lat": "17.191932060703778",
            "lng": "104.093259572982800",
            "name": "LINK G1A18L2"
        },
        {
            "bid": "G1A18L3",
            "desc": "G1A18L3",
            "id": 15,
            "image": "default.png",
            "is_node": False,
            "lat": "17.191634825789480",
            "lng": "104.093082547187820",
            "name": "LINK G1A18L3"
        },
        {
            "bid": "G1A18L4",
            "desc": "G1A18L3",
            "id": 16,
            "image": "default.png",
            "is_node": False,
            "lat": "17.191342715150290",
            "lng": "104.092921614646930",
            "name": "LINK G1A18L4"
        },
        {
            "bid": "G1A18L5",
            "desc": "G1A18L5",
            "id": 17,
            "image": "default.png",
            "is_node": False,
            "lat": "17.191101851645044",
            "lng": "104.092782139778150",
            "name": "LINK G1A18L5"
        },
        {
            "bid": "A18C1L1",
            "desc": "A18C1L1",
            "id": 18,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190579125513490",
            "lng": "104.092471003532420",
            "name": "LINK A18C1L1"
        },
        {
            "bid": "A18C1L2",
            "desc": "LINK A18C1L2",
            "id": 19,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190322886674830",
            "lng": "104.092326164245620",
            "name": "LINK A18C1L2"
        },
        {
            "bid": "A18C1L3",
            "desc": "LINK A18C1L3",
            "id": 20,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190056397906540",
            "lng": "104.092175960540770",
            "name": "LINK A18C1L3"
        },
        {
            "bid": "A18C1L4",
            "desc": "LINK A18C1L4",
            "id": 21,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189871905457720",
            "lng": "104.092063307762160",
            "name": "LINK A18C1L4"
        },
        {
            "bid": "A18C1L5",
            "desc": "LINK A18C1L5",
            "id": 22,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189748910389742",
            "lng": "104.091988205909730",
            "name": "LINK A18C1L5"
        },
        {
            "bid": "A18C1L6",
            "desc": "LINK A18C1L6",
            "id": 23,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189595166439904",
            "lng": "104.091907739639300",
            "name": "LINK A18C1L6"
        },
        {
            "bid": "C1E9L1",
            "desc": "LINK C1E9L1",
            "id": 24,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189467046384220",
            "lng": "104.091639518737810",
            "name": "LINK C1E9L1"
        },
        {
            "bid": "C1E9L2",
            "desc": "LINK C1E9L2",
            "id": 25,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189564417634620",
            "lng": "104.091473221778880",
            "name": "LINK C1E9L2"
        },
        {
            "bid": "C1E9L3",
            "desc": "LINK C1E9L3",
            "id": 26,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189666913632376",
            "lng": "104.091280102729800",
            "name": "LINK C1E9L3"
        },
        {
            "bid": "E9A9L3",
            "desc": "LINK E9A9L3",
            "id": 29,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189948777333733",
            "lng": "104.090765118598950",
            "name": "LINK E9A9L3"
        },
        {
            "bid": "E9A9L2",
            "desc": "LINK E9A9L2",
            "id": 28,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189851406285400",
            "lng": "104.090958237648010",
            "name": "LINK E9A9L2"
        },
        {
            "bid": "E9A9L1",
            "desc": "LINK E9A9L1",
            "id": 27,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189759159981865",
            "lng": "104.091124534606930",
            "name": "LINK E9A9L1"
        },
        {
            "bid": "E9A9L4",
            "desc": "LINK E9A9L4",
            "id": 30,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190041023542820",
            "lng": "104.090598821640030",
            "name": "LINK E9A9L4"
        },
        {
            "bid": "E9A9L5",
            "desc": "LINK E9A9L5",
            "id": 31,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190117895348628",
            "lng": "104.090427160263060",
            "name": "LINK E9A9L5"
        },
        {
            "bid": "E9A9L6",
            "desc": "LINK E9A9L6",
            "id": 32,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190215266256864",
            "lng": "104.090271592140210",
            "name": "LINK E9A9L6"
        },
        {
            "bid": "E9A1L1",
            "desc": "E9A1L1",
            "id": 33,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189939908032382",
            "lng": "104.090570390836670",
            "name": "LINK E9A1L1"
        },
        {
            "bid": "E9A1L2",
            "desc": "LINK E9A1L2",
            "id": 34,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189822037806103",
            "lng": "104.090485230697710",
            "name": "LINK E9A1L2"
        },
        {
            "bid": "E9A1L3",
            "desc": "E9A1L3",
            "id": 35,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189730187496040",
            "lng": "104.090392690916800",
            "name": "LINK E9A1L3"
        },
        {
            "bid": "E9A1L4",
            "desc": "E9A1L4",
            "id": 36,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189682393152857",
            "lng": "104.090231058535110",
            "name": "LINK E9A1L4"
        },
        {
            "bid": "C1E9L3-1",
            "desc": "C1E9L3-1",
            "id": 37,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189723286406963",
            "lng": "104.091194272041340",
            "name": "LINK C1E9L3-1"
        },
        {
            "bid": "E9A1L5",
            "desc": "E9A1L5",
            "id": 38,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189789011289054",
            "lng": "104.090002079331340",
            "name": "E9A1L5"
        },
        {
            "bid": "E9A1L6",
            "desc": "E9A1L6",
            "id": 39,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189857945394250",
            "lng": "104.089964557528460",
            "name": "E9A1L6"
        },
        {
            "bid": "E9A1L7",
            "desc": "E9A1L7",
            "id": 40,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189941585408462",
            "lng": "104.089960709139430",
            "name": "E9A1L7"
        },
        {
            "bid": "E9A1L8",
            "desc": "E9A1L8",
            "id": 41,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189999490010845",
            "lng": "104.089974178504560",
            "name": "E9A1L8"
        },
        {
            "bid": "E9A1L9",
            "desc": "E9A1L9",
            "id": 42,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190055556355690",
            "lng": "104.090030942257600",
            "name": "E9A1L9"
        },
        {
            "bid": "E9A1L10",
            "desc": "E9A1L10",
            "id": 43,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190114380042410",
            "lng": "104.090096364888280",
            "name": "E9A1L10"
        },
        {
            "bid": "E9A1L11",
            "desc": "E9A1L11",
            "id": 44,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190169527231724",
            "lng": "104.090146393958800",
            "name": "E9A1L11"
        },
        {
            "bid": "E9A9L4-1",
            "desc": "E9A9L4-1",
            "id": 45,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190102520990017",
            "lng": "104.090502262115490",
            "name": "E9A9L4-1"
        },
        {
            "bid": "E9A9L4-2",
            "desc": "E9A9L4-2",
            "id": 46,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190179392770318",
            "lng": "104.090352058410660",
            "name": "E9A9L4-2"
        },
        {
            "bid": "A1E9L11",
            "desc": "A1E9L11",
            "id": 47,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190298824638308",
            "lng": "104.090073852681300",
            "name": "A1E9L11"
        },
        {
            "bid": "A9A7L1",
            "desc": "A9A7L1",
            "id": 48,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190358760133577",
            "lng": "104.089998006820700",
            "name": "A9A7L1"
        },
        {
            "bid": "A9A7L2",
            "desc": "A9A7L2",
            "id": 49,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190415132697588",
            "lng": "104.089890718460100",
            "name": "A9A7L2"
        },
        {
            "bid": "A9A7L3",
            "desc": "A9A7L3",
            "id": 50,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190471505244425",
            "lng": "104.089788794517530",
            "name": "A9A7L3"
        },
        {
            "bid": "A9A7L4",
            "desc": "A9A7L4",
            "id": 51,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190512503449543",
            "lng": "104.089702963829050",
            "name": "A9A7L4"
        },
        {
            "bid": "A9A7L5",
            "desc": "A9A7L5",
            "id": 52,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190625248466805",
            "lng": "104.089676141738890",
            "name": "A9A7L5"
        },
        {
            "bid": "E8",
            "desc": "สำนักวิทยบริการและเทคโนโลยีสารสนเทศ (ห้องสมุด)",
            "id": 53,
            "image": "default.png",
            "is_node": True,
            "lat": "17.190261694450708",
            "lng": "104.089793064312740",
            "name": "สำนักวิทยบริการและเทคโนโลยีสารสนเทศ (ห้องสมุด)"
        },
        {
            "bid": "E1L1",
            "desc": "E1L1",
            "id": 54,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190321270030857",
            "lng": "104.089838661867460",
            "name": "E1L1"
        },
        {
            "bid": "A7E7L2",
            "desc": "A7E7L2",
            "id": 57,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190584250286644",
            "lng": "104.089579582214370",
            "name": "A7E7L2"
        },
        {
            "bid": "A7E7L3",
            "desc": "A7E7L3",
            "id": 58,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190620123694770",
            "lng": "104.089520573616030",
            "name": "A7E7L3"
        },
        {
            "bid": "A7E7L4",
            "desc": "A7E7L4",
            "id": 59,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190645747553468",
            "lng": "104.089466929435740",
            "name": "A7E7L4"
        },
        {
            "bid": "A7E7L5",
            "desc": "A7E7L5",
            "id": 60,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190681620949686",
            "lng": "104.089402556419390",
            "name": "A7E7L5"
        },
        {
            "bid": "A7E7L6",
            "desc": "A7E7L6",
            "id": 61,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190707244799874",
            "lng": "104.089332818984990",
            "name": "A7E7L6"
        },
        {
            "bid": "E9A9L6-1",
            "desc": "E9A9L6-1",
            "id": 62,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190240890171577",
            "lng": "104.090217947959900",
            "name": "E9A9L6-1"
        },
        {
            "bid": "E9A9L6-2",
            "desc": "E9A9L6-2",
            "id": 63,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190271638864548",
            "lng": "104.090175032615680",
            "name": "E9A9L6-2"
        },
        {
            "bid": "E9A9L3-1",
            "desc": "E9A9L3-1",
            "id": 64,
            "image": "default.png",
            "is_node": False,
            "lat": "17.189984650864943",
            "lng": "104.090711474418650",
            "name": "E9A9L3-1"
        },
        {
            "bid": "E9A9L3-2",
            "desc": "E9A9L3-2",
            "id": 65,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190015399600460",
            "lng": "104.090657830238360",
            "name": "E9A9L3-2"
        },
        {
            "bid": "G1A18L5-1",
            "desc": "G1A18L5-1",
            "id": 66,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190973732631640",
            "lng": "104.092712402343760",
            "name": "G1A18L5-1"
        },
        {
            "bid": "G1A18L5-2",
            "desc": "G1A18L5-2",
            "id": 67,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190866112591890",
            "lng": "104.092642664909360",
            "name": "G1A18L5-2"
        },
        {
            "bid": "G1A18L5-3",
            "desc": "G1A18L5-3",
            "id": 68,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190778991561530",
            "lng": "104.092583656311050",
            "name": "G1A18L5-3"
        },
        {
            "bid": "G1A18L5-4",
            "desc": "G1A18L5-4",
            "id": 69,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190702120030114",
            "lng": "104.092546105384840",
            "name": "G1A18L5-4"
        },
        {
            "bid": "A18C1L1-1",
            "desc": "A18C1L1-1",
            "id": 70,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190486879572410",
            "lng": "104.092406630516070",
            "name": "A18C1L1-1"
        },
        {
            "bid": "A18C1L2-1",
            "desc": "A18C1L2-1",
            "id": 71,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190235765388920",
            "lng": "104.092267155647290",
            "name": "A18C1L2-1"
        },
        {
            "bid": "C7",
            "desc": "สี่แยกอาคาร 7",
            "id": 72,
            "image": "default.png",
            "is_node": True,
            "lat": "17.190917360237677",
            "lng": "104.088930487632770",
            "name": "สี่แยกอาคาร 7"
        },
        {
            "bid": "A7C7L1",
            "desc": "A7C7L1",
            "id": 73,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190773866793760",
            "lng": "104.089225530624400",
            "name": "A7C7L1"
        },
        {
            "bid": "A7C7L2",
            "desc": "A7C7L2",
            "id": 74,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190794365863987",
            "lng": "104.089166522026060",
            "name": "A7C7L2"
        },
        {
            "bid": "A7C7L3",
            "desc": "A7C7L3",
            "id": 75,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190855863061040",
            "lng": "104.089053869247450",
            "name": "A7C7L3"
        },
        {
            "bid": "A6",
            "desc": "อาคารวิทยาศาสตร์",
            "id": 76,
            "image": "default.png",
            "is_node": True,
            "lat": "17.191031420775560",
            "lng": "104.088733620239500",
            "name": "อาคาร 6"
        },
        {
            "bid": "C7A6L1",
            "desc": "C7A6L1",
            "id": 77,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190963483106742",
            "lng": "104.088850021362320",
            "name": "C7A6L1"
        },
        {
            "bid": "C7A6L2",
            "desc": "C7A6L2",
            "id": 78,
            "image": "default.png",
            "is_node": False,
            "lat": "17.190999356441424",
            "lng": "104.088785648345960",
            "name": "C7A6L2"
        }
       
    ]
    for building in buildings:
        db.session.add(BuildingModel(**building))
    db.session.commit()
