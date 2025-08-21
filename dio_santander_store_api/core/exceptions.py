from fastapi import status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


class BaseException(Exception):
    message: str = "Internal server error"

    def __init__(self, message: str | None = None):
        if message:
            self.message = message


class NotFoundException(BaseException):
    message: str = "Not found"


def register_exception_handlers(app):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc: RequestValidationError):
        errors = exc.errors()

        first_error = errors[0] if errors else {}
        message = first_error.get("msg", "Erro de validação")
        field = ".".join(str(loc) for loc in first_error.get("loc", []))

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "detail": {
                    "field": field,
                    "message": message,
                }
            },
        )
