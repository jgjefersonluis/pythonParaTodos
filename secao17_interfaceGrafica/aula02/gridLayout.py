from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit, QGridLayout, QPushButton)


class ExemploLineEdit(QWidget):
    def __init__(self):
        super(ExemploLineEdit, self).__init__()
        self.setWindowTitle("Exemplo QGridLayout")
        self.adicionarComponentes()
        self.definirLayoutTela()

    def adicionarComponentes(self):
        self.label_linha_0_coluna_0 = QLabel("Coluna 0")
        self.edit_linha_1_coluna_0 = QLineEdit()

        self.label_linha_0_coluna_1 = QLabel("Coluna 1")
        self.edit_linha_1_coluna_1 = QLineEdit()

        self.label_linha_0_coluna_2 = QLabel("Coluna 2")
        self.edit_linha_1_coluna_2 = QLineEdit()

        self.label_linha_2_coluna_0_ate_coluna2 = QLabel("Todas as colunas")
        self. edit_linha_3_coluna_0_ate_coluna2 = QLineEdit()

    def definirLayoutTela(self):
        layoutTela = QGridLayout()
        layoutTela.addWidget(self.label_linha_0_coluna_0, 0, 0)
        layoutTela.addWidget(self.edit_linha_1_coluna_0, 1, 0)
        layoutTela.addWidget(self.label_linha_0_coluna_1, 0, 1)
        layoutTela.addWidget(self.edit_linha_1_coluna_1, 1, 1)
        layoutTela.addWidget(self.label_linha_0_coluna_2, 0, 2)
        layoutTela.addWidget(self.edit_linha_1_coluna_2, 1, 2)

        layoutTela.addWidget(self.label_linha_2_coluna_0_ate_coluna2, 2, 0)
        layoutTela.addWidget(self.edit_linha_3_coluna_0_ate_coluna2, 3, 0, 1, 3)

        self.setLayout(layoutTela)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    janela = ExemploLineEdit()
    janela.show()
    sys.exit(app.exec_())
