'''
api router para ligar o back-end com o front-end redireção
da aplicação

'''
# import da api rota controller - template
from fastapi import APIRouter,Depends,Request
# conexão sqlite
from sqlalchemy.orm import Session
# conexão com engine
from database import SessionLocal
# modelos nome e email
from models import SessionLocal
# metodo http, redirecionar o código para o html
from fastapi.responses import HTMLResponse
# motor gráfica do template renderizar o html
from fastapi.templating import Jinja2Templates

# criar o roteador para organizar as rotas
router=APIRouter()

# configurar a pasta do front-end 'templates' Jinja2
templates=Jinja2Templates(directory="viwes") # pasta do index.html

#d ependância para abrir e fechar sessão com o banco de dados
def get_db():
    db = SessionLocal() # conexão com o banco de dados
    try:
        yield db # coletar o banco de dados
    finally:
        db.close() #finaliza fechando a conexão
        
# rota inicial (renderiza o index.html)
@router.get("/",response_class=HTMLResponse)

# função para fazer request no index.html e trazer os dados do banco de dados
async def home(request:Request,db:Session=Depends(get_db)):
    # buscar todos os usuários
    usuarios=db.query(usuarios).all()
    # retornar os dados para a página html
    return templates.TemplateResponse("index.html",{
        "request":request,"usuarios":usuarios
    })