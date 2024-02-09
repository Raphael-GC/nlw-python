class HttpUnprocessableEntityError(Exception): # The new class that has been created inherits from the 'Exception' class.

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "UnprecessableEntity"
        self.status_code = 422
