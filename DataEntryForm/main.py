import tkinter
from tkinter import ttk, messagebox
import openpyxl
import os

def enter_data():
    # check if the user is checked or not
    sureCheck = sure_check_var.get()
    if sureCheck == "Sure":
        # getting the inputs
        firstname = firstName_textBox.get()
        lastName = lastName_textBox.get()

        #making sure that the user inputted their first and last name
        if firstname and lastName:
            gender = gender_comboxBox.get()
            age = age_spinBox.get()
            # music taste
            bestKanye = kanye_comboBox.get()
            bestKendrick = kendrick_comboBox.get()

            output = ("-----------------------------------------------------------------------\n" \
                      "USER DETAILS\n" \
                      "Name: " + firstname + " " + lastName + "\n" \
                      "Gender: " + gender + "\n" \
                      "Age : " + age + "\n\n" \
                      "MUSIC TASTE\n" \
                      "Best Kanye West Album : " + bestKanye + "\n" \
                      "Best Kendrick Lamar Album : " + bestKendrick)

            messagebox.showinfo(title = "Details Saved", message=output)

            #setting up a filepath for excel file
            filepath = r"C:\Users\gayur\Desktop\Coding stuff\Python\pythonPractice\DataEntryForm\details.xlsx"

            #checking if the file is already there or not
            if not os.path.exists(filepath):
                #it would create a new excel workbook
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                #Heading
                heading = ["First Name", "Last Name", "Age",
                           "Gender", "Best Kanye West Album",
                           "Best Kendrick Lamar Album"]
                sheet.append(heading)#adds it to the sheet
                workbook.save(filepath) # save the file in the path
            #loading the excel file
            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            #adding the details to the file
            sheet.append([firstname,lastName,age,gender,bestKanye,bestKendrick])
            workbook.save(filepath)


        else:
            messagebox.showerror(title="You're forgetting", message="Where's your name?????")

    else:
        messagebox.showerror(title="You're forgetting", message="you gotta be sure first :|")





main = tkinter.Tk() # initializing the parent main window
main.title("Fill in the details idk........") #title of the window
main.resizable(False,False)

#initializing a Frame inside the main window
frame = tkinter.Frame(main)
frame.pack()

#First frame
userDetailFrame = tkinter.LabelFrame(frame, text = "User Details")
userDetailFrame.grid(row = 0, column = 0, padx = 10, pady = 10)

#Inside the first frame
firstName_label = tkinter.Label(userDetailFrame, text = "First Name")
firstName_label.grid(row = 0, column = 0)
firstName_textBox = tkinter.Entry(userDetailFrame)
firstName_textBox.grid(row = 1, column = 0)

lastName_label = tkinter.Label(userDetailFrame, text = "Last Name")
lastName_label.grid(row = 0, column = 1)
lastName_textBox = tkinter.Entry(userDetailFrame)
lastName_textBox.grid(row = 1, column = 1)

gender_label = tkinter.Label(userDetailFrame, text = "Gender")
gender_comboxBox = ttk.Combobox(userDetailFrame, values = ["Male", "Female", "Some other shit", "ChatGPT", "Lol"], state = "readonly")
gender_label.grid(row = 0, column = 2)
gender_comboxBox.grid(row = 1, column= 2)

age_label = tkinter.Label(userDetailFrame, text="Age")
age_spinBox = tkinter.Spinbox(userDetailFrame, from_= 0, to = 100, increment = 1)
age_label.grid(row =2, column=1)
age_spinBox.grid(row = 3, column=1)

#simple for each loop that would space out each widget in the first frame
for widget in userDetailFrame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# Questioning music taste (2nd frome)
musicFrame = tkinter.LabelFrame(frame, text = "Music Taste")
musicFrame.grid(row = 1, column = 0, sticky="news", padx = 10, pady = 10)

kanye_label = tkinter.Label(musicFrame, text="Best Kanye Album")
kanye_label.grid(row = 0, column= 0)
kanye_comboBox = ttk.Combobox(musicFrame, values=["The College Dropout",
                                                       "Late Registration",
                                                       "Graduation",
                                                       "808s & Heartbreak",
                                                       "My Beautiful Dark Twisted Fantasy ",
                                                       "Watch the Throne",
                                                       "Yeezus",
                                                       "The Life of Pablo",
                                                       "Ye",
                                                       "Kids See Ghost",
                                                       "Jesus is King",
                                                       "Donda"], state = "readonly")
kanye_comboBox.grid(row = 1, column=0)

kendrick_label = tkinter.Label(musicFrame, text= "Best K-Dot Album")
kendrick_label.grid(row = 0, column= 1)
kendrick_comboBox = ttk.Combobox(musicFrame, values = ["Overly Dedicated",
                                                       "Section.80",
                                                       "good kid, m.A.A.d city",
                                                       "To Pimp a Butterfly",
                                                       "untitled",
                                                       "DAMN",
                                                       "Mr. Morale & The Big Steppers"], state = "readonly")
kendrick_comboBox.grid(row = 1, column= 1)


#simple for each loop that would space out each widget in the first frame
for widget in musicFrame.winfo_children():
    widget.grid_configure(padx=50, pady=10)

#3rd Frame
sureFrame = tkinter.LabelFrame(frame, text = "Are you sure this is all?")
sureFrame.grid(row = 2, column = 0, sticky="news", padx = 10, pady = 10)

sure_check_var = tkinter.StringVar(value="Not Sure")
sure_check = tkinter.Checkbutton(sureFrame, text = "Yes", variable= sure_check_var, onvalue= "Sure", offvalue= "Not Sure")
sure_check.grid(row = 0, column = 0)

#Button
button = tkinter.Button(frame, text = "Enter the details", command= enter_data)
button.grid(row = 3, column = 0,sticky="news", padx = 10, pady = 10)


main.mainloop() #opens the main window
