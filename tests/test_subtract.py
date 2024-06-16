"""
This module provides basic unit testing of functions created .
"""
from mymodules.calculator import subtract


Number_One = 50
Number_Two = 2


def test_subtraction():
    """
    Function to test subtract() function
    """
    assert subtract(Number_One,Number_Two) == 48
