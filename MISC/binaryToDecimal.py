
bruh = str(input("Enter a string of bits: "))
decimal = 0

exponent = len(bruh) - 1

for digit in bruh:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1

print("The integer value is ", decimal)