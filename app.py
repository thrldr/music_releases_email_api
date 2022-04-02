from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from os import getenv

from database.database import DBManager
from models.user import User
# from security import authenticate, identity
from resources.user import UserRegister
from config.db import connection_data


app = Flask(__name__)
# app.secret_key = getenv("secret_key")
# jwt = JWT(app, authenticate, identity)

api = Api(app)
api.add_resource(UserRegister, '/')

db = DBManager(connection_data) 

if __name__ == '__main__':
    app.run(port=5000, debug=True)
