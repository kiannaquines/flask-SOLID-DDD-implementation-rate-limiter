from abc import ABC, abstractmethod

class TaskRepositoryInterface(ABC):
    @abstractmethod
    def create_task(self, task):
        pass

    @abstractmethod
    def get_one_task(self, task_id):
        pass

    @abstractmethod
    def list_task(self):
        pass

    @abstractmethod
    def update_task(self, task_id, title=None, description=None, is_completed=None):
        pass

    @abstractmethod
    def delete_task(self, task):
        pass 