class ApplicationError(Exception):
    error_code = "application_error"
    status_code = 500

    def __init__(self, message: str = None):
        super().__init__(message)
        self.message = message or "An unexpected error occurred."
