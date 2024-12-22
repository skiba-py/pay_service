from enum import Enum


class PaymentStatus(str, Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELED = "Canceled"
