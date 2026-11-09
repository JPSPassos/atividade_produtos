import os
import sqlite3


CAMINHO_BANCO = os.path.join(os.path.dirname(__file__), "produtos.db")


def conectar_banco(caminho=None):
    if caminho is None:
        caminho = CAMINHO_BANCO
    conexao = sqlite3.connect(caminho)
    conexao.row_factory = sqlite3.Row
    return conexao


def inicializar_banco(caminho=None):
    conexao = conectar_banco(caminho)
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL,
            categoria VARCHAR(50)
        )
    ''')
    conexao.commit()
    conexao.close()