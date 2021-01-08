from fastapi import APIRouter
from connector import databasemanager as db
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse
from models import userModel
router = APIRouter()


def getToken(email, password):
    return (db.getToken(email, password))


@router.post("/auth/")
async def create_user(user: userModel):
    return db.get_token(user.email, user.password)

