import pytest

# Reusable function

@pytest.fixture(scope='session')
def prework():
    print("Browser Login Page")
    yield
    print("Everything done")



@pytest.fixture(scope='session')
def postwork():
    print("Browser logout Page")
    return "END"
