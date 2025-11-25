from ...infrastructure.task.task_interface import TaskRepositoryInterface
from ...application.task.task_service_interface import TaskServiceInterface
from ...domain.task import Task

class TaskService(TaskServiceInterface):
    def __init__(self, task_repository: TaskRepositoryInterface):
        self.task_repository = task_repository
    
    def create_task(self, title, description=None):
        task = Task(title, description)
        self.task_repository.create_task(task)
        return task
    
    def get_one_task(self, task_id):
        return self.task_repository.get_one_task(task_id)
    
    def list_task(self):
        return self.task_repository.list_task()
    
    def update_task(self, task_id, title=None, description=None, is_completed=None):
        return self.task_repository.update_task(task_id, title, description, is_completed)
    
    def delete_task(self, task):
        return self.task_repository.delete_task(task)