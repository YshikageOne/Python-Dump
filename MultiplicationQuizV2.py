def questionTime (x):
    print(questions[x])
    for allchoices in choices[x]:
        print(allchoices)

questions = ["16x16","23x3","425x526","50x50","221x220"] #list of questions

choices = [("a : 256", "b : 255","c : 257","d : 32"),
           ("a : 63", "b : 26", "c : 69", "d : 30"),
           ("a : 242,530", "b : 223,550", "c : 214,123", "d : 256,356"),
           ("a : 1500", "b : 100", "c : 250", "d : 2500"),
           ("a : 48,620", "b : 48,600", "c : 48,622", "d : 48,626")] #list of the choices for the questions

rightAnswer = ["a", "c", "b", "d","a"] # answer key

userAnswers = [] # list of your inputted answers
finalScore = 0
questionNumber = 0
answerPrompt = "Enter your answer: "

#askin part
while questionNumber < 5:
    questionTime(questionNumber)
    answer = input(answerPrompt)
    userAnswers.append(answer)
    #checking and scoring
    if answer == rightAnswer[questionNumber]:
        finalScore += 1
        print("Correct")
    else:
        print("Wrong, the right answer is", rightAnswer[questionNumber])
    questionNumber += 1

print("---------------------")
print("          RESULTS            ")
print("---------------------")

print(finalScore, "/", len(questions))