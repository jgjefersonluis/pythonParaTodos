from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPicture, QPixmap
import sys

class ExemploLabel(QWidget):
    def __init__(self):
        super(ExemploLabel, self).__init__()
        self.setWindowTitle("Exemplo QLabel (Rótulo)")
        self.setGeometry(200, 200, 400, 200)

        # Criando os componentes
        self.label_nome = QLabel("Nome")
        self.edit_nome = QLineEdit()
        self.label_sobrenome = QLabel("Sobrenome")
        self.edit_sobrenome = QLineEdit()
        self.label_celular = QLabel("&Celular")
        self.edit_celular = QLineEdit()
        self.label_nascimento = QLabel("&Data de nascimento")
        self.edit_nascimento = QLineEdit()
        self.label_numero = QLabel()
        self.label_figura = QLabel()
        self.label_imagem = QLabel()

        # Caso seja utilizado & mas não seja setado o objeto que
        # vai receber o foco utilizando alt com setBuddy(),
        # o & será exibido como um texto qualquer
        # Ao definir com setBuddy(), a letra à direita vira um atalho
        # ao pressionar alt + letra, posicionando o cursor no componente
        # informado em setBuddy() [companheiro, camarada]
        self.label_endereco = QLabel("&Endereço completo")
        self.edit_endereco = QLineEdit()

        # alterando o texto do label com setText()
        self.label_nome.setText("&Primeiro nome")

        # Definindo o estilo com setFrameStyle()
        #   QFrame.Panel    O label é exibido com bordas, como se fosse um painel
        #   QFrame.Raised   Coloca as bordas do painel em alto-relevo, é usado em conjunto com Panel
        #   QFrame.Sunken   Coloca as bordas do painel em baixo-relevo, é usado em conjunto com Panel
        self.label_sobrenome.setFrameStyle(QFrame.Panel)
        self.label_celular.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.label_nascimento.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        # Definindo o alinhamento com setAlignment
        # AlignCenter   Alinha o texto ao centro
        # AlignRight   Alinha o texto à direita
        # AlignLeft   Alinha o texto à esquerda
        self.label_sobrenome.setAlignment(Qt.AlignCenter)
        self.label_celular.setAlignment(Qt.AlignRight)
        self.label_nascimento.setAlignment(Qt.AlignLeft)

        # Definindo qual componente vai receber o foco,
        # quando for usado "alt+letra sublinhada".
        # A letra sublinhada é definida com o caractere "&"
        self.label_nome.setBuddy(self.edit_nome)
        self.label_sobrenome.setBuddy(self.edit_sobrenome)
        self.label_celular.setBuddy(self.edit_celular)
        self.label_nascimento.setBuddy(self.edit_nascimento)

        # Criando um objeto QVBoxLayout e adicionando os componentes
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_nome)
        self.layout.addWidget(self.edit_nome)
        self.layout.addWidget(self.label_sobrenome)
        self.layout.addWidget(self.edit_sobrenome)
        self.layout.addWidget(self.label_celular)
        self.layout.addWidget(self.edit_celular)
        self.layout.addWidget(self.label_nascimento)
        self.layout.addWidget(self.edit_nascimento)
        self.layout.addWidget(self.label_endereco)
        self.layout.addWidget(self.edit_endereco)
        self.layout.addWidget(self.label_numero)
        self.layout.addWidget(self.label_figura)

        # Informando o texto exibido ao passar o mouse sobre o label
        self.label_nome.setToolTip("Informe o nome")

        # Definindo um número texto do label (pode ser inteiro ou double)
        self.label_numero.setNum(10.5)

        # Usando o QPicture para armazenar uma figura criada com QPainter
        # E usando setPicture para definir a figura para o label
        figura = QPicture()
        pintor = QPainter();
        pintor.begin(figura)
        # drawEllipse(x, y, largura, altura)
        # como vou desenhar no label, o ponto inicial vai ser indiferente
        pintor.drawEllipse(0, 0, 60, 60)
        pintor.end()
        self.label_figura.setPicture(figura)

        # Usando QPixmap para carregar uma imagem
        # e definindo a imagem para o label com setPixmap
        pixmap = QPixmap('img/teste2.jpg')
        self.label_imagem.setPixmap(pixmap)

        # Definindo o "layout" como layout da janela
        self.setLayout(self.layout)

app = QApplication(sys.argv)
jan = ExemploLabel()
jan.show()
sys.exit(app.exec_())





































