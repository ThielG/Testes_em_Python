import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QGridLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Consulta de endereço")
        self.setGeometry(100, 100, 500, 250)

        self.label_cep = QLabel("Digite o CEP:", self)

        # Configurações do campo de entrada
        self.campo_cep = QLineEdit(self)


        # Configurações do botão de consulta
        self.botao_consultar = QPushButton("Consultar", self)
        self.botao_consultar.clicked.connect(self.consultar_endereco)

        # Configurações do botão de limpar
        self.botao_limpar = QPushButton("Limpar", self)
        self.botao_limpar.clicked.connect(self.limpar_campos)

        # Configurações dos labels de saída
        self.label_logradouro = QLabel("", self)
        self.label_bairro = QLabel("", self)
        self.label_localidade = QLabel("", self)
        self.label_uf = QLabel("", self)

        # Em QGridLayout trabalhamos com linhas e colunas, onde o primeiro argumento é a linha e o segundo é a coluna
        # Configurações do layout da janela
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)
        self.layout.addWidget(self.label_cep, 0, 0)
        self.layout.addWidget(self.campo_cep, 0, 1)
        self.layout.addWidget(self.botao_consultar, 0, 2)
        self.layout.addWidget(self.botao_limpar, 0, 3)
        self.layout.addWidget(self.label_logradouro, 1, 0)
        self.layout.addWidget(self.label_bairro, 2, 0)
        self.layout.addWidget(self.label_localidade, 3, 0)
        self.layout.addWidget(self.label_uf, 4, 0)

    def consultar_endereco(self):
        cep = self.campo_cep.text()

        # Faz a requisição à API dos Correios
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)

        if response.status_code == 200:
            # Exibe os componentes do endereço nos QTextEdit
            endereco = response.json()
            self.label_logradouro.setText(f"Logradouro: {endereco['logradouro']}")
            self.label_bairro.setText(f"Bairro: {endereco['bairro']}")
            self.label_localidade.setText(f"Localidade: {endereco['localidade']}")
            self.label_uf.setText(f"UF: {endereco['uf']}")
        else:
            self.label_logradouro.setText("Erro ao consultar o endereço.")
            self.label_bairro.setText("")
            self.label_localidade.setText("")
            self.label_uf.setText("")

    def limpar_campos(self):
        # Limpa o conteúdo dos campos de texto
        self.campo_cep.setText("")
        self.label_logradouro.setText("")
        self.label_bairro.setText("")
        self.label_localidade.setText("")
        self.label_uf.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
