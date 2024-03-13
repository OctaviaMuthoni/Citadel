from uuid import UUID
from dataclasses import dataclass


@dataclass
class Grade:
    grade_uuid: UUID
    grade: int

