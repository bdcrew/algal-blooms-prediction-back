from math import exp

import pandas as pd
from sklearn.linear_model import LogisticRegression
from fastapi import HTTPException
from pandas import DataFrame
from sqlalchemy.orm import Session
from ocean.payload.ocean import IndependentVariablesPayload

from ocean.repository.waterline_marine_information import WaterlineMarineInformationRepository
from src.config.db import conn


class OceanModel:
    """
    로지스틱 회귀 모델 입혀보기
    """
    def __init__(self, dependent_variable: str = '', independent_variable: list[str] = None):
        self.dependent_variable = dependent_variable # 종속변수
        self.independent_variables = independent_variable # 독립변수
        self.independent_variables_with_constant = None
        self.waterline_marine_info_df = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.logit_model = LogisticRegression()

    async def load_data(self, db: Session):
        waterline_marine_information_repository = WaterlineMarineInformationRepository(db)
        data = await waterline_marine_information_repository.get_all()

        self.waterline_marine_info_df = DataFrame(data)
        self.waterline_marine_info_df = self.waterline_marine_info_df.dropna()
        
    async def split_train_data(self, payload: IndependentVariablesPayload):
        pass


    async def fit_model(self):
        """
        모델 입히기
        :return:
        """
        self.logit_model.fit(self.independent_variables_with_constant, self.dependent_variable)

    async def summary(self):
        pass

    def __inverse_logit(self, model_formula: float):
        return 1.0 / (1.0 + exp(-model_formula))
    
    async def predict_input_average(self):
        """
        평균값을 통한 예측값 나오도록 개발
        :return:
        """
        pass


    async def predict(self):
        # 예측 모델에 대해서 알아서 판단.
        pass

