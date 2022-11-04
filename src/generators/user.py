import re
import urllib
from faker import Faker

from src.enums.user_enums import UserErrors
from src.baseclasses.base_user import BuilderBaseClass


class User(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.fake = Faker()
        self.reset()

    def set_email(self, email=None):
        if email is None:
            self.result['email'] = self.fake.email()
        else:
            self.result['email'] = email
        return self

    def set_password(self, password='asDSAd4312432r*(0'):
        self.result['password'] = password
        return self

    def set_password_confirmation(self, password_confirmation=None):
        if password_confirmation is None:
            self.result['password_confirmation'] = self.result['password']
        else:
            self.result['password_confirmation'] = password_confirmation
        return self

    def set_name(self, name=None):
        if name is None:
            self.result['name'] = self.fake.first_name()
        else:
            self.result['name'] = name
        return self

    def set_phone(self, phone='89183454565'):
        self.result['phone'] = phone
        return self

    def reset(self):
        self.set_password()
        self.set_password_confirmation()
        self.set_email()
        self.set_phone()
        self.set_name()
        return self



