sentence = input("Enter a sentence: ")

listOfWords = sentence.split()
print("There are", len(listOfWords), "words. ")

sum = 0

for word in listOfWords:
   sum += len(word)

print("The average word length is", sum / len(listOfWords))