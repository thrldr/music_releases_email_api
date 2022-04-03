from flask_restful import Resource
from models.user import UserModel
from database.initialize import db
from flask_jwt_extended import jwt_required, get_jwt_identity


class ActivateNotifications(Resource):
    '''A resource that activates email notifications'''
    
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()
        user_data = db.find_by_value('users', 'email', identity)
        user = UserModel(db, *user_data[1:])
        user.activate()
        return {"Message": "Successfully activated"}

