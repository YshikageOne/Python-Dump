
class shirt:

    def __init__(self, color, size):
        self.color = color
        self.size = size

    def displayDetails(self):
        print("Shirt Color: " + self.color)
        print("Shirt Size: " + self.size)

userColor = str(input("What's the color of your shirt?"))
userSize = str(input("What's the size of your shirt?"))


myShirt = shirt(userColor, userSize)
myShirt.displayDetails()
