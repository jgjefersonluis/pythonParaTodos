import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QToolButton
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

w = QMainWindow()
w.setGeometry(50, 50, 250, 200)
w.setWindowTitle('Meu aplicativo com QMainWindow!!!!')
w.setWindowIcon(QIcon("img/teste.jpg"))
w.statusBar().showMessage('Mensagem da barra de status.')

# Criando um objeto de ícone QIcon
icone = QIcon()
# Definindo a imagem do ícone
icone.addFile("img/sair.png")

# Criando um botão para a barra de ferramentas
tb_sair = QToolButton()
# Definindo o ícone do botão
tb_sair.setIcon(icone)
# Definindo o evento para o método de clique
tb_sair.clicked.connect(QApplication.instance().quit)

# Criando a barra de ferramentas
barra = QToolBar()

# Adicionando o botão na barra de ferramentas
barra.addWidget(tb_sair)

# Adicionando a barra de ferramentas à nossa janela
w.addToolBar(barra)
w.show()

sys.exit(app.exec_())