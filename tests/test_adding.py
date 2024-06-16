"""
This module provides basic unit testing of functions created.
"""
from mymodules.calculator import adding,Test_Number_One, Test_Number_Two

# Test addition function
def test_addition():
    """
    Function to test adding() function
    """
    assert adding(Test_Number_One,Test_Number_Two) == 52
