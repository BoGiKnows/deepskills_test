import requests
import pytest
import time
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

VISITOR_URL = 'https://stage.deepskills.ru/api/v1/visitors'
REGISTRATION_URL = 'https://stage.deepskills.ru/auth'

fake = Faker()


@pytest.mark.skip('selenium not used, only requests')
@pytest.mark.parametrize('email, password', [
    ('dsf', '45dsfsdf@#4334534543'),
    (fake.email(), '23'),
    (fake.email(), ''),
    ('', '45dsfsdf@#4334534543'),
    ('dsfsdf.ru', '45dsfsdf@#4334534543')

])
def test_registration(email, password, get_user_generator):
    user = get_user_generator
    user.set_email(email)
    user.set_password(password).set_password_confirmation()
    visitor = user.make_visitor()
    vis_req = requests.post(url=VISITOR_URL, json=visitor)
    user_req = requests.post(url=REGISTRATION_URL, json=user.result)
    assert user_req.status_code != 200, 'Status code is not what we expected'


def test_registration_positive(get_user_generator, setup):
    user = get_user_generator
    visitor = {
        'name': user.result['name'],
        'phone': user.result['phone'],
        'email': user.result['email'],
    }
    driver = setup
    driver.find_element(By.XPATH, "//input[@placeholder='Ваше имя']").send_keys(user.result['name'])
    driver.find_element(By.XPATH, "//input[@placeholder='Ваш e-mail']").send_keys(user.result['email'])
    driver.find_element(By.XPATH, "//input[@placeholder='Ваш номер телефона']").send_keys(user.result['phone'])
    driver.find_element(By.XPATH, "//button[text() = 'Далее']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, "//input[@placeholder='Введите пароль']").send_keys(user.result['password'])
    driver.find_element(By.XPATH, "//input[@placeholder='Повторите пароль']").send_keys(
        user.result['password_confirmation'])
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


@pytest.mark.parametrize('email, password', [
    ('dsf', '45dsfsdf@#4334534543'),
    (fake.email(), '23'),
    (fake.email(), ''),
    ('', '45dsfsdf@#4334534543'),
    ('dsfsdf.ru', '45dsfsdf@#4334534543')

])
def test_registration_negative(email, password, get_user_generator, setup):
    user = get_user_generator
    user.set_email(email)
    user.set_password(password).set_password_confirmation()
    visitor = {
        'name': user.result['name'],
        'phone': user.result['phone'],
        'email': user.result['email'],
    }
    driver = setup
    driver.find_element(By.XPATH, "//input[@placeholder='Ваше имя']").send_keys(user.result['name'])
    driver.find_element(By.XPATH, "//input[@placeholder='Ваш e-mail']").send_keys(user.result['email'])
    driver.find_element(By.XPATH, "//input[@placeholder='Ваш номер телефона']").send_keys(user.result['phone'])
    try:
        driver.find_element(By.XPATH, "//button[text() = 'Далее']").click()
    except ElementClickInterceptedException:
        pass
    else:
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Введите пароль']").send_keys(user.result['password'])
        driver.find_element(By.XPATH, "//input[@placeholder='Повторите пароль']").send_keys(
            user.result['password_confirmation'])
        try:
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
        except ElementClickInterceptedException:
            pass


@pytest.mark.parametrize('name', [
    'asfdas123412#$#$',
    ' Oleg',
    'Ol eg',
    'Oleg ',
    r'\n',
    r'\r',
    'a',
    'SELECT * FROM USERS;',
    '<script>alert("I hacked this!")</script>',
])
def test_name_positive(name, get_user_generator, setup):
    user = get_user_generator
    user.set_name(name)
    driver = setup
    driver.find_element(By.XPATH, "//input[@placeholder='Ваше имя']").send_keys(user.result['name'])
    driver.find_element(By.XPATH, "//input[@placeholder='Ваш e-mail']").send_keys(user.result['email'])
    driver.find_element(By.XPATH, "//input[@placeholder='Ваш номер телефона']").send_keys(user.result['phone'])
    driver.find_element(By.XPATH, "//button[text() = 'Далее']").click()


@pytest.mark.parametrize('name', [
    ' ',
    '\n',
    'a' * 1000,
    '23123123123',
])
def test_name_negative(name, get_user_generator, setup):
    user = get_user_generator
    user.set_name(name)
    driver = setup
    driver.find_element(By.XPATH, "//input[@placeholder='Ваше имя']").send_keys(user.result['name'])
    driver.find_element(By.XPATH, "//input[@placeholder='Ваш e-mail']").send_keys(user.result['email'])
    driver.find_element(By.XPATH, "//input[@placeholder='Ваш номер телефона']").send_keys(user.result['phone'])
    try:
        driver.find_element(By.XPATH, "//button[text() = 'Далее']").click()
        raise ValueError('Warning! Website accepted invalid data')
    except ElementClickInterceptedException:
        pass


fake_email = fake.email()
@pytest.mark.parametrize('email', [
    'asfdas123412#$#$' + fake_email,
    'Ol eg' + fake_email,
    ' ',
    fake_email + r'\n',
    fake_email + r'\r',
    '\n',
    'a',
    'SELECT * FROM USERS;',
    '',
    'неАСКИ@example.ru'
    '<script>alert("I hacked this!")</script>',
    'a' * 1000 + fake_email,
])
def test_email_negative(email, get_user_generator, setup):
    user = get_user_generator
    user.set_email(email)
    print(user.result['email'])
    driver = setup
    driver.find_element(By.XPATH, "//input[@placeholder='Ваше имя']").send_keys(user.result['name'])
    driver.find_element(By.XPATH, "//input[@placeholder='Ваш e-mail']").send_keys(user.result['email'])
    driver.find_element(By.XPATH, "//input[@placeholder='Ваш номер телефона']").send_keys(user.result['phone'])
    try:
        driver.find_element(By.XPATH, "//button[text()='Далее']").click()
        raise ValueError('Warning! Website accepted invalid data')
    except ElementClickInterceptedException:
        pass


