from datetime import datetime, timezone, timedelta
from typing import Optional, List
from pydantic import BaseModel, Field

class logSchema(BaseModel):
    timestamp: datetime = Field(...)
    email: str = Field(min_length=1)
    caducidad: datetime = Field(...)
    token: str = Field(min_length=1)

    model_config = {
        "json_schema_extra": {
            "example": {
            "timestamp": "2023-11-01T14:00:00.000",
            "email": "maria@example.com",
            "caducidad": "2023-11-01T15:00:00.000",
            "token": "a1b2c3d4e5f6g7h8i9j0"
            }
        }
    }