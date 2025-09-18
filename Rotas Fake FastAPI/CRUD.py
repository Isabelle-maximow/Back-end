# CRUD FSTAPI
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

# app fastapi:
app = FastAPI(title = "FastPI itens com sqlite")
BANCO = "itens.bd"

# criar tabela:
def criar_tabela():
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS Itens (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Price REAL NOT NULL,
        Quant INTEGER NOT NULL)""")
    conexao.commit()
    conexao.close()
criar_tabela()

# inserir um dado:
# conexao = sqlite3.connect(BANCO)
# cursor = conexao.cursor()
# cursor.execute(""" INSERT INTO Itens (
#     Nome, Price, Quant) VALUES ('caneta', 1.27, 50 )""")
# conexao.commit()

class Item(BaseModel):
    nome:str
    price:float
    quantidade:int

@app.get("/")
async def listar_itens():
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()
    cursor.execute("""SELECT * FROM itens""")
    todos_itens = cursor.fetchall()
    return{"itens":todos_itens}

# endpoint pegar pelo id:
@app.get("/")
async def get_itens():
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()
    cursor.execute("""SELECT * FROM itens""")
    itens = cursor.fetchall()
    if itens:
        return{"item": itens}
    return{"ERRO": "Item não encontrado"}