"""
This module provides basic unit testing of functions created.
"""
from mymodules.calculator import divide


Number_One = 50
Number_Two = 2


def test_division():
    """
    Function to test division() function
    """
    assert divide(Number_One,Number_Two) == 25
