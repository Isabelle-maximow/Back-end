# models.py
from sqlalchemy import Column,Integer,String
from database import Base,engine

# criar o modelo para usuários
class Usuario(Base):
    __tablename__="usuarios"#nome da tabela
    id = Column(Integer,primary_key=True,index=True)
    nome = Column(String,index=True)
    email = Column(String,index=True,unique=True)
    #unique para email@ hiperlink
    
# Criar tabela do banco de dados
Base.metadata.create_all(bind=engine)


# criar um usuário teste
def criar_usuario(nome:str,email:str):
    session = SessionLocal()
    usuario = Usuario(nome=nome,email=email)
    session.add(usuario)
    session.commit()
    
# criar o usuário
criar_usuario("teste","teste@email.com")