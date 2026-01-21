from fastapi import APIRouter
from app.schemas.activity_schema import ActivityCreate
from app.repository.in_memory import InMemoryActivityRepository

router = APIRouter(prefix="/activities", tags=["Activities"])

# Single shared in-memory repository
repo = InMemoryActivityRepository()

@router.post("")
def log_activity(activity: ActivityCreate):
    repo.add(activity)
    return {
        "message": "Activity logged successfully",
        "activity": activity
    }
