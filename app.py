from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from os import getenv


app = Flask(__name__)
app.secret_key = getenv("secret_key")
jwt = JWT(app, authenticate, identity)

api = Api(app)
api.add_resource(UserRegister, '/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
