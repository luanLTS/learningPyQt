from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

import sys

# inicia o objeto necessario para montar a app
app = QApplication(sys.argv)

# cria um widget vazio para ser o principal elemento da app
# window = QWidget()
# button = QPushButton("Clique Aqui")

# subclasse para criar uma janela customizada
class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Primeira App")
        
        botao = QPushButton("Clique Aqui!")
        
        self.setFixedSize(QSize(400, 300))
        
        self.setCentralWidget(botao)


window = JanelaPrincipal()

# mostra o widget na tela
window.show()

# inicia o loop de eventos
app.exec()