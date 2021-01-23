from pydantic import BaseModel


class Animal(BaseModel):
    id: int
    name: str
    photo: str
    type: int
