import os
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)
from PyQt6.QtGui import QFont

# Funções de arquivo
def ler_arquivo():
    if not os.path.exists('produtos.txt'):
        return []
    with open('produtos.txt', 'r') as file:
        produtos = [linha.strip().split(', ') for linha in file.readlines()]
    return produtos

def salvar_arquivo(produtos):
    with open('produtos.txt', 'w') as file:
        for produto in produtos:
            file.write(', '.join(produto) + '\n')

# Interface gráfica
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastramento de Roupas")
        self.setGeometry(100, 100, 600, 400)

        # Layout principal
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Título
        titulo = QLabel("Cadastramento de Roupas")
        titulo.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.layout.addWidget(titulo)

        # Formulário
        self.form_layout = QHBoxLayout()
        self.layout.addLayout(self.form_layout)

        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("ID")
        self.form_layout.addWidget(self.id_input)

        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Nome")
        self.form_layout.addWidget(self.nome_input)

        self.desc_input = QLineEdit()
        self.desc_input.setPlaceholderText("Descrição")
        self.form_layout.addWidget(self.desc_input)

        self.preco_input = QLineEdit()
        self.preco_input.setPlaceholderText("Preço")
        self.form_layout.addWidget(self.preco_input)

        # Botões
        self.botao_layout = QHBoxLayout()
        self.layout.addLayout(self.botao_layout)

        self.adicionar_btn = QPushButton("Adicionar Produto")
        self.adicionar_btn.clicked.connect(self.adicionar_produto)
        self.botao_layout.addWidget(self.adicionar_btn)

        self.remover_btn = QPushButton("Remover Produto")
        self.remover_btn.clicked.connect(self.remover_produto)
        self.botao_layout.addWidget(self.remover_btn)

        # Tabela de produtos
        self.produtos_tabela = QTableWidget()
        self.produtos_tabela.setColumnCount(4)
        self.produtos_tabela.setHorizontalHeaderLabels(["ID", "Nome", "Descrição", "Preço"])
        self.layout.addWidget(self.produtos_tabela)

        # Carregar produtos iniciais
        self.produtos = ler_arquivo()
        self.atualizar_tabela()

    def adicionar_produto(self):
        id_produto = self.id_input.text().strip()
        nome = self.nome_input.text().strip()
        descricao = self.desc_input.text().strip()
        preco = self.preco_input.text().strip()

        if not id_produto or not nome or not descricao or not preco:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios!")
            return

        if not preco.replace('.', '', 1).isdigit():
            QMessageBox.warning(self, "Erro", "Preço inválido! Use um número.")
            return

        # Adicionar produto à lista e salvar
        self.produtos.append([id_produto, nome, descricao, preco])
        salvar_arquivo(self.produtos)
        self.atualizar_tabela()

        # Limpar inputs
        self.id_input.clear()
        self.nome_input.clear()
        self.desc_input.clear()
        self.preco_input.clear()

        QMessageBox.information(self, "Sucesso", "Produto adicionado com sucesso!")

    def remover_produto(self):
        linha_selecionada = self.produtos_tabela.currentRow()
        if linha_selecionada == -1:
            QMessageBox.warning(self, "Erro", "Selecione um produto para remover.")
            return

        # Remover produto da lista e salvar
        self.produtos.pop(linha_selecionada)
        salvar_arquivo(self.produtos)
        self.atualizar_tabela()

        QMessageBox.information(self, "Sucesso", "Produto removido com sucesso!")

    def atualizar_tabela(self):
        self.produtos_tabela.setRowCount(len(self.produtos))
        for row, produto in enumerate(self.produtos):
            for col, valor in enumerate(produto):
                self.produtos_tabela.setItem(row, col, QTableWidgetItem(valor))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Aplicar o CSS
    css_path = "style.css"
    if os.path.exists(css_path):
        with open(css_path, "r") as file:
            app.setStyleSheet(file.read())
    else:
        print(f"Arquivo de estilo '{css_path}' não encontrado. Usando estilos padrão.")

    janela = App()
    janela.show()
    sys.exit(app.exec())
