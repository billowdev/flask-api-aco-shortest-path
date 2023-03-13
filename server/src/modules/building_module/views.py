import decimal
from flask import jsonify, request
from src.constatns.http_status_codes import HTTP_201_CREATED
from src.constatns.http_status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from src.modules.building_module.models import BuildingModel
from src.modules.user_module.models import UserModel
from src.utils.aco.aco_nearest_node import aco_nearest_node
from src.utils.aco.aco_shourtest_path import aco_shortest_path
from . import building_bp
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.database.db_instance import db


@building_bp.post("/navigate")
def handle_navigate_building():
    payload = request.get_json().get('payload', '')
    try:
        if 'bid_start' in payload and 'bid_goal' in payload:
            bid_start = payload['bid_start']
            bid_goal = payload['bid_goal']
            # print(bid_start, bid_goal)
            raw_buildings = BuildingModel.query.all()
            buildings = []
            for each_building in range(len(raw_buildings)):
                buildings.append(raw_buildings[each_building].to_dict())

            # print(buildings)
            # buildings = buildings
            # use aco to find best path
            aco_navigation_path = aco_shortest_path(
                buildings, bid_start, bid_goal)

            best_path = aco_navigation_path['best_path']
            navigate_data = []
            for node in best_path:
                building_model = BuildingModel.query.filter_by(bid=node).first()
                building = building_model.to_dict()
                navigate_data.append({
                    'bid':building['bid'],
                    'lat':building['lat'],
                    'lng':building['lng'],
                })
                print(navigate_data)
                
            return jsonify({
                'message': 'Building navigate successfully',
                'payload': {
                    "from_start": bid_start,
                    "to_goal": bid_goal,
                    "distance": aco_navigation_path['distance'],
                    "best_path": aco_navigation_path['best_path'],
                    "navigation":navigate_data
                }
            }), HTTP_200_OK
        else:
            return jsonify({'message': 'bid_start or bid_goal is required'}), HTTP_400_BAD_REQUEST
    except BaseException as e:
        return jsonify({'message': 'navigate to building was failed'}), HTTP_400_BAD_REQUEST


@building_bp.post("/nearest")
def handle_nearest_building():
    payload = request.get_json().get('payload', '')
    try:
        if 'bid' in payload:
            # present_lat = payload['present_lat']
            # present_lng = payload['present_lng']
            bid = payload['bid']
            raw_buildings = BuildingModel.query.all()
            buildings = []
            for each_building in range(len(raw_buildings)):
                buildings.append(raw_buildings[each_building].to_dict())

            # buildings = buildings
            # use aco to find best path
            aco_nearest = aco_nearest_node(
                 buildings, bid)
            # print(aco_nearest)
            return jsonify({
                'message': 'Building navigate successfully',
                'payload': {
                    "nearest_building": aco_nearest,
                     # "aco_nearest": aco_nearest,
                }
            }), HTTP_200_OK
        else:
            return jsonify({'message': 'present_lat or present_lng is required or something went wrong'}), HTTP_400_BAD_REQUEST
    except BaseException as e:
        print(e)
        return jsonify({'message': 'find nearest building was failed'}), HTTP_400_BAD_REQUEST


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
        return jsonify({'message': 'Building was created successfully', 'payload': building.to_dict()}), HTTP_201_CREATED
    except KeyError as e:
        key_error = ['bid', 'name', 'desc', 'lat', 'lng']
        if str(e)[1:-1] in key_error:
            print(f"{str(e)} key error")
        else:
            print("other key error")
        return jsonify({'message': f'create building was failed that {str(e)[1:-1]} key error'}), HTTP_400_BAD_REQUEST
    except BaseException as e:
        print("other exception occurred")
        print(e)
        # if(e == 'desc'):
        #     print("erorr - desc")

        return jsonify({'message': 'create building was failed'}), HTTP_400_BAD_REQUEST


@building_bp.route("/update/<int:building_id>", methods=['PUT', 'PATCH'])
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
