from http import HTTPStatus

from fastapi import Request
from fastapi.responses import JSONResponse

from exception.client_exception import ClientException
from exception.generic_exception import GenericException

def register_exception_handlers(app):
    @app.exception_handler(GenericException)
    async def generic_exception_handler(request: Request, exc: GenericException):
        print(request)
        return JSONResponse(
            status_code=exc.response_code.value,
            content={"error": exc.client_message},
        )

    @app.exception_handler(ClientException)
    async def client_exception_handler(request: Request, exc: ClientException):
        print(request)
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={"error": exc.message},
        )
