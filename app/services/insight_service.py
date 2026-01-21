from typing import List
from app.models.activity import Activity

HEALTH_WEEKLY_THRESHOLD = 150

def wellness_warning(activities: List[Activity]) -> bool:
    """
    Returns True if weekly Health activity is below threshold.
    """
    health_minutes = sum(
        a.value for a in activities if a.activity_type == "Health"
    )
    return health_minutes < HEALTH_WEEKLY_THRESHOLD


def generate_recommendation(activities: List[Activity]) -> str:
    """
    Simple rule-based recommendation engine.
    """
    learning_minutes = sum(
        a.value for a in activities if a.activity_type == "Learning"
    )
    health_minutes = sum(
        a.value for a in activities if a.activity_type == "Health"
    )

    if learning_minutes >= 300 and health_minutes < HEALTH_WEEKLY_THRESHOLD:
        return "Consider rebalancing your growth plan."

    return "Your growth plan looks balanced."
