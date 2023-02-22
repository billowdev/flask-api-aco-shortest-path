# define your seeder function
from src import db
from src.modules.user_module.models import RolesEnum, UserModel
from src.utils.password_hasher import password_hasher
from datetime import datetime

seeder_pass = password_hasher("test1234")


def seed():
    users = [
        {
            'username': 'alice',
            'email': 'alice@gmail.com',
            'role': RolesEnum.USER,
            'hash_password': seeder_pass,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            'username': 'bob',
            'email': 'bob@gmail.com',
            'role': RolesEnum.USER,
            'hash_password': seeder_pass,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            'username': 'john',
            'email': 'john@gmail.com',
            'role': RolesEnum.ADMIN,
            'hash_password': seeder_pass,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
    ]
    for user in users:
        db.session.add(UserModel(**user))
    db.session.commit()
