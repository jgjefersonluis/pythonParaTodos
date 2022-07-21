import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QMenu, QMenuBar, QToolButton, QToolBar, QMessageBox, \
    QFileDialog, QApplication


class Editor(QMainWindow):
    def __init__(self):
        self.nome_arquivo = ""
        self.texto_alterado = False
        super(Editor, self).__init__()
        self.setGeometry(200, 50, 600, 600)
        self.setWindowTitle('My editor txt em PyQt5.')
        self.setWindowIcon(QIcon("img/teste.jpg"))
        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.onTextChanged)
        self.setCentralWidget(self.text_edit)
        self.definir_acoes()
        self.definir_menus()
        self.definir_barra_ferramentas()

    def onTextChanged(self):
        if(self.text_edit.toPlainText().__len__()) > 0:
            self.texto_alterado = True
        else:
            self.texto_alterado = False

    # novo| abrir| salvar| sair| copiar| colar
    def definir_acoes(self):
        self.acao_novo = QAction("&Novo")
        self.acao_novo.setShortcut("Ctrl+N")
        self.acao_novo.triggered.connect(self.novo)

        self.acao_abrir = QAction("&Abrir")
        self.acao_abrir.setShortcut("Ctrl+B")
        self.acao_abrir.triggered.connect(self.abrir)

        self.acao_salvar = QAction("&Salvar")
        self.acao_salvar.setShortcut("Ctrl+R")
        self.acao_salvar.triggered.connect(self.salvar)

        self.acao_sair = QAction("&Sair")
        self.acao_sair.setShortcut("Ctrl+S")
        self.acao_sair.triggered.connect(self.sair)

        self.acao_copiar = QAction("&Copiar")
        self.acao_copiar.setShortcut("Ctrl+C")
        self.acao_copiar.triggered.connect(self.copiar)

        self.acao_colar = QAction("Co&lar")
        self.acao_colar.setShortcut("Ctrl+V")
        self.acao_colar.triggered.connect(self.colar)

        self.acao_sobre = QAction("Sobre")
        self.acao_sobre.triggered.connect(self.sobre)

    def definir_menus(self):
        self.menu_arquivo = QMenu()
        self.menu_arquivo.setTitle("&Arquivo")
        self.menu_arquivo.addAction(self.acao_novo)
        self.menu_arquivo.addAction(self.acao_abrir)
        self.menu_arquivo.addAction(self.acao_salvar)
        self.menu_arquivo.addAction(self.acao_sair)

        self.menu_editar = QMenu()
        self.menu_editar.setTitle("&Editar")
        self.menu_editar.addAction(self.acao_copiar)
        self.menu_editar.addAction(self.acao_colar)

        self.menu_ajuda = QMenu()
        self.menu_ajuda.setTitle("Aj&uda")
        self.menu_ajuda.addAction(self.acao_sobre)

        self.menu = QMenuBar()
        self.menu.addMenu(self.menu_arquivo)
        self.menu.addMenu(self.menu_editar)
        self.menu.addMenu(self.menu_ajuda)

        self.setMenuBar(self.menu)

    def definir_barra_ferramentas(self):
        self.icone_novo = QIcon()
        self.icone_novo.addFile("img/new.png")
        self.tb_novo = QToolButton()
        self.tb_novo.setIcon(self.icone_novo)
        self.tb_novo.clicked.connect(self.novo)

        self.icone_abrir = QIcon()
        self.icone_abrir.addFile("img/open.png")
        self.tb_abrir = QToolButton()
        self.tb_abrir.setIcon(self.icone_abrir)
        self.tb_abrir.clicked.connect(self.abrir)

        self.icone_salvar = QIcon()
        self.icone_salvar.addFile("img/save.png")
        self.tb_salvar = QToolButton()
        self.tb_salvar.setIcon(self.icone_salvar)
        self.tb_salvar.clicked.connect(self.salvar)

        self.icone_sair = QIcon()
        self.icone_sair.addFile("img/close.png")
        self.tb_sair = QToolButton()
        self.tb_sair.setIcon(self.icone_sair)
        self.tb_sair.clicked.connect(self.sair)

        self.barra_de_ferramentas = QToolBar()
        self.barra_de_ferramentas.addWidget(self.tb_novo)
        self.barra_de_ferramentas.addWidget(self.tb_abrir)
        self.barra_de_ferramentas.addWidget(self.tb_salvar)
        self.barra_de_ferramentas.addWidget(self.tb_sair)

        self.addToolBar(self.barra_de_ferramentas)

    def novo(self):
        if self.texto_alterado:
            resposta = self.mensagem_confirmacao("Confirmação", f"Deseja salvar o arquivo {self.nome_arquivo}?")
            if resposta == QMessageBox.Yes:
                self.salvar()

            self.text_edit.clear()
            self.texto_alterado = False
            self.nome_arquivo = ""

    def abrir(self):
        if self.texto_alterado:
            resposta = self.mensagem_confirmacao("Confirmação", f"Deseja salvar o arquivo {self.nome_arquivo}?")
            if resposta == QMessageBox.Yes:
                self.salvar()

        fd = QFileDialog()
        arquivo = fd.getOpenFileName(None, "Abrir", "", "Arquivos de Texto (*.txt)")
        self.nome_arquivo = arquivo[0]

        if self.nome_arquivo:
            arq = open(arquivo[0])
            self.text_edit.setText(arq.read())
            arq.close()
            self.texto_alterado = False

    def salvar(self):
        if self.texto_alterado:
            if not self.nome_arquivo:
                fd = QFileDialog()
                self.nome_arquivo = fd.getSaveFileName(None, "Salvar Arquivo")
                if self.nome_arquivo:
                    self.nome_arquivo = self.nome_arquivo[0]

            if self.nome_arquivo:
                with open(self.nome_arquivo, "w") as file:
                    file.write(self.text_edit.toPlainText())
                    file.close()
                    self.texto_alterado = False

    def sair(self):
        if self.texto_alterado:
            if self.texto_alterado:
                resposta = self.mensagem_confimacao("Confirmação", f"Deseja salvar o arquivo {self.nome_arquivo}?")

                if resposta == QMessageBox.Yes:
                    self.salvar()
        QApplication.instance().quit()

    def copiar(self):
        self.text_edit.copy()

    def colar(self):
        self.text_edit.paste()

    def sobre(self):
        self.mensagem_aviso("Sobre o sistema", "Sistema de exemplo usando PyQt5.")

    def mensagem_aviso(self, titulo, texto):
        self.msgBox = QMessageBox()
        self.msgBox.setWindowTitle(titulo)
        self.msgBox.setText(texto);
        self.msgBox.setIcon(QMessageBox.Question)
        self.msgBox.addButton(QMessageBox.Yes)
        self.msgBox.addButton(QMessageBox.No)
        return self.msgBox.exec();

def iniciar():
    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec_())

iniciar()













