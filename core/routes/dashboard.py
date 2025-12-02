from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required

dashboard_ns = Namespace('Dashboard', description='Dashboard operations')

@dashboard_ns.route('')
@dashboard_ns.doc(security='Bearer Auth')
class Dashboard(Resource):
    @jwt_required()
    def get(self):
        return "Welcome to the Task Management System!"