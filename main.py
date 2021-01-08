from starlette.responses import JSONResponse, Response

from fastapi import FastAPI
from connector import databasemanager

app = FastAPI()


@app.post("/token/")
async def root(reuzqr):
    return JSONResponse({"TEST": databasemanager.verify_token("aaaaa", 1)})


@app.get("/")
async def root():
    return {"message": "Hello World"}
