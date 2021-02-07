from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm


from starlette.responses import PlainTextResponse, JSONResponse
from models import logsModel
router = APIRouter()


@router.post("/")

async def create_session():
    
    return PlainTextResponse("Create Session and generate Token")

