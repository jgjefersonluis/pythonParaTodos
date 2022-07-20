import sys
from PyQt5.QtWidgets import QApplication, QDialog

# Criando a instância da aplicação
app = QApplication(sys.argv)

# Imprimindo os argumentos passados por linha de comando
print(sys.argv)

# QDialog é a classe base para janelas de diálogo
janela = QDialog()

# Exibindo a janel
janela.show()

# Executando a aplicação e encerrando em seguida
# Aqui entramos no mainloop da aplicação
sys.exit(app.exec_())

