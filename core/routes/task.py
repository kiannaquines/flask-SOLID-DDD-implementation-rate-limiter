from flask import request, current_app
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required

task_ns = Namespace('Tasks', description='Task management operations - Create, Read, Update, Delete tasks')

# Response models
task_model = task_ns.model('Task', {
    'id': fields.Integer(readonly=True, description='The task unique identifier', example=1),
    'title': fields.String(required=True, description='The task title', min_length=1, max_length=200, example='Complete project documentation'),
    'description': fields.String(description='The task description', example='Write comprehensive API documentation with examples'),
    'is_completed': fields.Boolean(description='Task completion status', default=False, example=False)
})

task_create_model = task_ns.model('TaskCreate', {
    'title': fields.String(required=True, description='The task title', min_length=1, max_length=200, example='Complete project documentation'),
    'description': fields.String(description='The task description', example='Write comprehensive API documentation with examples')
})

task_update_model = task_ns.model('TaskUpdate', {
    'title': fields.String(description='The task title', min_length=1, max_length=200, example='Updated task title'),
    'description': fields.String(description='The task description', example='Updated task description'),
    'is_completed': fields.Boolean(description='Task completion status', example=True)
})

task_list_model = task_ns.model('TaskList', {
    'tasks': fields.List(fields.Nested(task_model), description='List of tasks')
})

error_model = task_ns.model('Error', {
    'message': fields.String(description='Error message', example='Task not found')
})

auth_error_model = task_ns.model('AuthError', {
    'message': fields.String(description='Error message', example='Invalid token format. Use \'Authorization: Bearer <your_token>\''),
    'error': fields.String(description='Error code', example='invalid_token'),
    'hint': fields.String(description='Helpful hint', example='Make sure to include \'Bearer \' before your token')
})

@task_ns.route('/')
@task_ns.doc(security='Bearer Auth')
class TaskList(Resource):
    @jwt_required()
    @task_ns.doc(
        description='Retrieve all tasks for the authenticated user',
        responses={
            200: ('Success', task_list_model),
            401: ('Unauthorized - Invalid or missing token. Use format: Bearer <token>', auth_error_model),
            500: 'Internal Server Error'
        }
    )
    @task_ns.marshal_with(task_list_model)
    def get(self):
        """List all tasks"""
        tasks = current_app.task_service.list_task()
        return {"tasks": [task.to_dict() for task in tasks]}

@task_ns.route('/<int:task_id>')
@task_ns.doc(security='Bearer Auth', params={'task_id': 'The task identifier'})
class TaskDetail(Resource):
    @jwt_required()
    @task_ns.doc(
        description='Get a specific task by ID',
        responses={
            200: ('Success', task_model),
            401: 'Unauthorized - Invalid or missing token',
            404: ('Not Found', error_model),
            500: 'Internal Server Error'
        }
    )
    @task_ns.marshal_with(task_model)
    def get(self, task_id):
        """Get task by ID"""
        task = current_app.task_service.get_one_task(task_id)
        if not task:
            task_ns.abort(404, message=f"Task {task_id} not found")
        return task.to_dict()

@task_ns.route('/create')
@task_ns.doc(security='Bearer Auth')
class TaskCreate(Resource):
    @jwt_required()
    @task_ns.doc(
        description='Create a new task',
        responses={
            201: ('Created', task_model),
            400: ('Bad Request', error_model),
            401: 'Unauthorized - Invalid or missing token',
            500: 'Internal Server Error'
        }
    )
    @task_ns.expect(task_create_model, validate=True)
    @task_ns.marshal_with(task_model, code=201)
    def post(self):
        """Create a new task"""
        data = request.get_json()
        title = data.get('title', '')
        description = data.get('description', '')
        
        if not title or not title.strip():
            task_ns.abort(400, message="Title is required and cannot be empty")
        
        task = current_app.task_service.create_task(title, description)
        return task.to_dict(), 201

@task_ns.route('/<int:task_id>/update')
@task_ns.doc(security='Bearer Auth', params={'task_id': 'The task identifier'})
class TaskUpdate(Resource):
    @jwt_required()
    @task_ns.doc(
        description='Update an existing task',
        responses={
            200: ('Success', task_model),
            400: ('Bad Request', error_model),
            401: 'Unauthorized - Invalid or missing token',
            404: ('Not Found', error_model),
            500: 'Internal Server Error'
        }
    )
    @task_ns.expect(task_update_model, validate=True)
    @task_ns.marshal_with(task_model)
    def put(self, task_id):
        """Update a task"""
        task = current_app.task_service.get_one_task(task_id)
        if not task:
            task_ns.abort(404, message=f"Task {task_id} not found")
        
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        is_completed = data.get('is_completed')
        
        update = current_app.task_service.update_task(task_id, title, description, is_completed)
        if not update:
            task_ns.abort(400, message="Update failed")
        
        return update.to_dict(), 200

@task_ns.route('/<int:task_id>/delete')
@task_ns.doc(security='Bearer Auth', params={'task_id': 'The task identifier'})
class TaskDelete(Resource):
    @jwt_required()
    @task_ns.doc(
        description='Delete a task',
        responses={
            204: 'No Content - Task successfully deleted',
            401: 'Unauthorized - Invalid or missing token',
            404: ('Not Found', error_model),
            500: 'Internal Server Error'
        }
    )
    def delete(self, task_id):
        """Delete a task"""
        task = current_app.task_service.get_one_task(task_id)
        if not task:
            task_ns.abort(404, message=f"Task {task_id} not found")
        
        current_app.task_service.delete_task(task)
        return '', 204