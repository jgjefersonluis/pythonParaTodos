from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QApplication


class ExemploBoxLayout(QWidget):
    def __init__(self):
        super(ExemploBoxLayout, self).__init__()
        self.setWindowTitle("Exemplo QHBoxLayout e QVBoxLayout")
        self.adicionarComponentes()
        self.definirLayoutTela()

    def adicionarComponentes(self):
        self.label1 = QLabel("Label 1")
        self.edit1 = QLineEdit()
        self.edit1.setText("Edit 1")
        self.label2 = QLabel("Label 2")
        self.edit2 = QLineEdit()
        self.edit2.setText("Edit 2")
        self.label3 = QLabel("Label 3")
        self.edit3 = QLineEdit()
        self.edit3.setText("Edit 3")
        self.label4 = QLabel("Label 4")
        self.edit4 = QLineEdit()
        self.edit4.setText("Edit 4")

    def definirLayoutTela(self):
        layoutTela = QHBoxLayout()
        layoutTela.addWidget(self.label1)
        layoutTela.addWidget(self.edit1)
        layoutTela.addWidget(self.label2)
        layoutTela.addWidget(self.edit2)
        layoutTela.addWidget(self.label3)
        layoutTela.addWidget(self.edit3)
        layoutTela.addWidget(self.label4)
        layoutTela.addWidget(self.edit4)
        self.setLayout(layoutTela)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    janela = ExemploBoxLayout()
    janela.show()
    sys.exit(app.exec_())













