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
############################################################


######################################################
#Novo post login do usuário normal ou admin
@router.post("/login")
def login(request:Request, email:str=Form(...),
        senha:str=Form(...), db:Session=Depends(get_db)
):
    usuario=db.query(Usuario).filter(Usuario.email==email).first()
    if not usuario or not verificar_hash_senha(senha,
                                               usuario.senha):
        return {"mensagem":"Credenciais inválidas"}
    #criar um token com o campos 'is_admin'
    token=criar_token({"sub":usuario.email,
                       "is_admin":usuario.is_admin})
    #criar um if de admin ou user normal
    if usuario.is_admin:
        destino="/admin"
    else:
        destino="/dashboard"
    response=RedirectResponse(url=destino,status_code=303)
    response.set_cookie(key="token",value=token,
                        httponly=True)
    return response

######################################################
######################################################
#rota de admin crud nos produtos
@router.get("/admin",response_class=HTMLResponse)
def pagina_admin(request:Request,db:Session=Depends(get_db)):
    #token do admin
    token=request.cookies.get("token")
    payload=verificar_token(token)
    if not payload or not payload.get("is_admin"):
        return RedirectResponse(url="/",status_code=303)
    produtos=db.query(Produto).all()
    return templates.TemplateResponse("admin.html",{
        "request":request,"produtos":produtos
    })
#rota criar produto
@router.post("/admin/produto")
def criar_produto(request:Request,nome:str=Form(...),
    preco:float=Form(...),quantidade:int=Form(...),
    imagem:UploadFile=File(...),db:Session=Depends(get_db)
                  ):
    caminho_arquivo=f"{UPLOAD_DIR}/{imagem.filename}"
    with open(caminho_arquivo,"wb") as arquivo:
        shutil.copyfileobj(imagem.file,arquivo)
    novo_produto=Produto(nome=nome,preco=preco,
        quantidade=quantidade,imagem=imagem.filename)
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return RedirectResponse(url="/admin",status_code=303)

#editar produto get edição do produto
@router.get("/admin/produto/editar/{id}",
            response_class=HTMLResponse)
def editar_produto(id:int,request:Request,
                   db:Session=Depends(get_db)):
    token=request.cookies.get("token")
    payload=verificar_token(token)
    if not payload or not payload.get("is_admin"):
        return RedirectResponse(url="/",status_code=303)
    produto=db.query(Produto).filter(Produto.id==id).first()
    if not produto:
        return RedirectResponse(url="/admin",status_code=303)
    return templates.TemplateResponse("editar.html",{
        "request":request,"produto":produto
    })

#rota editar produto
@router.post("/admin/produto/atualizar/{id}")
def atualizar_produto(id:int,nome:str=Form(...),
    preco:float=Form(...),quantidade:int=Form(...),
    imagem:UploadFile=File(None),db:Session=Depends(get_db)
                  ):
    produto=db.query(Produto).filter(Produto.id==id).first()
    if not produto:
        return RedirectResponse(url="/admin",status_code=303)
    #atualiza os campos
    produto.nome=nome
    produto.preco=preco
    produto.quantidade=quantidade
    #atualizar a imagem se tiver
    if imagem and imagem.filename !="":
        caminho_arquivo=f"{UPLOAD_DIR}/{imagem.filename}"
    with open(caminho_arquivo,"wb") as arquivo:
        shutil.copyfileobj(imagem.file,arquivo)
    produto.imagem=imagem.filename
    db.commit()
    db.refresh(produto)
    return RedirectResponse(url="/admin",status_code=303)

#deletar produto
@router.post("/admin/produto/deletar/{id}")
def deletar_produto(id:int,db:Session=Depends(get_db)):
    produto=db.query(Produto).filter(Produto.id==id).first()
    if produto:
        db.delete(produto)
        db.commit()
    return RedirectResponse(url="/admin",status_code=303)
    return response

# criar rota do dashboard do usuario. pagina protegida:
@router.get("/dashboard", response_class= HTMLResponse)
def dashboard(request: Request):
    token = request.cookies.get("token")
    if not token or verificar_token(token):
        return RedirectReponse (url = "/", status_code = 303)
    return templates.TemplateResponse("dashboard.html", {"request": request}
#carrinho simples em memória
carrinhos={}
#adicionar item ao carrinho
@router.post("/carrinho/adicionar/{produto_id}")
def adicionar_carrinho(request:Request,
    produto_id:int,quantidade:int=Form(1),
    db:Session=Depends(get_db)
):
    token=request.cookies.get("token")
    payload=verificar_token(token)
    if not payload:
        return RedirectResponse(url="/login",status_code=303)
    email=payload.get("sub")
    usuario=db.query(Usuario).filter_by(email=email).first()
    produto=db.query(Produto).filter_by(id=produto_id).first()
    if not produto:
        return{"mensagem":"Produto não encontrado"}
    carrinho=carrinhos.get(usuario.id,[])
    carrinho.append({
        "id":produto.id,
        "nome":produto.nome,
        "preco":produto.preco,
        "quantidade":quantidade
    })
    carrinhos[usuario.id]=carrinho
    return RedirectResponse(url="/carrinho",status_code=303)
#ver o carrinho
@router.get("/carrinho",response_class=HTMLResponse)
def ver_carrinho(request:Request,db:Session=Depends(get_db)):
    token=request.cookies.get("token")
    payload=verificar_token(token)
    if not payload:
        return RedirectResponse(url="/login",status_code=303)
    email=payload.get("sub")
    usuario=db.query(Usuario).filter_by(email=email).first()
    carrinho=carrinhos.get(usuario.id,[])
    total=sum(item["preco"]*item["quantidade"] for item in carrinho)
    return templates.TemplateResponse("carrinho.html",{
        "request":request,"carrinho":carrinho,"total":total
    })
#finalizar compra checkout
@router.post("/checkout")
def checkout(request:Request,db:Session=Depends(get_db)):
    token=request.cookies.get("token")
    payload=verificar_token(token)
    if not payload:
        return RedirectResponse(url="/login",status_code=303)
    email=payload.get("sub")
    usuario=db.query(Usuario).filter_by(email=email).first()
    carrinho=carrinhos.get(usuario.id,[])
    if not carrinho:
        return {"mensagem":"Carrinho vazio"}
    total=sum(item["preco"]*item["quantidade"] for item in carrinho)
    pedido=Pedido(usuario_id=usuario.id,total=total)
    db.add(pedido)
    db.commit()
    db.refresh(pedido)
    #novo item ao carrinho
    for item in carrinho:
        novo_item=ItemPedido(
            pedido_id=pedido.id,
            produto_id=item["id"],
            quantidade=item["quantidade"],
            preco_unitario=item["preco"]
        )
        db.add(novo_item)
    db.commit()
    #limpar o carrinho
    carrinhos[usuario.id]=[]
    return RedirectResponse(url="/meus-pedidos",
                            status_code=303)
#listar pedidos do usuário
@router.get("/meus-pedidos",response_class=HTMLResponse)
def meus_pedidos(request:Request,db:Session=Depends(get_db)):
    token=request.cookies.get("token")
    payload=verificar_token(token)
    if not payload:
        return RedirectResponse(url="/login",status_code=303)
    email=payload.get("sub")
    usuario=db.query(Usuario).filter_by(email=email).first()
    pedidos=db.query(Pedido).filter_by(usuario_id=usuario.id).all()
    return templates.TemplateResponse("meus_pedidos.html",
            {"request":request,"pedidos":pedidos})



#painel do usuário rota /me/painel
@router.get("/me/painel",response_class=HTMLResponse)
def painel_usuario(request:Request,
        db:Session=Depends(get_db)):
    token=request.cookies.get("token")
    payload=verificar_token(token)
    if not payload:
        return RedirectResponse(url="/",status_code=303)
    usuario=db.query(Usuario).filter(Usuario.email==payload["sub"]).first()
    pedidos=db.query(Pedido).filter(Pedido.usuario_id==usuario.id).first()
    return templates.TemplateResponse("painel_usuario.html",{
        "request":request,"usuario":usuario,"pedidos":pedidos
    })
#dados usuário
@router.get("/me/dados",response_class=HTMLResponse)
def meus_dados(request:Request,db:Session=Depends(get_db)):
    token=request.cookies.get("token")
    payload=verificar_token(token)
    if not payload:
        return RedirectResponse(url="/",status_code=303)
    usuario=db.query(Usuario).filter(Usuario.email==payload["sub"]).first()
    return templates.TemplateResponse("meus_dados.html",{
        "request":request,"usuario":usuario
    })
#remove o cookie do token do usuário
@router.get("/logout")
def logout(request:Request):
    response=RedirectResponse(url="/",status_code=303)
    response.delete_cookie(key="token")
    return response
