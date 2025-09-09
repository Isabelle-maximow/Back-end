#Aula 14 ORM: exemplos básicos de ORM (Mapeamento Objeto-Relacional)
"""
O ORM SQLAlchemy em Python é uma ferramenta que facilita o
trabalho com bancos de dados relacionais, como SQLite,
MySQL ou PostgreSQL, usando objetos Python em vez de
comandos SQL diretamente.

# '''
# Como funciona o SQLAlchemy ORM?
# Modelos: Você define classes Python que representam tabelas do
# banco de dados. Cada atributo da classe vira uma coluna da
# tabela.
# Mapeamento: O SQLAlchemy mapeia essas classes para as tabelas
# reais do banco. Sessão: Você usa uma sessão para criar, ler,
# atualizar e deletar registros no banco, tudo usando objetos
# Python.
# Abstração: Não precisa escrever SQL manualmente para operações
# básicas; o ORM converte suas ações em comandos SQL.

# Vantagens.
# Produtividade: Menos código SQL, mais foco na lógica do programa.
# Segurança: Evita SQL Injection, pois os dados são tratados
# como objetos.
# Portabilidade: O mesmo código pode funcionar em diferentes
# bancos de dados, mudando apenas a configuração.

# Resumindo
# O SQLAlchemy ORM permite que você trabalhe com bancos de dados
# de forma mais natural em Python, usando classes e objetos,
# sem se preocupar com detalhes do SQL.
# Isso torna o desenvolvimento mais rápido, seguro e organizado.
# '''


O que é ORM?
ORM significa Object-Relational Mapping
(Mapeamento Objeto-Relacional).
Ele faz a ponte entre o mundo dos objetos (Python) e o
mundo das tabelas (SQL).
Com ORM, você manipula dados do banco como se fossem objetos
Python, tornando o código mais intuitivo e seguro.
"""

'''
sqlachemy slite3 crud (Create, Read, Update, Delete).

chamadas de importação:
create_engine função cria uma instância de forma padrão para
acessar URL do banco de dados <database_urls> e escreve no
dialeto do sql em forma de string com argumentos de objeto
Column= representa uma coluna no database table
Integer= tipo int inteiro para database table
string=str texto é o varchar do database table

sqlalchemy.orm:
função para configuração do ORM método construtor para mapeamento
do objeto relacional
declarative_base:construtor para declaração de classes
produz os objetos do sqlalchemy para mapeamento de tabelas
chama o orm mapper com base nas informações fornecidas
sessionmaker:configuração de sessão gerar novos objetos
quando chamado com base nos argumentos
session: cria uma sessão para interagir com o banco de dados
'''
#pip install sqlalchemy
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker

Base = declarative_base() # criar uma classe para definir os modelos ORM

class Usuario (Base):
    # nome da tabela usar metodo especial do python
    __tablename__ = 'usuarios'
    # definir os dados da coluna tabela 
    id = Column (Integer, primary_key = True) # coluna id chave primaria 
    nome = Column (String)
    email = Column (String)
    
    # metodo para retornar as informações p pytho em str:
    def __repr__(self):
        return f"Usuário (ID = {self.id} Nome = {self.nome} E-mail = {self.email})"
    
# CRIAR O BANCO DE DADOS NO SQLITE E A TABELA
engine = create_engine ('sqlite://usuarios.db') # conecta e acessa o .db
# criar tabela:
Base.metadata.create_all(engine) # metadata p criar tabela 

# criar uma sessão para interagir com o banco de dados:
Session = sessionmaker(bind = engine) # bind = vincular o engine 

# instanciar a sessão do banco de dados:
session = Session() 

# fazer o crud 
usuario = Usuario (nome = "Maya", email = "mayazinha@gmail.com")
# add user ao banco:
session.add (usuario)
session.commit()

# read - consultar os dados do banco:
usuario_consulta = session.query(Usuario).all() # = SELECT * FROM
print("Usuarios Cadastrados")
for i in usuario_consulta:
    print(i)
    
# UPDATE atualizar o banco de dados
usuario_update = session.query(Usuario).filter_by(nome = "Maya").fisrt()
# query = consulta | filter = filro e busca | first = trazer o dado

if usuario_update:
    # novo dados:
    usuario_update.email = "mayanaozinha@gmail.com" 
    session.commit()
    print("Email atualizado com sucesso!!")
else:
    print ("Usuario não encontrado")
    
# DELETE - remover usuario
usuario_delete = session.query(Usuario).filter_by(nome = "Maya").first()
if usuario_delete:
    session.delete(usuario_delete)
    session.commit()
    print("Usuário deletado")
else:
    print("Não encontrado")