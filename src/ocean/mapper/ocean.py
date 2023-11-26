import datetime
from typing import List

from pydantic import BaseModel


class WaterlineMarineInfoMapper(BaseModel):
    observationd_date: datetime.datetime
    temperature: float
    salinity: float
    phosphate_phosphorus: float
    nitrous_acid_nitrogen: float
    nitric_acid_nitrogen: float
    silicic_acid_silicon: float
    harmful_algal_bloom_presence: int
    probability: float


class SummaryMapper(BaseModel):
    coefficients: List[float]  # 계수
    standard_errors: List[float]  # 표준 오차
    t_values: List[float]  # T-value
    p_values: List[float]  # p-value
