"""
This module provides basic unit testing of functions created.
"""
from mymodules.calculator import divide


VALUE_ONE = 50
VALUE_TWO = 2


def test_division():
    """
    Function to test division() function
    """
    assert divide(VALUE_ONE,VALUE_TWO) == 25
