import math

from numpy import add,subtract,multiply,divide


def printIntro():
    print("This is a simple calculator.")
print("Select an operation:\n1) Add\n2) Subtract\n3) Divide\n4) Multiply")

while True:
    operator = input("Enter your choice of + - / *: \n")

    if operator in('+', '-', '/', '*'):
        #continue asking for numbers until user ends
        #store numbers in an array

        list = []
        num = int(input("What are your numbers?: "))
        for n in range(num):
            numbers = float(input("What are your numbers?: "))
        list.append(numbers)
        if n == '':
            break

        if operator == '+':
            print(add(list))

        if operator == '-':
            print(subtract(list))

        if operator == '/':
            print(divide(list))

        if operator == '*':
            print(multiply(list))
    else:
        break