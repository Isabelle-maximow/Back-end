#models/usuario.py
# criar tabela:
from sqlalchemy import Column, Integer, String

#importar a conexão com o sqlite do database.py
from database import Base, engine

class Usuario(Base):
    __tablehme__ = "usuarios"
    id = Column (Integer, primary_key = True, index = True)
    # index no input do steamlit:
    nome = Column (String, index = True)
    email = Column (String, index = True)
    
# criar tabela usuarios no sqlite:
Base.metadata.create_all(bind = engine)

