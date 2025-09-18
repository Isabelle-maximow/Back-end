# ROTAS FAKE FAST API
# métodos http get, pot, put ee delete
from fastapi import FastAPI
from pydantic import BaseModel

# instancia da api:
app = FastAPI( title = "Rotas fake API")
# endpoint simples de teste
@app.get("/")
async def teste_api():
    return {"mensagem": "teste get API"}

# rodar api pasta do arquivo da API:
# python -m uvicorn nome_arquivo:app --reload

# diciconarios de produtos fake para teste:
produtos = {
    1: {"nome": "caneta", "price" : 2.55, "quant": 100},
    1: {"nome": "borracha", "price" : 1.55, "quant": 100},
    1: {"nome": "lapis", "price" : 3.55, "quant": 100},
}

# ---- GETS: ----
# endpoint todos os produtos:
@app.get("/produtos")
async def get_produtos():
    return produtos

# endpoint proutos:
@app.get("/get-produtos/{id_podutos}")
async def produtos_id (id_produto: int):
    return produtos[id_produto]

# endpoint produto por nome:
@app.get("/get-produto-nome")
async def get_produto_nome(nome: str):
    for i in produtos: 
        if produtos [i] ["nome"] == nome: # retornar o produto pelo index
            return produtos[i] #retorna o produto pelo index
    return {"dados": "Produto não encontrado"}


# pydantic com manipulação de dados 
class Item(BaseModel):
    # objeto produto nome, preço e quantidade:
    nome: str
    price: float 
    quant: int

# ---- POST: ----
# endpoint para criar um item em produtos:
@app.post("/items")
async def criar_item(item:Item): # instanciar o BaseModel
    return {"item": item}

# ---- PUT: ----
# endpoint para atualizar um item 
@app.put("/items-update/{item_id}") #atualiar item pelo id
async def update_item(item_id: int, item:Item):
    return {"item_id": item_id, "update_item": item}

# ---- DELETE: ----
# endpoint para dltar um item put
@app.delete("/items-update/{item_id}") # deletar item pelo id
async def deletar_item(item_id: int):
    return {"mensagem": f"Item {item_id} deletado"}