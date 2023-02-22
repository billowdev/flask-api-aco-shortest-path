from flask import Flask
import os
from src.constatns.common_constant import ENDPOINT
from src.database.database import db
from src.services.buildings import buildings

def create_app(test_config=None):
	app = Flask(__name__,
				instance_relative_config=True)
	if test_config is None:
		app.config.from_mapping(
			# SECRET_KEY=os.environ.get("SECRET_KEY"),
			SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
			SQLALCHEMY_TRACK_MODIFICATIONS=False,
			# JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
		)
	else:
		app.config.from_mapping(test_config)
	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	db.app = app
	db.init_app(app)
	
	app.register_blueprint(buildings)
 
	# @app.get(f"{ENDPOINT}/hello")
	# def say_hello():
	# 	return {"message": "Hello World"}

	return app


	
	