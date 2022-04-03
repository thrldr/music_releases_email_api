from flask_restful import Resource
from resources.parser import make_parser
from database.initialize import db
from models.user import UserModel
from hashlib import md5


class UserRegister(Resource):
    '''A resource that has a single endpoint responsible for registering a new user'''

    parser = make_parser(['password', 'email'])

    def post(self):
        data = UserRegister.parser.parse_args()
        hashed_password = md5(data['password'].encode()).hexdigest()

        new_user = UserModel(
                db,
                hashed_password,
                data['email'],
                False
               ) 

        new_user.save_to_database()
        return {"message": "successfully registered"}, 201


