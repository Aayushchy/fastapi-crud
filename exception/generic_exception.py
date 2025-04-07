from http import HTTPStatus


class GenericException(Exception):
    def __init__(self, response_code: HTTPStatus, internal_message: str, client_message: str):
        self.internal_message = internal_message
        self.client_message = client_message
        self.response_code = response_code
        super().__init__(internal_message)

