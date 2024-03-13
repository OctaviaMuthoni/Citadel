import decimal
from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Subscription:

    subscription: str

    # library charges for particular subscription
    registration: decimal.Decimal
    activation: decimal.Decimal
    overdue: decimal.Decimal
    card: decimal.Decimal
    card_replacement: decimal.Decimal
    loss_damage: decimal.Decimal

    validity: int  # the validity period for the subscription in months
    limit: int  # maximum borrowing limit

    subscription_id: str = str(uuid4())
