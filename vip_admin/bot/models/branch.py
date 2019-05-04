from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String
from vip_admin.database import BaseModel


class Branch(BaseModel):
    __tablename__ = 'branch'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(Integer)
    employees = relationship("Employee")
    customers = relationship("Customer")
