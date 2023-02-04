def checkingAnswer(x, y): # checks the right answer x = inputted answer y = right one
    if x == y:
        print("Correct")
        return True
    else:
        print("Wrong, the right answer is", y)
        return False

#answer key
firstRightAnswer = str("a")
secondRightAnswer = str("c")
thirdRightAnswer = str("b")
forthRightAnswer = str("d")
fifthRightAnswer = str("a")

#question 1
print("16x16")
print("a : 256")
print("b : 255")
print("c : 257")
print("d : 32")

answerPrompt = str("Enter your answer: ")
firstAnswer = str(input(answerPrompt))

checkingAnswer(firstAnswer, firstRightAnswer)

#question 2
print("23x3")
print("a : 63")
print("b : 26")
print("c : 69")
print("d : 30")

secondAnswer = str(input(answerPrompt))

checkingAnswer(secondAnswer, secondRightAnswer)

#question 3
print("425x526")
print("a : 242,530")
print("b : 223,550")
print("c : 214,123")
print("d : 256,356")

thirdAnswer = str(input(answerPrompt))

checkingAnswer(thirdAnswer, thirdRightAnswer)

#question 4
print("50x50")
print("a : 1500")
print("b : 100")
print("c : 250")
print("d : 2500")

forthAnswer = str(input(answerPrompt))

checkingAnswer(forthAnswer, forthRightAnswer)

#question 5
print("221x220")
print("a : 48,620")
print("b : 48,600")
print("c : 48,622")
print("d : 48,626")

fifthAnswer = str(input(answerPrompt))

checkingAnswer(fifthAnswer, fifthRightAnswer)

