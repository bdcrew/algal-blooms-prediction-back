import logging

import numpy as np
from pandas import DataFrame
from scipy.stats import stats
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sqlalchemy.orm import Session

from src.ocean.mapper.ocean import SummaryMapper
from src.ocean.repository.waterline_marine_information import WaterlineMarineInformationRepository


class OceanModel:

    def __init__(self, dependent_variable: str = '', independent_variable: list[str] = None):
        self.dependent_variable = dependent_variable  # 종속변수
        self.independent_variables = independent_variable  # 독립변수
        self.waterline_marine_info_df = None
        self.X = None
        self.y = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.logit_model = LogisticRegression()

    async def load_data(self, db: Session):
        waterline_marine_information_repository = WaterlineMarineInformationRepository(db)
        data = await waterline_marine_information_repository.get_all()

        self.waterline_marine_info_df = DataFrame(data)
        # self.waterline_marine_info_df = self.waterline_marine_info_df.dropna()

        self.y = self.waterline_marine_info_df['harmful_algal_bloom_presence'].astype(bool)
        self.X = self.waterline_marine_info_df[self.independent_variables]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.4,
                                                                                random_state=0)
        logging.info('success load_data')

    async def fit_model(self):
        """
        모델 입히기
        :return:
        """
        self.logit_model.fit(self.X_train, self.y_train)
        logging.info('complete fitting model')

    async def summary(self) -> SummaryMapper:
        logging.info("Coefficients: {}".format(self.logit_model.coef_))
        logging.info("Intercept: {}".format(self.logit_model.intercept_))

        # 계수(Coefficients)
        coefficients = self.logit_model.coef_[0]
        # 예측값
        preds = self.logit_model.predict(self.X_train)
        # 디자인 행렬
        X_design = np.hstack([np.ones((self.X_train.shape[0], 1)), self.X_train])
        # 피팅된 값
        fitted_vals = preds
        # 잔차
        residuals = self.y_train - fitted_vals

        # 분산-공분산 행렬
        V = np.dot(residuals.T, residuals) * np.linalg.inv(np.dot(X_design.T, X_design)).diagonal()
        # 표준 오차
        SE = np.sqrt(V)

        # T-값
        t_values = coefficients / SE

        # P-값
        p_values = [2 * (1 - stats.norm.cdf(np.abs(i))) for i in t_values]

        # 값 넣기
        return SummaryMapper(coefficients=coefficients, standard_errors=SE, t_values=t_values, p_values=p_values)

    async def predict_input_average(self):
        """
        평균값을 통한 예측값 나오도록 개발
        :return:
        """
        pass

    async def predict(self):
        # 예측 모델에 대해서 알아서 판단.
        pass
