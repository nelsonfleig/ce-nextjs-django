from datetime import datetime

from ninja import Schema
from pydantic import EmailStr


class WaitlistEntryCreateSchema(Schema):
    email: EmailStr


class WaitlistEntryDetailSchema(Schema):
    email: EmailStr
    timestamp: datetime
