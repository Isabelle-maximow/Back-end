#database.py
#conexão com o banco de dados
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

#conexao com o sqlite
engine=create_engine("sqlite:///usuario_z.db")
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()

#criar o database usuario_z.db:
#Base.metadata.create_all(bind=engine)


# DEU ERRADO (NO OUTRO ARQUIVO):
#models/usuario.py
# criar tabela:
from sqlalchemy import Column, Integer, String

#importar a conexão com o sqlite do database.py
# from database import Base, engine

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column (Integer, primary_key = True, index = True)
    # index no input do steamlit:
    nome = Column (String, index = True)
    email = Column (String, index = True)
    
# criar tabela usuarios no sqlite:
Base.metadata.create_all(bind = engine)


# TESTE:

from database import SessionLocal
from database import Usuario 
# criar usuario  listr os usuarios:
def criar_usuario(nome: str, email: str):
    session = SessionLocal()
    usuario = Usuario(nome = nome, email = email)
    session.add(usuario)
    session.commit()
    session.close()

# testar:
criar_usuario("teste", "teste@gmail")

