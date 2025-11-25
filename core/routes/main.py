from flask_restx import Namespace, Resource

main_ns = Namespace('Main', description='Main operations')

@main_ns.route('')
class Main(Resource):
    def get(self):
        return "Welcome to the Task Management System!"