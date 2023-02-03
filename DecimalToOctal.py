decimalNum = int(input("Enter a decimal integer: "))
print("Quotient Remainder Octal")

octal = 0
count = 1

while decimalNum !=0:
     remainder = decimalNum % 8
     octal += remainder * count
     count = count * 10
     decimalNum //= 8
     print(str(decimalNum) + "         " + str(remainder) + "         " + str(octal))

print("The octal representation is " + str(octal))

