from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import unset_jwt_cookies
from flask import request, current_app, jsonify

auth_ns = Namespace('Auth', description='Authentication related operations')

register_model = auth_ns.model('Auth', {
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The user password'),
    'email': fields.String(description='The user email (for registration)')
})

login_model = auth_ns.model('Login', {
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The user password')
})

@auth_ns.route('/login')
@auth_ns.doc(security=[])
class AuthLogin(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        data = request.get_json()
        result = current_app.user_service.login_user(
            data.get("username"),
            data.get("password")
        )

        if result["success"]:
            return {"access_token": result["access_token"]}, 200

        return result, 401

@auth_ns.route('/register')
@auth_ns.doc(security=[])
class AuthRegister(Resource):
    @auth_ns.expect(register_model)
    def post(self):
        data = request.get_json()
        result = current_app.user_service.register_user(
            data.get("username"), data.get("password"), data.get("email")
        )

        if result["success"]:
            return {"message": "User registered successfully"}, 201

        return result, 400

@auth_ns.route('/logout')
class AuthLogout(Resource):
    def post(self):
        response = jsonify(message="Logout successful")
        result = current_app.user_service.logout_user()

        if result["success"]:
            unset_jwt_cookies(response)
            response.status_code = 200
            return response

        return result, 400