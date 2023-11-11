import pytest

@pytest.fixture(scope="module",autouse=True)
def testcase_calSum_firstExec():
    print("3.public test fixture in testcase {} directory".format('calSum'))
