from .task.task_repository import TaskRepository
from ..config.extension import db

def bind_task_repository():
    return TaskRepository()