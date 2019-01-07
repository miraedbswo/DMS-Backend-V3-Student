from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

swag = Swagger()
db = SQLAlchemy()
jwt = JWTManager()