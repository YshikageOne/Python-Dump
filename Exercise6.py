sum = 0
count = 0
average = 0
data = input("Enter a number or press enter to quit: ")

while data:
    count += 1
    number = data
    sum += int(number)
    average = sum / count
    data = input("Enter a number or press enter to quit: ")


print("The sum is " + str(sum))
print("The average is "+ str(average))