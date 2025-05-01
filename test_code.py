from base_file import a,b,add_two_numbers, subtract_two_numbers, multiply_two_numbers, divide_two_numbers

print(a,b,add_two_numbers(1,2), subtract_two_numbers(5,3), multiply_two_numbers(2,3), divide_two_numbers(6,2))

# the pytest code is in the test_code.py file
# test_code.py

import pytest
def test_add_two_numbers():
    assert add_two_numbers(1, 2) == 3
    assert add_two_numbers(-1, 1) == 0
    assert add_two_numbers(0, 0) == 0

def test_subtract_two_numbers():
    assert subtract_two_numbers(5, 3) == 2
    assert subtract_two_numbers(0, 0) == 0
    assert subtract_two_numbers(-1, -1) == 0
    assert subtract_two_numbers(1, -1) == 2

def test_multiply_two_numbers():
    assert multiply_two_numbers(2, 3) == 6
    assert multiply_two_numbers(-1, 1) == -1
    assert multiply_two_numbers(0, 5) == 0

def test_divide_two_numbers():
    assert divide_two_numbers(6, 2) == 3
    assert divide_two_numbers(-6, -2) == 3
    with pytest.raises(ValueError):
        divide_two_numbers(1, 0)    
