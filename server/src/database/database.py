from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

# class RolesEnum(db.Enum):
#     admin = "ADMIN"
#     user = "USER"
    

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    # roles = db.Column(db.Enum(RolesEnum), default=RolesEnum.user)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())
    
    def __repr__(self) -> str:
        return 'User>> {self.username}'

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.Text, nullable=False)
    desc =  db.Column(db.Text, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    
    def __repr__(self) -> str:
        return 'Building>>> {self.name}'
    