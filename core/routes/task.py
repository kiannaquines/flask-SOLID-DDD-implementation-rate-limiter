from flask import request, current_app
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

task_ns = Namespace('Tasks', description='Task related operations')

task_model = task_ns.model('Task', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'title': fields.String(required=True, description='The task title'),
    'description': fields.String(description='The task description'),
    'is_completed': fields.Boolean(description='Task completion status')
})

@task_ns.route('/')
class TaskList(Resource):
    @jwt_required()
    def get(self):
        tasks = current_app.task_service.list_task()
        return {"tasks": [task.to_dict() for task in tasks]}

@task_ns.route('/<int:task_id>')
class TaskDetail(Resource):
    @jwt_required()
    @task_ns.marshal_with(task_model)
    def get(self, task_id):
        task = current_app.task_service.get_one_task(task_id)
        if not task:
            return "Task not found", 404
        return task.to_dict()

@task_ns.route('/create')
class TaskCreate(Resource):
    @jwt_required()
    @task_ns.expect(task_model)
    @task_ns.marshal_with(task_model, code=201)
    def post(self):
        data = request.get_json()
        title = data.get('title', '')
        description = data.get('description', '')
        task = current_app.task_service.create_task(title, description)
        return task.to_dict(), 201

@task_ns.route('/<int:task_id>/update')
class TaskUpdate(Resource):
    @jwt_required()
    @task_ns.expect(task_model)
    @task_ns.marshal_with(task_model)
    def put(self, task_id):
        task = current_app.task_service.get_one_task(task_id)
        if not task:
            return "Task not found", 404
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        is_completed = data.get('is_completed')
        update = current_app.task_service.update_task(task_id, title, description, is_completed)
        if not update:
            return "Update failed", 400
        
        return update.to_dict(), 200

@task_ns.route('/<int:task_id>/delete')
class TaskDelete(Resource):
    @jwt_required()
    def delete(self, task_id):
        task = current_app.task_service.get_one_task(task_id)
        if not task:
            return "Task not found", 404
        current_app.task_service.delete_task(task)
        return f"Delete Task {task_id}", 204