import tkinter as tk

main = tk.Tk() #initialize the GUI class as a variable

main.title("Deez") #title of the main window

main.geometry("640x480")#the resolution of the window

#setting up a label
label = tk.Label(main, text="Haiyaa!!", font =('Times New Roman', 24))
#Label(variable of the window, text, font(font family, font size))
label.pack(padx = 50, pady= 50)
#placing the label on the window
#padx = how much distance across the x axis between the border and the text
#pady = how much distance across the y axis between the border and the text

textbox = tk.Text(main, height=2 ,font =('Times New Roman', 14))
textbox.pack()
#JTextField version (variable, height of the box,the font that would display on the box)

entry = tk.Entry(main)
entry.pack()
#another version of JTextField where there is no multi-line
#used for password input

# button = tk.Button(main, text = "C L I C K", font = ('Arial' , 20))
# button.pack()
#JButton version

# button = tk.Button(main, text = "C L I C K", font = ('Arial' , 20))
# button.place(x = 200, y = 200, height = 100, width = 100)
# another version of placing the buttons where (coordinates for the x and y in pixels and dimensions of the button in pixels)


buttonframe = tk.Frame(main)
buttonframe.columnconfigure(0, weight = 1)
buttonframe.columnconfigure(1, weight = 1)
buttonframe.columnconfigure(2, weight = 1)

btn1 = tk.Button(buttonframe, text = "Deez", font = ('Arial' , 20))
btn1.grid(row = 0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text = "Deez", font = ('Arial' , 20))
btn2.grid(row = 0, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text = "Deez", font = ('Arial' , 20))
btn1.grid(row = 0, column=2, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text = "Deez", font = ('Arial' , 20))
btn1.grid(row = 1, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text = "Deez", font = ('Arial' , 20))
btn1.grid(row = 1, column=1, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text = "Deez", font = ('Arial' , 20))
btn1.grid(row = 1, column=2, sticky=tk.W+tk.E)
#making the button
#where the its placed in the button frame
#its placed like a grid where its placed on the selected row and column
# sticky=tk.W+tk.E where the button is streched from the left side to right side of the frame

buttonframe.pack(fill='x')
#placing the frame on the main window where its streched across the x axis

main.mainloop() #call in the GUI