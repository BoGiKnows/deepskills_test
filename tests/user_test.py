import requests
import pytest
import urllib
from faker import Faker

from src.generators.user import Visitor, User
# urllib.parse.quote_plus('Олег')
fake = Faker()



def test_email(get_visitor_generator, get_user_generator):
    visitor = get_visitor_generator
    vis_req = requests.post('https://stage.deepskills.ru/api/v1/visitors', json=visitor)
    print(vis_req)



# def test_email():
#     req = {
#       "email": "exampl1221@mail.ru",
#       "password": "sdsad23e3JKJ$#%",
#       "password_confirmation": "sdsad23e3JKJ$#%",
#       "name": 'Олег',
#       "phone": '89182345647'
#     }
#     # res = requests.post('https://stage.deepskills.ru/auth', json=req)
#     url_auth = 'https://stage.deepskills.ru/auth'
#     url = 'https://stage.deepskills.ru/api/v1/visitors'
#     req1 = {
#         'name': 'Олег',
#         'phone': '89182754645',
#         'email': 'exampl1221@mail.ru'
#     }
#     # res1 = requests.post(url, json=req1)
#     res1 = requests.post(url_auth, json=req)
#
#     print(res1)
#     print(res1.json())
#
# print(test_email())



# @pytest.mark.parametrize('email', [
#     'example@mail.ru',
#     'dfs343#$#dfsdf@dfgs.er',
#     ' example@mail.ru',
#     'exam ple@mail.ru',
#     'example@mail.ru ',
#     ' ',
#     r'example@mail.ru\n',
#     ''
# ])
# def test_email(email, get_user_generator):
#     get_user_generator.set_email(email).build()
