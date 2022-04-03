from flask_restful import Resource
from models.user import UserModel
from resources.parser import make_parser
from hashlib import md5
from database.initialize import db

from flask_jwt_extended import create_access_token


class UserLogin(Resource):
    '''A resource responsible for authentication'''
    
    parser = make_parser(['password', 'email'])

    def post(self):
        data = UserLogin.parser.parse_args()
        hashed_password = md5(data['password'].encode()).hexdigest()

        possible_user = UserModel(
                db,
                hashed_password,
                data['email']
            )
        
        if possible_user.in_database():
            token = create_access_token(identity=data['email'])
            return {"JWT": token}
        else:
            return {"message": "No user found"}, 401

