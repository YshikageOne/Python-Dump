import tkinter as tk
import mysql.connector
import tkinter.font as tkFont
import time

from datetime import datetime
from tkinter import messagebox, PhotoImage, ttk
from mysql.connector import Error
from tkcalendar import DateEntry

#Database connection
def connectDatabase():
    try:
        connect = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "db_equipmentCRUD"
        )
        if connect.is_connected():
            return connect
    except Error as e:
        messagebox.showerror("Database Connection Error", str(e))


#CRUD operations

#Create
def createEquipment(name, schedule, history):
    connect = connectDatabase()
    cursor = connect.cursor()

    formatted_schedule = datetime.strptime(schedule, '%m/%d/%Y').strftime('%Y-%m-%d')

    query = "Insert into tbl_equipmentcrud (equipmentName, maintenanceSchedule, repairHistory) VALUES (%s, %s, %s)"
   
    try:
        cursor.execute(query, (name, formatted_schedule, history))
        connect.commit()
        messagebox.showinfo("Success", "Equipment added successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()


#Read
def readEquipment():
    connect = connectDatabase()
    cursor = connect.cursor()

    query = "Select * from tbl_equipmentcrud"
    cursor.execute(query)
    records = cursor.fetchall()
    connect.close()
    return records

#Update
def updateEquipment(id, name, schedule, history):
    connect = connectDatabase()
    cursor = connect.cursor()

    formatted_schedule = datetime.strptime(schedule, '%m/%d/%Y').strftime('%Y-%m-%d')

    query = "UPDATE tbl_equipmentcrud SET equipmentName = %s, maintenanceSchedule = %s, repairHistory = %s WHERE equipmentID = %s"

    try:
        cursor.execute(query, (name, formatted_schedule, history, id))
        connect.commit()
        messagebox.showinfo("Success", "Equipment updated successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()

#Delete
def deleteEquipment(id):
    connect = connectDatabase()
    cursor = connect.cursor()

    query = "DELETE FROM tbl_equipmentcrud WHERE equipmentID = %s"

    try:
        cursor.execute(query, (id,))
        connect.commit()
        messagebox.showinfo("Success", "Equipment deleted successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()

#Extra stuff
def refresh_table(table):
    #Clear the current contents of the table
    for row in table.get_children():
        table.delete(row)
    #Load new data into the table
    load_data_into_table(table)
  
    root.after(5000, refresh_table, table)  #Refresh every 5 seconds

def get_selected_item_id(table):
    selected_item = table.selection()
    if selected_item:  
        item = table.item(selected_item)
        return item['values'][0] 
    else:
        messagebox.showwarning("Warning", "No item selected")
        return None

def on_treeview_select(event, name_entry, schedule_entry, history_entry, equipment_table):
    selected_item = equipment_table.selection()
    if selected_item:
        item = equipment_table.item(selected_item)
        record = item['values']
        name_entry.delete(0, tk.END)
        name_entry.insert(0, record[1])
        schedule_entry.set_date(datetime.strptime(record[2], '%Y-%m-%d').date())
        history_entry.delete(0, tk.END)
        history_entry.insert(0, record[3])

#GUI Setup
def setup_gui(root):
    root.title("Equipment Maintenance System by Clyde, Hosea, and Jhonna")
    root.geometry("974x488")
    root.resizable(False, False)

    #Load and set the background image
    background_image = PhotoImage(file="C:/Users/ausus/Desktop/Coding Stuff/Python/SchoolStuff/CRUD/assets/background.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image

    #Labels and Entry fields
    label_entry_frame = tk.Frame(root)
    label_entry_frame.place(x=10, y=10, width=300, height=120)

    #Font Size
    label_font = tkFont.Font(size=10)
    entry_font = tkFont.Font(size=10)

    tk.Label(label_entry_frame, text="Equipment Name:", font=label_font).grid(row=0, column=0, sticky='w')
    name_entry = tk.Entry(label_entry_frame, font=entry_font)
    name_entry.grid(row=0, column=1, sticky='we')

    tk.Label(label_entry_frame, text="Maintenance Schedule:", font=label_font).grid(row=1, column=0, sticky='w')
    schedule_entry = DateEntry(label_entry_frame, font=entry_font, width=12, date_pattern='mm/dd/yyyy', showweeknumbers=False)
    schedule_entry.grid(row=1, column=1, sticky='we')

    tk.Label(label_entry_frame, text="Repair History:", font=label_font).grid(row=2, column=0, sticky='w')
    history_entry = tk.Entry(label_entry_frame, font=entry_font)
    history_entry.grid(row=2, column=1, sticky='we')

    #Buttons
    button_frame = tk.Frame(root)
    button_frame.place(x=10, y=120, width=300, height=35)
    tk.Button(button_frame, text="Add", command=lambda: (
        messagebox.showwarning("Warning", "All fields are required.") 
        if not (name_entry.get() and schedule_entry.get() and history_entry.get()) 
        else createEquipment(name_entry.get(), schedule_entry.get(), history_entry.get())
    )).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    tk.Button(button_frame, text="Update", command=lambda: updateEquipment(
        get_selected_item_id(equipment_table),
        name_entry.get(),
        schedule_entry.get() if schedule_entry.get() else datetime.now().strftime('%Y-%m-%d'),  #Provide a default date if None
        history_entry.get()
    )).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    tk.Button(button_frame, text="Delete", command=lambda: deleteEquipment(get_selected_item_id(equipment_table))).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    #Table for displaying equipment records
    columns = ('equipment_id', 'equipment_name', 'maintenance_schedule', 'repair_history')
    equipment_table = ttk.Treeview(root, columns=columns, show='headings')
    equipment_table.place(x=320, y=10, width=600, height=468)  # Adjusted table width

    #Define headings and column widths
    for col in columns:
        equipment_table.heading(col, text=col.replace('_', ' ').title())
        equipment_table.column(col, width=140)  

    #Scrollbar for the table
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=equipment_table.yview)
    scrollbar.place(x=920, y=10, width=20, height=468)
    equipment_table.configure(yscroll=scrollbar.set)

    #Load data into the table
    load_data_into_table(equipment_table)
    root.after(5000, refresh_table, equipment_table)

    equipment_table.bind('<<TreeviewSelect>>', lambda event: on_treeview_select(event, name_entry, schedule_entry, history_entry, equipment_table))

def load_data_into_table(table):
    records = readEquipment()
    for record in records:
        table.insert('', tk.END, values=record)
    

root = tk.Tk()
setup_gui(root)
root.mainloop()

