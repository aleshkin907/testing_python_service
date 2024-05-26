from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from config.config import settings


POSTGRES_URL = f'postgresql+psycopg2://{settings.db.user}:{settings.db.password}@{settings.db.host}:{settings.db.port}/{settings.db.name}'


engine = create_engine(POSTGRES_URL)
Session = sessionmaker(engine, expire_on_commit=False)

session = Session()


class Base(DeclarativeBase):
    pass
