from fastapi import APIRouter
from app.api.activities import repo
from app.services.journal_service import calculate_consistency_score
from app.services.insight_service import wellness_warning

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/{goal_id}")
def get_dashboard(goal_id: str):
    activities = repo.get_by_goal(goal_id)

    return {
        "goal_id": goal_id,
        "total_activities": len(activities),
        "by_type": {
            "Learning": sum(1 for a in activities if a.activity_type == "Learning"),
            "Health": sum(1 for a in activities if a.activity_type == "Health"),
        },
        "consistency_score": calculate_consistency_score(activities),
        "wellness_warning": wellness_warning(activities)
    }
