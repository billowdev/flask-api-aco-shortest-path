from os import environ
SECRET_KEY = environ.get("SECRET_KEY")
SQLALCHEMY_DB_URI_DEV = environ.get("SQLALCHEMY_DB_URI_DEV")
SQLALCHEMY_DB_URI_PROD = environ.get("SQLALCHEMY_DB_URI_PROD")
SQLALCHEMY_DB_URI_TEST = environ.get("SQLALCHEMY_DB_URI_TEST")
JWT_SECRET_KEY= environ.get('JWT_SECRET_KEY')


MAIL_SERVER = environ.get("MAIL_SERVER")
MAIL_PORT = environ.get("MAIL_PORT")
MAIL_USE_TLS = environ.get("MAIL_USE_TLS").lower() in ('true', '1', 'yes')
MAIL_USERNAME = environ.get("MAIL_USERNAME")
MAIL_PASSWORD = environ.get("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = environ.get("MAIL_DEFAULT_SENDER")