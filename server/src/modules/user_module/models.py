from flask_sqlalchemy import SQLAlchemy
import datetime
from src.database.db_instance import db

class UserModel(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	# roles = db.Column(db.Enum(RolesEnum), default=RolesEnum.user)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now())
	updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())
	
	def __repr__(self):
		return '<UserModel {}>'.format(self.username)

	def to_dict(self):
		return {
			'id': self.id,
			'username': self.username,
			'email': self.email,
		}
