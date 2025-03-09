# Loja Virtual em PyQt6

## Descrição
Este projeto é uma aplicação de cadastro de roupas desenvolvida em Python utilizando PyQt6. Ele permite o cadastro e remoção de produtos em um arquivo de texto (`produtos.txt`).

## Funcionalidades
- Adicionar produtos com ID, Nome, Descrição e Preço
- Remover produtos da lista
- Exibir a lista de produtos em uma tabela
- Persistência de dados em arquivo TXT

## Instalação e Configuração
### 1. Instalação das bibliotecas necessárias
Antes de executar o programa, é necessário instalar o PyQt6 caso ainda não esteja instalado:
```sh
pip install PyQt6
```

### 2. Estrutura do Projeto
O projeto deve conter os seguintes arquivos:
```
LojaVirtual/
├── main.py          # Arquivo principal da aplicação
├── produtos.txt     # Arquivo de armazenamento dos produtos
└── style.css        # Arquivo de estilo para a interface
```

### 3. Como Executar o Projeto
Execute o arquivo principal `main.py`:
```sh
python main.py
```

## Como o Código Funciona
### 1. Importação das Bibliotecas
```python
import os
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)
from PyQt6.QtGui import QFont
```
- `os` e `sys`: Para manipulação de arquivos e controle do sistema.
- `PyQt6.QtWidgets`: Para criação da interface gráfica.
- `PyQt6.QtGui`: Para personalização de fontes.

### 2. Manipulação de Arquivos
A aplicação salva e carrega produtos de um arquivo `produtos.txt`:
```python
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
```

### 3. Interface Gráfica
A interface é criada utilizando `QWidget` e `QVBoxLayout`:
```python
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastramento de Roupas")
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
```

### 4. Adicionando Produtos
```python
def adicionar_produto(self):
    id_produto = self.id_input.text().strip()
    nome = self.nome_input.text().strip()
    descricao = self.desc_input.text().strip()
    preco = self.preco_input.text().strip()
    
    if not id_produto or not nome or not descricao or not preco:
        QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios!")
        return
    
    self.produtos.append([id_produto, nome, descricao, preco])
    salvar_arquivo(self.produtos)
    self.atualizar_tabela()
```

### 5. Removendo Produtos
```python
def remover_produto(self):
    linha_selecionada = self.produtos_tabela.currentRow()
    if linha_selecionada == -1:
        QMessageBox.warning(self, "Erro", "Selecione um produto para remover.")
        return
    
    self.produtos.pop(linha_selecionada)
    salvar_arquivo(self.produtos)
    self.atualizar_tabela()
```

## Conclusão
Este projeto é um exemplo simples de como criar uma aplicação de cadastro de produtos utilizando PyQt6. Ele pode ser expandido para incluir funcionalidades como edição de produtos, filtros e banco de dados para armazenar os dados de maneira mais eficiente.

