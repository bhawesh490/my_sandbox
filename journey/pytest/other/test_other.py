import pytest


# write a test case to check if if a given args is a integer
@pytest.mark.runthis
def test_integer():
    print("Testing integer.....")
    assert isinstance(1, int), "This is not an integer"
