import pytest
from faker import Faker

from models.user import User


@pytest.fixture
def random_user() -> User:
    return User(
        email=Faker().email(),
        username=Faker().name(),
        firstname=Faker().name(),
        lastname=Faker().name(),
        password=Faker().password(),
    )
