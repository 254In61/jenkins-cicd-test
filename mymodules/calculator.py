"""
This module provides basic functions to call when testing Jenkins cicd pipeline deployment.
The code is as simple as possible to achieve the objective.
"""


def multiply(first_number, second_number):
    """Function multiplies 2 numbers and returns the result."""
    return first_number * second_number


def divide(first_number, second_number):
    """Function divides a number with the other returns the divide result.
    Also error checks for zero denominator"""
    if second_number == 0:
        raise ValueError("Cannot divide by zero")
    return first_number / second_number


def adding(first_number, second_number):
    """Function add numbers and returns the value"""
    return first_number + second_number


def subtract(first_number, second_number):
    """Function subtracts one number from the other and returns the value"""
    return first_number - second_number
