class numberList:
    def __int__(self,numList):
        self.numList = numList


class Operation(numberList):
    def __int__(self,numList):
        super().__int__(numList)

    def addition(self,numList):
        self.numList = numList
        self.result = self.numList[0]

        for i in range(len(numList)-1):
            self.result += self.numList.pop(1)
        print("The sum is", self.result)

    def subtraction(self,numList):
        self.numList = numList
        self.result = self.numList[0]

        for i in range(len(numList) - 1):
            self.result -= self.numList.pop(1)
        print("The difference is", self.result)

    def multiplication(self,numList):
        self.numList = numList
        self.result = self.numList[0]

        for i in range(len(numList) - 1):
            self.result *= self.numList.pop(1)
        print("The product is", self.result)

    def division(self,numList):
        self.numList = numList
        self.result = self.numList[0]

        for i in range(len(numList) - 1):
            if self.numList[1] == 0:
                print("Can't divide by zero.")
                return
            self.result /= self.numList.pop(1)
        print("The quotient is", self.result)


print("Choose your operation")
print("1. Add(+)")
print("2. Subtract(-)")
print("3. Multiply(x)")
print("4. Divide(/)")

while True:
    choice = str(input("Enter your operation: "))
    mathTime = Operation()

    if choice in ("1", "2", "3", "4"):
        if choice == "1":
            num = []
            try:
                userInput = input("Enter a number or press enter to quit: ")
            except ValueError:
                print("Please put a number or press enter brother :|")
                continue

            while userInput != "":
                num.append(float(userInput))
                try:
                    userInput = input("Enter a number or press enter to quit: ")
                except ValueError:
                    print("Please put a number or press enter brother :|")
                    continue

            mathTime.addition(num)

        if choice == "2":
            num = []
            try:
                userInput = input("Enter a number or press enter to quit: ")
            except ValueError:
                print("Please put a number or press enter brother :|")
                continue

            while userInput != "":
                num.append(float(userInput))
                try:
                    userInput = input("Enter a number or press enter to quit: ")
                except ValueError:
                    print("Please put a number or press enter brother :|")
                    continue

            mathTime.subtraction(num)

        if choice == "3":
            num = []
            try:
                userInput = input("Enter a number or press enter to quit: ")
            except ValueError:
                print("Please put a number or press enter brother :|")
                continue

            while userInput != "":
                num.append(float(userInput))
                try:
                    userInput = input("Enter a number or press enter to quit: ")
                except ValueError:
                    print("Please put a number or press enter brother :|")
                    continue

            mathTime.multiplication(num)

        if choice == "4":
            num = []
            try:
                userInput = input("Enter a number or press enter to quit: ")
            except ValueError:
                print("Please put a number or press enter brother :|")
                continue

            while userInput != "":
                num.append(float(userInput))
                try:
                    userInput = input("Enter a number or press enter to quit: ")
                except ValueError:
                    print("Please put a number or press enter brother :|")
                    continue

            mathTime.division(num)

        calculateAgain = input("Wanna go again? (yes or no): ")
        if calculateAgain == "no":
            break
    else:
        print("Invalid Input")