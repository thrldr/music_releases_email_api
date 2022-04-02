from flask_restful import Resource, reqparse
from database.initialize import db
from models.user import UserModel
from hashlib import md5


def make_parser() -> reqparse.RequestParser:
    parser = reqparse.RequestParser()
    arguments = ['username', 'password', 'email']

    for argument in arguments:
        parser.add_argument(argument,
                type=str,
                required=True,
                help=f"Field '{argument}' cannot be omitted."
            )
    return parser


class UserRegister(Resource):
    '''A resource that has a single endpoint responsible for registering a new user'''

    parser = make_parser()

    def post(self):
        data = UserRegister.parser.parse_args()
        hashed_password = md5(data['password'].encode()).hexdigest()

        new_user = UserModel(db,
                data['username'],
                hashed_password,
                data['email']
               ) 
        new_user.save_to_database()
        return {"message": "successfully registered"}


