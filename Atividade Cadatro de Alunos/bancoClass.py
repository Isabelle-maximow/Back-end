import sqlite3
BANCO_DE_DADOS = "aluno.db"

class Banco:
    def __init__(self, nome = BANCO_DE_DADOS):
        self.nome = nome
        self.conexao = sqlite3.connect(self.nome)
        self.cursor = self.conexao.cursor()
        self.conectar_db()
        
    def conectar_db(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS aluno (
                        nome TEXT NOT NULL,
                        nota1 REAL NOT NULL,
                        nota2 REAL NOT NULL,
                        nota3 REAL NOT NULL,
                        media REAL NOT NULL,
                        situacao TEXT NOT NULL)''')
        self.conexao.commit()