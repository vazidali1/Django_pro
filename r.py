# app/app/api/models/referral.py
from pydantic import BaseModel
from datetime import datetime

class Referral(BaseModel):
    id: str
    referring_user_id: str
    referred_user_id: str
    timestamp: datetime
