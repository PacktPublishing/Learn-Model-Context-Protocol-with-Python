from pydantic import BaseModel
from typing import List, Dict 
import pydantic

class OfficeHour(BaseModel):
    day: str
    from_: int
    to_: int

class Professor(BaseModel):
    id: int
    name: str
    office_hours: List[OfficeHour]

professor_dict = {
    "id": 1,
    "name": "Dr. Smith",
    "office_hours": [
        {"day": "Monday", "from_": 9, "to_": 12},
        {"day": "Wednesday", "from_": 14, "to_": 17}
    ]
}

professor = Professor(**professor_dict)

professor_serialized = professor.model_dump() # {"id": 1, "name": "Dr. Smith", "office_hours": [{"day": "Monday", "from_": 9, "to_": 12}, {"day": "Wednesday", "from_": 14, "to_": 17}]}}

print("Running pydantic version: ", pydantic.__version__)

print(professor)
print(professor_serialized)