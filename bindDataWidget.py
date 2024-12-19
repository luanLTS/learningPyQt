from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import QSize

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Minha Aplicação")
        
        self.label = QLabel()
        
        self.inputText = QLineEdit()
        self.inputText.textChanged.connect(self.label.setText)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.inputText)
        
        container = QWidget()
        container.setLayout(layout)
        container.setFixedSize(QSize(700,500))
        
        
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()