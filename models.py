from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(Enum):
    male = "male"
    female = "female"
    

class Role(Enum):
    admin = "admin"
    user = "user"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    role: List[Role]
    
class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    role: Optional[List[Role]]