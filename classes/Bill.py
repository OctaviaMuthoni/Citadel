import decimal
from datetime import datetime
from dataclasses import dataclass
from uuid import uuid4


class BillType:
    REGISTRATION = "Registration",
    ACTIVATION = "Activation",
    OVERDUE = "Overdue"
    CARD = "Card"
    CARD_REPLACEMENT = "Card replacement"
    LOSS_DAMAGE_PENALTY = "Damage penalty"

    # Estimate for damage caused
    DAMAGE_EST = "Damage estimation"

    # Estimate of the current market value to replace lost material
    MATERIAL_REPLACEMENT_EST = "Material replacement"


@dataclass
class Bill:
    member_id: str
    bill_type: BillType
    amount: decimal.Decimal
    bill_date: datetime.date
    due_date: datetime.date

    # auto generate unique id for each bill
    bill_id: str = str(uuid4())


