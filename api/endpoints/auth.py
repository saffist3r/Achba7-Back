from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm


from starlette.responses import PlainTextResponse, JSONResponse
from models import logsModel
router = APIRouter()


@router.post("/", response_model=logsModel)
async def create_session(form_data: OAuth2PasswordRequestForm = Depends()):
    
    return PlainTextResponse("Create Session and generate Token")

