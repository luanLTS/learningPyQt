import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize

from random import choice

titulos_da_janela = [
    "Minha aplicação",
    "Minha aplicação",
    "Ainda minha aplicação",
    "Ainda minha aplicação",
    "Ai meu Deus",
    "Ai meu Deus",
    "Isto é surpresa",
    "Isto é surpresa",
    "Algo deu errado"
]

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.botao_esta_verificado = True
        
        # self.setWindowTitle("Signals & Slots")
        self.setWindowTitle(titulos_da_janela[0])
        
        self.botao = QPushButton("Clique Aqui!")
        self.botao.clicked.connect(self.o_botao_for_clicado)
        
        self.windowTitleChanged.connect(self.o_titulo_da_janela_for_alterado)
        
        self.setFixedSize(QSize(700, 500))
        self.setCentralWidget(self.botao)
    
    def o_botao_for_clicado(self):
        print("Botão foi clicado!")
        
        self.setWindowTitle(choice(titulos_da_janela))
        
    def o_titulo_da_janela_for_alterado(self, novo_titulo):
        print("O titulo foi trocado para: ", novo_titulo)
        if novo_titulo == titulos_da_janela[-1]:
            self.botao.setDisabled(True)

app = QApplication(sys.argv)

janela = JanelaPrincipal()
janela.show()

app.exec()