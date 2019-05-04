import enum

from sqlalchemy import Integer, String, Column, Enum, ForeignKey
from sqlalchemy.orm import relation, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref
from vip_admin.database import BaseModel


class EmployeeSexEnum(enum.Enum):
    خانم = 1
    آقا = 2


class AccountOfficerStatusEnum(enum.Enum):
    ACTIVE = 1
    INACTIVE = 2


class Employee(BaseModel):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    family = Column(String)
    personnel_id = Column(Integer, unique=True, nullable=True)
    social_number = Column(Integer, nullable=True)
    email = Column(String, nullable=True)
    branch_id = Column(Integer, ForeignKey('branch.id'))
    sex = Column(Enum(EmployeeSexEnum))
    type = Column(String(20))
    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'employee'
    }


class AccountOfficer(Employee):
    status = Column(Enum(AccountOfficerStatusEnum))
    supervisor_id = Column(Integer, ForeignKey('employee.id'))
    supervisors = relationship('Employee')
    __mapper_args__ = {
        'polymorphic_identity': 'officer'
    }

