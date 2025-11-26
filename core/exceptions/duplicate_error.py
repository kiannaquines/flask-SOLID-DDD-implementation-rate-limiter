from .base_exception import ApplicationError
class DuplicateError(ApplicationError):
    error_code = "duplicate_error"
    status_code = 400