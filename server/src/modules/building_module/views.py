from src.constatns.common_constant import ENDPOINT
from flask import jsonify, request
from src.modules.building_module.models import BuildingModel
from . import building_bp
from flask_jwt_extended import jwt_required


@building_bp.route("/", methods=["GET"])
def handle_get_buildings():
    buildings = BuildingModel.query()
    data: list = []
    for building in buildings:
        data.append({
            'id': building.id,
            'name': building.name,
            'bid': building.bid,
            'desc': building.desc,
            'lat': building.lat,
            'lng': building.lng,
        })

    return jsonify({
        "msg": "get building successfully",
        "paylolad": data
    })


@building_bp.route("/create", methods=["POST"])
@jwt_required
def handle_get_buildings():
    data = request.get_json()
    # username = data.get('username')
    
    return jsonify({
        "msg": "create building successfully",
        "paylolad": data
    })
