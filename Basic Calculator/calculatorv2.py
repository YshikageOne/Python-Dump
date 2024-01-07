import tkinter as tk

class Calculator:

    def __init__(self):
        self.main = tk.Tk()

        # window details
        self.main.title("Calculator") #title of the main window
        self.main.geometry("357x420") #dimensions of the main window
        self.main.resizable(False, False) # making the window not resizable
        self.main.config(bg="gray") # background color

        # setting up the input textfield
        self.equation = tk.StringVar() #variable that would hold the input in the textfield
        self.entry_value = '' # holds the current value of the Entry
        self.entry = tk.Entry(width=17, bg = '#fff', font = ('Arial Bold' , 28), textvariable=self.equation)# single line entry
        self.entry.pack(side="top")

        # buttons of the calculator
        buttonframe = tk.Frame(self.main)
        # 1st column
        tk.Button(width=11, height=4, text='(',relief='flat',bg='white', command=lambda:self.showResult('(')).place(
            x=0,y=50)
        tk.Button(width=11, height=4, text=')',relief='flat',bg='white', command=lambda:self.showResult(')')).place(
            x=90,y=50)
        tk.Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.showResult('%')).place(
            x=180, y=50)
        tk.Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.showResult('/')).place(
            x=270, y=50)

        # 2nd column
        tk.Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.showResult('1')).place(
            x=0, y=125)
        tk.Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.showResult('2')).place(
            x=90, y=125)
        tk.Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.showResult('3')).place(
            x=180, y=125)
        tk.Button(width=11, height=4, text='x', relief='flat', bg='white', command=lambda: self.showResult('*')).place(
            x=270, y=125)

        # 3rd column
        tk.Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.showResult('4')).place(
            x=0, y=200)
        tk.Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.showResult('5')).place(
            x=90, y=200)
        tk.Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.showResult('6')).place(
            x=180, y=200)
        tk.Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.showResult('-')).place(
            x=270, y=200)

        # 4th column
        tk.Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.showResult('7')).place(
            x=0, y=275)
        tk.Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.showResult('8')).place(
            x=90, y=275)
        tk.Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.showResult('9')).place(
            x=180, y=275)
        tk.Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.showResult('+')).place(
            x=270, y=275)

        # 5th column
        tk.Button(width=11, height=4, text='C', relief='flat', bg='white', command=self.clearInput).place(
            x=0, y=350)
        tk.Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.showResult('0')).place(
            x=90, y=350)
        tk.Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.showResult('.')).place(
            x=180, y=350)
        tk.Button(width=11, height=4, text='=', relief='flat', bg='white', command=self.calculate).place(
            x=270, y=350)

        buttonframe.pack(expand=True, fill="both")


        self.main.mainloop()

    def showResult(self, value):
        self.entry_value += str(value) # appends the value to the entry_value
        self.equation.set(self.entry_value) # updates the variable with the entry_value

    def clearInput(self):
        self.entry_value = '' # setting the current value to empty
        self.equation.set(self.entry_value)  # updates the variable with the entry_value

    def calculate(self):
        result = eval(self.entry_value) # eval means it would calculate the entry_value which would like (2+2)
        self.equation.set(result) # updates the variable with the result





Calculator()