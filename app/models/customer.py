from sqlalchemy import Column, DateTime, Float, String

from app.models.base import Base


class CustomerModel(Base):
    __tablename__ = "customer"

    name = Column(String, nullable=False)
