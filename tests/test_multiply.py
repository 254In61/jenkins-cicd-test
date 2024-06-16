"""
This module provides basic unit testing of functions created.
"""
from mymodules.calculator import multiply


VALUE_ONE = 50
VALUE_TWO = 2


def test_multiplication():
    """
    Function to test multiply() function
    """
    assert multiply(VALUE_ONE,VALUE_TWO) == 100
