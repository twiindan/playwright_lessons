import pytest


# Is possible define any function as a fixture and pass it as a parameter in a test.
@pytest.fixture
def setup():
    print("\nFirst setup")
    return 'parameter'


def test_initial_check(setup):
    print("\nThis is my first test")
    assert setup == 'parameter'
