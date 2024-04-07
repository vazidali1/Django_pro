# app/app/api/models/user.py
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: str
    name: str
    email: str
    password: str
    referral_code: str
    registration_timestamp: datetime
