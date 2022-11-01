import pytest


@pytest.mark.parametrize('email', [
    'example@mail.ru',
    'dfs343#$#dfsdf@dfgs.er',
    ' example@mail.ru',
    'exam ple@mail.ru',
    'example@mail.ru ',
    ' ',
    r'example@mail.ru\n',
    ''
])
def test_email(email, get_user_generator):
    get_user_generator.set_email(email).build()
