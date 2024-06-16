"""
This module provides basic unit testing of functions created.
"""
from mymodules.calculator import multiply


Number_One = 50
Number_Two = 2


def test_multiplication():
    """
    Function to test multiply() function
    """
    assert multiply(Number_One,Number_Two) == 100
