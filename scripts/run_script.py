"""
This module provides basic script run to test the created fuctions in mymodules/.
The code is as simple as possible to achieve the objective.
"""

from mymodules.calculator import adding, subtract, multiply, divide

X = 2


def display(number_input):
    """
    Function that displays the output
    """
    print(f"{number_input} + {X} = {adding(number_input, X)} ")
    print(f"{number_input} - {X} = {subtract(number_input, X)} ")
    print(f"{number_input} * {X} = {multiply(number_input, X)} ")
    print(f"{number_input} /{X} = {divide(number_input, X)}")


def main():
    """
    Main function that runs the code.
    """
    arr1 = [22, 246, 67, 888]
    for item in arr1:
        print("\n=======")
        display(item)


if __name__ == "__main__":
    main()
