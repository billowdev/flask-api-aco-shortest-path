from contextlib import suppress
import os
from flask import Flask, current_app, jsonify, render_template, send_from_directory
from .constatns.http_status_codes import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from .utils.password_hasher import password_hasher, verify_password
from .database.db_instance import db
from .database.seeders import building_seeder
from .modules.building_module import building_bp
from .modules.user_module import user_bp
from .config import common_config
from .database.seeders import seeders
from .database.seeders import production_seeder
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from os import path
from flask_cors import CORS
from sqlalchemy import text


def create_app():
    template_dir = path.dirname(path.abspath(path.dirname(__file__)))
    template_dir = path.join(template_dir, 'src', 'templates')

    app = Flask(__name__,instance_relative_config=True, template_folder = template_dir)

    # set up database URI based on the environment
    if app.config['ENV'] == 'development':
        app.config.from_mapping(
            UPLOAD_FOLDER= common_config.UPLOAD_FOLDER,
            SECRET_KEY=common_config.SECRET_KEY,
            SQLALCHEMY_DATABASE_URI=common_config.SQLALCHEMY_DB_URI_DEV,
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=common_config.JWT_SECRET_KEY
        )
    elif app.config['ENV'] == 'production':
        app.config.from_mapping(
            UPLOAD_FOLDER= common_config.UPLOAD_FOLDER,
            SECRET_KEY=common_config.SECRET_KEY,
            SQLALCHEMY_DATABASE_URI=common_config.SQLALCHEMY_DB_URI_PROD,
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=common_config.JWT_SECRET_KEY
        )
    elif app.config['ENV'] == 'testing':
        app.config.from_mapping(
            UPLOAD_FOLDER= common_config.UPLOAD_FOLDER,
            SECRET_KEY=common_config.SECRET_KEY,
            SQLALCHEMY_DATABASE_URI=common_config.SQLALCHEMY_DB_URI_TEST,
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=common_config.JWT_SECRET_KEY
        )
    else:
        raise ValueError(f"Unknown environment: {app.config['ENV']}")
    # ensure the instance folder exists
    
    db.app = app
    db.init_app(app)
    JWTManager(app)
    
    app.register_blueprint(building_bp)
    app.register_blueprint(user_bp)

    Mail().init_app(app)
    app.config.from_mapping(
            MAIL_SERVER=common_config.MAIL_SERVER,
            MAIL_PORT=common_config.MAIL_PORT,
            MAIL_USE_TLS=common_config.MAIL_USE_TLS,
            MAIL_USERNAME=common_config.MAIL_USERNAME,
            MAIL_PASSWORD=common_config.MAIL_PASSWORD,
            MAIL_DEFAULT_SENDER=common_config.MAIL_DEFAULT_SENDER,
    )

    CORS(app, resources={r"/api/v1/*": {"origins": "http://localhost:3000"}})

    # create database tables
    with app.app_context():
        if app.config['ENV'] == 'development':
            db.session.execute(text('DROP SCHEMA public CASCADE;'))
            db.session.execute(text('CREATE SCHEMA public;'))
            db.session.commit()
            print('Dropped all tables was successfully!')
            db.create_all()
            print('Created all tables was successfully!')
            with suppress(BaseException):
                seeders.run_seed()
        elif app.config['ENV'] == 'testing' and not app.testing:
            raise ValueError(
                "Testing database can only be created when app is testing")
        elif app.config['ENV'] == 'production':
            db.create_all()
            # seed the building table
            ## run in first time for create simulate or seeder data
            # with suppress(BaseException):
            #     production_seeder.run_seed()

            
    # @app.get("/")
    # def say_hello():
    #     return {"message": "Hello World", "test": app.config['ENV']}

    @app.get("/")
    def test_template():
        return render_template('index.html')
    
    @app.get("/login")
    def login():
        return render_template('login.html')

    @app.get('/buildings/images/<filename>')
    def get_building_image(filename):
        try:
            print( current_app.config['UPLOAD_FOLDER'])
            path = os.path.join(os.getcwd(), current_app.config['UPLOAD_FOLDER'], 'buildings')        
            return send_from_directory(path, filename)
        except FileNotFoundError:
            return jsonify({'message': 'File not found'}), HTTP_404_NOT_FOUND
        except Exception as e:
            return jsonify({'message': f'Error: {e}'}), HTTP_500_INTERNAL_SERVER_ERROR


    return app
