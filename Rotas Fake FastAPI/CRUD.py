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
@app.get("/itens-nome/{item_nome}")
async def get_item_nome(item_nome: str):
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()
    cursor.execute("""SELECT * FROM itens WHERE nome = ?""",
                   (item_nome,))
    itens = cursor.fetchall()
    if itens:
        return{"item": itens}
    return{"ERRO": "Item não encontrado"}

# endpoint criar item (post)
@app.post("/itens-criar/")
async def criar_item(item: Item):
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()
    cursor.execute("""INSERT INTO itens (
        nome, price, quantidade) VALUES (?,?,?)""",
        item.nome, item.price, item.quantidade)
    conexao.commit()
    item_id = cursor.lastrowid # criar o item na ultima linha
    return {"id": item_id, "mensagem": "item criado"}
    
# endpoint PUT atualizar dados
@app.put("/itens-atualizar/{item_id}")
async def update_item (item_id: int):
    conexao = sqlite3.connect(BANCO)
    cursor = conexao.cursor()
    cursor.execute("""UPDATE itens SET nome = ?, price = ?, 
                   quantidade = ?  WHERE id = ?""",
        item.nome, item.price, item.quantidade)
    conexao.commit()