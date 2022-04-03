from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.status import GetStatus
from resources.register import UserRegister
from resources.login import UserLogin
from resources.activate import ActivateNotifications
from os import getenv


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = getenv("SECRET_KEY")

jwt = JWTManager(app)
api = Api(app)

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(GetStatus, '/status')
api.add_resource(ActivateNotifications, '/activate')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
