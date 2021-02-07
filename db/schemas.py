from pydantic import BaseModel


class AlertType(BaseModel):
    id: int
    name: str
    description: str
    photo: str

    class Config:
        orm_mode = True


class Animal(BaseModel):
    id: int
    name: str
    photo: str
    type: int

    class Config:
        orm_mode = True


class AnimalType(BaseModel):
    id: int
    name: str
    description: str
    photo: str

    class Config:
        orm_mode = True


class Logs(BaseModel):
    token: str
    date: str
    user: int

    class Config:
        orm_mode = True


class Observation(BaseModel):
    id: int
    type: str
    date: str
    long: str
    lat: str
    desc: str
    photo: str

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    name: str
    surname: str
    photo: str
    fonction: str
    date: str
    email: str
    telephone: str
    city: str
    country: str
    password: str

    class Config:
        orm_mode = True
