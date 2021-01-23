from pydantic import BaseModel


class AlertType(BaseModel):
    id: int
    name: str
    description: str
    photo: str
