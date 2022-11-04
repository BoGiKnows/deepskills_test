import requests
import pytest
import time
from faker import Faker
from selenium.webdriver.common.by import By

fake = Faker()


def test_registration(get_user_generator, setup):
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
    driver.find_element(By.XPATH, "// button[text() = 'Далее']").click()








