#controller.py
from models import Produto,Usuario#import novo
from auth import gerar_hash_senha,verificar_hash_senha, criar_token, verificar_token #import novo


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
    
    # criando verificando e token:
    token = criar_token ({"sub": usuario.email})
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
    return templates.TemplateResponse("dashboard.html", {"request": request})