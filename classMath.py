class Math:
    def operations(self, number1, number2):
        self.addition = number1 + number2
        self.subraction = number1 - number2
        self.multiplication = number1 * number2
        self.division = number1 / number2
    def printops(self, number1, number2):
        print("The sum of " + str(number1) + " and " + str(number2) + " is " + str(self.addition))
        print("The difference of " + str(number1) + " and " + str(number2) + " is " + str(self.subraction))
        print("The product of " + str(number1) + " and " + str(number2) + " is " + str(self.multiplication))
        print("The quotient of " + str(number1) + " and " + str(number2) + " is " + str(self.division))

mathtime = Math()

num1 = int(input(""))
num2 = int(input(""))

mathtime.operations(num1, num2)
mathtime.printops(num1, num2)
