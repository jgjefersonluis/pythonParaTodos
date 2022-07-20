import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication(sys.argv)

# Criando a janela da aplicação com QMainWindow
w = QMainWindow()

# Definindo posicionamento da janela na tela
# setGeometry(esquerda, topo, largura, altura)
w.setGeometry(50,50,300,100)

w.setWindowTitle('Meu aplicativo com QMainWindow!')
w.setWindowIcon(QIcon('teste.jpg'))

# Adicionando uma mensagem à barra de status da aplicação
w.statusBar().showMessage('Mensagem da barra de status.')

btn = QPushButton('Sair!', w)
btn.clicked.connect(QApplication.instance().quit)
btn.setToolTip('Este é um <b>QPusButton</b>!')
btn.setGeometry(50, 50, 50, 25)

w.show()
sys.exit(app.exec_())
