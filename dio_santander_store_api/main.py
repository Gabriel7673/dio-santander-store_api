from fastapi import FastAPI

from dio_santander_store_api.core.config import settings
from dio_santander_store_api.core.exceptions import register_exception_handlers
from dio_santander_store_api.routers import api_router


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH,
        )


app = App()
register_exception_handlers(app)
app.include_router(api_router)
