import datetime

from sqlalchemy import DateTime, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.config.db import Base, session


class WaterlineMarineInfomation(Base):
    __tablename__ = "waterline_marine_information"

    observation_date: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True)
    temperature: Mapped[float] = mapped_column(Float)
    salinity: Mapped[float] = mapped_column(Float)
    phosphate_phosphorus: Mapped[float] = mapped_column(Float)
    nitrous_acid_nitrogen: Mapped[float] = mapped_column(Float)
    nitric_acid_nitrogen: Mapped[float] = mapped_column(Float)
    silicic_acid_silicon: Mapped[float] = mapped_column(Float)
    harmful_algal_bloom_presence: Mapped[float] = mapped_column(Integer)
    probability: Mapped[float] = mapped_column(Float)


session.add_all([WaterlineMarineInfomation])
