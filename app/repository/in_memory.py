from typing import List
from app.models.activity import Activity
from app.repository.base import ActivityRepository

class InMemoryActivityRepository(ActivityRepository):
    def __init__(self):
        self._activities: List[Activity] = []

    def add(self, activity: Activity) -> None:
        self._activities.append(activity)

    def get_by_goal(self, goal_id: str) -> List[Activity]:
        return [a for a in self._activities if a.goal_id == goal_id]

    def get_all(self) -> List[Activity]:
        return self._activities
