# define your seeder function
from src import db
from src.modules.user_module.models import UserModel
from src.utils.password_hasher import password_hasher
from datetime import datetime

seeder_pass = password_hasher("test1234")

def seed():
    users = [
        {
            'username': 'alice',
            'email': 'alice@gmail.com',
            'password_hash': seeder_pass,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            'username': 'bob',
            'email': 'bob@gmail.com',
            'password_hash': seeder_pass,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            'username': 'john',
            'email': 'john@gmail.com',
            'password_hash': seeder_pass,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
    ]
    for user in users:
        db.session.add(UserModel(**user))
    db.session.commit()
