class Letter:
    def __init__(self,letterTo, letterFrom):
        self.letterTo = letterTo
        self.letterFrom = letterFrom
        self.letterLine = ""
    def addLine(self, line):
        self.letterLine = self.letterLine + line + "\n"
    def getText(self):
        print("Dear " + self.letterTo + ": \n\n" + self.letterLine + "\n" + "Sincerely,\n\n" + self.letterFrom)

# le result

letter = Letter("John", "Mary")
letter.addLine("I am sorry we must part.")
letter.addLine("I wish you all the best.")

letter.getText()


