from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

USER = "contigency_user"
PASSWORD = "teste123"
#ADDRESS = "127.0.0.1"
ADDRESS = "18.118.23.107" #Load balancer
#ADDRESS = "18.220.17.160" #Banco Master
DATA_BASE = "banco"
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{ADDRESS}/{DATA_BASE}?charset=utf8mb4"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    echo=True, 
    future=True,
    pool_size=20
)

#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = Session(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()