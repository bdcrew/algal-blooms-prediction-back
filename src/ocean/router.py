from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.depends import get_db

router = APIRouter(
    prefix="ocean",
    tags=["ocean"],
)


@router.post("/")
async def input_predict_data():
    """
    예측 데이터 설정
    """
