from sqlalchemy import Column, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class PurchaseHistoryModel(Base):
    __tablename__ = "purchase_history"

    category_id = Column(String(36), ForeignKey("category.id"), nullable=False)
    purchase_id = Column(String, nullable=False)
    money_spent = Column(Float, nullable=False)
    purchase_date = Column(DateTime, nullable=False)
    customer_id = Column(String, nullable=False)

    category = relationship("Category")
