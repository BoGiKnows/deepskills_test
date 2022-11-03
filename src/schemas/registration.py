from pydantic import BaseModel, validator, EmailStr
import re


from src.enums.user_enums import UserErrors


class Visitors:
    name: str
    phone: str
    email: str


class Auth(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str
    name: str
    phone: str

