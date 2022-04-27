from sqlalchemy import Column, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class PurchaseHistoryModel(Base):
    __tablename__ = "request_history"

    customer_id = Column(String(36), ForeignKey("customer.id"), nullable=False)
    initial_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    status = Column(DateTime, nullable=False)

    customer = relationship("Customer")
