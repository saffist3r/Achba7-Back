from fastapi import APIRouter
from api.endpoints import auth, user
from db import crud, models, schemas
from db.database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(user.router, prefix="/user", tags=["user"])


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api_router.get("/")
async def root():
    return {"message": "Achba7 - API"}
