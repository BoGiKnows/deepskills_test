from enum import Enum
from .pyenum import PyEnum
from faker import Faker

fake = Faker()


class UserErrors(Enum):
    EMAIL_ERROR = "Invalid Email"


