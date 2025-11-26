from .user_service_interface import UserServiceInterface
from flask_jwt_extended import create_access_token, unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest as BadRequestError

from ...exceptions.not_found_error import NotFoundError
from ...exceptions.database_error import DatabaseError
from ...exceptions.duplicate_error import DuplicateError


class UserService(UserServiceInterface):
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user_by_id(self, user_id: int):
        try:
            user = self.user_repository.get_user_by_id(user_id)
            user_data = {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
            return {"success": True, "data": user_data}

        except NotFoundError as e:
            return {"success": False, "error": "not_found", "message": e.message}

        except DatabaseError as e:
            return {"success": False, "error": "database_error", "message": e.message}

        except Exception:
            return {"success": False, "error": "unknown_error", "message": "Unknown error occurred."}


    def login_user(self, username: str, password: str):
        try:
            user = self.user_repository.login_user(username)

            if user and check_password_hash(user.password_hash, password):
                token = create_access_token(identity=user.id)
                return {"success": True, "access_token": token}

            return {
                "success": False,
                "error": "invalid_credentials",
                "message": "Invalid username or password"
            }

        except NotFoundError:
            return {
                "success": False,
                "error": "invalid_credentials",
                "message": "Invalid username or password"
            }

        except DatabaseError as e:
            return {"success": False, "error": "database_error", "message": e.message}

        except Exception:
            return {"success": False, "error": "unknown_error", "message": "Unknown error occurred."}


    def register_user(self, username: str, password: str, email: str):
        try:
            password_hash = generate_password_hash(password)
            user = self.user_repository.register_user(username, password_hash, email)
            user_data = {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
            return {"success": True, "data": user_data}

        except DuplicateError as e:
            return {"success": False, "error": "duplicate", "message": e.message}

        except DatabaseError as e:
            return {"success": False, "error": "database_error", "message": e.message}

        except Exception:
            return {"success": False, "error": "unknown_error", "message": "Unknown error occurred."}


    def logout_user(self):
        try:
            return {"success": True, "message": "Logout successful"}

        except BadRequestError as e:
            return {"success": False, "error": "bad_request", "message": str(e)}

        except Exception:
            return {"success": False, "error": "unknown_error", "message": "Unknown error occurred."}
