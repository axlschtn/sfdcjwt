from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

class UserUpdate(BaseModel):
    data: User
