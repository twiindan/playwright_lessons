import pytest

# Setup is executed at the beginning of tests

@pytest.fixture
def setup():
    print("\nFirst setup")


def test_initial_check(setup):
    print("\nThis is my first test")

