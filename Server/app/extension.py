from flasgger import Swagger
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

swag = Swagger()
db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()
