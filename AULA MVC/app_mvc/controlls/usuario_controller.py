# from mols.usuarios import Usuario /n ta funcionando
from app_mvc.database import SessionLocal
from app_mvc.database import Usuario  # ou Usuario, se você corrigir o nome da classe

# criar usuario  listr os usuarios:
def criar_usuario(nome: str, email: str):
    session = SessionLocal()
    usuario = Usuario(nome = nome, email = email)
    session.add(usuario)
    session.commit()
    session.close()

# testar:
criar_usuario("teste", "teste@gmail")

def listar_usuario():
    session = SessionLocal()
    usuario = session.query(Usuario).all()
    session.close()
    return usuario