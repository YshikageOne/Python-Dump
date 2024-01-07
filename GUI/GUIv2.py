import tkinter as tk
from tkinter import messagebox

#importing the tkinter and getting messagebox which is like JOptionPane

class GUI:

    #constructor for the GUI
    def __init__(self):

        self.main = tk.Tk()
        self.main.title("LOL")
        self.main.geometry("640x480")
        self.main.resizable(False,False)

        # setting a menu bar
        self.menubar = tk.Menu(self.main)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)# removing the broken line when opening the menu
        self.filemenu.add_command(label = "Close", command=self.closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Force Exit", command=exit)

        self.menubar.add_cascade(menu=self.filemenu, label="Menu")

        self.main.config(menu=self.menubar)

        # putting the top label for the text field
        self.label = tk.Label(self.main, text = "Insert your funny message here pls", font = ('Tahoma', 18, 'bold'))
        self.label.pack(padx= 15, pady= 15)

        # putting the JTextField
        self.textbox = tk.Text(self.main, height = 5, font = ('Comic Sans MS', 24))
        self.textbox.pack(padx=15, pady=15)

        # setting up a keybind that enters the text with ctrl+enter
        self.textbox.bind("<KeyPress>", self.keyBind)

        # putting the checkBox

        # initializing the state of the checkbox as a variable
        self.checkState = tk.IntVar()

        self.check = tk.Checkbutton(self.main, text="Show the funny message on a new window?", font = ('Arial', 16), variable= self.checkState)
        self.check.pack(padx=15, pady=15)

        # putting the button
        self.button = tk.Button(self.main, text = "Show the funny", font =('Tahoma', 16), command=self.showTheFunny) # puts an actionHandler when the button is present
        self.button.pack(padx=15, pady=15)

        # setting up a window event that would display a window message when closing the main window
        self.main.protocol("WM_DELETE_WINDOW", self.closing)

        self.main.mainloop()

    # method that would display the inputted text
    def showTheFunny(self):
        if self.checkState.get() == 0:
            print(self.textbox.get('1.0',tk.END))
        else:
            messagebox.showinfo(title="Funny Message", message=self.textbox.get('1.0', tk.END))

    def keyBind(self, event):
        # event.state is an integer that state of various keys and buttons
        # event.keysym is the symbolic name of the key associated with the event
        if event.state == 12 and event.keysym == "Return":
            self.showTheFunny()

    # method for the window closing
    def closing(self):
        # setting up a messagebox if the user wants to truly close it
        if messagebox.askyesno(title = "No more funny?", message="Are you sure do you want to close it?"):
            self.main.destroy()


GUI()