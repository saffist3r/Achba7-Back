from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse
from models import userModel
router = APIRouter()


@router.post("/user/create/")
async def create_user(user: userModel):
    return PlainTextResponse("OK")


@router.get("/user/")
async def get_user():
    return JSONResponse(status_code=204)


@router.post("/user/delete/")
async def delete_user(request: Request):
    return PlainTextResponse("OK")



