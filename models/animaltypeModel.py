from pydantic import BaseModel


class AnimalType(BaseModel):
    id: int
    name: str
    description: str
    photo: str
