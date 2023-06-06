from math import exp

import pandas as pd
import statsmodels.api as sm
from fastapi import HTTPException
from pandas import DataFrame, Series

from src.config.db import conn


async def logistic_ocean_data():
    # 데이터를 가져온다.

    # 종속 변수를 선언한다.

    # 독립 변수를 선언한다.

    # 로지스틱 회귀모형에 피팅한다.

    # summary를 출력한다.

    # 회귀 계수 해석을 한다.

    # 평균값을 입력하


class OceanModel:
    """
    바다 모델에 대해서 작업하는 방법
    """
    def __init__(self, dependent_variable: str = 'on_off', independent_variable: list[str] = None):
        self.dependent_variable = dependent_variable # 종속변수
        self.independent_variables = independent_variable # 독립변수
        self.independent_variables_with_constant = None
        self.logit_model = None

    async def load_ocean_data(self):
        if self.independent_variables is None || self.dependent_variable is None:
            raise HTTPException(status_code=418, detail="데이터 입력을 하지 않았습니다.")

        # 관련 종속 변수의 데이터를 가져옵니다.
        ocean_df = await pd.read_sql('ocean', con=conn)

        # 개발 환경에서 작업을


    async def fit_model(self):
        self.independent_variables_with_constant = sm.add_constant(self.independent_variables, prepend=True)
        self.logit_model = sm.Logit(self.dependent_variable, self.independent_variables, missing='drop').fit()

    async def summary(self):
        return self.logit_model.summary()

    def __inverse_logit(self, model_formula: float):
        return 1.0 / (1.0 + exp(-model_formula))
    
    async def predict_input_average(self):
        """
        평균값을 통한 예측값 나오도록 개발
        :return:
        """



    async def predict(self):
        # 예측 모델에 대해서 알아서 판단.

