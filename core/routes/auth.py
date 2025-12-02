from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import unset_jwt_cookies
from flask import request, current_app, jsonify

auth_ns = Namespace('Auth', description='Authentication and authorization operations')

# Request models
register_model = auth_ns.model('Register', {
    'username': fields.String(required=True, description='The username (must be unique)', min_length=3, max_length=50, example='john_doe'),
    'password': fields.String(required=True, description='The user password (min 6 characters)', min_length=6, example='SecurePass123!'),
    'email': fields.String(required=True, description='The user email address', example='john.doe@example.com')
})

login_model = auth_ns.model('Login', {
    'username': fields.String(required=True, description='The username', example='john_doe'),
    'password': fields.String(required=True, description='The user password', example='SecurePass123!')
})

# Response models
token_response_model = auth_ns.model('TokenResponse', {
    'access_token': fields.String(description='JWT access token', example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...')
})

success_message_model = auth_ns.model('SuccessMessage', {
    'message': fields.String(description='Success message', example='User registered successfully')
})

error_response_model = auth_ns.model('ErrorResponse', {
    'message': fields.String(description='Error message', example='Invalid credentials'),
    'success': fields.Boolean(description='Operation success status', example=False)
})

@auth_ns.route('/login')
class AuthLogin(Resource):
    @auth_ns.doc(
        description='Authenticate user and receive JWT access token',
        responses={
            200: ('Success - Returns JWT token', token_response_model),
            401: ('Unauthorized - Invalid credentials', error_response_model),
            400: ('Bad Request - Missing fields', error_response_model),
            500: 'Internal Server Error'
        }
    )
    @auth_ns.expect(login_model, validate=True)
    @auth_ns.marshal_with(token_response_model, code=200)
    def post(self):
        """Login and get JWT token"""
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        
        if not username or not password:
            auth_ns.abort(400, message="Username and password are required")
        
        result = current_app.user_service.login_user(username, password)

        if result["success"]:
            return {"access_token": result["access_token"]}, 200

        auth_ns.abort(401, message=result.get("message", "Invalid credentials"))

@auth_ns.route('/register')
class AuthRegister(Resource):
    @auth_ns.doc(
        description='Register a new user account',
        responses={
            201: ('Created - User registered successfully', success_message_model),
            400: ('Bad Request - Validation error or user already exists', error_response_model),
            500: 'Internal Server Error'
        }
    )
    @auth_ns.expect(register_model, validate=True)
    @auth_ns.marshal_with(success_message_model, code=201)
    def post(self):
        """Register a new user"""
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        
        if not username or not password or not email:
            auth_ns.abort(400, message="Username, password, and email are required")
        
        if len(password) < 6:
            auth_ns.abort(400, message="Password must be at least 6 characters long")
        
        result = current_app.user_service.register_user(username, password, email)

        if result["success"]:
            return {"message": "User registered successfully"}, 201

        auth_ns.abort(400, message=result.get("message", "Registration failed"))

@auth_ns.route('/logout')
class AuthLogout(Resource):
    @auth_ns.doc(
        description='Logout user and clear JWT cookies',
        responses={
            200: ('Success - Logout successful', success_message_model),
            400: ('Bad Request - Logout failed', error_response_model),
            500: 'Internal Server Error'
        }
    )
    @auth_ns.marshal_with(success_message_model)
    def post(self):
        """Logout user"""
        response = jsonify(message="Logout successful")
        result = current_app.user_service.logout_user()

        if result["success"]:
            unset_jwt_cookies(response)
            response.status_code = 200
            return response

        auth_ns.abort(400, message=result.get("message", "Logout failed"))