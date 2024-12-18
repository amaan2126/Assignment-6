import pytest
from fibonacci import Fibonacci

def test_non_integer():
    with pytest.raises(ValueError):
        Fibonacci("Not integer")
    with pytest.raises(ValueError):
        Fibonacci(3.14)

def test_zero_value():
    assert list(Fibonacci(0)) == [0]