#controller.py
from models import Produto,Usuario#import novo
from auth import gerar_hash_senha,verificar_hash_senha, criar_token, verificar_token #import novo
import os, shutil
from models imports Produto, Usuario # tem mt mais 


#Cadastro de usuário rotas de autenticação
@router.get("/register",response_class=HTMLResponse)
def pagina_cadastro(request:Request):
    return templates.TemplateResponse("register.html",{
        "request":request
    })
#formulário criar usuário
@router.post("/register")
def cadastrar_usuario( request:Request,
    nome:str = Form(...), email:str=Form(...),
    senha:str=Form(...),db:Session=Depends(get_db)
):
    usuario=db.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        return {"mensagem":"E-mail já cadastrado!"}
    senha_hash=gerar_hash_senha(senha)
    novo_usuario=Usuario(nome=nome,email=email,senha=senha_hash)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return RedirectResponse(url="/",status_code=303)

# rota de login usuario:
@router.get("/login", response_class = HTMLResponse)
def home (request: Request):
    return templates.TemplateResponse("login.html",
                                      {"request": request})
   
# post login do usuario:
@router.post("/login")
def login( request: Request, email: str = Form (...),
          senha: str = Form(...), db: Session = Depends (get_db)):
    usuario = db.query(Usuario),filter(usuario.email==email).first()
    if not usuario or not verificar_hash_senha(senha, usuario.senha):
        return {"mensagem": "Credenciais inválidas"}
    
    # criando verificando e token: COM O CAMPOS 'IS_ADMIN
    token = criar_token ({"sub": usuario.email,
                          "is_admin": usuario.is_admin})
    
    # criar um if .... COLOCAR AQUI 
    response = RedirectResponse(url= "/dashboard", status_code = 300)
    response.set_cookie(key = "token", value = token,
                        httponly = True)
    return response

# criar rota do dashboard do usuario. pagina protegida:
@router.get("/dashboard", response_class= HTMLResponse)
def dashboard(request: Request):
    token = request.cookies.get("token")
    if not token or verificar_token(token):
        return RedirectReponse (url = "/", status_code = 303)
    return templates.TemplateResponse("dashboard.html", {"request": request}

# carrinho simples com memoria:
carrinhos = {}
# add item ao carrinho:
@router.post ("/carrinho/adicionar/{produto_id}")
def adicionar_carrinho(request: Request,
                       produto_id: int, quantidade: int = Form(1),
                       db: Session = Depends (get_db)):
    token = request.cookies.get("token")
    payload = verificar_token(token)
    if not payload:
        return RedirectResponse(url = "/login", status_code= 303)
        email = payload.get("sub")
        usuario = db.query(Usuario).filter_by(email=email).first()
        produto = db.query(Produto).filter_by(id=produto_id).first()
        if not produto:
            return{"mensagem" : "produto não encontrado "}
            carrinho = carrinhos.get(usuario.id, [])
            carrinho.append({
                "id": produto.id,
                "nome": produto.nome,
                "preco": produto.preco,
                "quantidade" = quantidade
            })
            carrinhos[usuario.id] = carrinho 
            return RedirectResponse(url = "/carrinho", status_code = 303)
            
            
@router.get("/carrinho", response_class= HTMLResponse)
def ver_carrinho(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("token")
    if not payload:
        return RedirectResponse(url = "/login", status_code= 303)
    email = payload.get("sub")
    usuario = db.query(Usuario).filter_by(email=email).first()
    carrinho = carrinhos.get(usuario.id, [])
    total=sum(item["preco"]*item["quantidade"] for item in carrinho)
    return templates.TemplateResponse("carrinho.html",{
        "request":request,"carrinho":carrinho,"total":total
    })
    
# finalizar checkout:
@router.post("/checkout")
def checkout(request: request, "carrinho": carrinho, "total: total")
