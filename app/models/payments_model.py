from sqlalchemy import Column, Integer, String, DateTime

from app.db import Base
from app.models.base_model import BaseModel


class Payments(BaseModel, Base):
    __tablename__ = "payments"
