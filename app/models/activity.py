from datetime import datetime
from typing import Literal
from pydantic import BaseModel

class Activity(BaseModel):
    goal_id: str
    activity_type: Literal["Learning", "Health"]
    value: int
    timestamp: datetime
