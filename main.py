from fastapi import FastAPI
from app.api.activities import router as activities_router
from app.api.dashboard import router as dashboard_router
from app.api.insights import router as insights_router

app = FastAPI(title="Life Design Backend Service")

app.include_router(activities_router)
app.include_router(dashboard_router)
app.include_router(insights_router)
