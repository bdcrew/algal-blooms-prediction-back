from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..config.db import get_db

ocean_router = APIRouter(
    prefix="/ocean",
    tags=["ocean"],
)


@ocean_router.post("/")
async def input_predict_data():
    """
    예측 데이터 설정
    """
    pass
