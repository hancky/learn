import pytest

@pytest.fixture(scope="session",autouse=True)
def firstExec():
    print("\n1.public test fixture in root directory")
