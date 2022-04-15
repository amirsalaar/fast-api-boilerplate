"""This module contains the settings for the application.

    - Any field that should be read from the `.env.*` file should be added as a
    field to the Setting Classes.
    - If it's a shared setting, add them to the base "Settings" class.
"""
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI-Boilerplate"
    API_V1_STR: str = "/api/v1"
    MONGODB_URL: str

    class Config:
        env_file = ".env"


class DevelopmentSettings(Settings):
    APP_ENV: str = "development"

    class Config:
        env_file = ".env.development"


class ProductionSettings(Settings):
    APP_ENV: str = "production"

    class Config:
        env_file = ".env.production"


@lru_cache
def get_settings(app_env: str = "development") -> Settings:
    """Generate the setting object which loads environment variables.

    Cache the result to improve performance and not loading the .env files
    every time.

    Args:
        APP_ENV (str, optional): _description_. Defaults to "development".

    Returns:
        Settings: _description_
    """
    if app_env == "development":
        return DevelopmentSettings()
    elif app_env == "production":
        return ProductionSettings()

    return Settings()
