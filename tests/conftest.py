import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.generators.user import User


@pytest.fixture
def get_user_generator():
    """
    Generating user object and throw it to tests
    """
    user = User()
    user.reset()
    return user


@pytest.fixture
def autosetter():
    pass


@pytest.fixture
def get_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture()
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


@pytest.fixture
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://stage.deepskills.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
