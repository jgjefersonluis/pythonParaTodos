from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit


class ExemploLineEdit(QWidget):
    def __int__(self):
        super(ExemploLineEdit, self).__init__()
        self.setWindowTitle("Exemplo QGridLayout")
        self.adicionarComponentes()
        self.definirLayoutTela()

    def adicionarComponentes(self):
        self.label_linha_0_coluna_0 = QLabel("Coluna 0")
        self.edit_linha_1_coluna_0 = QLineEdit()







    def definirLayoutTela(self):
        pass

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    janela = ExemploLineEdit()
    janela.show()
    sys.exit(app.exec_())
