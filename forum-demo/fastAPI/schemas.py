from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str
    email: str