from sqlite3 import IntegrityError
from flask import jsonify, request, current_app, url_for
from src.constatns.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from src.utils.password_hasher import password_hasher, verify_password
from . import user_bp
from src.modules.user_module.models import UserModel
from src.database.db_instance import db
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token, create_refresh_token
from flask_mail import Message, Mail


@user_bp.route('/users', methods=['GET'])
def get_users():
    users = UserModel.query.all()
    return jsonify({'users': [user.to_dict() for user in users]})


def send_reset_email(user, reset_token):
    """
    Send a password reset email to the user with a reset link containing a reset token.

    :param user: The user object to send the email to.
    :param reset_token: The reset token to include in the reset link.
    """
    # Generate the reset link using the reset token
    reset_link = url_for('user_bp.reset_password', reset_token=reset_token, _external=True)

    # Create the message body
    message_body = f"""
        Hello {user.username},

        You are receiving this email because you have requested to reset your password. Please follow the link below to reset your password:

        {reset_link}

        If you did not request this password reset, please ignore this email and your password will remain unchanged.

        Best regards,
        Your App Team
    """

    # Create and send the email message
    message = Message(subject='Password Reset Request', recipients=[user.email], body=message_body)
    Mail.send(message)

@user_bp.post('/login')
def login():
    email, username, password = "", "", ""

    if request.is_json:
        email: str = request.json.get('email', '')
        username: str = request.json.get('username', '')
        password: str = request.json.get('password', '')
    else:
        email: str = request.form.get('email', '')
        username: str = request.form.get('username', '')
        password: str = request.form.get('password', '')
    
    user: UserModel = {}
    if(email):
        user: UserModel = UserModel.query.filter_by(email=email).first()
    else:
        user: UserModel = UserModel.query.filter_by(username=username).first()

    if user:
        is_pass_correct = verify_password(user.hash_password, password)
        if is_pass_correct:
            refresh_token: str = create_refresh_token(
                identity=user.id, 
                additional_claims={'role': user.role.value}
                )
            access_token: str = create_access_token(identity=user.id, additional_claims={'role': user.role.value})

            return jsonify({
                'user': {
                    'refresh_token': refresh_token,
                    'access_token': access_token,
                    'username': user.username,
                    'email': user.email,
                    'role':user.role.value
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



@user_bp.route('/create', methods=['POST'])
@jwt_required()
def handle_create_user():
    current_user_id = get_jwt_identity()
    current_user = UserModel.query.get(current_user_id)

    if not current_user or not current_user.is_admin():
        return jsonify({'message': 'Forbidden'}), HTTP_403_FORBIDDEN

    try:
        data = request.get_json()
        hashing = password_hasher(data['password'])
        new_user = UserModel(username=data['username'], email=data['email'], hash_password=hashing, role=data['role'])
        db.session.add(new_user)
        db.session.commit()
    except KeyError as e:
        return jsonify({'message': f'create user failed due to missing {e} key'}), HTTP_400_BAD_REQUEST
    except IntegrityError:
        return jsonify({'message': f'create user failed due to duplicate email or username'}), HTTP_400_BAD_REQUEST
    except Exception:
        return jsonify({'message': 'create user failed'}), HTTP_500_INTERNAL_SERVER_ERROR

    return jsonify({'message': 'User created successfully'}), HTTP_201_CREATED

@user_bp.patch('/update/<int:user_id>')
@jwt_required()
def handle_update_user(user_id):
    current_user_id = get_jwt_identity()
    current_user = UserModel.query.get(current_user_id)
    user_to_update = UserModel.query.get(user_id)

    if not current_user or not current_user.is_admin():
        return jsonify({'message': 'Forbidden'}), HTTP_403_FORBIDDEN

    if not user_to_update:
        return jsonify({'message': 'User not found'}), HTTP_404_NOT_FOUND

    try:
        data = request.get_json()
        if 'username' in data:
            user_to_update.username = data['username']
        if 'email' in data:
            user_to_update.email = data['email']
        if 'role' in data:
            user_to_update.role = data['role']
        db.session.commit()
    except KeyError as e:
        return jsonify({'message': f'update user failed due to missing {e} key'}), HTTP_400_BAD_REQUEST
    except IntegrityError:
        return jsonify({'message': f'update user failed due to duplicate email or username'}), HTTP_400_BAD_REQUEST
    except Exception:
        return jsonify({'message': 'update user failed'}), HTTP_500_INTERNAL_SERVER_ERROR

    return jsonify({'message': 'User updated successfully'}), HTTP_200_OK


@user_bp.patch('/update_password/<int:user_id>')
@jwt_required()
def handle_update_password(user_id):
    current_user_id = get_jwt_identity()
    current_user = UserModel.query.get(current_user_id)
    user_to_update = UserModel.query.get(user_id)

    if not current_user or current_user.id != user_id:
        return jsonify({'message': 'Forbidden'}), HTTP_403_FORBIDDEN

    if not user_to_update:
        return jsonify({'message': 'User not found'}), HTTP_404_NOT_FOUND

    try:
        data = request.get_json()
        old_password = data.get('old_password')
        new_password = data.get('new_password')

        if not old_password or not new_password:
            return jsonify({'message': 'Both old and new passwords are required'}), HTTP_400_BAD_REQUEST

        if not user_to_update.check_password(old_password):
            return jsonify({'message': 'Invalid old password'}), HTTP_401_UNAUTHORIZED

        user_to_update.set_password(new_password)
        db.session.commit()
    except Exception:
        return jsonify({'message': 'Update password failed'}), HTTP_500_INTERNAL_SERVER_ERROR

    return jsonify({'message': 'Password updated successfully'}), HTTP_200_OK

@user_bp.post('/forgot_password')
def handle_forgot_password():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'message': 'Email address is required'}), HTTP_400_BAD_REQUEST

    user = UserModel.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'User not found'}), HTTP_404_NOT_FOUND

    # Generate a reset token with a short expiration time (e.g., 10 minutes)
    reset_token = user.get_reset_token(expiration=600)

    # Send an email to the user with a link to the password reset page
    # You can use any email service of your choice here
    # send_reset_email(user, reset_token)

    return jsonify({'message': 'Password reset email sent successfully'}), HTTP_200_OK

@user_bp.post('/reset_password')
def handle_reset_password():
    data = request.get_json()
    reset_token = data.get('reset_token')
    new_password = data.get('new_password')

    if not reset_token or not new_password:
        return jsonify({'message': 'Reset token and new password are required'}), HTTP_400_BAD_REQUEST

    user = UserModel.verify_reset_token(reset_token)

    if not user:
        return jsonify({'message': 'Invalid or expired reset token'}), HTTP_400_BAD_REQUEST

    # Set the user's new password
    user.set_password(new_password)

    # Clear the reset token and expiration time
    user.reset_token = None
    user.reset_token_expiration = None

    # Commit the changes to the database
    db.session.commit()

    return jsonify({'message': 'Password reset successful'}), HTTP_200_OK


@user_bp.route('/delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
def handle_delete_user(user_id):
    current_user_id = get_jwt_identity()
    current_user = UserModel.query.get(current_user_id)
    user_to_delete = UserModel.query.get(user_id)

    if not current_user or not current_user.is_admin():
        return jsonify({'message': 'Forbidden'}), HTTP_403_FORBIDDEN

    if not user_to_delete:
        return jsonify({'message': 'User not found'}), HTTP_404_NOT_FOUND
    
    if user_to_delete.id == current_user.id:
        return jsonify({'message': 'Admin cannot delete their own account'}), HTTP_403_FORBIDDEN
    
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return jsonify({'message': 'delete user successfully'}), HTTP_200_OK
    except Exception:
        return jsonify({'message': 'delete user failed'}), HTTP_500_INTERNAL_SERVER_ERROR
    
    
    