import logging

from fastapi import APIRouter
import pandas as pd

from src.ocean.payload.ocean import IndependentVariablesPayload

ocean_router = APIRouter(
    prefix="/ocean",
    tags=["ocean"],
)


@ocean_router.post("/")
async def input_predict_data(body: IndependentVariablesPayload):
    """
    예측 데이터 설정
    """
    # 값이 있는지 확인하기
    independent_variable_header = vars(body).keys()

    independent_variables = pd.Dataframe(columns=independent_variable_header, data=vars(body).values()
                                            , index=[0])
    logging.info(independent_variables)
    return {"message": "success"}
