from .base_exception import ApplicationError
class DatabaseError(ApplicationError):
    error_code = "database_error"
    status_code = 500