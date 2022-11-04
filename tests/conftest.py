import pytest
import requests
from src.generators.user import User


# @pytest.fixture
# def get_visitor_generator():
#     """
#     Generating visitor object and throw it to tests
#     """
#     visitor = Visitor()
#     visitor.reset()
#     return visitor


@pytest.fixture
def get_user_generator():
    """
    Generating user object and throw it to tests
    """
    user = User()
    user.reset()
    return user
