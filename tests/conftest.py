import pytest

from src.generators.user import User


@pytest.fixture
def get_user_generator():
    """
    Generating user object and throw it to tests
    """
    return User()