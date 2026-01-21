from fastapi import APIRouter
from app.api.activities import repo
from app.services.insight_service import generate_recommendation

router = APIRouter(prefix="/insights", tags=["Insights"])

@router.get("/optimization")
def optimization_insight():
    activities = repo.get_all()
    return {
        "recommendation": generate_recommendation(activities)
    }
