"""
This module provides basic unit testing of functions created.
"""
from mymodules.calculator import divide,Test_Number_One, Test_Number_Two


def test_division():
    """
    Function to test division() function
    """
    assert divide(Test_Number_One,Test_Number_Two) == 25
