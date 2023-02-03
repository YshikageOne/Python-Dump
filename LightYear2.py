myYear = int(input("Enter a number of years: "))

speed = int(300000000)

minute = int(60)
hour = int(minute*60)
day = int(hour*24)
year = int(day*365)

secondsInYear = int(year * myYear)

lightYear = str(secondsInYear * speed)

print("Light travels " + lightYear + " meters in " + str(myYear) + " year/s.")
