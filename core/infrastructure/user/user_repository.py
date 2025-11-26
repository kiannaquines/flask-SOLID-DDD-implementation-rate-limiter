from ...domain.user import User
from ...config.extension import db
from .user_repository_interface import UserRepositoryInterface
from sqlalchemy.exc import IntegrityError
from ...exceptions.database_error import DatabaseError
from ...exceptions.duplicate_error import DuplicateError
from ...exceptions.not_found_error import NotFoundError

class UserRepository(UserRepositoryInterface):
    def get_user_by_id(self, user_id):
        try:
            current_user = db.session.query(User).filter_by(id=user_id).first()

            if not current_user:
                raise NotFoundError("User not found") from e
            
            return current_user
        except DatabaseError as e:
            db.session.rollback()
            raise DatabaseError("An error occurred while retrieving the user by ID") from e
        
    def login_user(self, username):
        try:
            user = db.session.query(User).filter_by(username=username).first()
            return user
        except IntegrityError as e:
            db.session.rollback()
            raise NotFoundError("User not found") from e
        except Exception as e:
            db.session.rollback()
            raise DatabaseError("An error occurred while logging in the user") from e

    def register_user(self, username, password, email):
        try:
            register = User(username=username, password_hash=password, email=email)
    
            with db.session.begin():
                db.session.add(register)

            return register
        
        except IntegrityError as e:
            db.session.rollback()
            raise DuplicateError("Username or email already exists") from e
        
        except Exception as e:
            db.session.rollback()
            raise DatabaseError("An error occurred while registering the user") from e