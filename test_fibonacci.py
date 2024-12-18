import pytest
from fibonacci import Fibonacci

def test_non_integer():
    with pytest.raises(ValueError):
        Fibonacci("Not integer")
    with pytest.raises(ValueError):
        Fibonacci(3.14)
