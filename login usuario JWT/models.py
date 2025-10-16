#Aula24/25 login usuário jwt
#projeto base aula21#pip install python-jose
#pip install -U passlib 
#jose=JavaScript Object Signing and Encryption (JOSE)  tecnologias de Assinatura e Criptografia de Objetos JavaScript
#JWT=JSON Web Token (JWT)é um objeto JSON que traz consigo uma informação codificada e #assinada, de forma que #ela seja confiável entre duas partes

##################################
#aula21
#models.py
class Usuario(Base):
    __tablenome__="usuarios"
    id=Column(Integer,primary_key=True,index=True)
    nome=Column(String(50))
    email=Column(String(100),unique=True)
    senha=Column(String(200))
#criar banco de dados com a tabela e colunas
Base.metadata.create_all(bind=engine)
