import sqlite3
BANCO_DE_DADOS = "loja.bd"

# conectar ao banco:
class BancoDeDados:
    def __init__(self, nome_bd = BANCO_DE_DADOS): # instanciar o bd
        self.nome_bd = nome_bd
        self.conexao = sqlite3.connect(self.nome_bd)
        self.cursor = self.conexao.cursor()
    
    # metodos:
    def criar_tabela(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Produtos(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Preço REAL NOT NULL,
            Quantidade INTEGER NOT NULL)""")
        self.conexao.commit()
        
# banco = BancoDeDados()
# banco.criar_tabela()

    def fechar_conexao(self):
        self.conexao.close()
    def executar_comandos(self, comando, parametros = ()):
        self.cursor.execute(comando, parametros)
        self.conexao.commit()
    def buscar_dados(self, comando, parametros = ()):
        self.cursor.execute(comando, parametros)
        return self.cursor.fetchall()
    
banco = BancoDeDados()    
banco.executar_comando("""INSERT INTO Produtos(
    Nome, Preço, Quantidade) VALUES (?,?,?)""",
    ("Camisa", 80.91, 10))

# buscar produtos
produtos = banco.buscar_dados("SELECT * FROM Produtos")
for i in produtos:
    print(f"""
          ID: {i[0]}
          Nome: {i[1]}
          Preço: {i[2]}
          Quantidade: {i[3]}""")
    banco.fechar_conexao()