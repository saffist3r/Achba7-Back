from pydantic import BaseModel


class Logs(BaseModel):
    token: str
    date: str
    user: int
