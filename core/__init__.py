from flask import Flask, request

from .config.extension import db, migrate, limiter, jwt
from .config import ProductionConfig, DevelopmentConfig
from .routes.dashboard import dashboard_ns
from .routes.auth import auth_ns
from .routes.task import task_ns
from .infrastructure.di_binder import bind_task_repository, bind_user_repository
from .application.task.task_service import TaskService
from .application.user.user_service import UserService
from flask_restx import Api

authorizations = {
    "Bearer Auth": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "description": '''JWT Authorization header using the Bearer scheme.
        
**Format:** `Bearer <your_jwt_token>`

**Example:** `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`

**Important:** 
- You must include the word "Bearer" followed by a space before your token
- Click "Authorize" button above and enter: `Bearer <token>`
- Or in curl: `-H "Authorization: Bearer <token>"`
        ''',
    }
}

api = Api(
    version="1.0.0",
    title="Task Management API",
    description="""## A comprehensive Task Management REST API built with Flask
    
### Features:
- **Authentication**: Secure JWT-based authentication
- **Task Management**: Full CRUD operations for tasks
- **Rate Limiting**: Built-in API rate limiting for security
- **Clean Architecture**: Implements SOLID principles and DDD patterns

### Getting Started:
1. Register a new user via `/api/v1/auth/register`
2. Login to get your JWT token via `/api/v1/auth/login`
3. Use the token in the Authorization header for protected endpoints
4. Click the 'Authorize' button above to set your token for testing

### Support:
For issues or questions, contact: kjgnaquines@gmail.com
    """,
    contact="Support Team",
    contact_email="kjgnaquines@gmail.com",
    contact_url="https://github.com/kiannaquines/flask-SOLID-DDD-implementation-rate-limiter",
    license="MIT",
    license_url="https://opensource.org/licenses/MIT",
    authorizations=authorizations,
    security="Bearer Auth",
    prefix="/api/v1",
    doc="/docs",
    ordered=True,
    validate=True
)

def create_app(config=ProductionConfig):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config or DevelopmentConfig)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    api.init_app(app)
    limiter.init_app(app)
    # Dependency Injection
    task_repo = bind_task_repository()
    user_repo = bind_user_repository()

    # Create service instances
    task_service = TaskService(task_repo)
    user_service = UserService(user_repo)

    # Attach services to app for global access
    app.task_service = task_service
    app.user_service = user_service

    # Import models to register with SQLAlchemy
    from .domain.task import Task
    from .domain.user import User

    # Register namespaces
    api.add_namespace(dashboard_ns, path="/dashboard")
    api.add_namespace(auth_ns, path="/auth")
    api.add_namespace(task_ns, path="/tasks")

    # JWT error handlers
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return {
            "message": "The token has expired. Please login again to get a new token.",
            "error": "token_expired"
        }, 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return {
            "message": "Invalid token format. Use 'Authorization: Bearer <your_token>'",
            "error": "invalid_token",
            "hint": "Make sure to include 'Bearer ' before your token"
        }, 401

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return {
            "message": "Authorization header is missing. Please provide a valid JWT token.",
            "error": "authorization_required",
            "hint": "Use 'Authorization: Bearer <your_token>' in the request header"
        }, 401

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return {
            "message": "The token has been revoked. Please login again.",
            "error": "token_revoked"
        }, 401

    # Health check endpoint for monitoring
    @app.route('/health')
    def health_check():
        return {
            'status': 'healthy',
            'service': 'task-management-api',
            'version': '1.0.0'
        }, 200

    @app.route('/')
    def root():
        return {
            'message': 'Task Management API',
            'version': '1.0.0',
            'documentation': '/api/v1/docs',
            'endpoints': {
                'auth': '/api/v1/auth',
                'tasks': '/api/v1/tasks',
                'dashboard': '/api/v1/dashboard'
            }
        }, 200

    return app
