import pytest


@pytest.fixture(scope='session')
def setup_session():
    print("\nSession Setup")


@pytest.fixture(scope="function")
def setup_function():
    print("\nMethod Setup")


@pytest.fixture(scope="class")
def setup_class():
    print("\nClass setup")


@pytest.fixture(scope="module")
def setup_module():
    print("\nModule setup")

