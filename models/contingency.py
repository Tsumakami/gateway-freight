from pydantic import BaseModel
from config.database import Base
from sqlalchemy import Column, Float, Integer

class Contingency(Base):
    __tablename__ = "contingency"

    id = Column(Integer, primary_key=True)
    zip_code_start = Column(Integer)
    zip_code_end = Column(Integer)
    weight_start = Column(Float)
    weight_end = Column(Float)
    absolute_cost = Column(Float)
    delivery_time = Column(Integer)

    def __repr__(self):
        return f"Contingency(id={self.id!r}, zip_code_start={self.zip_code_start!r}, zip_code_end={self.zip_code_end!r}, weight_start={self.weight_start!r}, weight_end={self.weight_end!r}, absolute_cost={self.absolute_cost!r}, delivery_time={self.delivery_time!r})"

class ContingencyBase(BaseModel):
    zip_code_start: int
    zip_code_end: int
    weight_start: float
    weight_end: float
    absolute_cost: float
    delivery_time: int

class ContingencyCreate(ContingencyBase):
    pass

class ContingencySchema(ContingencyBase):
    id: int = None

    class Config:
        orm_mode = True