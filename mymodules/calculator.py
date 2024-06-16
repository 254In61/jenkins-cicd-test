# Function for multiplying
def multiply(x,y):
    """ Function multiplies 2 numbers and returns the result."""
    return x * y

# Function for division
def divide(x,y):
    """ Function divides a number with the other returns the divide result. Also error checks for zero denominator"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x/y

# Function for addition
def adding(x,y):
    """ Function add numbers and returns the value"""
    return x + y

# Function for subtraction
def subtract(x,y):
    """Function subtracts one number from the other and returns the value"""
    return x-y