from fastapi import APIRouter
from api.endpoints import auth, user

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(user.router, prefix="/user", tags=["user"])


@api_router.get("/")
async def root():
    return {"message": "Achba7 - API"}
