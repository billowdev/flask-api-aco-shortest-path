from flask import jsonify, request
from src.constatns.http_status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from src.modules.building_module.models import BuildingModel
from src.modules.user_module.models import UserModel
from . import building_bp
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.database.db_instance import db


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

    if not user or not user.is_admin():
        return jsonify({'message': 'Forbidden'}), HTTP_403_FORBIDDEN

    payload = request.get_json().get('payload', '')

    # bid = body
    if BuildingModel.query.filter_by(bid=payload['bid']).first():
        return jsonify({'message': 'Building or that node is already exists'}), HTTP_409_CONFLICT
    try:
        building = BuildingModel(
            bid=payload['bid'],
            name=payload['name'],
            desc=payload['desc'],
            lat=payload['lat'],
            lng=payload['lng']
        )
        db.session.add(building)
        db.session.commit()
    except KeyError as e:
        key_error = ['bid', 'name', 'desc', 'lat', 'lng']
        if str(e)[1:-1] in key_error:
            print(f"{str(e)} key error")
        else:
            print("other key error")
        return jsonify({'message': f'create building was failed that {str(e)[1:-1]} key error'}), HTTP_400_BAD_REQUEST
    except BaseException as e:
        print("other exception occurred")
        # if(e == 'desc'):
        #     print("erorr - desc")

        return jsonify({'message': 'create building was failed'}), HTTP_400_BAD_REQUEST

    return jsonify({'message': 'Welcome, admin!'}), HTTP_200_OK


@building_bp.route("/<int:building_id>", methods=['PUT', 'PATCH'])
@jwt_required()
def handle_update_building(building_id):
    current_user_id = get_jwt_identity()
    user = UserModel.query.filter_by(id=current_user_id).first()

    if not user or not user.is_admin():
        return jsonify({'message': 'Forbidden'}), HTTP_403_FORBIDDEN

    building = BuildingModel.query.filter_by(id=building_id).first()
    if not building:
        return jsonify({'message': 'Building not found'}), HTTP_404_NOT_FOUND

    payload = request.get_json().get('payload', '')

    # Update building fields
    try:
        if request.method == 'PUT':
            building.bid = payload['bid']
            building.name = payload['name']
            building.desc = payload['desc']
            building.lat = payload['lat']
            building.lng = payload['lng']
        elif request.method == 'PATCH':
            if 'bid' in payload:
                building.bid = payload['bid']
            if 'name' in payload:
                building.name = payload['name']
            if 'desc' in payload:
                building.desc = payload['desc']
            if 'lat' in payload:
                building.lat = payload['lat']
            if 'lng' in payload:
                building.lng = payload['lng']
        db.session.commit()
    except KeyError as e:
        key_error = ['bid', 'name', 'desc', 'lat', 'lng']
        if str(e)[1:-1] in key_error:
            return jsonify({'message': f'update building failed - {str(e)[1:-1]} key error'}), HTTP_400_BAD_REQUEST
        else:
            return jsonify({'message': 'update building failed - other key error'}), HTTP_400_BAD_REQUEST
    except BaseException as e:
        return jsonify({'message': 'update building failed'}), HTTP_400_BAD_REQUEST

    return jsonify({'message': 'Building updated successfully'}), HTTP_200_OK


@building_bp.route("/delete/<int:building_id>", methods=['DELETE'])
@jwt_required()
def handle_delete_building(building_id):
    current_user_id = get_jwt_identity()
    user = UserModel.query.filter_by(id=current_user_id).first()

    if not user or not user.is_admin():
        return jsonify({'message': 'Forbidden'}), HTTP_403_FORBIDDEN

    building = BuildingModel.query.filter_by(id=building_id).first()
    if not building:
        return jsonify({'message': 'Building not found'}), HTTP_404_NOT_FOUND

    try:
        db.session.delete(building)
        db.session.commit()
    except BaseException as e:
        return jsonify({'message': 'delete building failed'}), HTTP_400_BAD_REQUEST

    return jsonify({'message': 'Building deleted successfully'}), HTTP_200_OK
