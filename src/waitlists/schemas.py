from ninja import Schema
from datetime import datetime
from pydantic import EmailStr, model_validator
from .models import WaitlistEntry
from typing import List


class WaitlistEntryCreateSchema(Schema):
    email: EmailStr


class ErrorWaitlistEntryCreateSchema(Schema):
    email: List[dict]
    # non_field_errors = List[dict] = []

class WaitlistEntryListSchema(Schema):
    id: int
    email: EmailStr
    username: str
    
class WaitlistEntryDetailSchema(Schema):
    email: EmailStr
    updated: datetime
    timestamp: datetime