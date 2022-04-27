from sqlalchemy import Column, DateTime, Float, ForeignKey, String

from app.models.base import Base


class SuspiciousTransactionModel(Base):
    __tablename__ = "suspicious_transaction"

    category_id = Column(String(36), ForeignKey("category.id"), nullable=False)
    customer_id = Column(String(36), ForeignKey("customer.id"), nullable=False)

    purchase_id = Column(String, nullable=False)
    money_spent = Column(Float, nullable=False)
    purchase_date = Column(DateTime, nullable=False)
