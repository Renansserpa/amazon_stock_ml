from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr


class Message(BaseModel):
    message: str

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

class NasdaqReportLine(BaseModel):
    date: date
    close: float
    volume: int
    open: float
    high: float
    low: float