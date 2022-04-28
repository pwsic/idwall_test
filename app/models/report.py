from sqlalchemy import JSON, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class ReportModel(Base):
    __tablename__ = "report"

    customer_id = Column(String(36), ForeignKey("customer.id"), nullable=False)
    request_history_id = Column(
        String(36), ForeignKey("request_history.id"), nullable=False
    )
    expenses = Column(JSON, nullable=False)

    customer = relationship("CustomerModel")
    request_history = relationship("RequestHistoryModel")
