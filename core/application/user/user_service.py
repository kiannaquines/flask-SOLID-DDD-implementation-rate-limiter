from .user_service_interface import UserServiceInterface
from flask_jwt_extended import create_access_token, unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest as BadRequestError
from ...exceptions.not_found_error import NotFoundError
from ...exceptions.database_error import DatabaseError
from ...exceptions.duplicate_error import DuplicateError

from flask import jsonify

class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserServiceInterface):
        self.user_repository = user_repository

    def get_user_by_id(self, user_id: int):
        try:
            return self.user_repository.get_user_by_id(user_id)
        except NotFoundError as e:
            return jsonify({"success": False, "error": "not_found", "message": str(e)})
        except DatabaseError as e:
            return jsonify({"success": False, "error": "database_error", "message": str(e)})
        except Exception as e:
            return jsonify({"success": False, "error": "unknown_error", "message": "Unknown error occured. Please try again."})
            
    def login_user(self, username: str, password: str):

        try:
            attemp_login = self.user_repository.login_user(username)
            if attemp_login and check_password_hash(attemp_login.password, password):
                access_token = create_access_token(identity=attemp_login.id)
                return access_token
        except NotFoundError as e:
            return jsonify({"success": False, "error": "not_found", "message": str(e)})
        except DatabaseError as e:
            return jsonify({"success": False, "error": "database_error", "message": str(e)})
        except Exception as e:
            return jsonify({"success": False, "error": "unknown_error", "message": "Unknown error occured. Please try again."})

    def register_user(self, username: str, password: str, email: str):
        try:
            password_hash = generate_password_hash(password)
            register = self.user_repository.register_user(
                username, password_hash, email
            )
            return register
        except DuplicateError as e:
            return jsonify({"success": False, "error": "duplicate_error", "message": str(e)})
        except DatabaseError as e:
            return jsonify({"success": False, "error": "database_error", "message": str(e)})
        except Exception as e:
            return jsonify({"success": False, "error": "unknown_error", "message": "Unknown error occured. Please try again."})
        
    def logout_user(self, response):
        try:
            unset_jwt_cookies(response)
            return jsonify({"success": True, "message": "Logout successful"})
        except BadRequestError as e:
            return jsonify({"success": False, "error": "bad_request", "message": str(e)})
        except Exception as e:
            return jsonify({"success": False, "error": "unknown_error", "message": "Unknown error occured. Please try again."})