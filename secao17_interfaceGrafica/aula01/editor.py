from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QTextEdit


class Editor(QMainWindow):
    def __init__(self):
        self.nome_arquivo = ""
        self.texto_alterado = False
        super(Editor, self).__init__()
        self.setGeometry(200, 50, 600, 600)
        self.setWindowTitle('Meu aplicativo em PyQt5.')
        self.setWindowIcon(QIcon("img/teste.jpg"))
        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.onTextChanged)
        self.setCentralWidget(self.text_edit)
        self.definir_acoes()
        self.definir_menus()
        self.definir_barra_ferramentas()

