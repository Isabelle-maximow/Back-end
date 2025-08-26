import mysql.connector

# configurar a conexão com o banco de dados:
CONFIG_BANCO = {
    'host': 'localhost', # local do servidor de banco
    'user': 'root', # usuario que vi logar no servidor
    'password': 'dev1t@24', # senha definida no servidor 
    'database': 'isabelle_db', # nome do banco de dados
}

conexao = mysql.connector.connect(**CONFIG_BANCO) # conectando
cursor = conexao.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS teste (
    nome VARCHAR(100) NOT NULL)""")
conexao.commit()