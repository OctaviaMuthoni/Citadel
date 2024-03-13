from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Department:
    department: str
    department_id: str = str(uuid4())
    
