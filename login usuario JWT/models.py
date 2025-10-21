#Aula24/25 login usuário jwt
#projeto base aula21#pip install python-jose
#pip install -U passlib 
#jose=JavaScript Object Signing and Encryption (JOSE)  tecnologias de Assinatura e Criptografia de Objetos JavaScript
#JWT=JSON Web Token (JWT)é um objeto JSON que traz consigo uma informação codificada e #assinada, de forma que #ela seja confiável entre duas partes

##################################
#aula21
#models.py
#novo import
from sqlalchemy.orm import relationship#relação entre tabelas
from auth import *
from sqlalchemy import Column,Integer,String,Float,Boolean,ForeignKey

from sqlalchemy import text#add uma coluna nova
class Usuario(Base):
    __tablenome__="usuarios"
    id=Column(Integer,primary_key=True,index=True)
    nome=Column(String(50))
    email=Column(String(100),unique=True)
    senha=Column(String(200))
    is_admin = Column(Boolean, default=False) # novo campo

    # relação entre as tabelas
    pedidos = relationship("Pedido", back_populates="usuario")
# criar novas tabelas:
class Pedido (Base):
    __tablename__ = "pedidos"
    id = Column (Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    total = Column(Float, default=0.0)

class ItemPedido(Base):
    __tablename__= "item_pedido"
    id = Column()
    pedido_id = Column (Integer, ForeignKey("pedidos.id"))
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    quantidade = Column(Integer)
    preco_unitario = Column(Float)
    pedido = relationship("Pedido", back_populates="itens")    


#criar banco de dados com a tabela e colunas
Base.metadata.create_all(bind=engine)
# add nova coluna:
# with engine.connect() as conexao:
#     conexao.execute(text( 'ALTER TABLE usuarios ADD COLUMN id_admin BOOLEAN DEFAULT 0'))
    
db = SessionLocal()
admin = Usuario(nome = "admin", email= "admin@loja.com",
                senha = gerar_hash_senha("12345", is_admin = True))
db.add(admin)
db.commit()