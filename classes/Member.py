from dataclasses import dataclass
from datetime import datetime

from share import Gender


class MemberType:
    EMPLOYEE = "Employee"  # Employees can either be administrators, teachers or support staff
    STUDENT = "Student"


@dataclass
class Member:
    # from member sign up form
    member_id: str
    member_type: MemberType

    name: str
    profile_image: str
    dob: datetime.date
    gender: Gender

    phone: str
    email: str
    current_residence: str
    permanent_residence: str

    role: str

    join_date: datetime.date
    termination_date: datetime.date

    # for employees only
    id_number: int = None
    employee_number: str = None
    department: str = None

    # for students only
    nemis: str = None
    assessment: str = None
    admission: str = None
    grade: int = None
    stream: str = None
