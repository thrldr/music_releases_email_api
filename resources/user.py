from flask_restful import Resource, reqparse
from models.user import User
from hashlib import md5


def make_parser() -> reqparse.RequestParser:
    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type=str,
            required=True,
            help="This field cannot be omitted."
            )
    parser.add_argument('password',
            type=str,
            required=True,
            help="This field cannot be omitted."
            )
    parser.add_argument('email',
            type=str,
            required=True,
            help="This field cannot be omitted."
            )
    return parser


class UserRegister(Resource):
    '''A resource that has a single endpoint responsible for registering a new user'''

    parser = make_parser()
    def post(self):
        data = UserRegister.parser.parse_args()

        hashed_password = md5(data['password'].encode()).hexdigest()
        new_user = User(data['username'], hashed_password, data['email']) 
        new_user.save_to_database()


