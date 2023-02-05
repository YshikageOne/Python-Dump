def computepay(h, r):
    if h <= 40:
        pay = h * r
        return pay
    elif h > 40:
        pay = 40 * r + (h - 40) * 1.5 * r
        return pay

hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter rate per hour: ")
r = float(rate)
print("Pay",computepay(h,r))