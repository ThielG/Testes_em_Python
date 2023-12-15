import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class AplicacaoConsultaCNPJ(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consulta de CNPJ")
        self.setGeometry(100, 100, 600, 500)
        self.tamanho_original = self.size()

        # Componentes da interface
        self.cnpj_rotulo = QLabel("CNPJ:")
        self.cnpj_entrada = QLineEdit()

        self.botao_consultar = QPushButton("Consultar")
        self.botao_consultar.clicked.connect(self.consultar_cnpj)

        self.rotulo_resultado = QLabel("Resultado:")

        self.rotulo_nome = QLabel("Nome:")
        self.campo_nome = QLineEdit()

        self.rotulo_abertura = QLabel("Abertura:")
        self.campo_abertura = QLineEdit()

        self.rotulo_situacao = QLabel("Situação:")
        self.campo_situacao = QLineEdit()

        self.rotulo_tipo = QLabel("Tipo:")
        self.campo_tipo = QLineEdit()

        self.rotulo_logradouro = QLabel("Logradouro:")
        self.campo_logradouro = QLineEdit()

        self.rotulo_numero = QLabel("Número:")
        self.campo_numero = QLineEdit()

        self.rotulo_bairro = QLabel("Bairro:")
        self.campo_bairro = QLineEdit()

        self.rotulo_municipio = QLabel("Município:")
        self.campo_municipio = QLineEdit()

        self.rotulo_uf = QLabel("UF:")
        self.campo_uf = QLineEdit()

        self.rotulo_cep = QLabel("CEP:")
        self.campo_cep = QLineEdit()

        self.botao_limpar = QPushButton("Limpar Campos")
        self.botao_limpar.clicked.connect(self.limpar_campos)

        # Layout da interface
        layout = QVBoxLayout()
        layout.addWidget(self.cnpj_rotulo)
        layout.addWidget(self.cnpj_entrada)
        layout.addWidget(self.botao_consultar)
        layout.addWidget(self.rotulo_resultado)
        layout.addWidget(self.rotulo_nome)
        layout.addWidget(self.campo_nome)
        layout.addWidget(self.rotulo_abertura)
        layout.addWidget(self.campo_abertura)
        layout.addWidget(self.rotulo_situacao)
        layout.addWidget(self.campo_situacao)
        layout.addWidget(self.rotulo_tipo)
        layout.addWidget(self.campo_tipo)
        layout.addWidget(self.rotulo_logradouro)
        layout.addWidget(self.campo_logradouro)
        layout.addWidget(self.rotulo_numero)
        layout.addWidget(self.campo_numero)
        layout.addWidget(self.rotulo_bairro)
        layout.addWidget(self.campo_bairro)
        layout.addWidget(self.rotulo_municipio)
        layout.addWidget(self.campo_municipio)
        layout.addWidget(self.rotulo_uf)
        layout.addWidget(self.campo_uf)
        layout.addWidget(self.rotulo_cep)
        layout.addWidget(self.campo_cep)
        layout.addWidget(self.botao_limpar)

        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

    def validar_cnpj(self, cnpj):
        return cnpj.isnumeric() and len(cnpj) == 14

    def consultar_cnpj(self):
        cnpj = (self.cnpj_entrada.text().replace('.', '').replace('/', '')
                .replace('-', ''))  # Remove ".", "/", e "-"
        if not self.validar_cnpj(cnpj):
            self.rotulo_resultado.setText("CNPJ inválido.")
            return

        resposta = self.obter_dados_cnpj(cnpj)
        if resposta:
            self.preencher_formulario(resposta)
        else:
            self.rotulo_resultado.setText("CNPJ não encontrado ou erro na requisição.")

    def obter_dados_cnpj(self, cnpj):
        url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
        try:
            resposta = requests.get(url)
            if resposta.status_code == 200:
                dados = resposta.json()
                return dados
        except Exception as e:
            print(e)
        return None

    def preencher_formulario(self, dados):
        self.campo_nome.setText(dados.get("nome", ""))
        self.campo_abertura.setText(dados.get("abertura", ""))
        self.campo_situacao.setText(dados.get("situacao", ""))
        self.campo_tipo.setText(dados.get("tipo", ""))
        self.campo_logradouro.setText(dados.get("logradouro", ""))
        self.campo_numero.setText(dados.get("numero", ""))
        self.campo_bairro.setText(dados.get("bairro", ""))
        self.campo_municipio.setText(dados.get("municipio", ""))
        self.campo_uf.setText(dados.get("uf", ""))
        self.campo_cep.setText(dados.get("cep", ""))

    def limpar_campos(self):
        self.cnpj_entrada.clear()
        self.campo_nome.clear()
        self.campo_abertura.clear()
        self.campo_situacao.clear()
        self.campo_tipo.clear()
        self.campo_logradouro.clear()
        self.campo_numero.clear()
        self.campo_bairro.clear()
        self.campo_municipio.clear()
        self.campo_uf.clear()
        self.campo_cep.clear()
        self.resize(self.tamanho_original)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = AplicacaoConsultaCNPJ()
    janela.show()
    sys.exit(app.exec())
