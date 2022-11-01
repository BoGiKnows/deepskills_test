from pydantic import BaseModel, validator, EmailStr
import re

from src.enums.user_enums import UserErrors


class Registration(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str
    password_confirmation: str

    @validator('email')
    def check_email(cls, email):
        regex = r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
        if re.search(regex, email):
            return email
        else:
            raise ValueError(UserErrors.EMAIL_ERROR.value)
