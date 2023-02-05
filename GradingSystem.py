gradeInput = input("Enter a grade: ")
grade = float(gradeInput)

if((grade >= 0) and (grade <= 1)):
    if grade >= 0.9:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    elif grade < 0.6:
        print("F")
else:
    print("Input a grade that between 0 and 1")
