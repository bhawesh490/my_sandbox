import pytest


@pytest.mark.runthis
def test_even_number_in_list():
    """
    Test case to check if all numbers in the list are even.
    """
    li = [2, 8, 10, 12]
    print("Testing...")
    assert all([i % 2 == 0 for i in li]), "List has at least one odd number.."


def test_first_letter_uppercase():
    """
    Test case to check if the first letter of a given text is uppercase.
    """
    text = "Python"
    assert text[0].isupper(), "First letter is not uppercase.."


@pytest.mark.runthis
def test_list_at_least_three_elements():
    """
    Test case to check if a list has at least three elements.
    """
    li = [1, 2, 3, 4, 8, 19, 10]
    assert len(li) >= 3, "List does not have at least 3 elements."


def test_key_has_device():
    """
    Test to check if the 'device' key is present in the dictionary.
    """
    di = {"name": "John", "age": 23, "device": "mac"}
    assert "device" in di, "device key is not in dictionary.."
