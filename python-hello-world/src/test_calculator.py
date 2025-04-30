import pytest
from calculator import add, subtract, multiply, absolute, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-3, -2) == -1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

def test_absolute():
    assert absolute(-5) == 5
    assert absolute(0) == 0
    assert absolute(3) == 3

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 2) == -3
    assert divide(0, 1) == 0
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)