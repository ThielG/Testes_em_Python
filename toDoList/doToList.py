import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, \
    QInputDialog


class AppListaTarefas(QWidget):
    def __init__(self):
        super().__init__()

        self.tarefas = []

        # Configuração da janela principal
        self.setWindowTitle('Aplicativo de Lista de Tarefas')
        self.setGeometry(100, 100, 400, 300)

        # Widgets da interface
        self.txt_tarefa = QLineEdit(self)
        self.btn_adicionar = QPushButton('Adicionar', self)
        self.btn_adicionar.clicked.connect(self.adicionar_tarefa)
        # personalização do botão
        self.btn_adicionar.setStyleSheet(
            "background-color: lightgreen; border-radius: 5px; border: 2px solid green;")  # Efeito de relevo

        self.btn_concluir = QPushButton('Concluir Tarefa', self)
        self.btn_concluir.clicked.connect(self.concluir_tarefa)
        # personalização do botão
        self.btn_concluir.setStyleSheet(
            "background-color: lightblue; border-radius: 5px; border: 2px solid blue;")  # Efeito de relevo

        self.btn_editar = QPushButton('Editar Tarefa', self)
        self.btn_editar.clicked.connect(self.editar_tarefa)
        # personalização do botão
        self.btn_editar.setStyleSheet(
            "background-color: lightyellow; border-radius: 5px; border: 2px solid orange;")  # Efeito de relevo

        self.btn_remover = QPushButton('Remover Tarefa', self)
        self.btn_remover.clicked.connect(self.remover_tarefa)
        # personalização do botão
        self.btn_remover.setStyleSheet(
            "background-color: lightcoral; border-radius: 5px; border: 2px solid red;")  # Efeito de relevo

        # Criação do widget QListWidget para exibir a lista de tarefas
        self.lista_tarefas = QListWidget(self)

        # Layout vertical
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.txt_tarefa)
        layout_vertical.addWidget(self.btn_adicionar)
        layout_vertical.addWidget(self.btn_concluir)
        layout_vertical.addWidget(self.btn_editar)
        layout_vertical.addWidget(self.btn_remover)
        layout_vertical.addWidget(self.lista_tarefas)

        self.setLayout(layout_vertical)

    def adicionar_tarefa(self):
        # Função para adicionar uma tarefa à lista
        tarefa = self.txt_tarefa.text()
        if tarefa:
            self.lista_tarefas.addItem(tarefa)
            self.txt_tarefa.clear()

    def concluir_tarefa(self):
        # Função para marcar uma tarefa como concluída
        selected_item = self.lista_tarefas.currentItem()
        if selected_item:
            # Define a tarefa como concluída e impede a seleção ou edição
            selected_item.setFlags(selected_item.flags() | Qt.ItemIsUserCheckable)
            selected_item.setCheckState(Qt.Checked)
            selected_item.setFlags(~Qt.ItemIsSelectable)
            selected_item.setFlags(~Qt.ItemIsEnabled)

    def editar_tarefa(self):
        # Função para editar uma tarefa
        selected_item = self.lista_tarefas.currentItem()
        if selected_item:
            # Exibe uma caixa de diálogo para editar o texto da tarefa
            new_text, ok = QInputDialog.getText(self, "Editar Tarefa", "Editar a tarefa:", text=selected_item.text())
            if ok and new_text:
                selected_item.setText(new_text)

    def remover_tarefa(self):
        # Função para remover uma tarefa
        selected_item = self.lista_tarefas.currentItem()
        if selected_item:
            # Remove a tarefa selecionada da lista
            self.lista_tarefas.takeItem(self.lista_tarefas.row(selected_item))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_lista_tarefas = AppListaTarefas()
    app_lista_tarefas.show()
    sys.exit(app.exec())
