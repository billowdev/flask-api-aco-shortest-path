import decimal
import os
from flask import current_app, jsonify, request
from src.constatns.http_status_codes import HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR
from src.constatns.http_status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from src.modules.building_module.models import BuildingModel
from src.modules.user_module.models import UserModel
from werkzeug.utils import secure_filename
from . import building_bp
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.database.db_instance import db
from src.utils.aco.aco_nearest_node import aco_nearest_node
from src.utils.aco.aco_shortest_path import aco_shortest_path
from src.utils.aco.aco_shortest_path_geo import aco_shortest_path_geo


@building_bp.route('/node', methods=['GET'])
def get_buildings():
    try:
        nodes = BuildingModel.query.filter_by(is_node=True).all()
        node_bids = [node.bid for node in nodes]
        return jsonify({"message": "Buildings retrieved successfully", "payload": [node_bids]}), 200
    except Exception as e:
        return jsonify({"message": f"Error: {e}"}), 500


@building_bp.route("/navigate", methods=['POST'])
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

    
            # buildings = buildings
            # use aco to find best path
            aco_navigation_path = aco_shortest_path(
                buildings, bid_start, bid_goal)
            # print(aco_navigation_path)
            best_path = aco_navigation_path['best_path']
            navigate_data = []
            for node in best_path:
                building_model = BuildingModel.query.filter_by(bid=node).first()
                building = building_model.to_dict()
                navigate_data.append({
                    'bid':building['bid'],
                    'lat':building['lat'],
                    'is_node':building['is_node'],
                    'lng':building['lng'],
                })
            # สกัดเอาแค่ โหนดเริ่มต้นจนถึงโหนดเป้าหมาย
            new_best_path = []
            for node in best_path:
                if(node != bid_goal):
                    new_best_path.append(node)
                else:
                    new_best_path.append(node)
                    break
            new_navigate_data = []
            for node in navigate_data:
                if(node['bid']!=bid_goal):
                    new_navigate_data.append(node)
                else:
                    new_navigate_data.append(node)
                    break
            # create coordinates list
            # print(navigate_data)
            coordinates = []
            for n in (new_navigate_data):
                c = [float(n['lat']), float(n['lng'])]
                coordinates.append(c)

            return jsonify({
                'message': 'Building navigate successfully',
                'payload': {
                    "from_start": bid_start,
                    "to_goal": bid_goal,
                    "distance": aco_navigation_path['distance'],
                    "best_path": new_best_path,
                    "navigation":new_navigate_data,
                    "coordinates": coordinates
                }
            }), HTTP_200_OK
        else:
            return jsonify({'message': 'bid_start or bid_goal is required'}), HTTP_400_BAD_REQUEST
    except BaseException as e:
        print(e)
        return jsonify({'message': 'navigate to building was failed'}), HTTP_400_BAD_REQUEST

@building_bp.post("/navigate/geo")
def handle_navigate_geo_building():
    payload = request.get_json().get('payload', '')
    try:
        if 'goal_state' in payload and 'start_state' in payload:
            start_state = payload['start_state']
            # print(start_state)
            bid_goal =payload['goal_state']
           
            # print(bid_start, bid_goal)
            raw_buildings = BuildingModel.query.all()
            buildings = []
            for each_building in range(len(raw_buildings)):
                buildings.append(raw_buildings[each_building].to_dict())

            aco_navigation_path = aco_shortest_path_geo(buildings, start_state, bid_goal)

            best_path = aco_navigation_path['best_path']
            navigate_data = []
            for node in best_path:
                building_model = BuildingModel.query.filter_by(bid=node).first()
                building = building_model.to_dict()
                navigate_data.append({
                    'bid':building['bid'],
                    'lat':building['lat'],
                    'is_node':building['is_node'],
                    'lng':building['lng'],
                })
            # สกัดเอาแค่ โหนดเริ่มต้นจนถึงโหนดเป้าหมาย
            new_best_path = []
            for node in best_path:
                if(node != bid_goal):
                    new_best_path.append(node)
                else:
                    new_best_path.append(node)
                    break
            new_navigate_data = []
            for node in navigate_data:
                if(node['bid']!=bid_goal):
                    new_navigate_data.append(node)
                else:
                    new_navigate_data.append(node)
                    break
          
            coordinates = []
            for n in (new_navigate_data):
                c = [float(n['lat']), float(n['lng'])]
                coordinates.append(c)

            return jsonify({
                'message': 'Building navigate successfully',
                'payload': {
                    "from_start": start_state,
                    "to_goal": bid_goal,
                    "distance": aco_navigation_path['distance'],
                    "best_path": new_best_path,
                    "navigation":new_navigate_data,
                    "coordinates": coordinates
                }
            }), HTTP_200_OK
        else:
            return jsonify({'message': 'bid_start or bid_goal is required'}), HTTP_400_BAD_REQUEST
    except BaseException as e:
        print(e)
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


@building_bp.post("/me/nearest")
def handle_find_nearest_building():
    payload = request.get_json()
    try:
        if 'current' in payload:
            current = payload['current']
            new_current = [decimal.Decimal(current[0]), decimal.Decimal(current[1])]
            raw_buildings = BuildingModel.query.all()
            buildings = []
            for each_building in range(len(raw_buildings)):
                buildings.append(raw_buildings[each_building].to_dict())

            # buildings = buildings
            # use aco to find best path
            aco_nearest = aco_shortest_path_geo(
                 buildings, new_current)
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
    
@building_bp.route("/get/all", methods=["GET"])
def handle_get_all_buildings():
    buildings = BuildingModel.query.all()
    data: list = []
    for building in buildings:
        data.append({
            'id': building.id,
            'name': building.name,
            'bid': building.bid,
            'image':building.image,
            'is_node': building.is_node,
            'desc': building.desc,
            'lat': building.lat,
            'lng': building.lng,
        })

    return jsonify({
        "msg": "get building successfully",
        "payload": data
    }), HTTP_200_OK

@building_bp.route("/get/<int:id>", methods=["GET"])
def handle_get_building_by_id(id: int):
    building = BuildingModel.query.filter_by(id=id).first()

    if building:
        data = {
            'id': building.id,
            'name': building.name,
            'bid': building.bid,
            'image': building.image,
            'is_node': building.is_node,
            'desc': building.desc,
            'lat': building.lat,
            'lng': building.lng,
        }

        return jsonify({
            "msg": "get building successfully",
            "payload": data
        }), HTTP_200_OK
    else:
        return jsonify({
            "msg": f"building with id {id} not found",
            "payload": {}
        }), HTTP_404_NOT_FOUND


@building_bp.route("/get/all/node", methods=["GET"])
def handle_get_node_buildings():
    buildings = BuildingModel.query.filter_by(is_node=True).all()
    data: list = []
    for building in buildings:
        data.append({
            'id': building.id,
            'name': building.name,
            'bid': building.bid,
            'image':building.image,
            'is_node': building.is_node,
            'desc': building.desc,
            'lat': building.lat,
            'lng': building.lng,
        })

    return jsonify({
        "msg": "get building successfully",
        "payload": data
    }), HTTP_200_OK


@building_bp.post("/create")
@jwt_required()
def handle_create_buildings():
    current_user_id = get_jwt_identity()
    user = UserModel.query.filter_by(id=current_user_id).first()

    if not user or not user.is_admin():
        return jsonify({'message': 'Forbidden'}), HTTP_403_FORBIDDEN
   
    payload = request.form

    if BuildingModel.query.filter_by(bid=request.form.get('bid')).first():
        return jsonify({'message': 'Building or that node is already exists'}), HTTP_409_CONFLICT

    try:
        # check if image is included in request files
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                # save the file to the server
                # filename = secure_filename(file.filename) 
                # unique_filename = f"{payload['bid']}_{filename}"
                unique_filename = secure_filename(str(payload['bid']) + '_' + file.filename)
                # filepath = os.path.join('public', 'upload', 'buildings', unique_filename)
                filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], 'buildings', unique_filename)
                file.save(filepath)
                image_filename = unique_filename
        else:
            image_filename = None

        building = BuildingModel(
            bid=payload.get('bid'),
            name=payload.get('name'),
            desc=payload.get('desc'),
            lat=payload.get('lat'),
            lng=payload.get('lng'),
            image=image_filename
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
        return jsonify({'message': 'create building was failed'}), HTTP_400_BAD_REQUEST


@building_bp.patch("/update/<int:building_id>")
@jwt_required()
def handle_update_building(building_id):
    current_user_id = get_jwt_identity()
    user = UserModel.query.filter_by(id=current_user_id).first()

    if not user or not user.is_admin():
        return jsonify({'message': 'Forbidden'}), HTTP_403_FORBIDDEN

    building = BuildingModel.query.filter_by(id=building_id).first()
    if not building:
        return jsonify({'message': 'Building not found'}), HTTP_404_NOT_FOUND
    payload = request.form
    try:
        if request.method == 'PATCH':
            if 'bid' in payload:
                building.bid = payload.get('bid')
            if 'name' in payload:
                building.name = payload.get('name')
            if 'desc' in payload:
                building.desc = payload.get('desc')
            if 'lat' in payload:
                building.lat = payload.get('lat')
            if 'is_node' in payload:
                if(payload.get('is_node') == 'true'):
                    building.is_node = True
                else:
                    building.is_node = False
            if 'lng' in payload:
                building.lng = payload.get('lng')
            if 'file' in request.files:
                file = request.files['file']
                if file.filename != '':
                    unique_filename = secure_filename(str(payload.get('bid')) + '_' + file.filename)
                    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], 'buildings', unique_filename)
                    try:
                        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], 'buildings', building.image))
                    except:
                        pass
                    file.save(filepath)
                    building.image = unique_filename
                else:
                    building.image = 'default.png'
        db.session.commit()
    except KeyError as e:
        key_error = ['bid', 'name', 'desc', 'lat', 'lng']
        if str(e)[1:-1] in key_error:
            return jsonify({'message': f'update building failed - {str(e)[1:-1]} key error'}), HTTP_400_BAD_REQUEST
        else:
            return jsonify({'message': 'update building failed - other key error'}), HTTP_400_BAD_REQUEST
    except BaseException as e:
        print(e)
        return jsonify({'message': 'update building failed'}), HTTP_400_BAD_REQUEST

    return jsonify({'message': 'Building updated successfully'}), HTTP_200_OK


@building_bp.delete("/delete/<int:building_id>")
@jwt_required()
def handle_delete_building(building_id):
    current_user_id = get_jwt_identity()
    user = UserModel.query.filter_by(id=current_user_id).first()
    if not user or not user.is_admin():
        return jsonify({'message': 'Forbidden'}), HTTP_403_FORBIDDEN

    building = BuildingModel.query.filter_by(id=building_id).first()
    try:
        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], 'buildings', building.image))
    except:
        pass
    if not building:
        return jsonify({'message': 'Building not found'}), HTTP_404_NOT_FOUND

    try:
        db.session.delete(building)
        db.session.commit()
        return jsonify({'message': 'Building deleted successfully'}), HTTP_200_OK
    except BaseException as e:
        return jsonify({'message': 'delete building failed'}), HTTP_400_BAD_REQUEST

    



@building_bp.route('/upload-image/<string:bid>', methods=['POST'])
def upload_image(bid):
    if 'image' not in request.files:
        return 'No file uploaded', 400

    file = request.files['image']
    if file.filename == '':
        return 'No file selected', 400

    # save the file to the server
    unique_filename = secure_filename(str(bid) + '_' + file.filename)
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], 'buildings', unique_filename)
    file.save(filepath)

    # update the BuildingModel record with the image filename
    building = BuildingModel.query.filter_by(bid=bid).first()
    if building:
        # delete old image if it exists
        try:
            os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], 'buildings', building.image))
        except Exception as e:
            print(f"Error deleting old image: {e}")
        building.image = unique_filename
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': f'Error updating database: {e}'}), HTTP_500_INTERNAL_SERVER_ERROR

    return  jsonify({'message': 'File uploaded successfully', 'payload': unique_filename}), HTTP_200_OK







