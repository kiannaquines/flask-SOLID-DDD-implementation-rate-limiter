from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity

dashboard_ns = Namespace('Dashboard', description='Dashboard and system information')

# Response models
dashboard_response_model = dashboard_ns.model('DashboardResponse', {
    'message': fields.String(description='Welcome message', example='Welcome to the Task Management System!'),
    'user': fields.String(description='Current authenticated user', example='john_doe'),
    'version': fields.String(description='API version', example='1.0.0'),
    'endpoints': fields.Raw(description='Available API endpoints')
})

@dashboard_ns.route('')
@dashboard_ns.doc(security='Bearer Auth')
class Dashboard(Resource):
    @jwt_required()
    @dashboard_ns.doc(
        description='Get dashboard information and API overview',
        responses={
            200: ('Success', dashboard_response_model),
            401: 'Unauthorized - Invalid or missing token',
            500: 'Internal Server Error'
        }
    )
    @dashboard_ns.marshal_with(dashboard_response_model)
    def get(self):
        """Get dashboard information"""
        current_user = get_jwt_identity()
        return {
            "message": "Welcome to the Task Management System!",
            "user": current_user,
            "version": "1.0.0",
            "endpoints": {
                "auth": "/api/v1/auth",
                "tasks": "/api/v1/tasks",
                "dashboard": "/api/v1/dashboard",
                "documentation": "/api/v1/docs"
            }
        }