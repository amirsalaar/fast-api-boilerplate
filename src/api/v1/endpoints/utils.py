from typing import Any
from fastapi import APIRouter
from src.services.mongo_client import client


router = APIRouter()


@router.get("/health/", status_code=200)
def health_check() -> Any:
    """
    Test server health.
    """
    return {"status": "ok"}


@router.get("/test-mongo/", status_code=200)
async def mongodb_check() -> Any:
    """Test mongodb connection health."""

    server_info = await client.server_info()

    return {"status": "ok" if server_info.get("ok") else "not ok"}
