import requests
import pytest
import time
from faker import Faker
from selenium.webdriver.common.by import By

fake = Faker()


@pytest.mark.skip("can't extract json from selenium yet")
def test_registration_selenium(get_user_generator, setup):
    user = get_user_generator
    visitor = {
        'name': user.result['name'],
        'phone': user.result['phone'],
        'email': user.result['email'],
    }
    driver = setup
    driver.find_element(By.XPATH, "//input[@placeholder='Ваше имя']").send_keys('Oleg')
    driver.find_element(By.XPATH, "//input[@placeholder='Ваш e-mail']").send_keys(user.result['email'])
    driver.find_element(By.XPATH, "//input[@placeholder='Ваш номер телефона']").send_keys(user.result['phone'])
    driver.find_element(By.XPATH, "//button[text() = 'Далее']").click()


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
    visitor = {
        'name': user.result['name'],
        'phone': user.result['phone'],
        'email': user.result['email'],
    }

    vis_req = requests.post('https://stage.deepskills.ru/api/v1/visitors', json=visitor)
    user_req = requests.post('https://stage.deepskills.ru/auth', json=user.result)
    assert user_req.status_code != 200, 'Status code is not what we expected'





