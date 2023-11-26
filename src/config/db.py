from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

from src.config.secret import get_os_secrets

# postgresql
conn = "postgresql+psycopg://{user}:{password}@{host}:{port}/{name}".format(
    user=get_os_secrets('DB_USER'),
    password=get_os_secrets('DB_PASSWORD'),
    host=get_os_secrets('DB_HOST'),
    port=get_os_secrets('DB_PORT'),
    name=get_os_secrets('DB_NAME'),
)

engine = create_engine(conn, echo=True, pool_size=20, max_overflow=0)

session = Session(engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = session() # type: ignore
    try:
        yield db
        db.commit()
    finally:
        db.close()
