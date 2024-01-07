import tkinter as tk
#imports the tkinter module, which provides the functionality to create graphical user interface


# function to perform the calculation
def calculate():
    try:
        # get the user input
        userinput = entry.get()

        # evalute the input and get the result
        result = eval(userinput)

        # clear the entry like the (1+1)
        entry.delete(0, tk.END) #tk.END means the last character in the text field

        # display the result (2)
        entry.insert(tk.END, str(result))

    except Exception as e:
        # handle any errors that occur during calculation
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# create the main window and sets the title of the window
window = tk.Tk()
window.title("Calculator WOOOOOO!!")

# create an entry widget to display the user input and results
entry = tk.Entry(window, width=30) #JTextField with width 30 and insertted to the window
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10) #position of the text field
# grid() method is used to specify the position of the entry widget in the grid layout of the window.
# it is placed in the first row (row=0), first column (column=0), and spans across all four columns (columnspan=4).
# padx and pady refers to the spacing of the text field to the borders of the main window

# create buttons labels for the digits 0-9 and operators +, -, *, /
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
operators = ['+', '-', '*', '/']
row = 1
col = 0
# the row and col variables are set to 1 and 0 to keep track of the current row and column for placing the buttons.

#for each loop that would create a button with a label from the digit list
for digit in digits:
    button = tk.Button(window, text=digit, width=5, command=lambda digit = digit: entry.insert(tk.END, digit))
    #the buttons would be placed on the window, with label from the list,
    #the lambda function takes the digit as an argument and inserts it at the end of the entry widget when the button is clicked.
    button.grid(row=row, column=col, padx=5, pady=5)
    #the button is then placed in the current row and column using grid().
    col += 1
    if col > 2:
        col = 0
        row += 1
    #the col variable is incremented, and if it exceeds 2 (indicating that three buttons have been placed in the current row),
    # it is reset to 0 and the row variable is incremented.


for operator in operators:
    button = tk.Button(window, text=operator, width=5, command=lambda operator = operator: entry.insert(tk.END, operator))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
# same goes for here but for the operators and the buttons are placed in the same row but different columns

# create the equals button to perform the calculation
equals_button = tk.Button(window, text="=", width=5, command=calculate)
equals_button.grid(row=row, column=col, padx=5, pady=5)

# Start the Tkinter event loop
window.mainloop()
#this line starts the Tkinter event loop, which allows the GUI to be displayed and interacted with by the user
# tt continuously listens for events such as button clicks and updates the GUI accordingly.