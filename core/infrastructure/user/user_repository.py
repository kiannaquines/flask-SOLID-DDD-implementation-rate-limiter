from ...domain.user import User
from ...config.extension import db
from .user_repository_interface import UserRepositoryInterface
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from ...exceptions.database_error import DatabaseError
from ...exceptions.duplicate_error import DuplicateError
from ...exceptions.not_found_error import NotFoundError


class UserRepository(UserRepositoryInterface):

    def get_user_by_id(self, user_id):
        try:
            user = db.session.query(User).filter_by(id=user_id).first()

            if not user:
                raise NotFoundError("User not found")

            return user

        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseError("Error retrieving user") from e


    def login_user(self, username):
        try:
            user = db.session.query(User).filter_by(username=username).first()

            if not user:
                raise NotFoundError("User not found")

            return user

        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseError("Login database error") from e


    def register_user(self, username, password_hash, email):
        try:
            user = User(username=username, password_hash=password_hash, email=email)

            with db.session.begin():
                db.session.add(user)

            return user

        except IntegrityError as e:
            db.session.rollback()
            raise DuplicateError("Username or email already exists") from e

        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseError("Database error during registration") from e

        except Exception as e:
            db.session.rollback()
            raise DatabaseError("Unexpected error during registration") from e