import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.botao_esta_verificado = True
        
        self.setWindowTitle("Signals & Slots")
        
        self.botao = QPushButton("Clique Aqui!")
        self.botao.clicked.connect(self.o_botao_for_clicado)
        
        self.setCentralWidget(self.botao)
    
    def o_botao_for_clicado(self):
        self.botao.setText("Você já clicou no botão!")
        self.botao.setEnabled(False)
        
        self.setWindowTitle("O titulo foi alterado na funcao")

app = QApplication(sys.argv)

janela = JanelaPrincipal()
janela.show()

app.exec()