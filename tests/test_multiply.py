"""
This module provides basic unit testing of functions created.
"""
from mymodules.calculator import multiply,Test_Number_One, Test_Number_Two


def test_multiplication():
    """
    Function to test multiply() function
    """
    assert multiply(Test_Number_One,Test_Number_Two) == 100
