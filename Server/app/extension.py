from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

swag = Swagger()
db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()
