from sqlalchemy import create_engine, Column, Integer, String, Float
# creative_engine = função para criar a instancia para a comunicação
# colunm = coluna | Integer = int | String = str | Float = float
 
from sqlalchemy.ext.declarative import declarative_base
# sqlalchemy.ext.declarative = construtor para a declaração de classes
# que produz os objetos para mapeamentos de tabelas
# declarative_base = função declarar as informções da tabela 

from sqlalchemy.orm import sessionmaker
# configuração de sessçai para gerar os comandos do sql

# criar o engine para conecta ao servidor do banco de dados:
engine = create_engine('sqlite:///titulo.db', echo = True) # para debugs 

# base para deinir os modelos:
Base = declarative_base()

# definir p modelo (equivalente a criar tabelas):
class Filme(Base):
    __tablename__ = "filmes" # nome da tabela no banco
    id = Column (Integer, primary_key=True, autoincrement=True)
    nome = Column (String, nullable= False)
    ano = Column (Float, nullable= False)
    nota = Column (Float, nullable= False)
    
    # metodo especial para trazer os dados string:
    def __repr__(self):
        return f"""
                ID: {self.id}
                FILMES: {self.nome}
                NOME: {self.ano}
                NOTA: {self.nota}"""

# criar tabela no banco de dados:
def criar_tabela():
    Base.metadata.create_all(engine)
    print("Tabela Filme criadacom sucesso")

# criar a sessão (conexão temporaria com o banco)
def criar_sessão():
    Session = sessionmaker (bind = engine)
    return Session()

#testar 
criar_tabela()