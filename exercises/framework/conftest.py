import pytest
from faker import Faker

from exercises.framework.models.user import User


@pytest.fixture(scope="session", autouse=True)
def random_user() -> User:
    return User(
        email=Faker().email(),
        username=Faker().name(),
        password=Faker().password(),
    )
