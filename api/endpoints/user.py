from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse

router = APIRouter()


@router.post("/")
async def create_user():
    return PlainTextResponse("Create")


@router.get("/")
async def get_user():
    return PlainTextResponse("Show user")


@router.delete("/")
async def delete_user(request: Request):
    return PlainTextResponse("delete")



