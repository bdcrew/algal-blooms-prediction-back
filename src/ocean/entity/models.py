import datetime
from sqlalchemy import Column, DateTime, Float, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.config.db import metadata_obj

# OceanAll = metadata_obj.tables['ocean_all_data']
# Ocean = metadata_obj.tables['ocean']


class Base(DeclarativeBase):
    pass


class WaterlineMarineInfomation(Base):
    __tablename__ = "waterline_marine_information"

    observation_date: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True)
    temperature: Mapped[float] = mapped_column(Float)
    salinity: Mapped[float] = mapped_column(Float)
    phosphate_phosphorus = mapped_column(Float)
    nitrous_acid_nitrogen = mapped_column(Float)
    nitric_acid_nitrogen = mapped_column(Float)
    silicic_acid_silicon = mapped_column(Float)
    harmful_algal_bloom_presence = mapped_column(Integer)
    probability = mapped_column(Float)




    
