import pytest


# Session scope is only executed one time at the beginning of test execution
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


class TestClass:
    def test_first_class_check(self, setup_class, setup_function, setup_module, setup_session):
        print("\nThis is my first class test")

    def test_second_class_check(self, setup_class, setup_function, setup_module, setup_session):
        print("\nThis is my second class test")


def test_initial_check(setup_function, setup_module, setup_session):
    print("\nThis is my first test")