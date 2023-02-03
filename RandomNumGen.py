import random

minNum = int(input("Enter your minimum number: "))
maxNum = int(input("Enter your maximum number: "))

genNum = int(random.randint(minNum, maxNum))
guessNum = int(input("Guess the number: "))

if guessNum == genNum:
    print("Nice you did it... have some titties Ꙭ")
else:
    print("The correct answer is:", genNum)
    print("nah bro practice sa")


