from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTableWidget
import sys

def qtPractice():
    # app = QApplication([])
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("DailyCost")
    layout = QVBoxLayout()
    table = QTableWidget(3, 4)

    layout.addWidget(table)
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)
    window.resize(600,600)
    
    window.show()
    app.exec()

if __name__ == "__main__":
    qtPractice()