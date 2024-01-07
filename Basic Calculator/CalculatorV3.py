def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x/y

print("Choose your operation")
print("1. Add(+)")
print("2. Subtract(-)")
print("3. Multiply(x)")
print("4. Divide(/)")

while True:
    choice = str(input("Enter your operation: "))

    if choice in ("1", "2", "3", "4"):
        try:
            firstNumber = int(input("Enter your first number: "))
            secondNumber = int(input("Enter your second number: "))
        except ValueError:
            print("Please put a number brother :|")
            continue

        if choice == "1":
            print(firstNumber, "+", secondNumber, "=", addition(firstNumber,secondNumber))
        elif choice == "2":
            print(firstNumber, "-", secondNumber, "=", subtraction(firstNumber, secondNumber))
        elif choice == "3":
            print(firstNumber, "x", secondNumber, "=", multiplication(firstNumber, secondNumber))
        elif choice == "4":
            print(firstNumber, "/", secondNumber, "=", division(firstNumber, secondNumber))

        calculateAgain = input("Wanna go again? (Yes or No): ")
        if calculateAgain == "No":
            break
    else:
        print("Invalid Input")