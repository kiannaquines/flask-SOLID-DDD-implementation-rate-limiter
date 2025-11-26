from flask import Flask
from .config.extension import db, migrate, limiter, jwt
from .config import DevelopmentConfig
from .routes.main import main_ns
from .routes.auth import auth_ns
from .routes.task import task_ns
from .infrastructure.di_binder import bind_task_repository, bind_user_repository
from .application.task.task_service import TaskService
from .application.user.user_service import UserService
from flask_restx import Api

api = Api(
    version="1.0.0",
    title="Task Management API",
    description="A python flask task management API",
    contact="Support Team",
    contact_email="kjgnaquines@gmail.com"
)

def create_app(config=DevelopmentConfig):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config or DevelopmentConfig)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    api.init_app(app)
    limiter.init_app(app)
    task_repo = bind_task_repository()
    user_repo = bind_user_repository()
    task_service = TaskService(task_repo)
    user_service = UserService(user_repo)
    app.task_service = task_service
    app.user_service = user_service

    from .domain.task import Task
    from .domain.user import User

    api.add_namespace(main_ns,path="/")
    api.add_namespace(auth_ns, path="/auth")
    api.add_namespace(task_ns, path="/tasks")

    return app
