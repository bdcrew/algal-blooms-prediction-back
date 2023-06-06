from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.depends import get_db

router = APIRouter(
    prefix="ocean",
    tags=["ocean"],
)


@router.get("/")
async def read_ocean(db: Session = Depends(get_db)):
    pass
