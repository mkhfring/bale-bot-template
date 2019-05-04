import enum

from sqlalchemy import Integer, String, Column, Enum, ForeignKey
from sqlalchemy.orm import relation, relationship
from sqlalchemy.ext.declarative import declarative_base
from vip_admin.database import BaseModel


class AccountOfficerStatusEnum(enum.Enum):
    ACTIVE = 0
    INACTIVE = 1
    SUSPEND = 2


class Customer(BaseModel):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    family = Column(String)
    social_number = Column(Integer, nullable=True)
    branch_id = Column(Integer, ForeignKey('branch.id'))
    type = Column(String)

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'employee'
    }


class IndevidualCustomer(Customer):
    __mapper_args__ = {
        'polymorphic_identity': 'Individual'
    }


class LegalCustomer(Customer):
    __mapper_args__ = {
        'polymorphic_identity': 'Legal'
    }

