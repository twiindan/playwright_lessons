import pytest


@pytest.fixture(scope="function")
def setup_function():
    print("\nMethod Setup")


# Class scope is executed only at the beginning of the Test Class
@pytest.fixture(scope="class")
def setup_class():
    print("\nClass setup")


@pytest.fixture(scope="module")
def setup_module():
    print("\nModule setup")


# You can group several tests in the same Class.
class TestClass:
    def test_first_class_check(self, setup_class, setup_function, setup_module):
        print("\nThis is my first class test")

    def test_second_class_check(self, setup_class, setup_function, setup_module):
        print("\nThis is my second class test")
