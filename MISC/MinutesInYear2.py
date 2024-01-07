myYear = int(input("Enter a number of years: "))

hour = int(60)
day = int(hour*24)
year = int(day*365)

minutes = str(myYear * year)

print("The number of minutes in " + str(myYear) + " year/s is " + minutes + "." )