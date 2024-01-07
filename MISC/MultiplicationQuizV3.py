import random

manyTime = int(input("How many questions do you want? "))
def quiz():
    score = 0
    for i in range(manyTime):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        answer = num1 * num2
        guess = int(input(f"What is {num1} x {num2}? "))
        if guess == answer:
            score += 1
            print("Correct!\n")
        else:
            print("Incorrect.\n")

    return score


result = quiz()
print("Your score is " + str(result) + "/" + str(manyTime))
