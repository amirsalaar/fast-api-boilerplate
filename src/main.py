import os
from fastapi import FastAPI
from src.api.v1.api import api_router
from src.config.settings import get_settings

APP_ENV = os.getenv("APP_ENV", "development")


def create_app():
    """Create the FastAPI application.
    Application Factory Pattern.
    """

    app_settings = get_settings(app_env=APP_ENV)

    app = FastAPI(
        title=app_settings.app_name, openapi_url=f"{app_settings.API_V1_STR}/openapi.json",
    )
    app.include_router(api_router, prefix=app_settings.API_V1_STR)

    return app


app = create_app()
