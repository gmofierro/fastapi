import datetime
from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    id: Optional[int] = None 
    created_at: Optional[datetime.datetime] = None
    name: str
    passwd: str
    email: str


    
 