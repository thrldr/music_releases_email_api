from flask_restful import Resource
from models.user import UserModel
from resources.parser import make_parser
from hashlib import md5
from database.initialize import db

from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


class GetStatus(Resource):
    '''A resource responsible for authentication'''
    
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()
        return db.find_by_value('users', 'email', identity)[-1]

