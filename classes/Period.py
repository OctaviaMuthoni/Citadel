import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Period:
    class PeriodStatus:
        OPEN = "OPEN",
        CLOSED = "CLOSED"

    period_id: uuid.UUID
    period: str
    start_date: datetime.date
    end_date: datetime.date
    status: PeriodStatus = PeriodStatus.OPEN
