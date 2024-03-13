"""
    This module contains a class that describe an author.
"""
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

from share import Gender


@dataclass
class Author:
    name: str
    yob: int
    yod: int | None
    career: str
    nationality: str
    gender: Gender
    profile_image: str | None

    # properties with default values
    author_id: str = str(uuid4())

    @property
    def deceased(self) -> bool:
        return True if self.yod else False

    @property
    def age(self) -> int:
        return self.yod - self.yob if self.deceased else datetime.today().date().year - self.yob
