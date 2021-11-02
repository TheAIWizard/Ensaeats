from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    surname: str
    username: str
    password: str
