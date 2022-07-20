import sys

from PyQt5.QtWidgets import QPushButton, QApplication, QWidget

app = QApplication(sys.argv)
w = QWidget()

# Alterando o tamanho da janela em pixels
w.resize(400, 150)

# Alterando a posição da janela na área de trabalho
# move(esquerda, topo)
w.move(0, 300)

# Definindo o título da janela
w.setWindowTitle('Janela com QWidget!')

# Criando um botão na janala
btn = QPushButton('Olá, mundo! PYQT5.', w)

# Adicionando evento do clique do botão para finalizar a aplicação
btn.clicked.connect(QApplication.instance().quit)

# Definindo o texto a ser exibido quando
# paramos o mouse sobre o botão
btn.setToolTip('Este é um <b>QPushButton</b>!')

# Mudando o posicionamento do botão na janela move(esquerda, topo)
btn.move(50, 50)

w.show()
sys.exit(app.exec_())


