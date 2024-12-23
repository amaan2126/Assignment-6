import pytest
from fibonacci import Fibonacci

def test_non_integer():
    with pytest.raises(ValueError):
        Fibonacci("Not integer")
    with pytest.raises(ValueError):
        Fibonacci(3.14)

def test_zero_value():
    assert list(Fibonacci(0)) == [0]


def test_one_value():
    assert list(Fibonacci(1)) == [0, 1]

def test_two_value():
    assert list(Fibonacci(2)) == [0, 1, 1]

def test_four_value():
    assert list(Fibonacci(4)) == [0, 1, 1, 2, 3]

def test_ten_value():
    assert list(Fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_negative_value():
    assert list(Fibonacci(-5)) == []