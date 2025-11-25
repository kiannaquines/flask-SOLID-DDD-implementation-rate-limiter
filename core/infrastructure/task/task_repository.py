from ...config.extension import db
from ...domain.task import Task
from ...infrastructure.task.task_interface import TaskRepositoryInterface

class TaskRepository(TaskRepositoryInterface):  
    def create_task(self, task):
        with db.session.begin():
            db.session.add(task)
    
    def get_one_task(self, task_id):
        return db.session.query(Task).filter_by(id=task_id).first()

    def list_task(self):
        return db.session.query(Task).all()
    
    def update_task(self, task_id, title=None, description=None, is_completed=None):
        with db.session.begin():
            db.session.query(Task).filter_by(id=task_id).update({
                'title': title,
                'description': description,
                'is_completed': is_completed
            })
            return db.session.query(Task).filter_by(id=task_id).first()

    def delete_task(self, task):
        with db.session.begin():
            db.session.delete(task)
