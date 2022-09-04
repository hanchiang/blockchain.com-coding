class DependencyNotFoundException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class EnvironmentVariableNotFoundException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
