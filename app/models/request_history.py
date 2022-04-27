from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class RequestHistoryModel(Base):
    __tablename__ = "request_history"

    customer_id = Column(String(36), ForeignKey("customer.id"), nullable=False)
    initial_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=False)
    status = Column(String, nullable=False)

    customer = relationship("CustomerModel")
