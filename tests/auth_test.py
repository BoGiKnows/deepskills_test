import pytest
from selenium.webdriver.common.by import By


AUTH_URL = 'https://stage.deepskills.ru/my-way?action=sign-in'


@pytest.mark.parametrize('email, password', [
    ('example@example.example', 'example')
])
def test_auth_positive(email, password, get_user_generator, setup):
    user = get_user_generator
    user.set_email(email)
    user.set_password(password).set_password_confirmation()
    visitor = {
        'name': user.result['name'],
        'phone': user.result['phone'],
        'email': user.result['email'],
    }
    driver = setup
    driver.get(AUTH_URL)
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys(user.result['email'])
    driver.find_element(By.XPATH, "//input[@placeholder='Введите пароль']").send_keys(
        user.result['password'])
    driver.find_element(By.XPATH, "//button[@type='submit']").click()