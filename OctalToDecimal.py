octalVal = int(input("Enter a string of octal digits: "))

num = 0
i = 0
decimalNum = 0
while octalVal!=0:
    a = octalVal%10
    if a>7:
        num = 1
        break
    decimalNum= decimalNum + (a * (8 ** i))
    i = i+1
    octalVal = int(octalVal/10)
print("The integer value is " + str(decimalNum))