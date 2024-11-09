from ninja import Schema
from datetime import datetime
from pydantic import EmailStr, model_validator
from .models import WaitlistEntry
from typing import List, Any


class WaitlistEntryCreateSchema(Schema):
    email: str


class ErrorWaitlistEntryCreateSchema(Schema):
    email: List[Any]
    # non_field_errors = List[dict] = []

class WaitlistEntryListSchema(Schema):
    id: int
    email: EmailStr
    username: str
    
class WaitlistEntryDetailSchema(Schema):
    email: EmailStr
    updated: datetime
    timestamp: datetime