from pydantic import BaseModel


class User(BaseModel):
    name : str
    surname : str
    photo : str
    fonction : str
    date_naissance : str
    email : str
    tel : str
    town: str
    country : str
    password : str
