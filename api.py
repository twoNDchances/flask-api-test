from flask_restful import Resource, Api as API, reqparse
from config import app, db
from datatable import User
from flask import request, Blueprint


api = API(app=app)

apiview = Blueprint(name='api', import_name=__name__)

class UserResource(Resource):
    def get(self):
        return [user.json() for user in User.query.all()]
    
    def post(self):
        json_data = request.get_json()
        db.session.add(User(name=json_data['name'], age=json_data['age']))
        db.session.commit()
        return json_data

api.add_resource(UserResource, '/api')