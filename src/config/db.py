from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

from src.config.secret import get_secret

conn = "postgresql+psycopg://{user}:{password}/{host}:{port}/{name}".format(
    user=get_secret('DB_USER'),
    password=get_secret('DB_PASSWORD'),
    host=get_secret('DB_HOST'),
    port=get_secret('DB_PORT'),
    name=get_secret('DB_NAME'),
)
engine = create_engine(conn, echo=True)

metadata_obj = MetaData()
metadata_obj.reflect(bind=engine)

Session = Session(engine, autoflush=False, autocommit=False)
