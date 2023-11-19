from pydantic import BaseModel

class IndependentVariablesPayload(BaseModel):
    temperature: float | None
    salinity: float | None
    phosphate_phosphorus: float | None
    nitrous_acid_nitrogen: float | None
    nitric_acid_nitrogen: float | None
    silicic_acid_silicon: float | None
    