from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

USER = "contingency_user"
PASSWORD = ""
ADDRESS = "127.0.0.1"
DATA_BASE = "contingency_db"
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{ADDRESS}/{DATA_BASE}?charset=utf8mb4"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, future=True
)

#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = Session(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()