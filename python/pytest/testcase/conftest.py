import pytest

@pytest.fixture(scope="module",autouse=True)
def testcase_firstExec():
    print("2.public test fixture in testcase directory")
