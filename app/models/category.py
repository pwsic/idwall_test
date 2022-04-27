from sqlalchemy import Column, String, Float, DateTime

from app.models.base import Base


class CategoryModel(Base):
    __tablename__ = 'category'

    name = Column(String, nullable=False)
