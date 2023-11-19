from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select

from ..entity.ocean_models import WaterlineMarineInfomation


class WaterlineMarineInformationRepository:
    """
    waterline marine information repository
    """
    def __init__(self, db: Session) -> None:
        self.db = db

    async def get_all(self) -> list[WaterlineMarineInfomation]:
        """
        모든 데이터를 읽어온다.
        """
        stmt = select(WaterlineMarineInfomation)
        return list(self.db.scalars(stmt))
    
    async def get_by_date(self, date: str) -> WaterlineMarineInfomation:
        """
        날짜에 해당하는 데이터를 읽어온다.
        """
        stmt = select(WaterlineMarineInfomation).where(WaterlineMarineInfomation.observation_date == date)
        return self.db.scalar(stmt)
    