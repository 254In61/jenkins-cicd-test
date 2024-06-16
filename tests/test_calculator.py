"""
This module provides basic unit testing of functions created .
"""

from mymodules.calculator import adding,subtract,multiply,divide

# Define variables
x = 50
y = 2

# Test addition function
def test_addition():
    """
    Function to test adding() function
    """
    assert adding(x,y) == 52

def test_subtraction():
    """
    Function to test subtract() function
    """
    assert subtract(x,y) == 48

def test_multiplication():
    """
    Function to test multiply() function
    """
    assert multiply(x,y) == 100

def test_division():
    """
    Function to test division() function
    """
    assert divide(x,y) == 25