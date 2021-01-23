from pydantic import BaseModel


class Observation(BaseModel):
    id: int
    type: str
    date: str
    long: str
    lat: str
    desc: str
    photo: str
