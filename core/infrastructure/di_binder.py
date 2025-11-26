from .task.task_repository import TaskRepository
from .user.user_repository import UserRepository

def bind_task_repository():
    return TaskRepository()

def bind_user_repository():
    return UserRepository()