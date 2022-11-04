import requests
import pytest
import urllib
from faker import Faker


# urllib.parse.quote_plus(user.result['name'])
fake = Faker()


def test_email(get_user_generator):
    user = get_user_generator
    user.set_name(' sdf  ')
    visitor = {
        'name': user.result['name'],
        'phone': user.result['phone'],
        'email': user.result['email'],
    }

    vis_req = requests.post('https://stage.deepskills.ru/api/v1/visitors', json=visitor)
    user_req = requests.post('https://stage.deepskills.ru/auth', json=user.result)
    print(user_req)
    print(vis_req)
    print(vis_req.json())


