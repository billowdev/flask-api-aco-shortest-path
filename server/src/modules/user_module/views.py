from flask import jsonify, request, current_app
from . import user_bp
from src.modules.user_module.models import UserModel
from src.database.db_instance import db


@user_bp.route('/users', methods=['GET'])
def get_users():
    users = UserModel.query.all()
    return jsonify({'users': [user.to_dict() for user in users]})

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    user = UserModel(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'user': user.to_dict()})
