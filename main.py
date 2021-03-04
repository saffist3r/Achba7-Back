from fastapi import FastAPI
from api.api import api_router

app = FastAPI(
    title="Achba7 - Backend",
    description="The backend for Achba7 project  for Wildlife Tracking",
    version="1.0.0",
)
app.include_router(api_router, prefix="/api")
