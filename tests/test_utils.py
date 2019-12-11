import lib.utils as utils
import pytest

@pytest.mark.parametrize(
    'input,expected_output',
    [
        (10, 20),
        (0, 0),
        (-5, -10),
     ]
)
def test_twice_1(input, expected_output):
    assert utils.twice(input) == expected_output


def test_thrice_1():
    assert utils.thrice(10) == 30, f"thrice(10) != 30"


def test_thrice_2():
    assert utils.thrice(0) == 0, f"thrice(0) != 0"


def test_thrice_3():
    assert utils.thrice(-5) == -15, f"thrice(-5) != -15"