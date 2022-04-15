from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.post("/health/", status_code=200)
def health_check() -> Any:
    """
    Test server health.
    """
    return {"status": "ok"}
