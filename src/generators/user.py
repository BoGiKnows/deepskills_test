import re
import urllib
from faker import Faker

from src.enums.user_enums import UserErrors
from src.baseclasses.base_user import BuilderBaseClass


class User(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.fake = Faker('ru_RU')
        self.reset()

    def set_email(self, email='example@mail.ru'):
        if not email:
            self.result['email'] = self.fake.email()
        else:
            self.result['email'] = email
        return self

    def set_password(self, password=None):
        if not password:
            self.result['password'] = self.fake.password()
        else:
            self.result['password'] = password
        return self

    def set_password_confirmation(self, password_confirmation=None):
        if not password_confirmation:
            self.result['password_confirmation'] = self.result['password']
        else:
            self.result['password_confirmation'] = password_confirmation
        return self

    def set_name(self, name=None):
        if not name:
            self.result['name'] = self.fake.first_name()
        else:
            self.result['name'] = name

    def set_phone(self, phone=None):
        if not phone:
            self.result['phone'] = self.fake.phone_number()
        else:
            self.result['phone'] = phone

    def reset(self):
        self.set_password()
        self.set_password_confirmation()
        self.set_email()
        self.set_phone()
        self.set_name()
        return self


class Visitor(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.fake = Faker('ru_RU')
        self.reset()


    def set_name(self, name=None):
        if not name:
            self.result['name'] = urllib.parse.quote_plus(self.fake.first_name())
        else:
            self.result['name'] = urllib.parse.quote_plus(name)

    def set_email(self, email=None):
        if not email:
            self.result['email'] = self.fake.email()
        else:
            self.result['email'] = email
        return self

    def set_phone(self, phone=None):
        if not phone:
            self.result['phone'] = self.fake.phone_number()
        else:
            self.result['phone'] = phone

    def reset(self):
        self.set_name()
        self.set_phone()
        self.set_email()
        return self

    def __str__(self):
        return f'Name: {self.result["name"]}\n' \
               f'Email: {self.result["email"]}\n' \
               f'Phone: {self.result["phone"]}'


v = Visitor()
v.reset().set_name('Олег')
print(v.result)
