import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QDateEdit, QPushButton, QFormLayout, QLineEdit
from PyQt5.QtWidgets import *
from datetime import date
from PyQt5.QtCore import QDateTime
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        iLayout = QVBoxLayout()
        sLayout = QHBoxLayout()
        layout = QHBoxLayout()
        self.date = QDateEdit()
        self.date.setCalendarPopup(True)
        self.date.setDateTime(QDateTime.currentDateTime())
        
        # self.date.editingFinished.connect(self.update)

        label = QLabel()
        label.setText("Date")

        sLayout.addWidget(label)
        sLayout.addWidget(self.date)

        form = QFormLayout()
        self.name = QLineEdit()
        self.type = QLineEdit()
        self.cost = QLineEdit()

        form.addRow("name", self.name)
        form.addRow("type", self.type)
        form.addRow("cost", self.cost)
        
        iLayout.addLayout(sLayout)
        iLayout.addLayout(form)
        
        self.result = QLabel()
        button = QPushButton("Add")
        button.pressed.connect(self.add_data)
        iLayout.addWidget(self.result)
        iLayout.addWidget(button)
        
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)

        self.table.setHorizontalHeaderLabels(["Date", "Cost Name", "Cost Type", "Cost", "Delete"])


        layout.addWidget(self.table)
        layout.addLayout(iLayout)

        self.submit = QPushButton("Submit")
        layout.addWidget(self.submit)





        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def print_date(self):
        value = str(self.date.date().toPyDate())
        print(type(self.date.date().toPyDate()))
        self.result.setText(value)
    
    def add_data(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(str(self.date.date().toPyDate())))
        self.table.setItem(row, 1, QTableWidgetItem(self.name.text()))
        self.table.setItem(row, 2, QTableWidgetItem(self.type.text()))
        self.table.setItem(row, 3, QTableWidgetItem(self.cost.text()))

        delButton= QPushButton("Delete")
        delButton.pressed.connect(self.delete)
        self.table.setCellWidget(row, 4, delButton)

        self.resetForm()
    
    # clean input data from form
    def resetForm(self):
        self.name.clear()
        self.type.clear()
        self.cost.clear()
    
    # functions for delete button
    def delete(self):
        row = self.table.currentRow()
        self.table.removeRow(row)



    # function to submit data to mongodb.
    # need to call mongo helper
    # change the fomat of date, may need to set primary key before submit data
    def submit(self):
        
        pass








def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()