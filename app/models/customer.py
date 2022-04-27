from sqlalchemy import Column, String, Float, DateTime

from app.models.base import Base


class CustomerModel(Base):
    __tablename__ = 'customer'

    name = Column(String, nullable=False)
