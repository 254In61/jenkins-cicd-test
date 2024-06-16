"""
This module provides basic unit testing of functions created .
"""
from mymodules.calculator import subtract


VALUE_ONE = 50
VALUE_TWO = 2


def test_subtraction():
    """
    Function to test subtract() function
    """
    assert subtract(VALUE_ONE,VALUE_TWO) == 48
