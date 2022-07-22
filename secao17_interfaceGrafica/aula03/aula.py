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
        self.validacaoGrupo = QGroupBox("Validação")
        validacaoLabel = QLabel("Tipo: ")
        self.validacaoComboBox = QComboBox()
        self.validacaoComboBox.addItem('Não validar')
        self.validacaoComboBox.addItem('Validar inteiro')
        self.validacaoComboBox.addItem('Validar double')
        self.validacaoLineEdit = QLineEdit()
        validacaoLayout = QGridLayout()
        validacaoLayout.addWidget(validacaoLabel, 0, 0)
        validacaoLayout.addWidget(self.validacaoComboBox, 0, 1)
        validacaoLayout.addWidget(self.validacaoLineEdit, 1, 0, 1, 2)
        self.validacaoGrupo.setLayout(validacaoLayout)

    def criarGrupoAlinhamento(self):
        self.alinhamentoGrupo = QGroupBox("Alinhamento")
        alinhamentoLabel = QLabel("Tipo: ")
        self.alinhamentoComboBox = QComboBox()
        self.alinhamentoComboBox.addItem('Esquerda')
        self.alinhamentoComboBox.addItem('Centro')
        self.alinhamentoComboBox.addItem('Direita')
        self.alinhamentoLineEdit = QLineEdit()
        alinhamentoLayout = QGridLayout()
        alinhamentoLayout.addWidget(alinhamentoLabel, 0, 0)
        alinhamentoLayout.addWidget(self.alinhamentoComboBox, 0, 1)
        alinhamentoLayout.addWidget(self.alinhamentoLineEdit, 1, 0, 1, 2)
        self.alinhamentoGrupo.setLayout(alinhamentoLayout)

    def criarGrupoMascara(self):
        self.mascaraGrupo = QGroupBox("Máscara de entrada")
        mascaraLabel = QLabel("Tipo: ")
        self.mascaraComboBox = QComboBox()
        self.mascaraComboBox.addItem('Sem máscara')
        self.mascaraComboBox.addItem('Celular')
        self.mascaraComboBox.addItem('Data')
        self.mascaraComboBox.addItem('CPF')
        self.mascaraLineEdit = QLineEdit()
        mascaraLayout = QGridLayout()
        mascaraLayout.addWidget(mascaraLabel, 0, 0)
        mascaraLayout.addWidget(self.mascaramboBox, 0, 1)
        mascaraLayout.addWidget(self.mascaraLineEdit, 1, 0, 1, 2)
        self.mascaraGrupo.setLayout(mascaraLayout)

    def criarGrupoEdicao(self):
        self.edicaoGrupo = QGroupBox("Edicão")
        edicaoLabel = QLabel("Somente leitura: ")
        self.edicaoComboBox = QComboBox()
        self.edicaoComboBox.addItem('Falso')
        self.edicaoComboBox.addItem('Verdadeiro')
        self.edicaoLineEdit = QLineEdit()
        edicaoLayout = QGridLayout()
        edicaoLayout.addWidget(edicaoLabel, 0, 0)
        edicaoLayout.addWidget(self.edicaoComboBox, 0, 1)
        edicaoLayout.addWidget(self.edicaoLineEdit, 1, 0, 1, 2)
        self.edicaoGrupo.setLayout(edicaoLayout)










