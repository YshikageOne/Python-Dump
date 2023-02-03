class Person:
    def setFullName(self, firstName, secondName):
        self.firstName= firstName
        self.secondName= secondName
    def printFullName(self):
        print(self.firstName, "", self.secondName)

name1 = str(input("Enter your first name: "))
name2 = str(input("Enter your second name: "))

personsName = Person()
personsName.setFullName(name1, name2)
personsName.printFullName()