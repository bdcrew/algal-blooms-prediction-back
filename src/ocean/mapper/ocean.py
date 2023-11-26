import datetime
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
