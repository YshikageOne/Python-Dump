import random
print("Hey kid, wanna play rock paper scissors? come on lad")
yourPlay = input(str("Type out(rock, paper, scissors): "))

listsel = ['null', 'rock', 'paper', 'scissors'] # List consisting of rock, paper, and scissors. Null cuz the list counting always starts at 0

if yourPlay in listsel: # Checks if your input is rock paper or scissors before the rest of the code executes
    genNum = int(random.randint(1, 3))
    genOutput = listsel[genNum]

    if yourPlay == listsel[genNum]:
        print("My choice was", listsel[genNum])
        print("Damn that's a tie")
    elif yourPlay == 'rock':
        if listsel[genNum] == 'scissors':
            print("My choice was", listsel[genNum])
            print("Damn you win")
        else:
            print("My choice was", listsel[genNum])
            print("Cringe you lose")
    elif yourPlay == 'paper':
        if listsel[genNum] == 'rock':
            print("My choice was", listsel[genNum])
            print("Damn you win")
        else:
            print("My choice was", listsel[genNum])
            print("Cringe you lose")
    elif yourPlay == 'scissors':
        if listsel[genNum] == 'paper':
            print("My choice was", listsel[genNum])
            print("Damn you win")
        else:
            print("My choice was", listsel[genNum])
            print("Damn you lose")


else:
    print("Type out rock, paper, scissor ONLY haiyaa")