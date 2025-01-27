import pytest


@pytest.fixture
def setup():
    print("\nFirst setup")


def test_initial_check(setup):
    print("\nThis is my first test")

