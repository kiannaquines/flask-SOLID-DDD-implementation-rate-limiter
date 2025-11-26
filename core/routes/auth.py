from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import get_jwt_identity, jwt_required, unset_jwt_cookies
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
class AuthLogin(Resource):
    @jwt_required(optional=True)
    @auth_ns.expect(login_model)
    def post(self):
        credentials = request.get_json()
        username = credentials.get('username')
        password = credentials.get('password')
        access_token = current_app.user_service.login_user(username, password)

        if access_token:
            return jsonify(access_token=access_token), 200
        
        return jsonify(message="Invalid credentials"), 401

@auth_ns.route('/register')
class AuthRegister(Resource):
    @auth_ns.expect(register_model)
    def post(self):
        credentials = request.get_json()
        username = credentials.get('username')
        password = credentials.get('password')
        email = credentials.get('email')
        register = current_app.user_service.register_user(username, password, email)
        if register:
            return jsonify(message="User registered successfully"), 201
        return jsonify(message="Registration failed"), 400

@auth_ns.route('/logout')
class AuthLogout(Resource):
    def post(self):
        response = jsonify(message="Logout successful")
        current_app.user_service.logout_user(response=response)
        return response, 200
    
@auth_ns.route('/dashboard')
class AuthDashboard(Resource):
    @jwt_required()
    def get(self):
        key = get_jwt_identity()
        return jsonify(message="Protected dashboard endpoint", jwt=key)