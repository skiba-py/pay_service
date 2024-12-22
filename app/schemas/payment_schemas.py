from decimal import Decimal

from pydantic import BaseModel


class PaymentSchema(BaseModel):
    user_id: str
    payment_id: str
    amount: Decimal
    email: str | None
    type: str | None
    company_id: int

    class Config:
        from_attributes = True
