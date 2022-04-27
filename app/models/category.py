from sqlalchemy import Column, DateTime, Float, String

from app.models.base import Base


class CategoryModel(Base):
    __tablename__ = "category"

    name = Column(String, nullable=False)
