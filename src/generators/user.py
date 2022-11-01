import re

from src.enums.user_enums import UserErrors
from src.baseclasses.base_user import BuilderBaseClass


class User(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.reset()

    def set_email(self, email="example@mail.ru"):
        regex = r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
        if re.search(regex, email):
            self.result['email'] = email
        else:
            raise ValueError(UserErrors.EMAIL_ERROR.value)

        return self

    def set_password(self, password='Aa1!Bb2@Cc3#'):
        self.result['password'] = password
        return self

    def set_password_confirmation(self, password_confirmation='Aa1!Bb2@Cc3#'):
        self.result['password_confirmation'] = password_confirmation
        return self

    def reset(self):
        self.set_password()
        self.set_password_confirmation()
        self.set_email()
        return self
