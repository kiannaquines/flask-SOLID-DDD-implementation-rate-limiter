from .base_exception import ApplicationError
class NotFoundError(ApplicationError):
    error_code = "not_found_error"
    status_code = 404