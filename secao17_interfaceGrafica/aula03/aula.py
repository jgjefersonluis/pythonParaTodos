from PyQt5.QtWidgets import QWidget, QGroupBox, QLabel, QComboBox, QLineEdit, QGridLayout


class ExemploLineEdit(QWidget):
    def __init__(self):
        super(ExemploLineEdit, self).__init__()
        self.setWindowTitle("Exemplo QLineEdit e QComboBox")
        self.criarGrupoSenha()
        self.criarGrupoValidacao()
        self.criarGrupoAlinhamento()
        self.criarGrupoMascara()
        self.criarGrupoEdicao()
        self.definirLayoutTela()
        self.definirEventos()

    def criarGrupoSenha(self):
        self.senhaGrupo = QGroupBox("Senha")
        senhaLabel = QLabel("Modo:")
        self.senhaComboBox = QComboBox()
        self.senhaComboBox.addItem("Normal")
        self.senhaComboBox.addItem("Senha")
        self.senhaComboBox.addItem("Senha ao sair")
        self.senhaComboBox.addItem("Não exibe")
        self.senhaLabelMostra = QLabel("")
        self.senhaLineEdit = QLineEdit()
        self.senhaLineEdit.setFocus()
        senhaLayout = QGridLayout()
        senhaLayout.addWidget(senhaLabel, 0, 0)
        senhaLayout.addWidget(self.senhaComboBox, 0, 1)
        senhaLayout.addWidget(self.senhaLineEdit, 1, 0, 1, 2)
        senhaLayout.addWidget(self.senhaLabelMostra, 2, 0, 1, 2)
        self.senhaGrupo.setLayout(senhaLayout)

    def criarGrupoValidacao(self):
        pass

    def criarGrupoAlinhamento(self):
        pass

    def criarGrupoMascara(self):
        pass

    def criarGrupoEdicao(self):
        pass










