from flask_restx import Namespace, Resource

auth_ns = Namespace('Auth', description='Authentication related operations')

@auth_ns.route('/login')
class AuthLogin(Resource):
    def post(self):
        return {"message": "Login endpoint"}

@auth_ns.route('/register')
class AuthRegister(Resource):
    def post(self):
        return {"message": "Register endpoint"}

@auth_ns.route('/logout')
class AuthLogout(Resource):
    def post(self):
        return {"message": "Logout endpoint"}