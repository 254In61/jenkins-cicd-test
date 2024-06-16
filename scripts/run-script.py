
from mymodules.calculator import adding,subtract,multiply,divide

X = 2

def main():
    arr1 = [ 22,246,67,888]

    for item in arr1:
        print("\n=======")
        print(f"{item} + {X} = {adding(item,X)} ")
        print(f"{item} - {X} = {subtract(item, X)} ")
        print(f"{item} * {X} = {multiply(item,X)} ")
        print(f"{item} /{X} = {divide(item,X)}")


if __name__ == "__main__":
    main()