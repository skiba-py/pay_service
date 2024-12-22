from sqlalchemy import Column, Integer, String, DateTime, UUID, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base
from app.models.base_model import BaseModel


class Payment(BaseModel, Base):
    __tablename__ = "payments"

    user_id = Column(String, nullable=False)
    payment_id = Column(String, nullable=False, unique=True)
    amount = Column(Numeric(10, 2), nullable=False)
    email = Column(String)
    type = Column(String(30), nullable=False)
    payment_status = Column(String(30), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.company_id"), nullable=False)

    def __repr__(self):
        return (
            f"<Payments(id={self.id}, user_id={self.user_id}, "
            f"payment_id={self.payment_id}, amount={self.amount}, "
            f"email={self.email}, type={self.type}, "
            f"payment_status={self.payment_status})>"
        )

    def __str__(self):
        return self.__repr__()
