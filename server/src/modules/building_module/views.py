from flask import jsonify, request
from src.constatns.http_status_codes import HTTP_200_OK
from src.modules.building_module.models import BuildingModel
from src.modules.user_module.models import UserModel
from . import building_bp
from flask_jwt_extended import jwt_required, get_jwt_identity


@building_bp.route("/get", methods=["GET"])
def handle_get_buildings():
    buildings = BuildingModel.query.all()
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
    }), HTTP_200_OK


@building_bp.route("/create", methods=['POST'])
@jwt_required()
def handle_create_buildings():
    current_user_id = get_jwt_identity()
    # data = request.get_json()
    user = UserModel.query.filter_by(id=current_user_id).first()
    # user = user.to_dict()
    print(user.is_admin())
    if not user or not user.is_admin():
        data = request.get_json()
        return jsonify({'message': 'Unauthorized'}), 200
    return jsonify({'message': 'Welcome, admin!'}), 200
    

    
    return jsonify({
        "msg": "create building successfully",
        "paylolad": user,
  
    })
