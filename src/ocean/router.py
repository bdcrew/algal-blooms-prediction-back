from fastapi import APIRouter

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
