from datetime import timedelta
from typing import List
from app.models.activity import Activity

def calculate_consistency_score(activities: List[Activity]) -> float:
    """
    Consistency Index between 0.0 and 1.0.
    Measures how often activities are logged on consecutive days.
    """
    if not activities:
        return 0.0

    dates = sorted({a.timestamp.date() for a in activities})

    if len(dates) == 1:
        return 1.0

    consecutive_days = 0
    for i in range(1, len(dates)):
        if dates[i] - dates[i - 1] == timedelta(days=1):
            consecutive_days += 1

    score = consecutive_days / (len(dates) - 1)
    return round(score, 2)
