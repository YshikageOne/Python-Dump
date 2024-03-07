import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QDateEdit, QMessageBox
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

#Database connection
Base = declarative_base()

class Equipment(Base):
    __tablename__ = 'tbl_equipmentcrud'
    equipmentID = Column(Integer, primary_key=True, autoincrement=True)
    equipmentName = Column(String(255))
    maintenanceSchedule = Column(Date)
    repairStatus = Column(String(255))

#Database connection
engine = create_engine('mysql+mysqlconnector://root:@localhost/db_equipmentCRUD')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

from contextlib import contextmanager

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

#CRUD

#Create
def create_equipment(name, schedule, history):
    with session_scope() as session:
        formatted_schedule = datetime.strptime(schedule, '%m/%d/%Y').date()
        new_equipment = Equipment(equipmentName=name, maintenanceSchedule=formatted_schedule, repairStatus=history)
        session.add(new_equipment)


#Read
def read_equipment():
    session = Session()
    equipment_list = session.query(Equipment).all()
    session.close()
    return equipment_list

#Update

def update_equipment(id, name, schedule, history):
    with session_scope() as session:
        equipment = session.query(Equipment).filter(Equipment.equipmentID == id).first()
        if equipment:
            equipment.equipmentName = name
            equipment.maintenanceSchedule = datetime.strptime(schedule, '%m/%d/%Y').date()
            equipment.repairStatus = history

#Delete
def delete_equipment(id):
    with session_scope() as session:
        equipment = session.query(Equipment).filter(Equipment.equipmentID == id).first()
        if equipment:
            session.delete(equipment)

#GUI Setup
class EquipmentMaintenanceSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Equipment Maintenance System by Clyde, Hosea, and Jhonna")
        self.setGeometry(100, 100, 974, 488)  #x, y, width, height

        #Set background image
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("C:/Users/ausus/Desktop/Coding Stuff/Python/SchoolStuff/CRUD/assets/background.png")))
        self.setPalette(palette)

        self.initUI()

    #CRUD Methods

    #Create
    def addEquipment(self):
        name = self.nameEntry.text()
        schedule = self.scheduleEntry.text()
        status = self.repairStatusCombobox.currentText()
        create_equipment(name, schedule, status)
        self.load_data_into_table()
        self.show_success_message("Equipment added successfully.")

    #Update
    def updateEquipment(self):
        selected_row = self.equipmentTable.currentRow()
        if selected_row >= 0:
            id = int(self.equipmentTable.item(selected_row, 0).text())
            name = self.nameEntry.text()
            schedule = self.scheduleEntry.text()
            status = self.repairStatusCombobox.currentText()
            update_equipment(id, name, schedule, status)
            self.load_data_into_table()
            self.show_success_message("Equipment updated successfully.")
        
    #Delete
    def deleteEquipment(self):
        selected_row = self.equipmentTable.currentRow()
        if selected_row >= 0:
            id = int(self.equipmentTable.item(selected_row, 0).text())
            delete_equipment(id)
            self.load_data_into_table()
            self.show_success_message("Equipment deleted successfully.")

    #Read
    def load_data_into_table(self):
        self.equipmentTable.setRowCount(0)
        equipment_list = read_equipment()
        for equipment in equipment_list:
            row_position = self.equipmentTable.rowCount()
            self.equipmentTable.insertRow(row_position)
            self.equipmentTable.setItem(row_position, 0, QTableWidgetItem(str(equipment.equipmentID)))
            self.equipmentTable.setItem(row_position, 1, QTableWidgetItem(equipment.equipmentName))
            self.equipmentTable.setItem(row_position, 2, QTableWidgetItem(equipment.maintenanceSchedule.strftime('%Y-%m-%d')))
            self.equipmentTable.setItem(row_position, 3, QTableWidgetItem(equipment.repairStatus))

    def initUI(self):
        #Main layout container
        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)

        #Set a common style for all labels
        labelStyle = "QLabel { font-size: 13px; font-weight: bold; }"

        #Equipment Name
        nameLayout = QHBoxLayout()
        self.nameLabel = QLabel("Equipment Name:")
        self.nameLabel.setStyleSheet(labelStyle)
        self.nameLabel.setFixedWidth(150)  
        self.nameEntry = QLineEdit()
        nameLayout.addWidget(self.nameLabel)
        nameLayout.addWidget(self.nameEntry)

        #Maintenance Schedule
        scheduleLayout = QHBoxLayout()
        self.scheduleLabel = QLabel("Maintenance Schedule:")
        self.scheduleLabel.setStyleSheet(labelStyle)
        self.scheduleLabel.setFixedWidth(150)  
        self.scheduleEntry = QDateEdit()
        self.scheduleEntry.setCalendarPopup(True)
        self.scheduleEntry.setDate(QDate.currentDate())
        self.scheduleEntry.setDisplayFormat("MM/dd/yyyy")
        scheduleLayout.addWidget(self.scheduleLabel)
        scheduleLayout.addWidget(self.scheduleEntry)

        #Repair Status
        statusLayout = QHBoxLayout()
        self.statusLabel = QLabel("Repair Status:")
        self.statusLabel.setStyleSheet(labelStyle)
        self.statusLabel.setFixedWidth(150) 
        self.repairStatusCombobox = QComboBox()
        self.repairStatusCombobox.addItems(['Broken', 'Fixed'])
        statusLayout.addWidget(self.statusLabel)
        statusLayout.addWidget(self.repairStatusCombobox)

        layout.addLayout(nameLayout)
        layout.addLayout(scheduleLayout)
        layout.addLayout(statusLayout)

        #Buttons
        buttonLayout = QHBoxLayout()
        layout.addLayout(buttonLayout)
        addButton = QPushButton("Add")
        addButton.clicked.connect(self.addEquipment)
        buttonLayout.addWidget(addButton)

        updateButton = QPushButton("Update")
        updateButton.clicked.connect(self.updateEquipment)
        buttonLayout.addWidget(updateButton)

        deleteButton = QPushButton("Delete")
        deleteButton.clicked.connect(self.deleteEquipment)
        buttonLayout.addWidget(deleteButton)

        #Equipment Table
        self.equipmentTable = QTableWidget()
        self.equipmentTable.setColumnCount(4)
        self.equipmentTable.setHorizontalHeaderLabels(['Equipment ID', 'Equipment Name', 'Maintenance Schedule', 'Repair Status'])
        self.equipmentTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.equipmentTable.setSelectionBehavior(QTableWidget.SelectRows)
        self.equipmentTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.equipmentTable.setFocusPolicy(Qt.NoFocus)
        self.equipmentTable.setAlternatingRowColors(True)

        #Connect the selection change of the table to the updateInputs method
        self.equipmentTable.itemSelectionChanged.connect(self.updateInputs)

        #Style adjustments to make the table look more like the one in the image
        self.equipmentTable.setStyleSheet("""
            QTableWidget {
                border: 1px solid #d6d9dc;
             gridline-color: #d6d9dc;
                font-size: 14px; /* Adjust the font size as needed */
            }
                                          
            QTableWidget::item {
                border-bottom: 1px solid #d6d9dc;
                padding: 5px; /* Add padding to match the image */
            }
                                          
            QHeaderView::section {
                background-color: #f0f0f0; /* Light grey header background */
                padding: 5px;
                border: 1px solid #d6d9dc;
                font-size: 14px; /* Adjust the font size as needed */
                font-weight: bold; /* Make the header text bold */
            }
                                          
            QTableWidget::item:selected {
                background-color: #e7e7e7; /* Lighter selection color */
            }
        """)

        
        layout.addWidget(self.equipmentTable)

        self.load_data_into_table()
    
    #Extra Stuff
    def show_success_message(self, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setWindowTitle("Success")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def updateInputs(self):
        selected_row = self.equipmentTable.currentRow()
        if selected_row >= 0:
            id_item = self.equipmentTable.item(selected_row, 0)
            name_item = self.equipmentTable.item(selected_row, 1)
            schedule_item = self.equipmentTable.item(selected_row, 2)
            status_item = self.equipmentTable.item(selected_row, 3)

            #Check if the row is not empty
            if id_item and name_item and schedule_item and status_item:
                self.nameEntry.setText(name_item.text())
                date = QDate.fromString(schedule_item.text(), "yyyy-MM-dd")
                self.scheduleEntry.setDate(date)
                #Set the combobox to the corresponding repair status
                index = self.repairStatusCombobox.findText(status_item.text(), Qt.MatchFixedString)
                if index >= 0:
                    self.repairStatusCombobox.setCurrentIndex(index)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EquipmentMaintenanceSystem()
    ex.show()
    sys.exit(app.exec_())