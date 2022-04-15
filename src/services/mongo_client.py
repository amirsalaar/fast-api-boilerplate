"""This module establishes the asynchronous MongoDB connection."""
import os
import motor.motor_asyncio
from src.config.settings import get_settings

app_settings = get_settings(os.getenv("APP_ENV", "development"))


client = motor.motor_asyncio.AsyncIOMotorClient(app_settings.MONGODB_URL)
