import time

import pytest
from selenium.webdriver.common.by import By


RESET_URL = 'https://stage.deepskills.ru/my-way?action=reset-password'


@pytest.mark.parametrize('email', [
    'bogomolovog@mail.ru'
])
def test_auth_positive(email, setup):
    driver = setup
    driver.get(RESET_URL)
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()