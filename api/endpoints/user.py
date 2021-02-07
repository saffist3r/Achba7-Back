from typing import List

from fastapi import APIRouter, Depends, HTTPException
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse

from sqlalchemy.orm import Session
from db import crud, models, schemas
from db.database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
async def create_user():
    return PlainTextResponse("Create")


@router.get("/users/", response_model=List[schemas.User])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/")
async def delete_user(request: Request):
    return PlainTextResponse("delete")




