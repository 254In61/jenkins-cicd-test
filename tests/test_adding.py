"""
This module provides basic unit testing of functions created.
"""
from mymodules.calculator import adding


Number_One = 50
Number_Two = 2


# Test addition function
def test_addition():
    """
    Function to test adding() function
    """
    assert adding(Number_One,Number_Two) == 52
