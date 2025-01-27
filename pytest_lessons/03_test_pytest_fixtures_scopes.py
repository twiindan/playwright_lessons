import pytest


@pytest.fixture(scope="function")
def setup_function():
    print("\nFunction Setup")


@pytest.fixture(scope="module")
def setup_module():
    print("\nModule setup")


def test_initial_check(setup_function, setup_module):
    print("\nThis is my first test")


def test_second_check(setup_function, setup_module):
    print("\nThis is my second test")
