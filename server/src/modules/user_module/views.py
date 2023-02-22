from flask import jsonify, request, current_app
from src.constatns.http_status_codes import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from src.utils.password_hasher import verify_password
from . import user_bp
from src.modules.user_module.models import UserModel
from src.database.db_instance import db
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token, create_refresh_token


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

# ============================================================
# ====================== AUTHENTICATION ======================
# ==========================================================
# ==


@user_bp.post('/login')
def login():
    email: str = request.json.get('email', '')
    username: str = request.json.get('username', '')
    password: str = request.json.get('password', '')
    user: UserModel = {}
    if(email):
        user: UserModel = UserModel.query.filter_by(email=email).first()
    else:
        user: UserModel = UserModel.query.filter_by(username=username).first()

    if user:
        is_pass_correct = verify_password(user.password_hash, password)
        if is_pass_correct:
            refresh_token: str = create_access_token(identity=user.id)
            access_token: str = create_access_token(identity=user.id)

            return jsonify({
                'user': {
                    'refresh_token': refresh_token,
                    'access_token': access_token,
                    'username': user.username,
                    'email': user.email
                }
            }), HTTP_200_OK
    return jsonify({
        'error': 'Wrrong credential'
    }), HTTP_401_UNAUTHORIZED


@user_bp.get("/me")
@jwt_required()
def me():
    user_id: str = get_jwt_identity()
    user: UserModel = UserModel.query.filter_by(id=user_id).first()

    return jsonify({
        'username': user.username,
        'email': user.email
    }), HTTP_200_OK
