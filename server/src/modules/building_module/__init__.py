from flask import Blueprint, jsonify
from src.database.db_instance import db
building_bp = Blueprint('buildings', __name__, url_prefix='/buildings')

# import views to register them with the blueprint
# from . import views

@building_bp.route("/", methods=["GET"])
def handle_get_buildings():
    locations = [
        {
            "name": "A7",
            "desc": "ตึก 7",
            "lat": 17.191058760990806,
            "lng": 104.0894708420397,
        },
        {
            "name": "A9",
            "desc": "ตึก 9",
            "lat": 17.190634027635916,
            "lng": 104.09040683236034
        },
        {
            "name": "A6",
            "desc": "ตึก 6",
            "lat": 17.190970159860075,
            "lng":  104.08848902422882
        },
        {
            "name": "C4",
            "desc": "แยกเนเซี่ยม",
            "lat": 17.189400286942945,
            "lng":  104.09174171837972
        },
        {
            "name": "C5",
            "desc": "ทางสามแยกทางเข้าครุศาสตร์",
            "lat": 17.188738469975437,
            "lng":  104.09137406371342
        },
        {
            "name": "C1",
            "desc": "หน้าอาคาร 1 ทางเข้าอาคารครุศาสตร์",
            "lat": 17.189578289590823,
            "lng":  104.09041195449454
        }

    ]

    return jsonify({
        "msg": "get building successfully",
        "paylolad": locations
    })

