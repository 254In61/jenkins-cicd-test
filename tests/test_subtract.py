"""
This module provides basic unit testing of functions created .
"""
from mymodules.calculator import subtract,Test_Number_One, Test_Number_Two


def test_subtraction():
    """
    Function to test subtract() function
    """
    assert subtract(Test_Number_One,Test_Number_Two) == 48
